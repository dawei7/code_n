# Maximum Size Subarray Sum Equals k

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 325 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/) |

## Problem Description
### Goal
Given an integer array that may contain positive values, negative values, and zeroes, choose a nonempty contiguous subarray whose elements sum exactly to `k`. The interval must use consecutive positions and cannot wrap around or skip elements.

Return the maximum length among all qualifying intervals, or `0` when none exists. Negative numbers mean extending a subarray can either increase or decrease its sum, so ordinary positive-only window assumptions do not apply. Several intervals may share the maximum length; only that length is returned, not the endpoints or subarray values.

### Function Contract
**Inputs**

- `nums`: the integer array
- `k`: the required subarray sum

**Return value**

The greatest length among contiguous subarrays summing to `k`, or zero if none exists.

### Examples
**Example 1**

- Input: `nums = [1,-1,5,-2,3], k = 3`
- Output: `4`

**Example 2**

- Input: `nums = [-2,-1,2,1], k = 1`
- Output: `2`

**Example 3**

- Input: `nums = [1,2,3], k = 7`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Turn a subarray sum into a difference of prefixes**

Let the running prefix through index `i` be `P`. A subarray starting after index `j` and ending at `i` sums to `k` exactly when `P - prefix[j] = k`, or equivalently `prefix[j] = P - k`.

Maintain a hash table from each prefix sum to the earliest index where it occurred. At each position, update the running sum and look for `running - k`. If present at index `j`, the subarray from $j + 1$ through the current position is valid, so compare its length with the best seen.

Seed the table with prefix sum zero at index `-1`. This represents the empty prefix before the array and lets a valid subarray beginning at index zero use the same formula.

**Preserve the earliest occurrence of every prefix**

When a prefix value repeats, do not replace its stored index. For a fixed ending index, the earliest matching prefix produces the longest subarray. A later occurrence can never yield a better length for this or any future end.

For `[1,-1,5,-2,3]` with target three, prefix zero is first stored at `-1` and appears again after `-1`; the earlier index is retained. At index three the running sum is three, so matching prefix zero gives length four for `[1,-1,5,-2]`.

Every reported interval is correct because subtracting its stored prefix from the current prefix equals `k`. Conversely, if an optimal interval ends at `i`, its preceding prefix sum is `running - k`; that value was stored when its earliest occurrence was scanned. The lookup therefore considers an interval at least as long as the optimum ending at `i`, proving the global maximum is found.

#### Complexity detail

The scan performs one expected-constant-time lookup and insertion per element, giving $O(n)$ expected time. At most $n + 1$ distinct prefix sums are stored, using $O(n)$ space.

#### Alternatives and edge cases

- **Enumerate every start and end:** is correct but takes $O(n^2)$ time even when rolling sums avoid a third loop.
- **Sliding window:** is not valid when negative values can make expansion decrease the sum or contraction increase it.
- **Overwrite repeated prefix indices:** can preserve correctness but lose the longest possible interval.
- Target zero and repeated zero prefixes are handled naturally. A whole-array match uses the seeded index `-1`, and no match leaves the answer at zero.

</details>
