from functools import partial, wraps
from itertools import chain
from collections.abc import Mapping
from inspect import signature


def curry(n_or_fn=None):
    def _curry(nargs, fn):
        @wraps(fn)
        def _curried(*args, **kwargs):
            arg_count = len(args) + len(kwargs)
            if (arg_count) >= nargs:
                return fn(*args, **kwargs)
            return partial(_curried, *args, **kwargs)
        return _curried
    if callable(n_or_fn):
        return _curry(len(signature(n_or_fn).parameters), n_or_fn)
    else:
        return partial(_curry, n_or_fn)


@curry(2)
def get_in(obj, *keys, default=None):
    keys = list(keys)
    while isinstance(obj, Mapping) and len(keys):
        obj = obj.get(keys.pop(0), default)
    return obj


@curry
def filter(pred, col):
    return (r for r in col if pred(r))


@curry
def conj(l, i):
    l.append(i)
    return l


@curry
def into(t, s):
    t += s
    return t


def last(i):
    l = None
    for x in iter(i):
        l=x
    return l


def first(i):
    for r in iter(i):
        return r
    return


@curry
def nth(i, k):
    for c, v in enumerate(i):
        if c == k:
            return v
    return

