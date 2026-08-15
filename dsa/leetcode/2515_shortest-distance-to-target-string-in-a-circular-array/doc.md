# Shortest Distance to Target String in a Circular Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2515 |
| Difficulty | Easy |
| Topics | Array, String |
| Official Link | [LeetCode](https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/) |

## Problem Description

### Goal

You are given a 0-indexed circular array of strings `words`. Its last position connects to its first: from index `i`, one forward step reaches `(i + 1) % n`, and one backward step reaches `(i - 1 + n) % n`, where $n$ is the array length.

Starting at `startIndex`, each step may move to either neighboring position. Find the fewest steps needed to reach any position whose word equals `target`.

Return `-1` when `target` does not occur in the array.

### Function Contract

**Inputs**

- `words`: A nonempty list of lowercase strings arranged circularly.
- `target`: The lowercase string to reach.
- `startIndex`: A valid 0-based starting index in `words`.

The array contains at most $100$ words, and each word and the target contain only lowercase English letters.

**Return value**

The minimum number of forward or backward steps needed to reach an occurrence of `target`, or `-1` if no occurrence exists.

### Examples

#### Example 1

- **Input:** `words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1`
- **Output:** `1`
- **Explanation:** Moving one step backward wraps from index `1` to the matching word at index `0`.

#### Example 2

- **Input:** `words = ["a","b","leetcode"], target = "leetcode", startIndex = 0`
- **Output:** `1`
- **Explanation:** One backward step wraps from index `0` to index `2`.

#### Example 3

- **Input:** `words = ["i","eat","leetcode"], target = "ate", startIndex = 0`
- **Output:** `-1`
- **Explanation:** No array position contains `ate`.
