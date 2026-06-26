# Fractional Knapsack (Greedy Bound)

| | |
|---|---|
| **ID** | `approx_05` |
| **Category** | approximation |
| **Complexity (required)** | $O(N \log N)$ |
| **Difficulty** | 3/10 |
| **Interview relevance** | 7/10 |
| **Wikipedia** | [Continuous knapsack problem](https://en.wikipedia.org/wiki/Continuous_knapsack_problem) |

## Problem statement

Given N items, each with a `weight` and a `value`, and a knapsack with a maximum `capacity`, find the maximum total value you can carry.
Unlike the 0-1 Knapsack problem where you must take an item whole or leave it, here you are allowed to take **fractions** of an item (e.g., 50% of an item gives you 50% of its weight and 50% of its value).

While this problem can be solved *exactly* using a Greedy approach, the result of this exact fractional solution is frequently used as an **upper bound approximation** for the NP-Hard 0-1 Knapsack problem in Branch and Bound algorithms.

**Input:** A list of `(value, weight)` pairs and a `capacity`.
**Output:** The maximum possible value (often a float).

## When to use it

- To solve resource allocation problems involving continuous materials (gold dust, liquids, grain).
- Crucially, it is used as the `Bounding` function in the Branch and Bound solution to the 0-1 Knapsack problem. By calculating the fractional knapsack value, you know the absolute theoretical maximum value of a branch. If this fractional maximum is worse than your current best 0-1 solution, you can instantly prune the branch!

## Approach

Because we can take fractions of items, we never have to worry about "wasting" space. We can always completely fill the knapsack to the brim (if we have enough total weight).
Therefore, the most logical greedy choice is to always pick the item that gives the **highest value per unit of weight**.

1. Calculate the ratio `value / weight` for every item.
2. Sort the items in **descending order** of this ratio.
3. Iterate through the sorted items:
   - If the entire item fits in the remaining capacity, take the whole thing! Deduct its weight from the capacity and add its value to the total.
   - If the entire item *doesn't* fit, take exactly enough fraction of it to perfectly fill the remaining capacity. Add the proportional value to the total, and **break** the loop (since the knapsack is now exactly full).
4. Return the total value.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for approx_05: Fractional Knapsack (Greedy).

Given n items each with a value and a weight, and a
"""


def solve(values, weights, n, capacity):
    """Fractional knapsack via greedy by value/weight ratio."""
    if capacity <= 0 or n == 0:
        return 0.0
    items = sorted(
        range(n),
        key=lambda i: values[i] / weights[i],
        reverse=True,
    )
    remaining = capacity
    total = 0.0
    for i in items:
        if remaining <= 0:
            break
        if weights[i] <= remaining:
            total += values[i]
            remaining -= weights[i]
        else:
            total += values[i] * (remaining / weights[i])
            remaining = 0
    return total
```

</details>

## Walk-through

`capacity = 50`
`items = [(V:60, W:10), (V:100, W:20), (V:120, W:30)]`

1. **Calculate Ratios:**
   - Item 1: 60 / 10 = 6.0
   - Item 2: 100 / 20 = 5.0
   - Item 3: 120 / 30 = 4.0
2. **Sort:** Already sorted `[Item 1, Item 2, Item 3]`.
3. **Iterate:**
   - **Item 1:** Weight 10 <= 50. Take all! `capacity = 40`, `total_value = 60`.
   - **Item 2:** Weight 20 <= 40. Take all! `capacity = 20`, `total_value = 60 + 100 = 160`.
   - **Item 3:** Weight 30 > 20. Cannot take all. Take fraction!
     - `fraction = 20 / 30 = 2/3`.
     - `value added = 120 * (2/3) = 80`.
     - `total_value = 160 + 80 = 240`.
     - `capacity = 0`. Break loop.

Output: 240.0. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(1)$ |
| **Average** | $O(N \log N)$ | $O(1)$ |
| **Worst** | $O(N \log N)$ | $O(1)$ |

Sorting the items takes $O(N \log N)$ time. The greedy iteration takes exactly $O(N)$ time. The bottleneck is the sorting, making the total time complexity strictly $O(N \log N)$.
Space complexity is $O(1)$ auxiliary space if sorted in place (or $O(N)$ depending on the sorting algorithm implementation).

## Variants & optimizations

- **$O(N)$ Selection Algorithm:** If N is massive, you don't actually need to sort the whole array! You can use a deterministic QuickSelect (Median of Medians) algorithm to find the "pivot" item that straddles the capacity line in exactly $O(N)$ time. You take everything with a higher ratio than the pivot, and a fraction of the pivot itself.

## Real-world applications

- **Commodity Trading:** Maximizing the dollar value of a cargo ship holding continuous bulk materials (grain, crude oil, liquid chemicals).

## Related algorithms in cOde(n)

- **[bb_03 - 0-1 Knapsack Branch and Bound](../branch_and_bound/bb_03_0-1-knapsack-least-cost-b-b.md)** — Uses this exact Fractional Knapsack algorithm internally to calculate the upper-bound theoretical limit of a branch!
- **[greedy_02 - Fractional Knapsack](../greedy/greedy_02_fractional-knapsack.md)** — The identical core algorithm.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
