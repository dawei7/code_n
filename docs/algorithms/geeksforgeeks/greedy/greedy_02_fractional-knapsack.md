# Fractional Knapsack Problem

| | |
|---|---|
| **ID** | `greedy_02` |
| **Category** | greedy |
| **Complexity (required)** | $O(N \log N)$ Time, $O(N)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 6/10 |
| **GeeksForGeeks Equivalent** | [Fractional Knapsack Problem](https://www.geeksforgeeks.org/fractional-knapsack-problem/) |

## Problem statement

Given `N` items where each item has a `value` and a `weight`. You have a knapsack with a maximum weight capacity `W`.
Your goal is to maximize the total value in the knapsack.
Crucially, you are allowed to break items into smaller fractions (e.g., taking 50% of an item's weight gives you 50% of its value).

**Input:** Maximum weight `W`, and an array of objects `items` with `value` and `weight` properties.
**Output:** A floating-point number representing the maximum total value achievable.

## When to use it

- Only when the problem explicitly states items are infinitely divisible (e.g., gold dust, sand, liquid).
- *Constraint:* If items CANNOT be broken (e.g., a solid gold bar, a laptop), this Greedy approach FAILS completely, and you must use the $O(N x W)$ Dynamic Programming "0/1 Knapsack" algorithm!

## Approach

**1. The Greedy Metric:**
If we want to maximize value and minimize weight, we should evaluate items based on their "Density"!
Calculate the `value-to-weight ratio` for every item (`ratio = value / weight`).
An item with a ratio of \10/kg is vastly superior to an item with a ratio of \2/kg.

**2. The Sorting:**
Sort all the items in descending order based on their `ratio`.

**3. The Packing:**
Iterate through the sorted items.
- If the entire item fits in the remaining capacity of the knapsack, take the whole thing! Subtract its weight from the capacity, and add its full value to your total.
- If the item is heavier than the remaining capacity, take a FRACTION of it! Specifically, take `remaining_capacity` kg of it. Add `remaining_capacity * ratio` to your total value. The knapsack is now exactly full! Break the loop.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for greedy_02: Fractional Knapsack.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n log n) time.
"""


def solve(values, weights, capacity, n):
    # Sort items by value-to-weight ratio (descending). Pair indices
    # so we can sort on the ratio without losing the alignment.
    order = sorted(range(n), key=lambda i: values[i] / weights[i], reverse=True)
    remaining = capacity
    total = 0.0
    for index in order:
        w = weights[index]
        if remaining >= w:
            total += values[index]
            remaining -= w
        else:
            total += values[index] * (remaining / w)
            break
    return total
```

</details>

## Walk-through

`W = 50`. Items: `I1(v=60, w=10)`, `I2(v=100, w=20)`, `I3(v=120, w=30)`.

1. Calculate ratios:
   - `I1`: 60 / 10 = 6.0
   - `I2`: 100 / 20 = 5.0
   - `I3`: 120 / 30 = 4.0
2. Sort descending by ratio: `[I1, I2, I3]`.
3. Evaluate `I1` (Weight 10):
   - 0 + 10 \le 50. Take all!
   - `total = 60`. `current_weight = 10`.
4. Evaluate `I2` (Weight 20):
   - 10 + 20 \le 50. Take all!
   - `total = 60 + 100 = 160`. `current_weight = 30`.
5. Evaluate `I3` (Weight 30):
   - 30 + 30 = 60 > 50. Too heavy! Take a fraction.
   - `remaining_capacity = 50 - 30 = 20`.
   - Take 20 weight out of the 30 available.
   - `fractional_value = 120 * (20 / 30) = 80`.
   - `total = 160 + 80 = 240`.
   - Break.

Result `240.0`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(1)$ or $O(N)$ |
| **Average** | $O(N \log N)$ | $O(1)$ or $O(N)$ |
| **Worst** | $O(N \log N)$ | $O(1)$ or $O(N)$ |

The time complexity is strictly dominated by the $O(N \log N)$ sorting of the items array based on ratio. The subsequent packing loop is a simple $O(N)$ linear scan.
Space complexity is $O(1)$ if we sort the items array in-place, or $O(N)$ if we need to create a new array of objects to store the ratios without modifying the input.

## Variants & optimizations

- **0/1 Knapsack Problem (`dp_01`):** The non-divisible DP version. Why does Greedy fail for 0/1? Consider `W=50`. Items: `A(v=60, w=10)`, `B(v=100, w=20)`, `C(v=120, w=30)`. Greedy takes A and B (Total 160, Weight 30). It cannot fit C, so it stops with 20 empty space. But the optimal choice was to skip A entirely and take B and C! (Total 220, Weight 50).

## Real-world applications

- **Commodity Trading:** Determining the optimal mix of bulk granular goods (like grains, sand, or liquids) to load into a cargo ship of limited tonnage to maximize profit on delivery.

## Related algorithms in cOde(n)

- **[dp_01 - 0/1 Knapsack Problem](../dynamic/dp_01_0-1-knapsack.md)** — The DP counterpart required when fractions are illegal.
- **[greedy_01 - Activity Selection](greedy_01_activity-selection.md)** — The other fundamental greedy introductory algorithm based on sorting a custom metric.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
