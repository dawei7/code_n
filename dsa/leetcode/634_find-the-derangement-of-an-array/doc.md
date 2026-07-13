# Find the Derangement of An Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 634 |
| Difficulty | Medium |
| Topics | Math, Dynamic Programming, Combinatorics |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-derangement-of-an-array/) |

## Problem Description
### Goal
Given a positive integer `n`, consider all permutations of `n` distinct values relative to their original positions. A derangement is a permutation in which no value appears at the same index it occupied originally.

Return the number of derangements of `n` values, modulo `1,000,000,007`. Every position must receive a different original value; a permutation with even one fixed point is excluded. For $n = 1$, no derangement exists because the sole value cannot move to another position.

### Function Contract
**Inputs**

- `n`: the positive number of distinct values and original positions

**Return value**

- The number of derangements of `n` values, reduced modulo `1,000,000,007`

### Examples
**Example 1**

- Input: `n = 3`
- Output: `2`

**Example 2**

- Input: `n = 2`
- Output: `1`

**Example 3**

- Input: `n = 1`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Separate the base arrangements**

With no values, the empty arrangement contributes one combinatorial base case: $D(0) = 1$. One value cannot move away from its own position, so $D(1) = 0$; two values have exactly one derangement.

**Choose where one distinguished value goes**

For $n \ge 2$, choose a non-original destination for one fixed value in $n - 1$ ways. If the value belonging to that destination moves back into the distinguished value's position, the remaining values contribute $D(n - 2)$. Otherwise, the unresolved positions reduce to a derangement counted by $D(n - 1)$.

**Turn the counting split into a recurrence**

The two cases are disjoint and exhaustive, giving $D(n) = (n - 1) \cdot (D(n - 1) + D(n - 2))$. Compute states in increasing order and reduce after every transition, which is valid because addition and multiplication respect modular equivalence.

**Keep only the two required states**

Each transition reads only the previous two derangement counts. After producing the next value, shift those two variables forward; the complete dynamic-programming table is unnecessary.

#### Complexity detail

The loop evaluates one constant-time modular transition for every size from `2` through `n`, taking $O(n)$ time. Two prior counts and the current loop index use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Full dynamic-programming array:** stores every `D(i)` and uses the same $O(n)$ time, but requires $O(n)$ space without benefiting later transitions.
- **Inclusion-exclusion:** computes $n! \cdot \operatorname{sum}((- 1) ^{k} / k!)$; it can be made linear with modular inverses, but its derivation and modular bookkeeping are less direct.
- **Backtracking over permutations:** checks the fixed-point condition explicitly but takes factorial time.
- **Repeated addition for each transition:** reproduces multiplication by $n - 1$ with an inner loop and is correct, but grows quadratically.
- $n = 1$ has no valid arrangement, while $n = 2$ has exactly the swap.
- Intermediate counts grow rapidly, so the modulus must be applied during every transition.
- The empty-state value is used only to seed the recurrence; the public input is positive.

</details>
