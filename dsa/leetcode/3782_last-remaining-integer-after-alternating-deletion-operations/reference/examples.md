## Examples

**Example 1**

- Input: `n = 8`
- Output: `3`
- Explanation:
  - Start with `[1, 2, 3, 4, 5, 6, 7, 8]`.
  - The first left-to-right sweep removes `2`, `4`, `6`, and `8`, leaving `[1, 3, 5, 7]`.
  - The right-to-left sweep visits `7` first, then removes `5`, keeps `3`, and removes `1`. In left-to-right order, the survivors are `[3, 7]`.
  - The final left-to-right sweep keeps `3` and removes `7`, so `3` remains.

**Example 2**

- Input: `n = 5`
- Output: `1`
- Explanation:
  - Start with `[1, 2, 3, 4, 5]`.
  - Sweeping from the left removes `2` and `4`, producing `[1, 3, 5]`.
  - Sweeping from the right keeps `5`, removes `3`, and keeps `1`; the remaining sequence is `[1, 5]`.
  - The next left-to-right sweep removes `5`, leaving `1`.

**Example 3**

- Input: `n = 1`
- Output: `1`
- Explanation:
  - The initial sequence is already `[1]`, so no deletion operation is needed and `1` is the last integer.
