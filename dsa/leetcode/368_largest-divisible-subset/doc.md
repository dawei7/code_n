# Largest Divisible Subset

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 368 |
| Difficulty | Medium |
| Topics | Array, Math, Dynamic Programming, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-divisible-subset/) |

## Problem Description
### Goal
Given a nonempty list of unique positive integers, choose a subset in which every pair is comparable by divisibility. For any two selected values `a` and `b`, either `a` divides `b` exactly or `b` divides `a` exactly.

Return any qualifying subset having maximum possible cardinality, with values in any order. Selection does not need to preserve original positions, and several maximum subsets may exist. Include each input value at most once. Pairwise divisibility across the complete subset is required; merely finding adjacent divisible pairs in an arbitrary ordering is insufficient unless they form a consistent divisibility chain.

### Function Contract
**Inputs**

- `nums`: a non-empty list of distinct positive integers

**Return value**

- Any largest subset of `nums` whose every pair is comparable by divisibility. The values may be returned in any order.

### Examples
**Example 1**

- Input: `nums = [1,2,3]`
- Output: `[1,2]`

**Example 2**

- Input: `nums = [1,2,4,8]`
- Output: `[1,2,4,8]`

**Example 3**

- Input: `nums = [3,4,16,8]`
- Output: `[4,8,16]`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Sort divisibility into a one-way relation**

Sort the values increasingly. For two sorted values $a \le b$, only $b \bmod a = 0$ can make them divisible unless they are equal. The subset can therefore be viewed as a chain whose later values are multiples of earlier values.

**Build the longest chain ending at each value**

For each sorted index `i`, let `length[i]` be the longest divisible chain ending at `values[i]`. Start it at one for the value itself. Inspect every earlier index `j`; when `values[i] % values[j] = 0`, the chain ending at `j` can be extended. If that produces a longer chain, update `length[i]` and record `j` as its predecessor.

**Why checking only the previous chain endpoint is sufficient**

Suppose a valid sorted chain ends at `values[j]` and `values[i]` is divisible by that endpoint. Every earlier chain value divides `values[j]`; divisibility is transitive, so every earlier value also divides `values[i]`. Extending the chain preserves the pairwise condition without rechecking all of its members.

Every maximum divisible subset becomes an increasing chain after sorting. Its final value appears at some index, and the dynamic program considers the predecessor used by that chain, so the recorded maximum length is optimal. Following predecessor links from the best ending index reconstructs one valid maximum subset.

**Trace a tied optimum**

For `[1,2,3]`, both `[1,2]` and `[1,3]` have length two. The dynamic program may retain either predecessor path; both satisfy the contract, which is why validation checks the property and optimal size rather than one serialization.

#### Complexity detail

Sorting costs $O(n \log n)$. The nested predecessor scan examines $O(n^2)$ pairs and dominates the runtime. The length and predecessor arrays use $O(n)$ space, and reconstruction stores at most `n` output values.

#### Alternatives and edge cases

- **Enumerate all subsets:** directly tests the definition but requires $O(2^n)$ candidates in the worst case.
- **Backtracking with divisibility pruning:** avoids some invalid branches but still has exponential worst-case behavior.
- **Store an entire chain at every index:** simplifies reconstruction but can consume $O(n^2)$ space through copied lists.
- Multiple maximum subsets may exist; any one is valid.
- Input values are distinct, so reconstruction cannot repeat a value.
- The value `1` can begin a chain with every positive integer but need not appear in every optimum.
- A single input value is itself the unique maximum-cardinality choice.

</details>
