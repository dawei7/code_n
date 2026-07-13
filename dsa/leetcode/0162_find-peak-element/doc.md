# Find Peak Element

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 162 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-peak-element/) |

## Problem Description
### Goal
Given a nonempty integer array whose adjacent elements are never equal, find a peak element. An element is a peak when it is strictly greater than the values immediately beside it; beyond either end of the array, imagine a value of negative infinity.

Return the index of any valid peak. Several peaks may exist, and the validator accepts any one of their indices rather than requiring a predetermined choice. An endpoint qualifies when it exceeds its only real neighbor, and the sole element of a length-one array is a peak. Meet the required logarithmic running time instead of scanning every position.

### Function Contract
**Inputs**

- `nums`: a nonempty integer list whose adjacent elements are unequal

**Return value**

Any valid peak index. The app validates the peak property rather than requiring one predetermined index.

### Examples
**Example 1**

- Input: `nums = [1,2,3,1]`
- Output: `2`

**Example 2**

- Input: `nums = [1,2,1,3,5,6,4]`
- Output: `1` or `5`

**Example 3**

- Input: `nums = [1]`
- Output: `0`

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

The array is not globally sorted, but every adjacent pair defines a local slope. That is enough for binary search because a rising slope guarantees that some peak lies to its right, while a falling slope guarantees that some peak lies at the current position or to its left.

Maintain a closed candidate interval `[left, right]`. While it contains more than one index, choose
`mid = left + (right - left) // 2` and compare `nums[mid]` with `nums[mid + 1]`. The access to `mid + 1` is safe because `left < right` ensures `mid < right`.

- If `nums[mid] < nums[mid + 1]`, the slope rises. Discard `mid` and everything left of it by setting `left = mid + 1`.
- If `nums[mid] > nums[mid + 1]`, the slope falls. Keep `mid`, because it may itself be the peak, and set `right = mid`.

Why can half the array be discarded without knowing its shape? Starting from a rising edge and moving right, either a later edge turns downward, creating a peak at the turning point, or the rise reaches the last element, which is a peak because the imaginary neighbor beyond the boundary is negative infinity. The falling case is symmetric when moving left.

Trace `[1, 2, 1, 3, 5, 6, 4]`: the first midpoint is index `3`, and $3 < 5$, so a peak is guaranteed in indices `4..6`. The next comparison sees $6 > 4$, so index `6` is discarded but index `5` remains. The interval collapses at index `5`, whose value `6` is indeed greater than both neighbors. Returning index `1` would also have been valid; the task asks for any peak.

The maintained interval always contains a peak. Initially the whole nonempty array does. On a rising middle edge, the finite sequence to the right must either turn downward or end at the right boundary, so the retained right interval contains a peak. On a falling edge, the same argument toward the left shows that `[left, mid]` contains a peak. Each update strictly shortens the interval. When `left = right`, the invariant leaves that single index as a peak, so returning it is correct.

#### Complexity detail

Each comparison removes roughly half of the remaining indices, so the loop performs $O(\log n)$ comparisons. It stores only interval boundaries and the midpoint, using $O(1)$ auxiliary space.

#### Alternatives and edge cases

- A linear scan can return the first descent's left endpoint, but its $O(n)$ time misses the required logarithmic bound.
- Finding the global maximum also returns a peak under the unequal-adjacent-values guarantee, yet still requires examining every value.
- A one-element array immediately returns index `0`. Strictly increasing and strictly decreasing arrays converge to the last and first index respectively.
- Multiple peaks are normal. Tests must validate the peak property rather than compare with one fixed index.
- Keeping `mid` in the falling case is essential: setting `right = mid - 1` could discard a valid peak at `mid`.

</details>
