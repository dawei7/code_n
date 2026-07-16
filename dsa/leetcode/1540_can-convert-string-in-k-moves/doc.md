# Can Convert String in K Moves

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1540 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/can-convert-string-in-k-moves/) |

## Problem Description
### Goal
You are given lowercase strings `s` and `t` and may perform at most `k` numbered moves. On move $i$, either do nothing or choose one position that has never been chosen before and advance its character by exactly $i$ alphabet steps. Shifts wrap around from `z` to `a`.

Each position can therefore be changed at most once, and two positions cannot both use the same move number. Determine whether some choices among moves $1$ through $k$ transform every character of `s` into the corresponding character of `t`. Strings of different lengths cannot be converted.

### Function Contract
**Inputs**

- `s`: the source string of lowercase English letters.
- `t`: the desired string of lowercase English letters.
- `k`: the greatest available move number, where $0 \le k \le 10^9$.
- Each string length is between $1$ and $10^5$.

**Return value**

`True` if `s` can be converted into `t` using no more than the first `k` moves; otherwise `False`.

### Examples
**Example 1**

- Input: `s = "input", t = "ouput", k = 9`
- Output: `True`
- Explanation: Use move `6` for `i` to `o` and move `7` for `n` to `u`.

**Example 2**

- Input: `s = "abc", t = "bcd", k = 10`
- Output: `False`
- Explanation: All three positions need shift `1`, but only move `1` supplies that residue within ten moves.

**Example 3**

- Input: `s = "aab", t = "bbb", k = 27`
- Output: `True`
- Explanation: The two `a` positions can use moves `1` and `27`, which are congruent modulo 26.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reduce each position to a shift residue**

For a source character and target character, the only relevant quantity is their forward cyclic difference from `0` through `25`. A zero difference needs no move. A nonzero difference `d` can use exactly the positive move numbers

`d, d + 26, d + 52, ...`

because adding 26 alphabet steps leaves the resulting letter unchanged.

**Schedule repeated residues in their earliest moves**

Maintain how many positions have already required each nonzero residue. If residue `d` has appeared `count` times before, its earliest unused compatible move is `d + 26 * count`. Reject immediately if that move exceeds `k`; otherwise reserve it by incrementing the count.

This greedy choice cannot harm another residue because different residues use disjoint move-number sequences modulo 26. Within one residue, assigning occurrences to compatible moves in increasing order is optimal: any other one-to-one assignment has a greatest move at least as large. Therefore every required position can be scheduled within `k` exactly when none of these earliest available moves exceeds the limit.

**Handle unchanged characters separately**

Positions where the characters already match do not consume a move. Treating their difference as residue zero would be wrong because move zero does not exist and moves `26`, `52`, and so on would unnecessarily alter scheduling. Skip them entirely.

Before scanning, compare the string lengths. A move changes a character but never inserts or deletes one, so unequal lengths make conversion impossible regardless of `k`.

#### Complexity detail

Let $n$ be the common string length. The algorithm examines each paired character once for $O(n)$ time. Its 26 residue counters occupy fixed $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Search previous positions for the same shift:** correctly finds which compatible move occurrence is needed, but repeated prefix scans take $O(n^2)$ time.
- **Store every assigned move in a set:** can test collisions, but uses $O(n)$ space and obscures the simpler residue-count structure.
- Equal strings are always convertible, including when `k = 0`, because every move may be skipped.
- Strings of unequal length are impossible to convert because moves cannot change length.
- Wraparound differences such as `z` to `a` require shift `1`, while `a` to `z` requires shift `25`.
- Several positions may require the same residue, but their scheduled moves must differ by 26; using the same numbered move twice is forbidden.
- A very large `k` does not require iterating through moves; only the largest assigned move for each residue matters.

</details>
