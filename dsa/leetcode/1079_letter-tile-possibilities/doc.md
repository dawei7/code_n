# Letter Tile Possibilities

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1079 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Backtracking, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [letter-tile-possibilities](https://leetcode.com/problems/letter-tile-possibilities/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/letter-tile-possibilities/).

### Goal
Given a multiset of letter tiles, count how many non-empty sequences can be formed by choosing any positive number of tiles and arranging them. Tiles with the same letter are indistinguishable.

### Function Contract
**Inputs**

- `tiles`: String whose characters represent available letter tiles.

**Return value**

Number of distinct non-empty sequences that can be made.

### Examples
**Example 1**

- Input: `tiles = "AAB"`
- Output: `8`

**Example 2**

- Input: `tiles = "AAABBC"`
- Output: `188`

**Example 3**

- Input: `tiles = "V"`
- Output: `1`

---

## Solution
### Approach
Count how many tiles of each letter are available. Backtrack by choosing one letter with a positive remaining count, appending it to the current sequence, and recursing after decrementing its count.

Every time a letter is chosen, one new non-empty sequence has been formed, so add `1` before exploring deeper choices. Using counts instead of individual tiles naturally avoids duplicates caused by repeated letters.

### Complexity Analysis
- **Time Complexity**: `O(P)`, where `P` is the number of distinct non-empty sequences generated.
- **Space Complexity**: `O(k)` for recursion and counts, where `k` is the number of tile types plus recursion depth.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
