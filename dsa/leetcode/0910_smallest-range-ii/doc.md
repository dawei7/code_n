# Smallest Range II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 910 |
| Difficulty | Medium |
| Topics | Array, Math, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-range-ii/) |

## Problem Description
### Goal
You are given an integer array `nums` and a nonnegative integer `k`. For every index `i`, change `nums[i]` to exactly one of the two values `nums[i] + k` or `nums[i] - k`. Each index makes its choice independently, and every index must be changed according to one of those alternatives.

The score of the resulting array is its maximum element minus its minimum element. Choose the sign used at every index so that this score is as small as possible, and return that minimum score.

### Function Contract
Let $n=\lvert\texttt{nums}\rvert$.

**Inputs**

- `nums`: an integer array with $1 \leq n \leq 10^4$ and $0 \leq \texttt{nums}[i] \leq 10^4$.
- `k`: an integer with $0 \leq \texttt{k} \leq 10^4$.

**Return value**

Return the minimum possible difference between the largest and smallest values after replacing every element by that element plus or minus `k`.

### Examples
**Example 1**

- Input: `nums = [1], k = 0`
- Output: `0`

**Example 2**

- Input: `nums = [0,10], k = 2`
- Output: `6`

Choosing `0 + 2` and `10 - 2` produces `[2,8]`.

**Example 3**

- Input: `nums = [1,3,6], k = 3`
- Output: `3`

One optimal choice produces `[4,6,3]`, whose score is $6-3=3$.

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Sort to expose the only useful sign boundary**

Let `values` be `nums` in ascending order. If a smaller value is assigned $-k$ while a larger value is assigned $+k$, those choices push the pair farther apart. Exchanging their signs moves both results inward and cannot enlarge the overall range. Therefore, some optimal assignment has a threshold: a prefix receives $+k$ and the remaining suffix receives $-k$.

The cases where every value receives the same sign retain the original score `values[-1] - values[0]`. Use that as the initial answer. Then place a split after each index `i` from `0` through `n - 2`. In this assignment, the largest changed value is

$$
\max(\texttt{values}[i]+k,\ \texttt{values}[-1]-k),
$$

because it must come from either the raised prefix's largest original value or the lowered suffix's largest original value. Similarly, the smallest changed value is

$$
\min(\texttt{values}[0]+k,\ \texttt{values}[i+1]-k).
$$

Subtract these two boundaries and keep the smallest score over every split. The exchange argument shows that at least one optimal assignment has this prefix/suffix form, and every such form is examined. The computed minimum is therefore globally optimal.

#### Complexity detail

Sorting the $n$ values costs $O(n\log n)$ time, and scanning the $n-1$ split positions costs $O(n)$ time. Keeping a sorted copy requires $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate all sign choices:** Trying all $2^n$ assignments is exact but exponential.
- **Rebuild every split:** Materializing the complete changed array and rescanning its extrema for each threshold is correct but takes $O(n^2)$ time after sorting.
- **Sort in place:** Mutating `nums` can reduce explicit copy space, but preserving the caller's input is safer for the app-local contract.
- **One element:** Both choices produce a one-element array, so the score is zero.
- **Zero `k`:** Every element remains unchanged and the answer is the original range.
- **Large `k`:** Lowered large values may fall below raised small values; the minimum and maximum formulas handle that crossing.
- **Duplicate values:** Equal elements may lie on opposite sides of a split without invalidating the threshold argument.
- **Negative results:** Subtracting `k` may produce a negative value, which is allowed because the constraints apply to the input values.

</details>
