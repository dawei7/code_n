## Examples

**Example 1**

- Input: `nestedList = [[1,1],2,[1,1]]`
- Output: `8`
- Explanation: The four `1` values are at depth `2` and therefore have weight `1`; the `2` is at depth `1` and has weight `2`. Thus `1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8`.

The source depth-and-weight illustration can be represented as follows:

```text
value:   [ [1,1], 2, [1,1] ]
depth:       2 2   1    2 2
weight:      1 1   2    1 1
```

**Example 2**

- Input: `nestedList = [1,[4,[6]]]`
- Output: `17`
- Explanation: The values `1`, `4`, and `6` have inverse-depth weights `3`, `2`, and `1`, respectively, so `1*3 + 4*2 + 6*1 = 17`.

The source illustration aligns ordinary depth with the reversed weights:

```text
value:   [ 1, [ 4, [ 6 ] ] ]
depth:     1     2     3
weight:    3     2     1
```
