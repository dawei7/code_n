# Target Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 494 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Backtracking |
| Official Link | [LeetCode](https://leetcode.com/problems/target-sum/) |

## Problem Description
### Goal
Given an integer array `nums` and an integer `target`, build an expression by placing exactly one `+` or `-` sign before every array element, keeping the elements in their original order. Evaluate the resulting signed sum after all positions have received a sign.

Return the number of different sign assignments whose expression evaluates to `target`. Choices are attached to array positions, so equal values remain separate decisions; for a zero, `+0` and `-0` are different expressions and must both be counted when valid. The function returns only the number of expressions, not their text or selected sign sequences.

### Function Contract
**Inputs**

- `nums`: a nonempty array of nonnegative integers
- `target`: the desired signed sum

**Return value**

- The number of distinct sign assignments whose value is `target`

### Examples
**Example 1**

- Input: `nums = [1, 1, 1, 1, 1], target = 3`
- Output: `5`

**Example 2**

- Input: `nums = [1], target = 1`
- Output: `1`

**Example 3**

- Input: `nums = [1], target = 2`
- Output: `0`

### Required Complexity

- **Time:** $O(n \cdot total)$
- **Space:** $O(total)$

<details>
<summary>Approach</summary>

#### General

**Store counts for reachable partial sums**

Begin with one way to make sum zero before processing any values. A mapping associates every reachable sum with the number of sign assignments that produce it.

**Apply both sign choices**

For each value, create a fresh mapping. Every prior sum with count `ways` contributes `ways` assignments to `sum + value` and another `ways` assignments to `sum - value`. Replacing the old mapping prevents one array element from being used more than once.

**Why the counts are exact**

After processing the first `k` values, induction shows the mapping counts precisely all $2^{k}$ sign assignments grouped by their sum. Extending each assignment once with plus and once with minus creates every assignment for value $k + 1$ exactly once. The target's final count is therefore the requested answer.

**Zeros still create distinct expressions**

For a zero, adding and subtracting reach the same numeric sum, but they are different sign choices. Performing both updates doubles the stored count as required.

#### Complexity detail

Let `total = sum(nums)`. At most `2 * total + 1` sums are reachable after each of `n` values, so time is $O(n \cdot total)$ and the two mappings use $O(total)$ space.

#### Alternatives and edge cases

- **Subset-sum transformation:** assigning plus signs to a subset reduces the problem to counting subsets with sum `(total + target) / 2`; it has the same pseudo-polynomial bounds.
- **Memoized recursion:** caches `(index, current_sum)` states and matches the dynamic-programming complexity.
- **Unmemoized recursion:** is correct but explores all $2^{n}$ sign assignments.
- **Target outside `[ - total, total]`:** has zero assignments.
- **Parity mismatch:** the subset-sum form must reject a nonintegral transformed target.
- **Zeros:** double every existing count.
- **Negative target:** requires no special case in the signed-sum mapping.

</details>
