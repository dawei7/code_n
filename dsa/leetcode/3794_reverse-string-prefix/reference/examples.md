## Examples

**Example 1**

- Input: `s = "abcd", k = 2`
- Output: `"bacd"`
- Explanation:
  - The selected prefix `"ab"` has length `k = 2` and becomes `"ba"` when reversed.
  - Appending the unchanged suffix `"cd"` produces `"bacd"`.

**Example 2**

- Input: `s = "xyz", k = 3`
- Output: `"zyx"`
- Explanation:
  - Here `k = 3` selects the entire string `"xyz"`.
  - Its reversal is `"zyx"`, and there is no remaining suffix.

**Example 3**

- Input: `s = "hey", k = 1`
- Output: `"hey"`
- Explanation:
  - Reversing the one-character prefix `"h"` leaves that prefix unchanged.
  - Joining it with the untouched suffix `"ey"` returns `"hey"`.
