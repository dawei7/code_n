# 3Sum Closest

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 16 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/3sum-closest/) |

## Problem Description
### Goal
You are given an integer array `nums` containing at least three values and an integer `target`. Choose three distinct array positions and add their values. Among all such triples, seek the sum whose absolute difference from the target is smallest.

Return that three-value sum, not the indices or the distance from the target. Duplicate values may participate when they occupy different positions. Every input is guaranteed to have exactly one closest sum, so no tie-breaking behavior is required.

### Function Contract
**Inputs**

- `nums`: `List[int]` containing at least three values
- `target`: `int`

**Return value**

An `int` containing the uniquely closest three-value sum.

### Examples
**Example 1**

- Input: `nums = [-1, 2, 1, -4], target = 1`
- Output: `2`

**Example 2**

- Input: `nums = [0, 0, 0], target = 1`
- Output: `0`

**Example 3**

- Input: `nums = [1, 1, 1, 0], target = -100`
- Output: `2`

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Reduce each fixed value to an ordered pair search**

Sort the values and initialize the best sum from any valid first triple. For each fixed index, place pointers at the beginning and end of the remaining suffix. Evaluate that triple and replace the best whenever its distance from the target is smaller.

If the sum is below the target, move the left pointer right to increase it. If above, move the right pointer left to decrease it. An exact match can be returned immediately because no smaller distance than zero exists.

**Move only in the direction that can approach the target**

For a fixed index, all pairs outside the current pointer interval have been evaluated or cannot improve in the direction needed. After a sum below target, keeping the same left value with a smaller right value would only decrease the sum further, so discard that left value by advancing it. After a sum above target, keeping the same right value with a larger left value would only increase it further, so discard that right value.

The stored `closest` is always the best sum among every triple examined so far.

**Trace a representative input**

Sort `[-1, 2, 1, -4]` into `[-4, -1, 1, 2]`. With `-4` fixed, pointer movement raises small sums. With `-1` fixed, the pair `1, 2` gives sum 2, only one away from target 1. No later candidate is closer, so return 2.

**Why pointer movement cannot hide a closer sum**

Fixing the first sorted index leaves a monotone pair-sum search. If the current total is below the target, moving the right pointer inward can only lower it further, so no pair using the current left value and a smaller right value can be closer from the needed direction; increase the left pointer. The symmetric argument applies above the target.

Each move removes only candidates dominated in the direction required to approach the target, while every evaluated total updates the smallest absolute difference seen. Repeating for every possible first index covers every triple that could improve the answer. An exact target match has zero distance and can return immediately.

#### Complexity detail

Sorting costs $O(n \log n)$. Each fixed index performs one linear two-pointer sweep, so the dominant running time is $O(n^2)$. The sorted copy uses $O(n)$ auxiliary space in the canonical implementation; an in-place sort can reduce explicit extra storage subject to the language's sorting implementation.

#### Alternatives and edge cases

- **Three nested loops:** checks every triple in $O(n^3)$ time.
- **Binary search for the third value:** for each pair, search near `target - pair`; this is $O(n^2 \log n)$, slower than two pointers.
- **Hashing:** exact 3Sum benefits from complement lookup, but “closest” requires ordered predecessor/successor information that a plain hash set does not provide.
- Initialize the best sum from an actual triple rather than an artificial infinity if the return type must remain integral.
- An exact target match can return immediately because absolute error zero is unbeatable. The contract guarantees a unique closest sum, so no tie-breaking rule is required.

</details>
