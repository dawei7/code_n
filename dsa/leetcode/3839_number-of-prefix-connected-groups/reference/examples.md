## Examples

**Example 1**

- Input: `words = ["apple","apply","banana","bandit"], k = 2`
- Output: `2`
- Explanation: The words are grouped by their first `k = 2` letters:
  - `words[0] = "apple"` and `words[1] = "apply"` share the prefix `"ap"`.
  - `words[2] = "banana"` and `words[3] = "bandit"` share the prefix `"ba"`.

Thus, there are two connected groups, and each contains at least two words.

**Example 2**

- Input: `words = ["car","cat","cartoon"], k = 3`
- Output: `1`
- Explanation: The words are evaluated using prefixes of length `k = 3`:
  - `words[0] = "car"` and `words[2] = "cartoon"` share the prefix `"car"`.
  - `words[1] = "cat"` has no other word with the same length-3 prefix.

Thus, there is one connected group.

**Example 3**

- Input: `words = ["bat","dog","dog","doggy","bat"], k = 3`
- Output: `2`
- Explanation: The words are evaluated using prefixes of length `k = 3`:
  - `words[0] = "bat"` and `words[4] = "bat"` form one group.
  - `words[1] = "dog"`, `words[2] = "dog"`, and `words[3] = "doggy"` share the prefix `"dog"`.

Thus, there are two connected groups, and each contains at least two words.
