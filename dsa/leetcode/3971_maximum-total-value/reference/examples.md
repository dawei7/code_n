## Examples

**Example 1**

- Input: `value = [6,5,4], decay = [2,1,1], m = 4`
- Output: `19`
- **Explanation:** One optimal sequence selects index `0` for gain `6`, index `1` for gain `5`, index `2` for gain `4`, and index `0` again for gain `6 - 2 = 4`. These four gains total `6 + 5 + 4 + 4 = 19`, and no sequence of at most four selections produces a larger total.

**Example 2**

- Input: `value = [7,2,2], decay = [3,2,1], m = 2`
- Output: `11`
- **Explanation:** Select index `0` twice. Its two gains are `7` and `7 - 3 = 4`, giving the optimal total `7 + 4 = 11`.

**Example 3**

- Input: `value = [4,3], decay = [5,4], m = 5`
- Output: `7`
- **Explanation:** Select index `0` once for `4` and index `1` once for `3`. Every subsequent term from either index is non-positive, so stopping after two selections yields the maximum total `4 + 3 = 7` even though up to five selections were permitted.
