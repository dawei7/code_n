# Reverse Subarray To Maximize Array Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1330 |
| Difficulty | Hard |
| Topics | Array, Math, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/) |

## Problem Description
### Goal
The value of an integer array is the sum of the absolute differences between every adjacent pair. For `nums`, it is

$$
V=\sum_{i=0}^{n-2}\lvert\texttt{nums[i]}-\texttt{nums[i+1]}\rvert.
$$

Choose one contiguous subarray and reverse its elements. The operation may cover any nonempty range, including the entire array; ranges of length one leave the array unchanged.

Return the maximum possible value after this one allowed reversal. Array elements may be negative, and the result is guaranteed to fit in a signed 32-bit integer.

### Function Contract
**Inputs**

- `nums`: an integer array of length $n$, where $2\le n\le3\cdot10^4$ and $-10^5\le\texttt{nums[i]}\le10^5$.

**Return value**

The greatest adjacent-difference sum obtainable after reversing one contiguous subarray.

### Examples
**Example 1**

- Input: `nums = [2,3,1,5,4]`
- Output: `10`
- Explanation: Reversing `[3,1,5]` produces `[2,5,1,3,4]`, whose adjacent differences sum to 10.

**Example 2**

- Input: `nums = [2,4,9,24,2,1,10]`
- Output: `68`

**Example 3**

- Input: `nums = [1,2,3]`
- Output: `3`
- Explanation: Reversing the first two values yields `[2,1,3]`.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Only reversal boundaries can change the value**

Inside a reversed range, every original adjacent pair remains adjacent in the opposite order and contributes the same absolute difference. Therefore a reversal changes only the edge entering the range and the edge leaving it. Begin with the original value $V$ and maximize the extra boundary contribution.

**Handle reversals touching an array endpoint**

For each adjacent pair `(a, b)`, reversing a prefix that ends at `a` replaces the pair's contribution with the distance from `nums[0]` to `b`. Reversing a suffix that starts at `b` replaces it with the distance from `a` to `nums[-1]`. Test both gains for every pair.

**Compress every interior choice into two extrema**

An interior reversal selects two cut edges. For an edge with endpoint values `a` and `b`, record its smaller endpoint $\min(a,b)$ and larger endpoint $\max(a,b)$. Across all edges, let $H$ be the greatest smaller endpoint and $L$ the least larger endpoint.

Pairing the edges that realize these extrema yields the best interior improvement,

$$
2(H-L),
$$

when it is positive. This follows from expanding the two possible cross-boundary absolute differences: the reversal can replace two edges by connections spanning the gap between the highest lower endpoint and lowest upper endpoint, counted twice. Taking the maximum of this gain, the endpoint gains, and zero covers every reversal form. Add that best gain to $V$.

#### Complexity detail

One pass computes $V$, tests both endpoint gains, and updates $H$ and $L$ for each of the $n-1$ edges. This takes $O(n)$ time and a constant number of scalar variables, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Enumerate reversal boundaries:** Computing the two-edge gain for every pair of boundaries is correct but takes $O(n^2)$ time.
- **Reverse and rescore every range:** Materializing each candidate and recomputing its value can take $O(n^3)$ time.
- **Two elements:** Reversing them preserves their sole absolute difference.
- **Equal values:** Zero-difference edges are valid cut choices; an all-equal array remains valued at 0.
- **Negative values:** Absolute differences and min/max endpoint reasoning apply without modification.
- **No beneficial reversal:** A length-one or whole-array reversal preserves $V$, so the maximum never falls below the original value.

</details>
