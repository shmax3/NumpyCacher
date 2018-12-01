import functools


def cacher(cache, n_args):
    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args):
            hashable = (*[arr.tostring() for arr in args[:n_args]],
                        *args[n_args:])
            if hashable in cache:
                return cache[hashable]
            result = func(*args)
            cache[hashable] = result
            return result
        return wrapped
    return decorator
