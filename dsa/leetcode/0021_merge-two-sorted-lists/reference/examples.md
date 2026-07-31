## Examples

**Example 1**

- Input: `list1 = [1, 2, 4], list2 = [1, 3, 4]`
- Output: `[1, 1, 2, 3, 4, 4]`

The source image is reproduced independently as a node-flow diagram:

```text
list1: 1 -> 2 ------> 4 ----\
                               -> 1 -> 1 -> 2 -> 3 -> 4 -> 4
list2: 1 ------> 3 -> 4 ----/
```

**Example 2**

- Input: `list1 = [], list2 = []`
- Output: `[]`

**Example 3**

- Input: `list1 = [], list2 = [0]`
- Output: `[0]`
