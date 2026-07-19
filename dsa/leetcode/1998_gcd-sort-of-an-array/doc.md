# GCD Sort of an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1998 |
| Difficulty | Hard |
| Topics | Array, Math, Union-Find, Sorting, Number Theory |
| Official Link | [LeetCode](https://leetcode.com/problems/gcd-sort-of-an-array/) |

## Problem Description

### Goal

Given an integer array `nums`, an operation may choose any two positions $i$ and $j$ and swap their current elements when

$$
\gcd(\texttt{nums[i]},\texttt{nums[j]})>1.
$$

The operation may be performed any number of times, and later swaps may use values moved by earlier ones. Determine whether some sequence of legal swaps can place the array in non-decreasing order.

### Function Contract

**Inputs**

- `nums`: an array of length $N$, where $1 \le N \le 3\cdot10^4$.
- Every value is between $2$ and $10^5$ inclusive.
- Let $M=\max(\texttt{nums})$.

**Return value**

Return `true` if legal greatest-common-divisor swaps can sort the array in non-decreasing order; otherwise, return `false`.

### Examples

**Example 1**

- Input: `nums = [7, 21, 3]`
- Output: `true`
- Explanation: Swap `7` with `21`, then `21` with `3`; the respective greatest common divisors are $7$ and $3$.

**Example 2**

- Input: `nums = [5, 2, 6, 2]`
- Output: `false`
- Explanation: The value `5` shares no factor greater than one with another value and cannot leave its incorrect position.

**Example 3**

- Input: `nums = [10, 5, 9, 3, 15]`
- Output: `true`
- Explanation: Shared factors connect the values through $3$ and $5$, permitting the needed rearrangement.

### Required Complexity

- **Time:** $O(M\log\log M+N\log M+N\log N)$
- **Space:** $O(M)$

<details>
<summary>Approach</summary>

#### General

**View legal swaps as connectivity.** Two values sharing a prime factor may swap directly. More importantly, values connected through a chain of shared factors can be permuted within the same connected component: adjacent swaps along paths can transport values through that component. A direct greatest common divisor greater than one is therefore not required between every pair that ultimately exchanges positions.

**Connect values through prime-factor nodes.** Build a disjoint-set structure indexed by every integer through $M$. Use a smallest-prime-factor sieve, then factor each array value. Union that value with each distinct prime dividing it. Values that share a factor—or are linked through other values and factors—then receive the same representative.

**Compare with the unique sorted target.** Let `target = sorted(nums)`. At position $i$, the original value must be able to move within its component to supply `target[i]`. Thus require `find(nums[i]) == find(target[i])` for every position. If all comparisons pass, each component contains exactly the multiset needed at its target positions, so its values can be rearranged to realize the sorted array. If one comparison fails, no allowed swap crosses the two components, making that target impossible.

#### Complexity detail

The smallest-prime-factor sieve costs $O(M\log\log M)$ time and $O(M)$ space. Factoring all values through that table and performing disjoint-set operations costs $O(N\log M)$ time under the displayed elementary bound. Sorting costs $O(N\log N)$ time. The disjoint-set and sieve arrays dominate the $O(M)$ space usage.

#### Alternatives and edge cases

- **Compare every pair with `gcd`:** Building connectivity from all value pairs is correct but takes $O(N^2\log M)$ time.
- **Require a direct common factor at each mismatched position:** This misses transitive swap chains in which the original and target values are coprime but connected through intermediates.
- An already non-decreasing array is valid even when every value is isolated.
- Duplicate values are interchangeable and naturally belong to the same value component.
- A prime value can move only if another present value is divisible by that prime.
- The array of length one is always sortable because no operation is needed.

</details>
