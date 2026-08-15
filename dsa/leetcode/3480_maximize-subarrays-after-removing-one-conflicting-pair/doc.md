# Maximize Subarrays After Removing One Conflicting Pair

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3480 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Segment Tree, Enumeration, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/) |

## Problem Description

### Goal

The integer `n` represents the ordered array containing every value from $1$ through $n$ exactly once. Each entry `[a, b]` in `conflictingPairs` declares that the two values $a$ and $b$ conflict.

Remove exactly one entry from `conflictingPairs`. After that removal, a non-empty subarray is valid when it does not contain both values from any remaining conflicting pair. The values themselves stay in the ordered array; only one conflict rule is discarded.

Return the maximum possible number of valid non-empty subarrays. The same removed pair must be used for the entire count.

### Function Contract

**Inputs**

- `n`: The final value and length of the implicit array `[1, 2, ..., n]`.
- `conflictingPairs`: A non-empty list of two-value conflict rules.

The constraints are $2 \le n \le 10^5$ and $1 \le \lvert\texttt{conflictingPairs}\rvert \le 2n$. Each pair contains two distinct values from $1$ through $n$.

**Return value**

Return the largest number of valid non-empty subarrays obtainable after removing exactly one conflicting-pair entry.

### Examples

#### Example 1

- **Input:** `n = 4`, `conflictingPairs = [[2, 3], [1, 4]]`
- **Output:** `9`

Removing `[2, 3]` leaves only the conflict `[1, 4]`. Of the ten non-empty subarrays of `[1, 2, 3, 4]`, only the complete array contains both remaining conflicting values, so nine are valid.

#### Example 2

- **Input:** `n = 5`, `conflictingPairs = [[1, 2], [2, 5], [3, 5]]`
- **Output:** `12`

Removing `[1, 2]` leaves the two conflicts ending at value 5. The maximum valid-subarray count is then twelve.
