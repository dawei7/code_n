# Two Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/two-sum/) |

## Problem Description
### Goal
You are given an integer array `nums` and an integer `target`. Choose two different positions whose stored values add exactly to the target, then return those positions rather than the values themselves. Array values may repeat, so equal numbers at distinct indices remain separate choices.

Every input is guaranteed to contain exactly one valid pair. An index cannot be selected twice, even when doubling one value would equal the target. Return the two indices in any order; no result for any other pair is required.

### Function Contract
**Inputs**

- `nums`: the integer array
- `target`: the required pair sum

**Return value**

A two-element list containing distinct indices whose values sum to `target`.

### Examples
**Example 1**

- Input: `nums = [2, 7, 11, 15], target = 9`
- Output: `[0, 1]`

**Example 2**

- Input: `nums = [3, 2, 4], target = 6`
- Output: `[1, 2]`

**Example 3**

- Input: `nums = [3, 3], target = 6`
- Output: `[0, 1]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**The second value is not another unknown**

A pair search treats both values as choices. Once the current value `x` is fixed, however, its partner is forced to be `target - x`. The problem becomes a membership question: has that complement appeared earlier?

Keep a hash table from each previously seen value to its index. At index `i`, compute the complement and look it up. If present, return its stored index with `i`; otherwise store the current value and continue.

**Look up before inserting**

The order of those two operations enforces the “different elements” rule. At the moment of lookup, the table contains only earlier indices, so a match can never reuse position `i` itself.

This also handles duplicates correctly. For `nums = [3, 3]` and `target = 6`, the first `3` finds nothing and is stored. The second `3` then finds the earlier occurrence and returns `[0, 1]`.

For `nums = [2, 7, 11, 15]` and `target = 9`, index zero stores `2`. At index one, the complement of `7` is `2`, which is already mapped to zero, so the answer is `[0, 1]`.

**Why the unique pair must be found**

Let the promised solution use indices $a < b$. By the time the scan reaches `b`, `nums[a]` is in the table. Since `nums[a] = target - nums[b]`, the lookup at `b` succeeds. No false pair can be returned because every successful lookup explicitly verifies the target sum.

#### Complexity detail

The scan performs one expected-constant-time lookup and insertion per element, for $O(n)$ expected time. The hash table stores at most `n` values and indices, using $O(n)$ space.

#### Alternatives and edge cases

- **Enumerate every pair:** uses constant auxiliary space but takes $O(n^2)$ time.
- **Sort and use two pointers:** takes $O(n \log n)$ and must retain original indices through the sort.
- **Two-pass hash table:** has the same asymptotic bounds, but needs an explicit check against matching an element with itself.
- Negative values, zero, and duplicate values need no special cases; lookup-before-insert handles them uniformly.

</details>
