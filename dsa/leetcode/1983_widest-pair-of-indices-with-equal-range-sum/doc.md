# Widest Pair of Indices With Equal Range Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1983 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/widest-pair-of-indices-with-equal-range-sum/) |

## Problem Description
### Goal
You are given two 0-indexed binary arrays `nums1` and `nums2` of the same
length. Choose indices `i` and `j` with $i \le j$ so that the sum of
`nums1[i:j + 1]` equals the sum over the identical inclusive range in `nums2`.
Only corresponding ranges with the same endpoints may be compared.

The width of such a pair is $j - i + 1$. Return the greatest achievable width
over all qualifying index pairs. If no nonempty range has equal sums in the two
arrays, return `0`.

### Function Contract
**Inputs**

- `nums1`: a binary list of length $N$.
- `nums2`: another binary list of the same length $N$, where
  $1 \le N \le 10^5$.

**Return value**

- The maximum length of a nonempty corresponding range whose sums in `nums1`
  and `nums2` are equal, or `0` if no such range exists.

### Examples
**Example 1**

- Input: `nums1 = [1, 1, 0, 1], nums2 = [0, 1, 1, 0]`
- Output: `3`

The range from index `1` through index `3` sums to `2` in both arrays.

**Example 2**

- Input: `nums1 = [0, 1], nums2 = [1, 1]`
- Output: `1`

The values at index `1` match, so that single-position range qualifies.

**Example 3**

- Input: `nums1 = [0], nums2 = [1]`
- Output: `0`

### Required Complexity
- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Convert two range sums into one prefix difference**

At each index, add `nums1[index] - nums2[index]` to a running difference.
The difference after index `j` equals the first array's prefix sum through `j`
minus the second array's corresponding prefix sum. Treat difference `0` as
already occurring at virtual index `-1`, before either array begins.

For a range from `i` through `j`, the two range sums are equal exactly when the
prefix difference after `j` equals the prefix difference before `i`. The
contributions preceding `i` then cancel from both sides.

**Keep only the earliest occurrence**

Store the first index at which each prefix difference occurs. When the same
difference appears again at index `j`, the range following its stored index
through `j` has equal sums, and its width is the distance between those two
prefix positions. Using the earliest occurrence produces the widest possible
range ending at `j`; replacing it with a later index could only shorten every
future candidate.

Take the maximum width over all repeated differences. If no difference repeats,
no nonempty equal-sum range exists and the initial answer `0` remains correct.

#### Complexity detail

The paired scan processes all $N$ positions once. Hash-table lookup and
insertion take expected constant time, giving $O(N)$ total time. At most
$2N + 1$ different prefix differences are possible, and at most $N + 1$ are
encountered, so the earliest-index map uses $O(N)$ space.

#### Alternatives and edge cases

- **Check every range:** Prefix sums can compare one chosen range in constant
  time, but enumerating all endpoint pairs still takes $O(N^2)$ time.
- **Difference array plus longest zero-sum subarray:** Materialize
  `nums1[index] - nums2[index]` and apply the standard longest zero-sum-range
  algorithm. This is equivalent but uses an unnecessary extra array.
- If the complete arrays have equal sums, prefix difference `0` repeats after
  the final position and the answer is $N$.
- Equal values at a single index form a valid width-one range even if no longer
  range qualifies.
- A strictly increasing or decreasing prefix difference never repeats, so the
  correct result is `0`.
- The arrays contain only binary values, but the running difference may be
  negative and must be stored without assuming a nonnegative index.

</details>
