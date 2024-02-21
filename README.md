## Description

This Python package provides a function `top_n` to retrieve the top N items in an array in descending order. It uses a basic bubble sort algorithm for simplicity.

## Functionality

The `top_n` function takes two arguments:
- `items` (array): List or array-like object containing elements to be sorted.
- `n` (int): Number of top items to return.

The function returns an array containing the top N items from the input array, sorted in descending order.

## Example Usage

```python
from top_n_package import top_n

# Example: Get the top 3 items from an array
result = top_n([8, 3, 2, 7, 4], 3)
print(result)  # Output: [8, 7, 4]
```

## Installation
You can install the package using pip:

pip install top-n-package

## How to Use

Import the top_n function from the package:

from top_n_package import top_n
Use the top_n function as demonstrated in the example.

## License
This package is distributed under the MIT license. See the LICENSE file for details.

This arrangement keeps the installation, usage instructions, and license details together for a more organized and user-friendly readme.
