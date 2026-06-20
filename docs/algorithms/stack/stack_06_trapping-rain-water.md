# Trapping Rain Water

| | |
|---|---|
| **ID** | `stack_06` |
| **Category** | stack |
| **Complexity (required)** | $O(N)$ |
| **Difficulty** | 7/10 |
| **Interview relevance** | 10/10 |
| **LeetCode Equivalent** | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) |

## Problem statement

Given `n` non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

**Input:** An integer array `height`.
**Output:** An integer representing the total trapped water.

**Example:**
`height = [0,1,0,2,1,0,1,3,2,1,2,1]`
Output: `6`.
*(Water trapped: 1 unit at index 2. 1 unit at index 4. 2 units at index 5. 1 unit at index 6. 1 unit at index 9. Total = 6).*

## When to use it

- Widely considered the most famous FAANG interview question.
- Can be solved via Dynamic Programming, Two Pointers, or a **Monotonic Stack**. We will cover the Stack approach here to demonstrate its power in resolving horizontal boundaries.

## Approach

Water is trapped in a "valley". A valley requires a left wall, a bottom, and a right wall.
If we use a **Monotonically Decreasing Stack**, we can find these valleys!

We iterate through the array. The stack stores the *indices* of the bars.
- As long as the current bar is smaller than or equal to the bar at the top of the stack, we push it. We are going down into a valley!
- The moment we find a bar `curr_height` that is *taller* than the stack's top, we have hit the right wall of a valley!
- We pop the stack top. This popped element is the **bottom** of the valley (`bottom_height`).
- Now, we look at the *new* top of the stack. This is the **left wall** of the valley.
- The height of the trapped water bounded by these three elements is `min(left_wall_height, right_wall_height) - bottom_height`.
- The width of the trapped water is `right_wall_index - left_wall_index - 1`.
- Add `height * width` to the total trapped water.
- Repeat the pop process until the stack is empty or `curr_height` is no longer taller than the stack top. Then push `curr_index`.

This calculates the water in horizontal "layers" from bottom to top!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for stack_06: Trapping Rain Water.

Given a non-negative integer array heights where each
"""


def solve(heights, n):
    """Trapping Rain Water via monotonic stack."""
    if n <= 2:
        return 0
    stack = []  # indices with increasing heights
    water = 0
    for i in range(n):
        while stack and heights[i] > heights[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            # Distance between current and new top of stack.
            dist = i - stack[-1] - 1
            # Bounded by min of the two walls minus the popped bottom.
            bounded = min(heights[i], heights[stack[-1]]) - heights[top]
            water += dist * bounded
        stack.append(i)
    return water
```

</details>

## Walk-through

`height = [2, 1, 0, 2]`

1. `i=0, h=2`. Push. `stack=[0]`.
2. `i=1, h=1`. `1 < 2`. Push. `stack=[0, 1]`. (Going down).
3. `i=2, h=0`. `0 < 1`. Push. `stack=[0, 1, 2]`. (Going down).
4. `i=3, h=2`. 
   - `2 > height[stack[-1]] (0)`. Right wall found!
   - Pop `2`. Bottom height is 0.
   - Left wall is stack top `1`. Left height is 1.
   - Bounded height = `min(1, 2) - 0 = 1`.
   - Width = `3 - 1 - 1 = 1`.
   - Water += 1 x 1 = 1. (Filled the bottom of the valley).
   - Stack is now `[0, 1]`.
   - `2 > height[stack[-1]] (1)`. Still right wall!
   - Pop `1`. Bottom height is 1.
   - Left wall is stack top `0`. Left height is 2.
   - Bounded height = `min(2, 2) - 1 = 1`.
   - Width = `3 - 0 - 1 = 2`.
   - Water += 1 x 2 = 2. (Filled the upper horizontal layer).
   - Stack is now `[0]`.
   - `2 > height[stack[-1]] (2)`? False.
   - Push `3`. `stack=[0, 3]`.

Total Water = `1 + 2 = 3`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(N)$ |
| **Average** | $O(N)$ | $O(N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

Every element is pushed onto the stack exactly once and popped at most once. Time complexity is strictly $O(N)$.
Space complexity is $O(N)$ because the array might be strictly decreasing (e.g., `[5, 4, 3, 2, 1]`), causing all N elements to be pushed to the stack without ever popping.

## Variants & optimizations

- **Two Pointers ($O(1)$ Space):** You can solve this without a stack using a Left and Right pointer moving inwards. You maintain `max_left` and `max_right`. Since water is determined by the minimum of the two peaks, you just process the side with the *smaller* max peak! If `max_left < max_right`, you can safely add `max_left - height[left]` to the total and move left. This achieves $O(N)$ time and $O(1)$ space.
- **Dynamic Programming ($O(N)$ Space):** Create two arrays, `left_max` and `right_max`, precomputed in two linear passes. Water at index `i` is simply `min(left_max[i], right_max[i]) - height[i]`. Easiest to understand, but takes 3 passes.

## Real-world applications

- **Topological Data Analysis:** Identifying persistence homology and local minima/maxima basins in 2D height maps or LIDAR terrain scans.

## Related algorithms in cOde(n)

- **[stack_04 - Largest Rectangle in Histogram](stack_04_largest-rectangle-in-histogram.md)** — Uses the exact same Monotonic Stack popping logic, just computing area under the bar instead of area above it.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
