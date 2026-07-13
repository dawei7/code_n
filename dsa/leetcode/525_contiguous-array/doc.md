# Contiguous Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 525 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/contiguous-array/) |

## Problem Description
### Goal
Given a binary array `nums`, choose a contiguous subarray and count its `0` and `1` values. A qualifying interval contains exactly the same number of zeroes as ones, so its length is necessarily even.

Return the maximum length of a qualifying contiguous subarray. The interval cannot skip positions or combine separated pieces, and equal total counts elsewhere in the array do not help a selected interval. If no nonempty balanced interval exists, return `0`; the function returns only the length, not the endpoints or balanced values.

### Function Contract
**Inputs**

- `nums`: a binary integer array

**Return value**

- The greatest length of a contiguous interval with equal zero and one counts, or `0` when none exists

### Examples
**Example 1**

- Input: `nums = [0, 1]`
- Output: `2`

**Example 2**

- Input: `nums = [0, 1, 0]`
- Output: `2`

**Example 3**

- Input: `nums = [0, 1, 1, 1, 1, 1, 0, 0, 0]`
- Output: `6`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Encode zeros and ones as opposite contributions**

Treat a one as `+1` and a zero as `-1`. The running balance after an index is therefore `ones - zeros` for that prefix. A subarray is balanced exactly when its net contribution is zero.

**Match equal prefix balances**

If the same balance appears at prefix boundaries `left` and `right`, subtracting those prefix totals gives zero across the elements between them. Initialize balance zero at virtual index `-1` so a balanced prefix beginning at index zero is handled identically.

**Keep only the earliest index for each balance**

When a balance repeats, its longest interval ending at the current index starts at the earliest occurrence. Compute that distance and update the maximum, but never replace the stored index. A later copy could only shorten every future interval with the same ending balance.

**Why every optimal interval is considered**

Any interval with equal zero and one counts has zero encoded sum, so the prefix balances immediately before and after it are equal. The scan finds that repeated balance at the interval's right boundary and compares against an occurrence no later than its true left boundary, producing an interval at least as long. Since every produced interval is balanced, the recorded maximum is exact.

#### Complexity detail

The scan performs expected constant-time hash operations for each of `n` values, giving $O(n)$ time. At most $2n + 1$ balance values are possible and at most $n + 1$ are observed, so space is $O(n)$.

#### Alternatives and edge cases

- **Array indexed by shifted balance:** replaces the hash table with a $2n + 1$ array and has the same bounds.
- **Enumerate all subarrays:** is correct but takes $O(n^2)$ time even when counts are updated incrementally.
- **Prefix sums plus every boundary pair:** makes balance tests constant time but still checks quadratically many intervals.
- **All zeros or all ones:** no positive-length balanced interval exists.
- **Balanced complete array:** the virtual prefix permits returning the full length.
- **Odd-length interval:** can never contain equal counts.
- **Repeated balance:** retain its earliest position, not the latest.

</details>
