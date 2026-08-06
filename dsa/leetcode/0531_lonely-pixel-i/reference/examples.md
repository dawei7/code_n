## Examples

**Example 1**

- Input: `picture = [["W","W","B"],["W","B","W"],["B","W","W"]]`
- Output: `3`
- **Explanation:** Each of the three black pixels is the only black pixel in both its row and its column.

The first source diagram is represented below. `B*` marks a lonely black pixel.

| Row \ Column | 0 | 1 | 2 |
|---:|:---:|:---:|:---:|
| 0 | W | W | B* |
| 1 | W | B* | W |
| 2 | B* | W | W |

**Example 2**

- Input: `picture = [["B","B","B"],["B","B","W"],["B","B","B"]]`
- Output: `0`

The second source diagram contains no lonely black pixel:

| Row \ Column | 0 | 1 | 2 |
|---:|:---:|:---:|:---:|
| 0 | B | B | B |
| 1 | B | B | W |
| 2 | B | B | B |
