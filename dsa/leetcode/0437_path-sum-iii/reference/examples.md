## Examples

**Example 1**

- Input: `root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8`
- Output: `3`
- Explanation: The three qualifying downward paths are `5 -> 3`, `5 -> 2 -> 1`, and `-3 -> 11`.

```mermaid
---
config:
  flowchart:
    nodeSpacing: 24
    rankSpacing: 30
---
flowchart TD
    accTitle: Example tree with three paths summing to eight
    accDescr: Root 10 has children 5 and -3. Node 5 has children 3 and 2; that 3 has children 3 and -2, and 2 has right child 1. Node -3 has right child 11. The paths 5 to 3, 5 to 2 to 1, and -3 to 11 each sum to 8.
    root["10"] --> left["5"]
    root --> right["-3"]
    left -- "Path 1" --> leftLeft["3"]
    left -- "Path 2" --> leftRight["2"]
    right -- "Path 3" --> rightRight["11"]
    leftLeft --> leafA["3"]
    leftLeft --> leafB["-2"]
    leftRight -- "Path 2" --> leafC["1"]
```

**Example 2**

- Input: `root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22`
- Output: `3`
