# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1343 |
| Difficulty | Medium |
| Topics | Array, Sliding Window |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/) |

## Problem Description
### Goal
Given an integer array `arr`, examine every contiguous subarray containing exactly `k` elements. A window qualifies when the arithmetic average of its elements is greater than or equal to `threshold`.

Return the number of qualifying windows. Overlapping subarrays are counted separately, the comparison is inclusive, and a non-integer average must be compared at its actual value rather than after rounding or integer division.

### Function Contract
**Inputs**

- `arr`: a positive-integer array of length $n$, where $1\le n\le10^5$ and $1\le\texttt{arr[i]}\le10^4$.
- `k`: the exact window length, where $1\le k\le n$.
- `threshold`: the minimum permitted average, where $0\le\texttt{threshold}\le10^4$.

**Return value**

The number of length-`k` contiguous subarrays whose average is at least `threshold`.

### Examples
**Example 1**

- Input: `arr = [2,2,2,2,5,5,5,8]`, `k = 3`, `threshold = 4`
- Output: `3`

**Example 2**

- Input: `arr = [11,13,17,23,29,31,7,5,2,3]`, `k = 3`, `threshold = 5`
- Output: `6`
- Explanation: Averages need not be integers.

**Example 3**

- Input: `arr = [1,1,1,1]`, `k = 2`, `threshold = 2`
- Output: `0`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Compare sums instead of dividing**

A length-`k` window has average at least `threshold` exactly when its sum is at least `k * threshold`. This equivalent integer comparison avoids both floating-point representation and accidental truncation.

Compute the sum of the first `k` elements and test it. Then move the window one position at a time: add the newly entering element and subtract the element that just left. Test the updated sum after every move and increment the answer when it reaches the target.

The initial sum is exact for the first window. Each update removes precisely the old left endpoint and adds precisely the new right endpoint, so by induction it remains the exact sum of the current window. Every possible length-`k` start is visited once, proving the final count.

#### Complexity detail

The initial window and all subsequent updates together read $O(n)$ elements and take $O(n)$ time. The rolling sum, target, and counter use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Prefix sums:** A prefix array answers every window sum in constant time after $O(n)$ preprocessing, but uses $O(n)$ extra space.
- **Rescan every window:** Explicitly summing each length-`k` subarray takes $O(nk)$ time and can become quadratic.
- **Window length one:** Compare each individual value with the threshold.
- **Whole array window:** When $k=n$, exactly one subarray is tested.
- **Exact threshold:** Equality qualifies.
- **Fractional average:** Compare sums rather than applying integer division.
- **Zero threshold:** Every legal positive-value window qualifies.
- **Overlapping windows:** Count each qualifying start independently.

</details>
