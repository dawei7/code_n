## Examples

**Example 1**

- Input: `s = "aaccb"`
- Output: `"aacb"`
- Explanation:
  - The reachable strings are `"acb"`, `"aacb"`, `"accb"`, and `"aaccb"`.
  - Among those four strings, `"aacb"` is lexicographically smallest.
  - One way to produce it is to choose `'c'` and delete the first occurrence of that letter.

**Example 2**

- Input: `s = "z"`
- Output: `"z"`
- Explanation:
  - No operation can be performed because no letter occurs twice.
  - Consequently, `"z"` is the only string that can be formed.
