# Merge Sorted Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 88 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Two Pointers, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/merge-sorted-array/) |

## Problem Description
### Goal
You are given two integer arrays, `nums1` and `nums2`, sorted in non-decreasing order. The first `m` positions of `nums1` contain its valid values, followed by exactly `n` reserved positions; `nums2` contains `n` valid values.

Merge both inputs into one array sorted in non-decreasing order inside `nums1`, preserving every duplicate and using all $m + n$ positions. The native method modifies `nums1` in place and returns nothing, while the app returns that mutated array for inspection. Either valid input portion may be empty.

### Function Contract
**Inputs**

- `nums1`: length $m + n$, with a sorted valid prefix of length `m`
- `m`: number of valid input values in `nums1`
- `nums2`: a sorted list of length `n`
- `n`: number of values in `nums2`

**Return value**

The merged `nums1` in the app adapter; LeetCode's `merge` method returns nothing.

### Examples
**Example 1**

- Input: `nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3`
- Output: `[1,2,2,3,5,6]`

**Example 2**

- Input: `nums1 = [1], m = 1, nums2 = [], n = 0`
- Output: `[1]`

**Example 3**

- Input: `nums1 = [0], m = 0, nums2 = [1], n = 1`
- Output: `[1]`

### Required Complexity

- **Time:** $O(m+n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Backward merging protects unread values in `nums1`**

Point `i` to the last valid value in `nums1`, `j` to the last value in `nums2`, and `write` to the final reserved position of `nums1`. Compare the two source endpoints, write the larger one at `write`, and move that source pointer and the destination left.

The destination is never before an unread `nums1` value: it begins after the valid prefix, and every write consumes one source value. This is why merging backward needs no buffer, while merging from the front would overwrite data still needed.

**Only a remaining `nums2` prefix needs explicit copying**

If `nums2` is exhausted first, any remaining `nums1` prefix is already in its final positions and the algorithm can stop. If `nums1` is exhausted first, copy the remaining `nums2` prefix backward into the open beginning. A single loop conditioned on $j \ge 0$ captures both cases.

**The filled suffix contains the globally largest merged values**

Positions after the destination pointer contain exactly the largest already-merged values in sorted order. Unconsumed source prefixes remain sorted, so their larger final value is always the correct next value to place.

**Trace equal values without losing multiplicity**

For `[1,2,3,0,0,0]` and `[2,5,6]`, place 6, then 5, then 3 at the right. Compare the two 2s and finish the remaining prefix, producing `[1,2,2,3,5,6]` without overwriting unread values.

**The largest remaining endpoint belongs at the destination end**

Because both unread prefixes are sorted, their greatest unmerged value must be one of their two current endpoints. Writing the larger endpoint into the rightmost open destination position therefore fixes that position permanently.

The destination index moves backward into reserved space or positions whose original value has already been consumed, so no unread `nums1` value is overwritten. Repeating until `nums2` is exhausted leaves either already-correct `nums1` values or a fully written merged prefix, making the entire array sorted and complete.

#### Complexity detail

Each input value is compared and written at most once, giving $O(m+n)$ time. Three indices use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Merge from the front:** overwrites unread `nums1` values unless they are shifted or copied.
- **Concatenate and sort:** costs $O((m+n) \log(m+n))$ time and ignores existing order.
- **Allocate a merged array:** is straightforward but uses $O(m+n)$ extra space.
- $n = 0$ leaves `nums1` unchanged. $m = 0$ copies all of `nums2` into the reserved array.
- Either equal endpoint may be selected first; both copies remain and sorted order is preserved.

</details>
