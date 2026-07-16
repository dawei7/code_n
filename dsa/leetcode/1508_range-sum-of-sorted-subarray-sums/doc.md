# Range Sum of Sorted Subarray Sums

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1508 |
| Difficulty | Medium |
| Topics | Array, Two Pointers, Binary Search, Sorting, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/range-sum-of-sorted-subarray-sums/) |

## Problem Description
### Goal

Given an array `nums` of $n$ positive integers, form the sum of every non-empty continuous subarray. There are $n(n+1)/2$ such sums. Sort this multiset in non-decreasing order, preserving duplicate values as separate entries.

Return the sum of the entries at 1-indexed positions `left` through `right`, inclusive. Because the result may be large, return it modulo $10^9+7$.

### Function Contract
**Inputs**

Let $S = \sum \texttt{nums[i]}$.

- `nums`: A non-empty array of positive integers.
- `n`: The length of `nums`.
- `left`, `right`: Inclusive 1-indexed positions satisfying $1 \leq \texttt{left} \leq \texttt{right} \leq n(n+1)/2$.

**Return value**

Return the sum of sorted subarray-sum ranks `left` through `right`, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 4], n = 4, left = 1, right = 5`
- Output: `13`
- Explanation: The sorted sums begin `[1, 2, 3, 3, 4]`, whose total is 13.

**Example 2**

- Input: `nums = [1, 2, 3, 4], n = 4, left = 3, right = 4`
- Output: `6`

**Example 3**

- Input: `nums = [1, 2, 3, 4], n = 4, left = 1, right = 10`
- Output: `50`

### Required Complexity

- **Time:** $O(n \log S)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Replace explicit sorting with a rank-prefix query**

Let $F(k)$ be the sum of the $k$ smallest subarray sums, counting duplicates. The requested interval is $F(\texttt{right})-F(\texttt{left}-1)$. It is therefore enough to compute one prefix of the conceptual sorted multiset without constructing its quadratic number of entries.

For a candidate threshold $x$, scan all subarrays whose sums are at most $x$. Positivity is crucial: for each right endpoint, increasing the left endpoint only decreases the sum. A sliding left pointer can therefore discard oversized prefixes, and all starts from that pointer through the right endpoint are valid. This counts qualifying subarrays in one pass.

**Accumulate qualifying sums in the same scan**

Ordinary prefix sums give a subarray sum as `prefix[end + 1] - prefix[start]`. For a fixed right endpoint with $c$ valid starts, their combined sum is $c$ copies of `prefix[end + 1]` minus the sum of the corresponding starting prefix values. A second prefix array over the prefix sums supplies that latter quantity in constant time.

Thus `count_and_sum(x)` returns both how many subarray sums do not exceed $x$ and their total in $O(n)$ time. Binary search the smallest $x$ whose count is at least $k$. If more than $k$ sums are at most that threshold, the extras must equal $x$ by minimality, so subtract `(count - k) * x` from the accumulated total.

**Why the two rank prefixes are exact**

At the selected threshold, every sum smaller than $x$ must belong to the first $k$ sorted entries. The remaining required positions are filled by occurrences equal to $x$; removing any surplus equal occurrences therefore leaves exactly $F(k)$. Subtracting the two exact prefixes isolates precisely ranks `left` through `right`, after which taking the modulus is safe.

#### Complexity detail

The threshold lies between 0 and $S$. Each binary-search step performs one $O(n)$ sliding-window scan, so one rank-prefix query costs $O(n\log S)$ time. Two queries preserve that bound.

The two length-$n+1$ prefix arrays use $O(n)$ space. The threshold scan itself uses constant additional state and never stores the $n(n+1)/2$ subarray sums.

#### Alternatives and edge cases

- **Generate and sort every sum:** simple and correct, but stores $\Theta(n^2)$ values and takes $O(n^2\log n)$ time in general.
- **Min-heap merge:** because all values are positive, each starting index generates an increasing sequence of sums. Merging them can produce the first `right` entries in $O((n+\texttt{right})\log n)$ time and $O(n)$ space, but approaches quadratic work when `right` is large.
- **Single element:** the only rank is the element itself.
- **Duplicate sums:** counts and the correction at the binary-search threshold must preserve multiplicity.
- **Whole rank range:** the method returns the sum of every subarray sum without materializing the sorted order.
- **Positive values:** sliding-window monotonicity depends on strict positivity; arbitrary negative values would invalidate the advancing-left argument.
- **Modulo timing:** perform threshold comparisons and rank-prefix arithmetic with full integer sums, applying the modulus only to the final interval result.

</details>
