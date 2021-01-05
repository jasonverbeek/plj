from functools import partial, wraps


def get_in(obj, *keys, default=None):
    r = dict(obj)
    for k in keys:
        r = r.setdefault(k, {})
    if r in [None, {}]:
        return default
    return r


def transduce(fn):
    @wraps(fn)
    def _transduced(*args):
        if len(args) == 2:
            return fn(*args)
        return partial(fn, *args)
    return _transduced


@transduce
def filter(pred, col):
    return (r for r in col if pred(r))


# def filter(pred, col=None):
#     if col is None:
#         return partial(_filter, pred)
#     return _filter(pred, col)
        
