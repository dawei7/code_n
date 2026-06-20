# Stock Span Problem

| | |
|---|---|
| **ID** | `stack_03` |
| **Category** | stack |
| **Complexity (required)** | $O(N)$ |
| **Difficulty** | 4/10 |
| **Interview relevance** | 6/10 |
| **LeetCode Equivalent** | [Online Stock Span](https://leetcode.com/problems/online-stock-span/) |

## Problem statement

The stock span problem is a financial problem where we have a series of N daily price quotes for a stock.
We need to calculate the **span** of the stock's price for all N days.
The span of the stock's price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is greater than or equal to its price on the previous days.
(A day's span always includes itself, so the minimum span is 1).

**Input:** An integer array `prices` representing daily stock prices.
**Output:** An integer array `spans` of the same length.

**Example:**
`prices = [100, 80, 60, 70, 60, 75, 85]`
Output: `[1, 1, 1, 2, 1, 4, 6]`.
*(On day 5 (price 75), it is higher than 60, 70, 60. So span is 4).*

## When to use it

- When you need to process an incoming stream of data and answer historical queries based on monotonic trends without keeping all history active.

## Approach

This is a direct application of the **Monotonic Stack**, specifically finding the **Previous Greater Element**.
If we know the index of the most recent day in the past where the price was strictly *greater* than today's price, then our "span" is simply the difference between today's index and that previous greater day's index!

We maintain a **Monotonically Decreasing Stack** of indices.
For the current day `i` with `prices[i]`:
- While the stack is not empty and `prices[stack.top()] <= prices[i]`:
  - The previous price is smaller than or equal to today's price. Today's price completely overshadows it! We can safely `pop` it from the stack forever, because any future day that needs to look back will hit *today's* larger price before it ever reaches the smaller popped price.
- After popping all smaller prices, the stack top now holds the index of the **Previous Greater Element**.
- If the stack is empty, it means today's price is the highest we've ever seen! The span is `i + 1` (all days from the beginning).
- Otherwise, the span is `i - stack.top()`.
- Finally, push today's index `i` onto the stack.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for stack_03: Stock Span Problem.

For each day i, the span is the number of consecutive days
just before i with a price <= arr[i] (plus today). Monotonic
stack: walk left to right, popping while the top's price is
<= today's. The span is i - (top index after popping), or
i + 1 if the stack is empty. O(n).
"""


def solve(arr, n):
    spans = [0] * n
    stack = []  # indices
    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            spans[i] = i - stack[-1]
        else:
            spans[i] = i + 1
        stack.append(i)
    return spans
```

</details>

## Walk-through

`prices = [100, 80, 60, 70]`

1. `i=0, price=100`. Stack empty. `spans[0] = 0 + 1 = 1`. Push `0`. `stack=[0]`.
2. `i=1, price=80`. 
   - `80 <= prices[0] (100)`? False.
   - Stack not empty. `spans[1] = i - stack[-1] = 1 - 0 = 1`.
   - Push `1`. `stack=[0, 1]`. (Values `[100, 80]`).
3. `i=2, price=60`.
   - `60 <= prices[1] (80)`? False.
   - Stack not empty. `spans[2] = i - stack[-1] = 2 - 1 = 1`.
   - Push `2`. `stack=[0, 1, 2]`. (Values `[100, 80, 60]`).
4. `i=3, price=70`.
   - `70 <= prices[2] (60)`? True! Pop `2`. `stack=[0, 1]`.
   - `70 <= prices[1] (80)`? False.
   - Stack not empty. `spans[3] = i - stack[-1] = 3 - 1 = 2`.
   - Push `3`. `stack=[0, 1, 3]`. (Values `[100, 80, 70]`).

Output: `[1, 1, 1, 2]`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(N)$ |
| **Average** | $O(N)$ | $O(N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

Although there is a `while` loop inside the `for` loop, every index from 0 to N-1 is pushed onto the stack exactly once and popped at most once. The total number of stack operations is linearly proportional to N. Thus, the time complexity is strictly amortized $O(N)$.
Space complexity is $O(N)$ for the stack and the output array.

## Variants & optimizations

- **Online Stream Processing:** If the prices come in one by one via an API (e.g., `next(price)`), you can encapsulate the stack inside a Class state. Instead of storing indices, the stack stores pairs of `(price, span)`. When popping smaller prices, you just accumulate their spans: `current_span += popped_span`. This completely decouples the logic from absolute indices!

## Real-world applications

- **UI Dashboards:** Dynamically rendering historical support/resistance bounds on live cryptocurrency ticker charts without rescanning the entire day's history on every new tick.

## Related algorithms in cOde(n)

- **[stack_02 - Next Greater Element](stack_02_next-greater-element.md)** — The foundational algorithm teaching the Monotonic Stack pattern.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
