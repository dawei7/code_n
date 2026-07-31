## Examples

**Example 1**

- Input: `nestedList = [[1,1],2,[1,1]]`
- Output: `10`
- Explanation: The four `1` values have depth `2`, while `2` has depth `1`; hence `1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10`.

```text
outer list (depth 1): [ [1,1], 2, [1,1] ]
                         depth 2      depth 2
```

**Example 2**

- Input: `nestedList = [1,[4,[6]]]`
- Output: `27`
- Explanation: The values `1`, `4`, and `6` occur at depths `1`, `2`, and `3`; thus `1*1 + 4*2 + 6*3 = 27`.

```text
depth 1: [1, [4, [6]]]
              ^   ^
           depth 2 depth 3
```

**Example 3**

- Input: `nestedList = [0]`
- Output: `0`
