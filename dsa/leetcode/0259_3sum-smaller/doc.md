# 3Sum Smaller

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 259 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/3sum-smaller/) |

## Problem Description
### Goal
Given an integer array `nums` and an integer `target`, consider every triple of distinct positions with indices $i < j < k$. A triple qualifies when `nums[i] + nums[j] + nums[k]` is strictly smaller than `target`.

Return the number of qualifying index triples. Duplicate values at different positions create separate triples, while permutations of the same three positions do not. Sums equal to the target are excluded. Arrays with fewer than three elements return `0`. The function reports only the count, not the value combinations or indices, and must account for all later choices efficiently after ordering the data.

### Function Contract
**Inputs**

- `nums`: an integer array
- `target`: the exclusive upper bound for a triple sum

**Return value**

The number of triples $i < j < k$ satisfying `nums[i] + nums[j] + nums[k] < target`.

### Examples
**Example 1**

- Input: `nums = [-2,0,1,3], target = 2`
- Output: `2`

**Example 2**

- Input: `nums = [], target = 0`
- Output: `0`

**Example 3**

- Input: `nums = [0,0,0], target = 1`
- Output: `1`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Sorting turns one valid pair into a valid block**

After sorting, fix index `i` and place two pointers at $i + 1$ and the last index. Their ordered movement counts many valid third indices at once.

For fixed `i`, when `nums[i] + nums[left] + nums[right]` is small enough, every index from `left + 1` through `right` also forms a valid triple with `i` and `left`. Add `right - left` and advance `left`; otherwise decrease `right`.

**Each pointer move settles every pair it skips**

When the sum at `(left, right)` is below the target, replacing `right` by any index between `left + 1` and `right` can only decrease the sum. Those `right - left` pairs are all valid and are counted together before `left` advances. When the sum is too large, any larger `left` value would keep it too large, so the current `right` cannot form a valid remaining pair and may be discarded. The sweep therefore settles all pairs for every fixed first index without omission or double counting.

#### Complexity detail

Sorting costs $O(n \log n)$. Each of `n` first indices performs one linear pointer sweep, for $O(n^2)$ total time; the sorted copy uses $O(n)$ space.

#### Alternatives and edge cases

- **Enumerate all triples:** takes $O(n^3)$.
- The inequality is strict; duplicates represent different index choices; fewer than three values produce zero.

</details>
