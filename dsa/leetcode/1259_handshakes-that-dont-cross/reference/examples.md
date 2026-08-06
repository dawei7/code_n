## Examples

**Example 1**

- Input: `numPeople = 4`
- Output: `2`
- Explanation: The two arrangements pair the people as `[(1,2),(3,4)]` and `[(2,3),(4,1)]`.

The first source diagram represents the same two arrangements:

| Arrangement | Handshake pairs |
|---:|---|
| 1 | `(1,2)`, `(3,4)` |
| 2 | `(1,4)`, `(2,3)` |

**Example 2**

- Input: `numPeople = 6`
- Output: `5`

The second source diagram enumerates the five counted arrangements:

| Arrangement | Handshake pairs |
|---:|---|
| 1 | `(1,2)`, `(3,4)`, `(5,6)` |
| 2 | `(1,2)`, `(3,6)`, `(4,5)` |
| 3 | `(1,4)`, `(2,3)`, `(5,6)` |
| 4 | `(1,6)`, `(2,3)`, `(4,5)` |
| 5 | `(1,6)`, `(2,5)`, `(3,4)` |
