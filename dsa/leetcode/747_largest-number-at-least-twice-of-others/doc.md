# Largest Number At Least Twice of Others

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 747 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/largest-number-at-least-twice-of-others/) |

## Problem Description

### Goal

Given an integer array `nums` whose largest value is unique, determine whether that largest element is at least twice as large as every other number in the array.

If it satisfies the condition for all other positions, return the zero-based index of the largest element. Otherwise return `-1`. Equality with exactly twice another value qualifies, while failing the comparison against even one other number makes the answer `-1`.

### Function Contract

**Inputs**

- `nums`: a list of non-negative integers with a unique maximum value.

**Return value**

- The maximum value's original index when it is at least twice every other value; otherwise `-1`.

### Examples

**Example 1**

- Input: `nums = [3, 6, 1, 0]`
- Output: `1`
- Explanation: `6` is at least twice each of `3`, `1`, and `0`.

**Example 2**

- Input: `nums = [1, 2, 3, 4]`
- Output: `-1`
- Explanation: The maximum `4` is not at least twice `3`.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Reduce every comparison to the runner-up**

Let `largest` be the unique maximum and `second_largest` the greatest remaining value. If `largest >= 2 * second_largest`, then the inequality also holds for every smaller number. If it fails for `second_largest`, the required condition is already false. Only these two values and the maximum's index matter.

**Maintain the two greatest values in one pass**

For each number, compare it with the current `largest`. A new maximum moves the old maximum into `second_largest` and records the new index. Otherwise, update `second_largest` when the number exceeds it. After the scan, test the single inequality against the runner-up.

The update rules keep `largest` and `second_largest` equal to the two greatest values in the processed prefix: a new greatest value shifts the previous leader down, while any other value can affect only the runner-up. Thus the final dominance check is equivalent to checking the maximum against every other array element.

#### Complexity detail

The array is scanned once, so the running time is $O(n)$. A fixed number of values and one index are stored, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Sort values with their indices:** The two greatest values become adjacent after sorting, but sorting costs $O(n \log n)$ time and $O(n)$ space for decorated entries.
- **Compare every candidate with every other value:** This directly mirrors the definition but can take $O(n^2)$ time.
- **Exactly two values:** The larger value needs to be at least twice the smaller one; the same runner-up test applies.
- **Zero runner-up:** Any non-negative unique maximum is at least twice zero.
- **Equality at twice the runner-up:** The condition is inclusive, so exact equality succeeds.
- **Original index:** Track the maximum's position during the scan; do not return its rank after sorting.

</details>
