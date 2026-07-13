# Matchsticks to Square

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 473 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/matchsticks-to-square/) |

## Problem Description
### Goal
Given positive matchstick lengths, determine whether all sticks can be assigned to four sides of one square. Every stick must be used exactly once, no stick may be broken, and side length is the sum of sticks assigned to that side.

Return `True` only when the four side sums can be equal and positive. The complete length must therefore be divisible by four, and no individual stick may exceed the required side length, though those conditions alone are not sufficient. Stick order inside a side is irrelevant, duplicate lengths remain separate occurrences, and the function need not return the grouping.

### Function Contract
**Inputs**

- `matchsticks`: positive integer stick lengths

**Return value**

- `True` if the sticks can be partitioned into four groups with equal sums; otherwise `False`

### Examples
**Example 1**

- Input: `matchsticks = [1, 1, 2, 2, 2]`
- Output: `True`

**Example 2**

- Input: `matchsticks = [3, 3, 3, 3, 4]`
- Output: `False`

**Example 3**

- Input: `matchsticks = [2, 2, 2, 1, 1]`
- Output: `True`

### Required Complexity

- **Time:** $O(n \cdot 2^n)$
- **Space:** $O(2^n)$

<details>
<summary>Approach</summary>

#### General

**Check the side length before state search**

The total length must be positive and divisible by four. Its quarter is the required side length, and no individual stick may exceed it. These conditions reject impossible inputs before exponential work.

**Store progress for each used-stick subset**

Use a bitmask to identify sticks already placed. Let `progress[mask]` be the filled length of the current side modulo the target, or `-1` if that subset cannot occur while completing prior sides exactly. Begin with zero used sticks and zero progress.

**Append one unused stick when it fits**

From each reachable mask, try every unused stick. If adding it does not exceed the target, mark the enlarged mask reachable with `(current + stick) % target`. Reaching the target resets progress to zero and begins the next side. Because the total sum is exactly four targets, a full mask with zero progress represents four completed sides.

**Why subset state is sufficient**

The sum of values selected by a mask is fixed, so its position within the current side is fixed modulo the target regardless of placement order. Multiple orders reaching the same mask have identical future options; storing it once removes repeated permutations without discarding a possible partition.

#### Complexity detail

There are $2^{n}$ masks and each may try `n` sticks, giving $O(n \cdot 2^n)$ time. The reachability/progress table uses $O(2^n)$ space.

#### Alternatives and edge cases

- **Four-side backtracking:** places sorted sticks into side totals and prunes symmetric sides, often fast but has a larger exponential worst case.
- **Unpruned side assignment:** tries equivalent empty or equal-length sides repeatedly and can approach $O(4^n)$.
- **Enumerate target-sum subsets:** must still ensure four selected subsets are disjoint and cover every stick.
- **Total not divisible by four:** cannot form equal sides.
- **Stick longer than a side:** makes a square impossible immediately.
- **Duplicate lengths:** masks distinguish physical sticks while subset-state merging removes order permutations.
- **Every stick is required:** the answer checks the full mask, so unused leftovers are not allowed.

</details>
