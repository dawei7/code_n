# Minimum Domino Rotations For Equal Row

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1007 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/) |

## Problem Description

### Goal

A row contains $N$ dominoes. For domino `i`, `tops[i]` is the number on its top half and `bottoms[i]` is the number on its bottom half; every number is from `1` through `6`.

You may rotate any domino, swapping its top and bottom values. Return the minimum number of rotations required to make every value in `tops` the same or every value in `bottoms` the same. If neither row can be made uniform, return `-1`.

### Function Contract

**Inputs**

- `tops`: an array of $N$ top-half values, where $2\le N\le2\cdot10^4$ and every value is from `1` through `6`.
- `bottoms`: an array of $N$ bottom-half values with `bottoms.length == tops.length` and the same value range.

**Return value**

- The minimum number of domino rotations that makes either entire row equal, or `-1` when no such arrangement exists.

### Examples

**Example 1**

- Input: `tops = [2, 1, 2, 4, 2, 2], bottoms = [5, 2, 6, 2, 3, 2]`
- Output: `2`
- Explanation: Rotating the second and fourth dominoes makes every top value equal to `2`.

**Example 2**

- Input: `tops = [3, 5, 1, 2, 3], bottoms = [3, 6, 3, 3, 4]`
- Output: `-1`
- Explanation: No number occurs on at least one half of every domino, so neither row can become uniform.

**Example 3**

- Input: `tops = [1, 1, 1], bottoms = [2, 3, 4]`
- Output: `0`
- Explanation: The top row is already uniform.

### Required Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Restrict the target using the first domino:** If a value can fill an entire row, it must appear on either half of every domino. In particular, it must equal `tops[0]` or `bottoms[0]`. These are therefore the only candidates that need validation, regardless of the row length.

**Count both possible destination rows:** For one candidate `target`, scan paired values `top` and `bottom`. If neither equals `target`, that candidate is impossible. Otherwise, a top-row solution must rotate exactly those dominoes whose top differs from `target`, while a bottom-row solution must rotate exactly those whose bottom differs. The smaller counter is the best result for this candidate.

**Choose the best feasible candidate:** Validate both values from the first domino and take the minimum finite count. Return `-1` only when both fail. If the first domino shows the same number on both halves, evaluating it twice is harmless and still constant extra work.

Any uniform final row must use one of the two candidates, and the scan determines the forced rotations for each destination row. Consequently, the minimum across these exhaustive possibilities cannot omit a better arrangement and never counts an unnecessary rotation.

#### Complexity detail

At most two candidates are checked, and each check visits all $N$ dominoes once, giving $O(N)$ time. The candidate values and two rotation counters use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Validate every observed value:** Trying each of the $2N$ top and bottom entries as a candidate is correct but can repeat the same full scan and take $O(N^2)$ time.
- **Frequency tables:** Counting top, bottom, and double occurrences for the six face values also gives $O(N)$ time, but needs more bookkeeping than validating the first domino's candidates.
- **Already uniform row:** Its rotation count is zero and must win even if the other row can also be made uniform.
- **Candidate missing from one domino:** Reject it immediately because rotating that domino cannot create a value absent from both halves.
- **Equal halves:** Rotating a domino whose two halves match changes nothing and is never required.

</details>
