from operator import attrgetter

from django.core.exceptions import ObjectDoesNotExist
from django.urls import NoReverseMatch


class MockObject:
    def __init__(self, **kwargs):
        self._kwargs = kwargs
        for key, val in kwargs.items():
            setattr(self, key, val)

    def __str__(self):
        kwargs_str = ', '.join([
            '%s=%s' % (key, value)
            for key, value in sorted(self._kwargs.items())
        ])
        return '<MockObject %s>' % kwargs_str


class MockQueryset:
    def __init__(self, iterable):
        self.items = iterable

    def __getitem__(self, val):
        return self.items[val]

    def get(self, **lookup):
        for item in self.items:
            if all([
                attrgetter(key.replace('__', '.'))(item) == value
                for key, value in lookup.items()
            ]):
                return item
        raise ObjectDoesNotExist()


class BadType:
    """
    When used as a lookup with a `MockQueryset`, these objects
    will raise a `TypeError`, as occurs in Django when making
    queryset lookups with an incorrect type for the lookup value.
    """

    def __eq__(self):
        raise TypeError()


def mock_reverse(view_name, args=None, kwargs=None, request=None, format=None):
    args = args or []
    kwargs = kwargs or {}
    value = (args + list(kwargs.values()) + ['-'])[0]
    prefix = 'http://example.org' if request else ''
    suffix = ('.' + format) if (format is not None) else ''
    return '%s/%s/%s%s/' % (prefix, view_name, value, suffix)


def fail_reverse(view_name, args=None, kwargs=None, request=None, format=None):
    raise NoReverseMatch()
