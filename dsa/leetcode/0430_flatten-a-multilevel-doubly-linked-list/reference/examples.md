## Examples

**Example 1**

- Input: `head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]`
- Output: `[1,2,3,7,8,11,12,9,10,4,5,6]`
- Explanation: The first source image depicts this multilevel input. Node `3` owns the child level beginning at
  `7`, and node `8` owns the child level beginning at `11`.

| Node | Original `next` | Original `child` |
|---:|---:|---:|
| 1 | 2 | none |
| 2 | 3 | none |
| 3 | 4 | 7 |
| 4 | 5 | none |
| 5 | 6 | none |
| 6 | none | none |
| 7 | 8 | none |
| 8 | 9 | 11 |
| 9 | 10 | none |
| 10 | none | none |
| 11 | 12 | none |
| 12 | none | none |

The second source image shows the flattened result:

| Direction | Complete traversal | Child links |
|---|---|---|
| `next` | `1 -> 2 -> 3 -> 7 -> 8 -> 11 -> 12 -> 9 -> 10 -> 4 -> 5 -> 6` | all `null` |
| `prev` | `6 -> 5 -> 4 -> 10 -> 9 -> 12 -> 11 -> 8 -> 7 -> 3 -> 2 -> 1` | all `null` |

**Example 2**

- Input: `head = [1,2,null,3]`
- Output: `[1,3,2]`
- Explanation: In the third source image, node `1` points next to `2` and owns child `3`.

| Node | Original `next` | Original `child` |
|---:|---:|---:|
| 1 | 2 | 3 |
| 2 | none | none |
| 3 | none | none |

The fourth source image shows the child inserted before the saved sibling:

| Direction | Complete traversal | Child links |
|---|---|---|
| `next` | `1 -> 3 -> 2` | all `null` |
| `prev` | `2 -> 3 -> 1` | all `null` |

**Example 3**

- Input: `head = []`
- Output: `[]`
- Explanation: The input list may be empty.
