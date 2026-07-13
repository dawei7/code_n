# Trapping Rain Water

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 42 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Two Pointers, Dynamic Programming, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/trapping-rain-water/) |

## Problem Description
### Goal
The array `height` describes adjacent vertical bars of unit width standing on a common baseline. After rain, water may collect in depressions between taller bars; water beyond either outer edge escapes.

For each horizontal position, the stable water level is limited by the tallest boundary available on both its left and right. Sum the water units held above every bar and return the total volume. Bars have nonnegative integer heights, and empty or too-short profiles trap no water.

### Function Contract
**Inputs**

- `height`: `List[int]` of non-negative bar heights

**Return value**

An `int` equal to the total trapped water volume.

### Examples
**Example 1**

- Input: `height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`
- Output: `6`

**Example 2**

- Input: `height = [4, 2, 0, 3, 2, 5]`
- Output: `9`

**Example 3**

- Input: `height = []`
- Output: `0`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Water at one bar is fixed by the lower side maximum**

For position `i`, trapped water is `min(max_left[i], max_right[i]) - height[i]`. Precomputing both maximum arrays works, but the same information can be finalized from the ends with two pointers.

Track `left_max` and `right_max` while pointers bound the unprocessed interval. When `height[left] <= height[right]`, the current right bar is a known opposite boundary at least as tall as the current left bar. The history of pointer choices also ensures that if `left_max` is taller than that right boundary, the right side would have been processed instead before this state could make the left calculation unsafe. Thus the left position's limiting side is known, and `left_max - height[left]` is final after updating `left_max`. Process right symmetrically when its current bar is lower.

**Once a side is selected, future interior bars cannot change its water**

Before each iteration, all positions outside `[left, right]` have their final water counted exactly once; `left_max` and `right_max` are the greatest bars seen from their respective ends. Selecting the lower current boundary proves an adequate wall exists on the opposite side. Any future bar inside the interval can raise that opposite maximum but cannot lower it, so it cannot reduce or otherwise revise the selected position's water.

Updating the selected side's maximum before adding water also prevents negative contributions: a new record-height bar traps zero above itself.

**Trace a basin whose right wall is already sufficient**

For `[4, 2, 0, 3, 2, 5]`, the left boundary 4 is lower than right boundary 5. Moving inward under left maximum 4 adds 2 above height 2, 4 above height 0, 1 above height 3, and 2 above height 2, totaling 9.

**The lower boundary makes one side's water final**

When the left boundary is no higher than the right boundary, some wall on the right is already tall enough not to be the limiting side for the current left position. The trapped level there is determined entirely by the best left wall seen so far, so `left_max - height`—clamped at zero—is final. Future interior bars cannot lower that established opposite boundary.

The symmetric argument applies when the right boundary is lower. Advancing exactly the decided pointer processes every interior position once, and each contribution uses the smaller of its true left and right maxima, yielding the exact total water.

#### Complexity detail

Exactly one pointer advances on every iteration, so every bar is processed once and time is $O(n)$. Two pointers, two maxima, and the accumulated volume use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Precompute left and right maxima:** runs in linear time but uses $O(n)$ extra arrays.
- **Monotonic stack:** also runs in $O(n)$ and computes water by bounded horizontal layers, using $O(n)$ space.
- **Scan both sides for every bar:** directly applies the formula but requires $O(n^2)$ time.
- Empty arrays and arrays shorter than three bars trap no water; the pointer loop naturally returns zero.
- Equal boundary heights may process either side. Plateaus and zero-height bars require no special cases.

</details>
