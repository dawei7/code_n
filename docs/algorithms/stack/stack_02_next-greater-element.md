# Next Greater Element (Monotonic Stack)

| | |
|---|---|
| **ID** | `stack_02` |
| **Category** | stack |
| **Complexity (required)** | $O(N)$ |
| **Difficulty** | 5/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Next Greater Element I & II](https://leetcode.com/problems/next-greater-element-i/) |

## Problem statement

Given an array of integers `nums`, find the **Next Greater Element** for every element in the array.
The Next Greater Element of an element `x` is the *first* element to the right of `x` that is strictly greater than `x`.
If no such element exists, output `-1` for that position.

**Input:** An integer array `nums`.
**Output:** An integer array of the same length containing the next greater elements.

**Example:**
`nums = [4, 5, 2, 25]`
Output: `[5, 25, 25, -1]`.
*(4's next is 5. 5's next is 25. 2's next is 25. 25 has no next greater).*

## When to use it

- To eliminate nested $O(N^2)$ loops when looking for the "closest larger/smaller value to the right/left".
- This introduces the **Monotonic Stack**, a critical concept that forms the backbone of advanced array-geometry problems like Trapping Rain Water and Largest Rectangle in Histogram.

## Approach

A naive solution takes $O(N^2)$ by scanning the right side of the array for every single element.
We can reduce this to $O(N)$ using a **Monotonic Decreasing Stack**.

A Monotonic Stack is a stack whose elements are always sorted in a specific order (e.g., strictly decreasing from bottom to top).
Instead of storing the values directly, we store their **indices**.

**The Logic:**
Iterate through the array from left to right.
For each element `curr = nums[i]`:
- While the stack is NOT empty AND `curr` is strictly greater than the element at the index sitting on top of the stack (`nums[stack.top()]`):
  - We have found the Next Greater Element for the item at `stack.top()`!
  - Pop the top index from the stack.
  - Set the answer for that popped index to `curr`.
- Push the current index `i` onto the stack so it can wait for its own Next Greater Element.

Elements left in the stack at the very end never found a greater element, so they default to `-1`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for stack_02: Next Greater Element.

Monotonic stack: walk left to right, maintaining a stack of
indices whose next-greater hasn't been found yet. When arr[i]
is greater than the top, pop and record i as the answer for
the popped index. O(n).
"""


def solve(arr, n):
    result = [-1] * n
    stack = []  # indices
    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)
    return result
```

</details>

## Walk-through

`nums = [4, 5, 2, 25]`
`result = [-1, -1, -1, -1]`. `stack = []`.

1. `i=0, curr=4`. Stack empty. Push `0`. `stack=[0]`.
2. `i=1, curr=5`. 
   - `5 > nums[stack[-1]]` (which is `nums[0] = 4`). Yes!
   - Pop `0`. `result[0] = 5`.
   - Push `1`. `stack=[1]`.
   - `result = [5, -1, -1, -1]`.
3. `i=2, curr=2`.
   - `2 > nums[stack[-1]]` (which is `nums[1] = 5`). No.
   - Push `2`. `stack=[1, 2]`. (Notice the values `[5, 2]` are monotonically decreasing).
4. `i=3, curr=25`.
   - `25 > nums[stack[-1]]` (which is `nums[2] = 2`). Yes!
   - Pop `2`. `result[2] = 25`.
   - `25 > nums[stack[-1]]` (which is `nums[1] = 5`). Yes!
   - Pop `1`. `result[1] = 25`.
   - Push `3`. `stack=[3]`.
   - `result = [5, 25, 25, -1]`.

Loop ends. Result is `[5, 25, 25, -1]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(N)$ |
| **Average** | $O(N)$ | $O(N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

Every element is pushed onto the stack exactly once, and popped from the stack at most once. Therefore, the `while` loop runs at most N times *across the entire execution of the program*. The time complexity is strictly $O(N)$.
Space complexity is $O(N)$ to store the result array and the stack.

## Variants & optimizations

- **Circular Array (NGE II):** If the array wraps around (the NGE for the last element might be the first element), you simply iterate through the array **twice** (i.e., `for i in range(2 * n): curr = nums[i % n]`), using the exact same stack logic!
- **Next Smaller Element:** Change the condition to `curr < nums[stack[-1]]` to maintain a Monotonically *Increasing* stack.
- **Previous Greater Element:** Iterate backwards from right to left instead.

## Real-world applications

- **Stock Market Trends:** Finding how many days you have to wait until the stock price exceeds today's price.

## Related algorithms in cOde(n)

- **[stack_03 - Stock Span Problem](stack_03_stock-span-problem.md)** — The direct application of looking backwards using the same monotonic logic.
- **[stack_04 - Largest Rectangle in Histogram](stack_04_largest-rectangle-in-histogram.md)** — Combines Next Smaller Element and Previous Smaller Element to calculate widths in $O(N)$.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
