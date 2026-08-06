## Examples

**Example 1**

- Input: `root = [1,null,3,2,4,null,5,6]`
- Output: `[[1],[3,2,4],[5,6]]`

Accessible rendering of the first source tree image:

| Parent | Ordered children |
|---:|---|
| 1 | 3, 2, 4 |
| 3 | 5, 6 |
| 2 | none |
| 4 | none |
| 5 | none |
| 6 | none |

**Example 2**

- Input: `root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]`
- Output: `[[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]`

Accessible rendering of the second source tree image:

| Parent | Ordered children |
|---:|---|
| 1 | 2, 3, 4, 5 |
| 2 | none |
| 3 | 6, 7 |
| 4 | 8 |
| 5 | 9, 10 |
| 6 | none |
| 7 | 11 |
| 8 | 12 |
| 9 | 13 |
| 10 | none |
| 11 | 14 |
| 12 | none |
| 13 | none |
| 14 | none |
