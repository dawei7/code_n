# Patching Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 330 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/patching-array/) |

## Problem Description
### Goal
Given an array `nums` of positive integers sorted in ascending order and a positive bound `n`, you may add new positive integers to the array. After patching, every target value from `1` through `n` must be representable as the sum of some subset of the available occurrences.

Return the minimum number of added values needed to guarantee this complete coverage. Each original or patched occurrence can be used at most once within a particular subset sum, though different targets choose subsets independently. Values larger than the currently uncovered gap cannot create that missing smaller sum. Return only the patch count, not the added values or all representing subsets.

### Function Contract
**Inputs**

- `nums`: a sorted list of positive integers
- `n`: the inclusive upper bound of the sums that must be representable

**Return value**

The minimum number of added values required to make every sum in `[1, n]` representable.

### Examples
**Example 1**

- Input: `nums = [1,3], n = 6`
- Output: `1`

**Example 2**

- Input: `nums = [1,5,10], n = 20`
- Output: `2`

**Example 3**

- Input: `nums = [1,2,2], n = 5`
- Output: `0`

### Required Complexity

- **Time:** $O(m + \log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Track the first sum that coverage cannot reach**

Maintain `missing` so every sum in `[1, missing - 1]` is representable. Initially `missing = 1`, describing an empty covered interval. If the next array value $x$ is at most `missing`, combining $x$ with every already representable sum extends coverage continuously through `missing + x - 1`; update `missing += x` and consume the value.

Because `nums` is sorted, when the next value exceeds `missing`, no unused input value can form the gap at `missing`. A patch is unavoidable.

**Patch with the missing value itself**

When a gap exists, add exactly `missing`. This new value alone covers the gap, and adding it to every old sum from zero through `missing - 1` extends coverage through `2 * missing - 1`. Set `missing *= 2` and count one patch.

No other single patch can extend coverage farther without leaving the current gap: a value larger than `missing` cannot form `missing`, while a smaller value was already within the covered interval and extends the upper endpoint by less. Thus choosing `missing` is both necessary for immediate feasibility and maximal for future coverage.

For `[1,5,10]`, consuming one covers through one, so `missing = 2`. The next input is too large, so patch two and then four, expanding coverage to seven. Five and ten can then be consumed, covering beyond twenty with two patches.

At every iteration the invariant interval is exact and gap-free. Consuming a usable input value needs no patch; when it is unusable, every valid solution must patch the current gap, and the greedy patch dominates every feasible alternative. Repeating this exchange argument proves the final patch count is minimal.

#### Complexity detail

Each of the `m` input values is consumed at most once. Every patch at least doubles `missing`, so at most $O(\log n)$ patches occur. Total time is $O(m + \log n)$, and the algorithm uses $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Maintain every reachable subset sum explicitly:** can require $O(n)$ space and much more work than tracking one continuous boundary.
- **Patch with the next input value or with one:** may cover the immediate gap poorly or fail to cover it at all, producing extra patches.
- **Use total input sum alone:** does not prove there are no holes in the representable interval.
- An empty array is handled by repeatedly doubling coverage. Inputs already spanning `[1,n]` need no patches, and values beyond `n` never need to be consumed.

</details>
