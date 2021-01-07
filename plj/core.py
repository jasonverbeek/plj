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
def filter(pred, coll):
    return (r for r in coll if pred(r))


@curry
def conj(coll, item):
    coll.append(item)
    return coll


@curry
def into(target, source):
    target += source
    return target


def last(coll):
    result = None
    for item in iter(coll):
        result=item
    return result


def first(coll):
    for item in iter(coll):
        return item
    return


@curry
def nth(coll, index):
    for i, value in enumerate(coll):
        if i == index:
            return value
    return

