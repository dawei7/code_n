## Examples

**Example 1**

- Input: `n = 3`
- Output: `3`
- Explanation: Use all three keypresses on `A`, producing the sequence `A, A, A` and leaving three characters on the screen.

**Example 2**

- Input: `n = 7`
- Output: `9`
- Explanation: The sequence `A, A, A, Ctrl-A, Ctrl-C, Ctrl-V, Ctrl-V` first creates three characters, copies the whole screen, and then appends that three-character buffer twice. The screen therefore contains nine `A` characters.
