## Problem Description & Examples
### Goal
Given `k` projects to select, initial capital `w`, and lists of `profits` and `capital` required, maximize your final capital by completing at most `k` projects.

### Function Contract
**Inputs**

- `k`: int - max projects
- `w`: int - initial capital
- `profits`: List[int]
- `capital`: List[int]

**Return value**

int - maximum capital after k projects

### Examples
**Example 1**

- Input: `k = 2, w = 0, profits = [1, 2, 3], capital = [0, 1, 1]`
- Output: `4`

**Example 2**

- Input: `k = 3, w = 0, profits = [1, 2, 3], capital = [0, 1, 2]`
- Output: `6`

**Example 3**

- Input: `k = 1, w = 2, profits = [1, 2], capital = [2, 3]`
- Output: `3`

---

## Underlying Base Algorithm(s)
- [Kth largest with heap](heap_02_kth-largest-element.md)
- [Top-K frequent elements](heap_03_top-k-frequent-elements.md)
- [Median in a stream](heap_04_median-in-a-stream.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
