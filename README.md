# NumpyCacher

NumpyCacher is a simple package for [caching](https://en.wikipedia.org/wiki/Cache_(computing)) your functions which has numpy array arguments.

## Installation
We encourage you to use pip to install NumpyCacher on your system.
```bash
git clone https://github.com/shmax3/NumpyCacher.git
pip install NumpyCacher/
```

## Requirements
The most basic features of NumpyCacher requires Python 3 and numpy.

## Example

The following code gives a quick overview how simple it is to implement unicacher to your function.

```python
from numpycacher import unicacher
import numpy as np


cache = {}

@unicacher(cache)
def f(x, y, a, b, z):
    return a*np.exp(x) + b*np.exp(y) + z
```

If you don't want to use cache directly you should write the same like this.
```python
from numpycacher import unicacher
import numpy as np


@unicacher({})
def f(x, y, a, b, z):
    return a*np.exp(x) + b*np.exp(y) + z
```

Sometimes you want to control cache capacity. You could set cache capacity to 100 in the following way.
```python
from numpycacher import unicacher
import numpy as np


@unicacher({}, 100)
def f(x, y, a, b, z):
    return a*np.exp(x) + b*np.exp(y) + z
```

If you use function with n numpy array arguments in first positions you could use quickcacher(cache, n) decorator. The following example has n = 3.

```python
from numpycacher import quickcacher
import numpy as np


cache = {}

# the first 3 arguments are numpy arrays, cache capacity is 100
@quickcacher(cache, 3, 100)
def f(x, y, z, a, b):
    return a*np.exp(x) + b*np.exp(y) + z
```
