# Largest Rectangle in Histogram

| | |
|---|---|
| **ID** | `stack_04` |
| **Category** | stack |
| **Complexity (required)** | $O(N)$ |
| **Difficulty** | 8/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/) |

## Problem statement

Given an array of integers `heights` representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

**Input:** An integer array `heights`.
**Output:** An integer representing the maximum rectangular area.

**Example:**
`heights = [2, 1, 5, 6, 2, 3]`
Output: `10`.
*(The largest rectangle is formed by the bars of height 5 and 6, which gives a rectangle of height 5 and width 2: `5 * 2 = 10`).*

## When to use it

- Considered the "final boss" of the Monotonic Stack data structure.
- Used extensively in 2D matrix dynamic programming problems (like Maximal Rectangle).

## Approach

If we want to form a rectangle, the height of that rectangle is bottlenecked by the **shortest** bar within its width.
Therefore, for every single bar `i` in the histogram, we can ask: *"If this bar `i` is the absolute shortest bar in a rectangle, how far left and right can I expand this rectangle?"*
The rectangle can expand left until it hits a bar *shorter* than `heights[i]`.
The rectangle can expand right until it hits a bar *shorter* than `heights[i]`.

This means we need to find the **Previous Smaller Element (PSE)** and **Next Smaller Element (NSE)** for every bar!
We can do this in a single pass using a **Monotonically Increasing Stack**.

As we iterate through the bars:
- We push indices onto the stack as long as the heights are strictly increasing.
- If we encounter a bar `curr` that is *shorter* than the bar at the top of the stack, it means `curr` is the **NSE** for the stack top!
- We pop the stack top. Its height is known. Its **NSE** is the current index `i`. Its **PSE** is the *new* top of the stack (because the stack is monotonically increasing, the element underneath it must be strictly smaller).
- The width of the rectangle for the popped bar is `NSE - PSE - 1`.
- Area = `height * width`. Update maximum area.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for stack_04: Largest Rectangle in Histogram.

Monotonic stack of bar indices with increasing heights. For each
bar popped, the rectangle extends from the previous-smaller on
the left to the current on the right. Track the max area across
all pops.
"""


def solve(heights, n):
    if n == 0:
        return 0
    stack = []
    best = 0
    for i in range(n + 1):
        cur_h = heights[i] if i < n else 0
        while stack and heights[stack[-1]] > cur_h:
            top = stack.pop()
            h = heights[top]
            left = stack[-1] + 1 if stack else 0
            right = i - 1
            area = h * (right - left + 1)
            if area > best:
                best = area
        stack.append(i)
    return best
```

</details>

## Walk-through

`heights = [2, 1, 5, 6, 2, 3, 0]` *(0 appended)*

1. `i=0 (2)`. Push. `stack=[0]`.
2. `i=1 (1)`. `1 < 2`. **Pop `0` (Height 2)**.
   - NSE is `i=1`. PSE is none (stack empty). `w = 1`.
   - Area = 2 x 1 = 2. `max=2`.
   - Push `1`. `stack=[1]`.
3. `i=2 (5)`. Push. `stack=[1, 2]`.
4. `i=3 (6)`. Push. `stack=[1, 2, 3]`.
5. `i=4 (2)`.
   - `2 < 6`. **Pop `3` (Height 6)**. NSE=`4`. PSE=`2` (stack top). `w = 4 - 2 - 1 = 1`. Area = 6 x 1 = 6. `max=6`.
   - `2 < 5`. **Pop `2` (Height 5)**. NSE=`4`. PSE=`1` (stack top). `w = 4 - 1 - 1 = 2`. Area = 5 x 2 = 10. `max=10`.
   - `2 < 1` is False.
   - Push `4`. `stack=[1, 4]`.
6. `i=5 (3)`. Push. `stack=[1, 4, 5]`.
7. `i=6 (0)`. Forces everything to pop.
   - **Pop `5` (Height 3)**. `w = 6 - 4 - 1 = 1`. Area = 3.
   - **Pop `4` (Height 2)**. `w = 6 - 1 - 1 = 4`. Area = 8.
   - **Pop `1` (Height 1)**. `w = 6`. Area = 6.

Output: `10`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(N)$ |
| **Average** | $O(N)$ | $O(N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

Every index is pushed onto the stack exactly once and popped exactly once. The time complexity is strictly bounded to $O(N)$ making it vastly superior to the $O(N^2)$ brute-force expansion.
Space complexity is $O(N)$ for the stack.

## Variants & optimizations

- **Maximal Rectangle in 2D Binary Matrix:** Given a 2D matrix of `0`s and `1`s, find the largest rectangle of `1`s. This is solved by treating each row as a base of a histogram. You maintain an array of heights that increments if the cell is `1`, and resets to `0` if the cell is `0`. You run this $O(N)$ histogram algorithm on every row, resulting in an $O(ROWS x COLS)$ solution!

## Real-world applications

- **Computer Vision:** Finding the largest unoccluded bounding box within a bitmask image for optical character recognition (OCR) partitioning.

## Related algorithms in cOde(n)

- **[stack_02 - Next Greater Element](stack_02_next-greater-element.md)** — Explains the foundational Monotonic Stack pattern used here.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
