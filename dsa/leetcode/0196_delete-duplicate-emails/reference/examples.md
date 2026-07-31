## Examples

**Example 1**

- Input: `Person = [[1,"john@example.com"],[2,"bob@example.com"],[3,"john@example.com"]]`

| id | email |
|---:|---|
| 1 | john@example.com |
| 2 | bob@example.com |
| 3 | john@example.com |

- Output: `Person = [[1,"john@example.com"],[2,"bob@example.com"]]`

| id | email |
|---:|---|
| 1 | john@example.com |
| 2 | bob@example.com |

- Explanation: `john@example.com` occurs twice, so the row with the smaller identifier, `1`, is retained.
