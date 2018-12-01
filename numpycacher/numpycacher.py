import functools
from collections import Hashable


def quickcacher(cache, n_args, cache_size=float('+inf')):
    """Cache a function through decorating. Uses your cache *cache*. It works
    with functions like f(x, y, a, b, c) where x and y are numpy arrays and
    a, b and c are hashable parameters. In this case you must set *n_args*
    to 2 since x and y are numpy arrays.
    :param cache: dict object which plays role of cache.
    :param n_args: number of numpy arrays in your prototype of caching function.
    For example, it equals 3 if caching function is f(x, y, z, c) where the
    first three arguments are numpy arrays.
    :return: Caching decorator.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args):
            hashable = (*[arr.tostring() for arr in args[:n_args]],
                        *args[n_args:])
            if hashable in cache:
                return cache[hashable]
            result = func(*args)
            if len(cache) >= cache_size:
                cache.popitem()
            cache[hashable] = result
            return result
        return wrapped
    return decorator


def unicacher(cache, cache_size=float('+inf')):
    """Cache a function through decorating. Uses your cache *cache*. It works
    with functions like f(x, y, a, b, z, c) where x, y, z are numpy arrays and
    a, b and c are hashable parameters.
    :param cache: dict object which plays role of cache.
    :return: Caching decorator.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args):
            hashable = tuple(item if isinstance(item, Hashable)
                             else item.tostring() for item in args)
            if hashable in cache:
                return cache[hashable]
            result = func(*args)
            if len(cache) >= cache_size:
                cache.popitem()
            cache[hashable] = result
            return result
        return wrapped
    return decorator
