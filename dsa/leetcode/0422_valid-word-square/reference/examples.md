## Examples

**Example 1**

- Input: `words = ["abcd", "bnrt", "crmy", "dtye"]`
- Output: `true`
- Explanation: Each row matches its corresponding column, as the accessible grid reading below shows. Therefore,
  the words form a valid word square.

| Position | Row | Column |
|---:|---|---|
| 1 | `abcd` | `abcd` |
| 2 | `bnrt` | `bnrt` |
| 3 | `crmy` | `crmy` |
| 4 | `dtye` | `dtye` |

**Example 2**

- Input: `words = ["abcd", "bnrt", "crm", "dt"]`
- Output: `true`
- Explanation: The ragged rows still match all corresponding columns, so this is a valid word square.

| Position | Row | Column |
|---:|---|---|
| 1 | `abcd` | `abcd` |
| 2 | `bnrt` | `bnrt` |
| 3 | `crm` | `crm` |
| 4 | `dt` | `dt` |

**Example 3**

- Input: `words = ["ball", "area", "read", "lady"]`
- Output: `false`
- Explanation: The third row reads `read`, but the third column reads `lead`. The mismatch makes the word square
  invalid.

| Position | Row | Column |
|---:|---|---|
| 1 | `ball` | `ball` |
| 2 | `area` | `area` |
| 3 | `read` | `lead` |
| 4 | `lady` | `lady` |
