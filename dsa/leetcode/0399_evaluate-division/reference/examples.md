## Examples

**Example 1**

- Input: `equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]`
- Output: `[6.00000,0.50000,-1.00000,1.00000,-1.00000]`
- Explanation: From `a / b = 2.0` and `b / c = 3.0`, the first two answers are `6.0` and `0.5`. Variable `e` is unknown, `a / a` is `1.0`, and undefined `x` makes `x / x` indeterminate, producing `-1.0`.

**Example 2**

- Input: `equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]`
- Output: `[3.75000,0.40000,5.00000,0.20000]`

**Example 3**

- Input: `equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]`
- Output: `[0.50000,2.00000,-1.00000,-1.00000]`
