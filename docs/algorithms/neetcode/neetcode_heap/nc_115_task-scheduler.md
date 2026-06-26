## Problem Description & Examples
### Goal
Given a list of CPU `tasks` (characters) and a cooldown `n`, find the minimum intervals needed to finish all tasks. Idle time is allowed if a task is on cooldown.

### Function Contract
**Inputs**

- `tasks`: List[str] - task identifiers
- `n`: int - cooldown

**Return value**

int - minimum intervals needed

### Examples
**Example 1**

- Input: `tasks = ["A", "A", "A", "B", "B", "B"], n = 2`
- Output: `8`

**Example 2**

- Input: `tasks = ['D', 'D'], n = 0`
- Output: `2`

**Example 3**

- Input: `tasks = ['B', 'E'], n = 0`
- Output: `2`

---

## Underlying Base Algorithm(s)
- [Kth largest with heap](heap_02_kth-largest-element.md)
- [Top-K frequent elements](heap_03_top-k-frequent-elements.md)
- [Median in a stream](heap_04_median-in-a-stream.md)

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.
