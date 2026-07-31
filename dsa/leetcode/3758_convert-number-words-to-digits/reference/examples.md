## Examples

**Example 1**

- Input: `s = "onefourthree"`
- Output: `"143"`
- Explanation: Reading left to right extracts the complete words `"one"`, `"four"`, and `"three"`. They map respectively to `1`, `4`, and `3`, producing `"143"`.

**Example 2**

- Input: `s = "ninexsix"`
- Output: `"96"`
- Explanation: The first valid word is `"nine"`, which contributes `9`. The following character `"x"` is not the beginning of any valid number word, so it is skipped. The remaining `"six"` contributes `6`, yielding `"96"`.

**Example 3**

- Input: `s = "zeero"`
- Output: `""`
- Explanation: No position begins a complete valid number word. Every character is skipped, incomplete fragments are ignored, and the result remains empty.

**Example 4**

- Input: `s = "tw"`
- Output: `""`
- Explanation: No position begins a complete valid number word. The incomplete fragment is ignored as its characters are skipped, so the result is the empty string.
