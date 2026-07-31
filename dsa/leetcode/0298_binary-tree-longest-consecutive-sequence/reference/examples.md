## Examples

**Example 1**

- Input: `root = [1,null,3,2,4,null,null,null,5]`
- Output: `3`
- Explanation: The longest valid path is `3 -> 4 -> 5`, which contains three nodes.

```text
1
 \
  3
 / \
2   4
     \
      5

consecutive path: 3 -> 4 -> 5
```

**Example 2**

- Input: `root = [2,null,3,2,null,1]`
- Output: `2`
- Explanation: `2 -> 3` is a valid increasing path. The downward chain `3 -> 2 -> 1` decreases, so it is not a consecutive sequence for this problem.

```text
2
 \
  3
 /
2
/
1

valid path: 2 -> 3
```
