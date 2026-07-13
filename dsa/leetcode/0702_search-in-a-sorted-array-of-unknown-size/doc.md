# Search in a Sorted Array of Unknown Size

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 702 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Interactive |
| Official Link | [LeetCode](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/) |

## Problem Description
### Goal
An integer array is sorted in strictly increasing order, but its length is not available. You may read a position only through `ArrayReader.get(index)`, which returns the stored value for a valid non-negative index and a sentinel greater than every legal array value when the index is outside the array.

Given `target`, return its zero-based index if it occurs and `-1` otherwise. The search must discover a sufficient index range through the reader rather than relying on a supplied length, and it must treat the out-of-bounds sentinel as unavailable data rather than as a possible match.

### Function Contract
**Inputs**

- `reader`: the sorted values behind the unknown-size reader; app-local cases provide them as a list, while the native LeetCode method receives an `ArrayReader`
- `target`: the value to locate

**Return value**

- The zero-based index of `target`, or `-1` when it is absent

### Examples
**Example 1**

- Input: `reader = [-1,0,3,5,9,12], target = 9`
- Output: `4`

**Example 2**

- Input: `reader = [-1,0,3,5,9,12], target = 2`
- Output: `-1`

**Example 3**

- Input: `reader = [1,2,4,8,16], target = 16`
- Output: `4`

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Create an upper bound without knowing the length**

Start with candidate indices `0` and `1`. While the value at the right index is smaller than `target`, every index through that point is too small because the data is sorted. Move the left boundary past it and double the right index.

**Let the sentinel stop expansion**

If doubling steps beyond the real array, the accessor returns its large sentinel. That value is not smaller than any legal target, so the expansion terminates even when `target` is absent beyond the last element.

**Binary-search the discovered bracket**

The target, if present, is now between the inclusive boundaries. Compare the middle accessor value with `target`, discard the impossible sorted half, and continue until finding equality or exhausting the interval.

**Why no possible index is skipped**

Expansion discards a prefix only after its rightmost value is below `target`, proving the whole prefix is too small. The final bracket therefore contains every possible target position. Ordinary binary-search reasoning preserves that possibility at each halving, and an empty bracket proves absence.

#### Complexity detail

Doubling reaches or passes an array position `p` in $O(\log(p + 1))$ accessor calls, and binary search over that bracket uses the same order. This is $O(\log n)$ in the worst case and uses only boundary indices, for $O(1)$ extra space.

#### Alternatives and edge cases

- **Linear reader scan:** request indices in order until reaching `target` or a larger value; it is correct but takes $O(n)$ calls.
- **Binary search a fixed maximum index:** this works only when the API publishes a reliable global bound; exponential bracketing adapts to the actual target position.
- The target may be the first value, so the initial bracket must include index `0`.
- A target smaller than the first value is rejected by the first binary-search comparisons.
- A target larger than the last value is bounded by the out-of-range sentinel and returns `-1`.
- Strictly increasing values guarantee that any returned index is unique.

</details>
