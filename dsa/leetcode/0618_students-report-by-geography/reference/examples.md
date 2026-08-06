## Examples

**Example 1**

- **Input:** `Student = [["Jane","America"],["Pascal","Europe"],["Xi","Asia"],["Jack","America"]]`
- **Output:** `[["Jack","Xi","Pascal"],["Jane",null,null]]`

`Student` table:

| name | continent |
|---|---|
| Jane | America |
| Pascal | Europe |
| Xi | Asia |
| Jack | America |

Result:

| America | Asia | Europe |
|---|---|---|
| Jack | Xi | Pascal |
| Jane | `NULL` | `NULL` |
