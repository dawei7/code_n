## Examples

**Example 1**

- **Input:** `Submissions = [[1,null],[2,null],[1,null],[12,null],[3,1],[5,2],[3,1],[4,1],[9,1],[10,2],[6,7]]`

| sub_id | parent_id |
|---:|---:|
| 1 | NULL |
| 2 | NULL |
| 1 | NULL |
| 12 | NULL |
| 3 | 1 |
| 5 | 2 |
| 3 | 1 |
| 4 | 1 |
| 9 | 1 |
| 10 | 2 |
| 6 | 7 |

- **Output:** `[[1,3],[2,2],[12,0]]`

| post_id | number_of_comments |
|---:|---:|
| 1 | 3 |
| 2 | 2 |
| 12 | 0 |

- **Explanation:** Post `1` has comments `3`, `4`, and `9`; the repeated row for comment `3` counts only once. Post `2` has comments `5` and `10`. Post `12` has no comments. Comment `6` refers to deleted post `7`, so it is ignored.
