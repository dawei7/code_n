# Find Minimum in Rotated Sorted Array II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 154 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/) |

## Problem Description
### Goal
You are given a nonempty integer array that was sorted in ascending order and then rotated by an unknown number of positions. Duplicate values are allowed, so equal elements may occur on both sides of the rotation boundary and can obscure which portion is normally ordered.

Return the minimum array value, including when every element is equal or when no effective rotation occurred. The answer is a value rather than its index, and multiple positions may contain it. Preserve correctness despite duplicate boundary values; although logarithmic progress is often possible, ambiguous all-equal ranges can force the worst case to inspect more elements.

### Function Contract
**Inputs**

- `nums`: a rotated nondecreasing list of integers, possibly with duplicates

**Return value**

The smallest array value.

### Examples
**Example 1**

- Input: `nums = [1,3,5]`
- Output: `1`

**Example 2**

- Input: `nums = [2,2,2,0,1]`
- Output: `0`

**Example 3**

- Input: `nums = [10,1,10,10,10]`
- Output: `1`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Retain the same minimum-containing closed interval**

As in problem 153, maintain `[left,right]` containing at least one global minimum and compare `nums[mid]` with the right endpoint. Strict comparisons still expose which rotation segment contains `mid`; duplicates add one ambiguous case.

**Greater and smaller midpoint values retain logarithmic elimination**

If `nums[mid] > nums[right]`, discard through `mid` because the minimum lies strictly right. If `nums[mid] < nums[right]`, retain `mid` and discard positions after it. These cases remove approximately half the interval exactly as in the distinct array.

**Equality permits removing only a redundant endpoint**

When `nums[mid] = nums[right]`, either side may contain the pivot. Decrement `right` by one. If that removed endpoint was a minimum, the equal midpoint inside the retained interval is another occurrence of the same minimum; otherwise removing it plainly cannot lose the minimum.

No comparison can safely discard half in this case. An array of all equal values therefore forces linear endpoint shrinking.

**The interval contains at least one minimum occurrence**

The closed search interval always contains a minimum value. Strict comparisons discard a segment known not to contain it; equality removes only a redundant endpoint value.

**Trace a minimum hidden between equal values**

For `[10,1,10,10,10]`, midpoint and right values are repeatedly equal, so right shrinks until an informative comparison exposes `1`. The algorithm never assumes the equal `10` region is wholly on one rotation side.

**Equal values permit only a cautious one-step reduction**

The strict comparisons retain the minimum for the same reason as in the distinct-value problem: a middle value above the right endpoint places the pivot to the right, while a smaller middle value places it at or to the left of `mid`.

When `nums[mid] = nums[right]`, the comparison cannot identify a side. Discarding only `right` is nevertheless safe: if that endpoint holds the minimum, the equal value at `mid` remains in the interval as another occurrence. Every iteration therefore preserves at least one global-minimum occurrence, and the final single index must hold that value.

#### Complexity detail

Most comparisons halve the interval, but equal values can force removing only one endpoint, so the worst case is $O(n)$ time. Boundary indices use $O(1)$ space.

#### Alternatives and edge cases

- **Linear `min`:** has the same worst-case bound but discards the logarithmic behavior available when comparisons are informative.
- **Apply distinct-value binary search unchanged:** can discard the wrong side when both endpoints equal the middle.
- **Remove all duplicates first:** costs extra space or mutation and still requires a scan.
- All values may be equal. The minimum can be surrounded by duplicates, occur at either endpoint, or appear more than once across the rotation boundary.
- Worst-case $O(n)$ is inherent to comparison ambiguity, but informative inputs still obtain binary-search behavior.

</details>
