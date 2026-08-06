## Examples

**Example 1**

- **Input:** `height = 5, width = 7, tree = [2,2], squirrel = [4,4], nuts = [[3,0],[2,5]]`

The source image places the objects in this coordinate grid:

| row \ column | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---:|---|---|---|---|---|---|---|
| 0 |  |  |  |  |  |  |  |
| 1 |  |  |  |  |  |  |  |
| 2 |  |  | tree |  |  | nut |  |
| 3 | nut |  |  |  |  |  |  |
| 4 |  |  |  |  | squirrel |  |  |

- **Output:** `12`

- **Explanation:** The minimum route begins with the nut at `[2,5]`. Reaching that nut from `[4,4]` costs `3` moves, carrying it to the tree costs `3`, and the round trip from the tree to the nut at `[3,0]` costs `6`, for a total of `12`.

**Example 2**

- **Input:** `height = 1, width = 3, tree = [0,1], squirrel = [0,0], nuts = [[0,2]]`

The second source image is the following one-row garden:

| row \ column | 0 | 1 | 2 |
|---:|---|---|---|
| 0 | squirrel | tree | nut |

- **Output:** `3`
