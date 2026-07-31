## Examples

**Example 1**

- Input: `n = 3, edges = [[0,1],[1,2]], baseTime = [9,5,3]`
- Output: `17`
- **Explanation:** Task `2` is a leaf and finishes at `3`. Task `1` has that single child, so `earliest = latest = 3`, its own duration is `5`, and it finishes at `3 + 5 = 8`. Task `0` likewise has one child finishing at `8`; its own duration is `9`, so the root finishes at `8 + 9 = 17`.

**Example 2**

- Input: `n = 3, edges = [[0,1],[0,2]], baseTime = [4,7,6]`
- Output: `12`
- **Explanation:** Leaf tasks `1` and `2` finish at `7` and `6`. For task `0`, `earliest = 6` and `latest = 7`, so its own duration is `(7 - 6) + 4 = 5`. The root finish time is `7 + 5 = 12`.

**Example 3**

- Input: `n = 4, edges = [[0,1],[0,2],[2,3]], baseTime = [5,8,2,1]`
- Output: `18`
- **Explanation:** Task `1` finishes at `8`, while leaf task `3` finishes at `1`. Task `2` has only task `3` as a child, so its own duration is `2` and it finishes at `1 + 2 = 3`. The root's children therefore finish at `8` and `3`; `earliest = 3`, `latest = 8`, and the root's own duration is `(8 - 3) + 5 = 10`. Its finish time is `8 + 10 = 18`.
