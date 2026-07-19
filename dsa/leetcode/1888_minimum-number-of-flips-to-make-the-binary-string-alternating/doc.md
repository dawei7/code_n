# Minimum Number of Flips to Make the Binary String Alternating

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/) |
| Frontend ID | 1888 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Given a binary string `s`, two operations may be applied in any order and any number of times. A type-1 operation removes the first character and appends it to the end, cyclically rotating the string left by one position. A type-2 operation chooses any one position and flips its bit from `0` to `1` or from `1` to `0`.

A binary string is alternating when every adjacent pair contains different characters, as in `010` or `1010`. Use type-1 rotations freely, and return the minimum number of type-2 flips needed to obtain an alternating string. Only bit flips contribute to the returned cost.

### Function Contract

**Inputs**

- `s`: a binary string of length $N$ containing only `0` and `1`.
- $1 \le N \le 10^5$.

**Return value**

- Return the minimum number of type-2 bit flips needed after choosing any number of type-1 left rotations.

### Examples

**Example 1**

- Input: `s = "111000"`
- Output: `2`

Two left rotations produce `100011`; flipping its third and sixth characters yields `101010`.

**Example 2**

- Input: `s = "010"`
- Output: `0`

The original string is already alternating.

**Example 3**

- Input: `s = "1110"`
- Output: `1`

Flipping the second character produces `1010`.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Represent every rotation as a circular window**

Any sequence of type-1 operations selects a cyclic rotation of `s`. View the characters through virtual indices from $0$ to $2N-1$, reading position $i$ as the original character at index $i \bmod N$. Every rotation is then a contiguous window of length $N$ in this virtual doubled sequence; no doubled string needs to be stored.

There are only two alternating patterns at those virtual indices: one expects `0` at even indices and `1` at odd indices, while the other expects the opposite. For a fixed window, the number of mismatches against a pattern is exactly the number of type-2 flips required to realize it.

**Slide both mismatch counts**

Scan the virtual indices while maintaining the mismatch totals for both patterns. Add the entering character's mismatch. Once the window would exceed length $N$, subtract the outgoing character's mismatch. For each full-length window, minimize the answer with both totals.

Every possible cyclic rotation appears as one such window, and every alternating binary string must match one of the two patterns. The mismatch total is both necessary—each wrong position must be flipped—and sufficient—flipping exactly those positions produces the pattern. Taking the minimum across all windows and both patterns therefore gives the optimal number of paid operations.

#### Complexity detail

The scan processes $2N$ virtual positions, doing constant work at each, so it takes $O(N)$ time. It stores two mismatch counters, window indices, and the current minimum. Characters are read from the original string with modular indices, so the auxiliary-space bound is $O(1)$ rather than $O(N)$.

#### Alternatives and edge cases

- **Materialize `s + s`:** The same sliding-window reasoning is simpler to visualize with a doubled string and still takes $O(N)$ time, but it uses $O(N)$ auxiliary space.
- **Check every rotation independently:** Comparing all $N$ rotations with both alternating patterns is correct but takes $O(N^2)$ time.
- **Single character:** It is already alternating, so no flip is needed.
- **Odd length:** Moving one character across the boundary changes its parity, so different rotations can have different costs.
- **Even length:** A rotation may swap which of the two patterns is named first, but both mismatch totals are always considered.
- **Free rotations:** Type-1 operations are never added to the answer; only type-2 flips are counted.

</details>
