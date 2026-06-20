# Maximal Rectangle

| | |
|---|---|
| **ID** | `dp_26` |
| **Category** | dynamic |
| **Complexity (required)** | $O(M * N)$ Time, $O(N)$ Space |
| **Difficulty** | 9/10 |
| **Interview relevance** | 7/10 |
| **LeetCode Equivalent** | [Maximal Rectangle](https://leetcode.com/problems/maximal-rectangle/) |

## Problem statement

Given a `rows x cols` binary matrix filled with `0`'s and `1`'s, find the largest rectangle containing only `1`'s and return its area.

**Input:** An `m x n` matrix `matrix` where elements are chars `'0'` or `'1'`.
**Output:** An integer representing the area of the largest rectangle.

## When to use it

- To show mastery of combining Dynamic Programming (to compress 2D data into 1D histograms) with Monotonic Stacks (to solve the 1D histograms).
- You CANNOT use the simple `min(Up, Left, Diagonal)` trick from Maximal Square (`dp_25`). Rectangles do not scale symmetrically.

## Approach

**1. The Mathematical Reduction:**
Imagine slicing the matrix horizontally row by row.
If you treat the `1`s stretching upward from the current row as "buildings", each row forms a skyline or a histogram!
For example:
```
1 0 1 0  -> Histogram: [1, 0, 1, 0]
1 1 1 1  -> Histogram: [2, 1, 2, 1]  (Buildings grow taller!)
1 1 1 0  -> Histogram: [3, 2, 3, 0]  (A '0' instantly drops the building to height 0)
```
If we can convert the matrix into a sequence of histograms row-by-row, the problem perfectly reduces to running the **"Largest Rectangle in Histogram"** algorithm on every single row!

**2. Dynamic Programming (Building the Histograms):**
We maintain a 1D DP array `heights` of size `N`.
For each row `i`, we iterate through each column `j`:
- If `matrix[i][j] == '1'`, then `heights[j] += 1` (the building grows taller).
- If `matrix[i][j] == '0'`, then `heights[j] = 0` (the building foundation is destroyed).

**3. Monotonic Stack (Solving the Histogram):**
For the current `heights` array, how do we find the largest rectangle?
We iterate through the histogram. We maintain a Monotonic Increasing Stack of indices.
When we encounter a bar `heights[k]` that is *shorter* than the bar at the top of the stack, it means the taller bar in the stack can no longer expand to the right!
We pop the taller bar.
- Its height `H` is `heights[popped_index]`.
- Its width `W` is determined by its boundaries: The left boundary is the new top of the stack (the nearest shorter bar to the left). The right boundary is `k` (the nearest shorter bar to the right).
- Area = `H * W`.
We track the `max_area` across all pops, across all rows!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dp_26: Maximal Rectangle.

For each row, build a heights[] histogram. Run the largest-
rectangle-in-histogram algorithm (monotonic stack) on each
row. Track the global maximum area across all rows.
"""


def solve(matrix, m, n):
    if m == 0 or n == 0:
        return 0
    heights = [0] * (n + 1)  # Extra sentinel 0 at end
    max_area = 0
    for i in range(m):
        for j in range(n):
            heights[j] = heights[j] + 1 if matrix[i][j] == "1" else 0
        stack = [-1]
        for k in range(n + 1):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[k]:
                h = heights[stack.pop()]
                w = k - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(k)
    return max_area
```

</details>

## Walk-through

`matrix = [["1","0","1","0"], ["1","1","1","1"]]`.
M=2, N=4. `heights = [0, 0, 0, 0, 0]`.

1. **Row 0 (`1 0 1 0`):**
   - `heights` becomes `[1, 0, 1, 0, 0]`.
   - Stack execution:
     - `j=0` (h=1): Push `0`. Stack=`[0]`.
     - `j=1` (h=0): `0 < heights[0]`. Pop `0`. h=1, w=1-0=1. Area=1. `max_area=1`. Push `1`. Stack=`[1]`.
     - `j=2` (h=1): Push `2`. Stack=`[1, 2]`.
     - `j=3` (h=0): `0 < heights[2]`. Pop `2`. h=1, w=3-1-1=1. Area=1. Push `3`.
     - ... (Flushes). `max_area = 1`.

2. **Row 1 (`1 1 1 1`):**
   - `heights` becomes `[2, 1, 2, 1, 0]`. (Notice index 1 grew from 0 to 1, index 0 grew from 1 to 2).
   - Stack execution:
     - `j=0` (h=2): Push `0`.
     - `j=1` (h=1): `1 < 2`. Pop `0`. h=2, w=1-0=1. Area=2. `max=2`. Push `1`. Stack=`[1]`.
     - `j=2` (h=2): Push `2`. Stack=`[1, 2]`.
     - `j=3` (h=1): `1 < 2`. Pop `2`. h=2, w=3-1-1=1. Area=2. Push `3`. Stack=`[1, 3]`.
     - `j=4` (h=0): `0 < 1`. Pop `3`. h=1, w=4-1-1=2. Area=2.
       - Pop `1` (h=1). w=4-0=4. Area = 1 x 4 = 4. `max=4`!
   - `max_area = 4`.

Result `max_area` is 4. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(M * N)$ | $O(N)$ |
| **Average** | $O(M * N)$ | $O(N)$ |
| **Worst** | $O(M * N)$ | $O(N)$ |

The outer loop runs M times. The inner DP loop runs N times. The Monotonic Stack loop processes every index j exactly twice (one push, one pop). Total time is strictly $O(M \times N)$.
Space complexity is strictly $O(N)$ for the `heights` array and the `stack`.

## Variants & optimizations

- **DP Only Array Optimization:** You can actually replace the Monotonic Stack entirely with two more DP arrays: `left[j]` and `right[j]`. For each row, you do a left-to-right pass to find the left boundary of the building at `j`, and a right-to-left pass to find the right boundary. This remains $O(M \times N)$ time but is purely mathematical and often runs faster in practice because it avoids stack push/pop overhead.

## Real-world applications

- **VLSI Design:** Finding the largest continuous rectangular area of empty silicon on a wafer to place a massive logic block (like a CPU core) without overlapping existing routed traces.

## Related algorithms in cOde(n)

- **[dp_25 - Maximal Square](dp_25_maximal-square.md)** — The strictly square, purely DP variant of this problem.
- **[stack_02 - Largest Rectangle in Histogram](../stacks/stack_02_largest-rectangle-in-histogram.md)** — The 1D Monotonic Stack algorithm that acts as the core engine for this 2D solution.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
