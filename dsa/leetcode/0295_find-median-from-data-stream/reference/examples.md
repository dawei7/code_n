## Examples

**Example 1**

- Input: `operations = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"], arguments = [[], [1], [2], [], [3], []]`
- Output: `[null, null, null, 1.5, null, 2.0]`
- Explanation: Construct an empty `MedianFinder`, then add `1` and `2`. The first median query returns `1.5`, the mean of those two values. After adding `3`, the stored values are `[1,2,3]`, so the next query returns `2.0`.
