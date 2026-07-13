# Count of Range Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 327 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Divide and Conquer, Binary Indexed Tree, Segment Tree, Merge Sort, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/count-of-range-sum/) |

## Problem Description
### Goal
Given an integer array and bounds `lower <= upper`, consider every nonempty contiguous subarray. A subarray qualifies when the sum of all its elements lies within the inclusive interval `[lower, upper]`.

Return the number of qualifying index intervals. Different start or end positions count separately even when their values or sums are equal, and sums exactly at either boundary are included. Negative values and zero prevent simple monotone-window reasoning. The answer is a count rather than a list of ranges, and the required solution must avoid enumerating and summing all quadratic subarrays independently.

### Function Contract
**Inputs**

- `nums`: the integer array
- `lower`: the inclusive lower sum bound
- `upper`: the inclusive upper sum bound

**Return value**

The number of index pairs defining a contiguous subarray with sum between the two bounds, inclusive.

### Examples
**Example 1**

- Input: `nums = [-2,5,-1], lower = -2, upper = 2`
- Output: `3`

**Example 2**

- Input: `nums = [0], lower = 0, upper = 0`
- Output: `1`

**Example 3**

- Input: `nums = [1], lower = 0, upper = 0`
- Output: `0`

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Express every range sum as an ordered prefix pair**

Build prefix sums with an initial zero. The sum of `nums[i:j]` is `prefix[j] - prefix[i]`, so a valid subarray corresponds to an ordered pair $i < j$ satisfying `lower <= prefix[j] - prefix[i] <= upper`.

A divide-and-conquer split counts three disjoint groups: pairs entirely in the left prefix half, pairs entirely in the right half, and cross pairs whose earlier index is left of the split and later index is right of it. Recursive calls count the first two groups and leave each half sorted by prefix value.

**Two monotone boundaries count all cross pairs**

For one left-half prefix value `P`, scan the sorted right half with two pointers. Advance the first while `right - P < lower`; advance the second while `right - P <= upper`. The half-open interval between them contains exactly the valid right prefixes for `P`.

As left values are visited in sorted order, both numeric thresholds `P + lower` and `P + upper` only increase. Neither right pointer ever moves backward, so all cross pairs at one recursion level are counted in linear time. The strict comparison at the lower pointer and inclusive comparison at the upper pointer are what make both range endpoints inclusive.

**Merge the halves instead of sorting them again**

After counting, merge the two sorted prefix halves into one auxiliary buffer and copy that interval back. A fresh `sorted()` call at every recursion node would add an extra logarithmic factor; the linear merge preserves the standard merge-sort bound.

Every valid ordered prefix pair belongs uniquely to the left recursion, right recursion, or cross group of its first separating recursion node. The two-pointer window counts every cross pair exactly once, and the merge changes only value order used by ancestors—not the already enforced original-index side of the split. Thus the final count is exact.

#### Complexity detail

Each recursion level performs linear cross-pair scanning and linear merging across all prefix values. There are $O(\log n)$ levels, giving $O(n \log n)$ time. The prefix array, merge buffer, and recursion stack use $O(n)$ space overall.

#### Alternatives and edge cases

- **Enumerate all subarrays with rolling sums:** avoids recomputing sums but still takes $O(n^2)$ time.
- **Fenwick tree with coordinate compression:** also achieves $O(n \log n)$ by querying prior prefixes inside a numeric interval.
- **Sliding window:** fails because negative values destroy monotonicity of the running sum.
- Repeated equal prefixes represent distinct index pairs and must all be counted. Equal lower and upper bounds are valid, and prefix sums may exceed 32-bit range even when individual values do not.

</details>
