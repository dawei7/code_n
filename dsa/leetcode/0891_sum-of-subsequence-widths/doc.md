# Sum of Subsequence Widths

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 891 |
| Difficulty | Hard |
| Topics | Array, Math, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-subsequence-widths/) |

## Problem Description
### Goal
The width of a sequence is its maximum element minus its minimum element. A subsequence of `nums` is formed by deleting any number of elements without changing the order of those that remain.

Consider every non-empty subsequence, including distinct index selections that may contain equal values. Single-element subsequences are included and have width zero. Sum all widths and return the result modulo $10^9+7$.

### Function Contract
Let $n=\lvert\texttt{nums}\rvert$.

**Inputs**

- `nums`: an integer array where $1 \leq n \leq 10^5$ and $1 \leq \texttt{nums[i]} \leq 10^5$.

**Return value**

Return the sum of `maximum - minimum` over every non-empty subsequence, reduced modulo $10^9+7$.

### Examples
**Example 1**

- Input: `nums = [2,1,3]`
- Output: `6`

The seven non-empty subsequences have widths `0, 0, 0, 1, 1, 2, 2`.

**Example 2**

- Input: `nums = [2]`
- Output: `0`

**Example 3**

- Input: `nums = [1,2]`
- Output: `1`

Only the subsequence containing both values has nonzero width.

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Count extrema instead of enumerating subsequences**

Sort the values as $a_0 \leq a_1 \leq \dots \leq a_{n-1}$. Width depends only on the selected values, not their order, so sorting does not change the aggregate over index subsets. When $a_i$ is selected as a subsequence maximum, any subset of the $i$ earlier positions may accompany it, giving $2^i$ choices. As a minimum, it can be accompanied by any subset of the $n-1-i$ later positions, giving $2^{n-1-i}$ choices.

Thus the total width is

$$
W=\sum_{i=0}^{n-1} a_i\left(2^i-2^{n-1-i}\right).
$$

Equal values at different indices are still counted separately, exactly as distinct subsequences require.

**Pair the positive and negative contributions**

Reindex the minimum half of $W$ to obtain

$$
W=\sum_{i=0}^{n-1}\left(a_i-a_{n-1-i}\right)2^i.
$$

Scan the sorted array once, multiply each paired difference by the current power, and update `power = power * 2 % MOD`. Reduce the accumulated answer modulo $10^9+7$ at the end.

Every subsequence contributes its maximum once to the positive count and its minimum once to the negative count. The combinatorial factors enumerate exactly the optional lower or higher ranked positions, so their difference sums precisely every subsequence width.

#### Complexity detail

Sorting dominates at $O(n\log n)$ time, and the contribution scan takes $O(n)$. The sorted copy uses $O(n)$ space; the rolling power and accumulator use $O(1)$ additional space.

#### Alternatives and edge cases

- **Enumerate all subsequences:** Computing each width directly is correct but requires $O(n2^n)$ time.
- **Precompute every power of two:** A power array gives the same formula in $O(n)$ post-sort time but uses another $O(n)$ storage.
- **Sort the input in place:** This keeps the same time bound and can reduce auxiliary storage when mutating `nums` is acceptable.
- **Duplicate values:** Treat equal entries as distinct sorted positions; their contributions may differ even though their values match.
- **Single element:** Its maximum and minimum are equal, so the only width and the answer are zero.
- **Negative intermediate sum:** Apply the final modulo so paired negative contributions produce the required nonnegative residue.
- **Order-preserving definition:** Although subsequences preserve original order, every index subset has the same extrema after sorting its selected values, so contribution counting remains valid.

</details>
