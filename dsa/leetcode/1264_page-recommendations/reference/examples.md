## Examples

**Example 1**

- **Input:** `Friendship = [[1,2],[1,3],[1,4],[2,3],[2,4],[2,5],[6,1]], Likes = [[1,88],[2,23],[3,24],[4,56],[5,11],[6,33],[2,77],[3,77],[6,88]]`

Friendship:

| user1_id | user2_id |
|---:|---:|
| 1 | 2 |
| 1 | 3 |
| 1 | 4 |
| 2 | 3 |
| 2 | 4 |
| 2 | 5 |
| 6 | 1 |

Likes:

| user_id | page_id |
|---:|---:|
| 1 | 88 |
| 2 | 23 |
| 3 | 24 |
| 4 | 56 |
| 5 | 11 |
| 6 | 33 |
| 2 | 77 |
| 3 | 77 |
| 6 | 88 |

- **Output:** `[[23],[24],[56],[33],[77]]`

| recommended_page |
|---:|
| 23 |
| 24 |
| 56 |
| 33 |
| 77 |

- **Explanation:** User `1` is friends with users `2`, `3`, `4`, and `6`. Those friends supply pages `23`, `24`, `56`, and `33`, respectively. Both users `2` and `3` like page `77`, which is recommended only once. Page `88` is excluded because user `1` already likes it. (The source explanation appears to attribute page `56` to user `3`; the input table shows that it belongs to user `4`.)
