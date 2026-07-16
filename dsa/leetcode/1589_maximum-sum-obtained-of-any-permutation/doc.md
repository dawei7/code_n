# Maximum Sum Obtained of Any Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1589 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/) |

## Problem Description
### Goal

You are given an integer array `nums` and several requests. Each request `[start, end]` asks for the sum of the values at every index from `start` through `end`, including both endpoints. All indices are zero-based.

Before evaluating the requests, you may permute the values of `nums` in any way. The same chosen permutation is then used for every request. Find the largest possible total after adding all requested range sums together.

Return that maximum modulo $10^9+7$.

### Function Contract
**Inputs**

- `nums`: An array of $N$ integers, where $1 \le N \le 10^5$ and $0 \le \texttt{nums[i]} \le 10^5$.
- `requests`: An array of $R$ inclusive ranges `[start, end]`, where $1 \le R \le 10^5$ and $0 \le \texttt{start} \le \texttt{end} < N$.

**Return value**

Return the maximum total of all request sums over every permutation of `nums`, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4,5], requests = [[1,3],[0,1]]`
- Output: `19`

**Example 2**

- Input: `nums = [1,2,3,4,5,6], requests = [[0,1]]`
- Output: `11`

**Example 3**

- Input: `nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]]`
- Output: `47`

### Required Complexity

- **Time:** $O(N\log N+R)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Replace all range sums with one weighted sum**

For every array index, count how many requests include it. If index `i` is covered $c_i$ times, then the value placed there contributes $c_i$ copies of itself to the total. After choosing a permutation `p`, the objective is therefore

$$
\sum_{i=0}^{N-1} c_i\,\texttt{p[i]}.
$$

This separates the fixed request geometry, represented by the coverage counts, from the movable values.

**Compute coverage with a difference array**

Create `difference` of length $N+1$. For an inclusive request `[left, right]`, add one at `difference[left]` and subtract one at `difference[right + 1]`. The prefix sum of this array is increased exactly from `left` through `right`, so one scan recovers every $c_i$ after $O(1)$ work per request.

The extra position at index $N$ makes `right + 1` safe even when a request ends at the final array element.

**Pair large values with heavily requested positions**

Sort both `nums` and the coverage counts in the same order and multiply corresponding entries. To see why this is optimal, suppose $a \le b$ are values assigned to counts $x \le y$. Their aligned contribution is $ax+by$. Swapping them would give $ay+bx$, smaller by

$$
(b-a)(y-x) \ge 0.
$$

Thus every inversion in which a larger value is paired with a smaller count can be removed without reducing the total. Repeating this exchange argument yields the sorted pairing, so the computed dot product is maximum. Apply the modulus only to the final sum; modular reduction does not affect which ordinary integer total is largest.

#### Complexity detail

Processing $R$ requests and prefix-summing coverage takes $O(N+R)$ time. Sorting the $N$ values and $N$ counts takes $O(N\log N)$ time, which dominates, for total $O(N\log N+R)$.

The difference/coverage storage and sorted arrays require $O(N)$ auxiliary space.

#### Alternatives and edge cases

- **Endpoint-event map:** store `+1` and `-1` events in a dictionary and sweep all indices. It has the same asymptotic complexity and is an independent form of the difference-array method.
- **Increment every requested index:** directly add one throughout each range. It is correct but can require $O(NR)$ time when many requests span most of the array.
- **Try permutations:** enumerating $N!$ arrangements is infeasible and ignores the weighted-sum structure.
- **Single request:** assign the largest values to that request's covered positions; uncovered positions have weight zero.
- **Repeated or nested requests:** every occurrence contributes separately to coverage.
- **Whole-array requests:** all positions gain the same weight, so their internal permutation is irrelevant.
- **Zero values:** sorting naturally places them at the least-covered positions.
- **Inclusive right endpoint:** decrement at `right + 1`, not at `right`.
- **Large total:** compute the full weighted sum with adequate integer range and return it modulo $10^9+7$.

</details>
