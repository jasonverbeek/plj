from functools import partial, wraps
from itertools import chain
from inspect import signature


def get_in(obj, *keys, default=None):
    r = dict(obj)
    for k in keys:
        r = r.setdefault(k, {})
    if r in [None, {}]:
        return default
    return r


def transduce(fn):
    """
    Generic wrapper to turn a function into a transducer
        fn: function to wrap

    NOTE: very EXPERIMENTAL
    TODO: check should not be based on a number.
    """
    nargs = len(signature(fn).parameters)

    @wraps(fn)
    def _transduced(*args):
        if len(args) == nargs:
            return fn(*args)
        return partial(fn, *args)
    return _transduced


@transduce
def filter(pred, col):
    return (r for r in col if pred(r))


def conj(l, i):
    return (x for x in chain(iter(l), [i]))


def into(t, s):
    return (x for x in chain(iter(t), iter(s)))

