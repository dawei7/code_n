# 0-1 Knapsack (Branch and Bound)

| | |
|---|---|
| **ID** | `bb_01` |
| **Category** | branch_and_bound |
| **Complexity (required)** | $O(2^N)$ Worst Case |
| **Difficulty** | 7/10 |
| **Interview relevance** | 4/10 |
| **Wikipedia** | [Branch and bound](https://en.wikipedia.org/wiki/Branch_and_bound) |

## Problem statement

Given N items, each with a `weight` and a `value`, and a knapsack with a maximum `capacity`, find the maximum total value you can carry. You must either take an item entirely or leave it (0-1 property).
Unlike the Dynamic Programming solution which takes pseudo-polynomial $O(N \cdot W)$ time and fails if W is massive, you must solve this using **Branch and Bound**. This systematically searches the exponential state space but aggressively prunes invalid or suboptimal paths to achieve fast average-case performance.

**Input:** A list of `(value, weight)` pairs and a `capacity`.
**Output:** The maximum possible value.

## When to use it

- When the knapsack capacity W is astronomical (e.g., millions), rendering the standard DP table impossible to allocate in memory.
- Branch and Bound is the absolute industry standard for solving exact NP-Hard combinatorial optimizations (like Integer Linear Programming).

## Approach

A standard Backtracking solution explores every possible combination of taking or not taking an item, forming a massive binary tree of height N. This takes $O(2^N)$ time.

**Branch and Bound** improves this by instantly stopping (pruning) branches that we know mathematically cannot possibly beat our current best answer!

1. **Sort:** Sort the items by their `value/weight` ratio in descending order. This ensures we evaluate the "best" items first, finding a strong solution early to prune the rest.
2. **The State:** A node in our search tree tracks:
   - `level`: the current item index.
   - `profit`: total value collected so far.
   - `weight`: total weight collected so far.
3. **The Bound (Upper Bound):** For any node, what is the absolute *mathematical maximum* profit we could possibly get if we continued down this branch?
   - We calculate this using the **Greedy Fractional Knapsack** algorithm! We take the current `profit`, and then greedily add the remaining items (allowing fractions) until the capacity is perfectly full.
   - If this `upper_bound` is **less than or equal to** our global `max_profit` found so far, we immediately stop exploring this node! Even in a mathematically perfect fractional world, this branch cannot beat our current best.
4. **Traversal:** We use a simple Queue (BFS/FIFO) to explore the tree. (For an even faster approach using Priority Queues, see `bb_03`).

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for bb_01: 0/1 Knapsack.

Each item is either in the knapsack or not. Recursive choice
with a capacity check. Setup keeps n small (n <= 8) so
exhaustive search is feasible; a real solver would use DP or
branch-and-bound with a fractional-relaxation upper bound.
"""


def solve(values, weights, capacity, n):
    best = 0

    def helper(i, value, weight):
        nonlocal best
        if i == n:
            if value > best:
                best = value
            return
        # Skip item i.
        helper(i + 1, value, weight)
        # Take item i (only if it fits).
        if weight + weights[i] <= capacity:
            helper(i + 1, value + values[i], weight + weights[i])

    helper(0, 0, 0)
    return best
```

</details>

## Walk-through

*(Conceptual)*
`capacity = 10`
`Items (sorted by ratio): (v:40, w:4), (v:50, w:5), (v:20, w:5)`

1. **Root Node:** Level -1. `profit=0`, `weight=0`. Max theoretical bound: Take item 0 (w=4), item 1 (w=5), and 1/5 of item 2 (w=1). Bound = 40 + 50 + (1/5 * 20) = 94.
2. **Explore Take Item 0:** `profit=40`, `weight=4`. Bound = 94. Valid branch! `max_profit = 40`.
3. **Explore Skip Item 0:** `profit=0`, `weight=0`. Bound calculation: Take item 1 (w=5), item 2 (w=5). Bound = 50 + 20 = 70. Valid branch, but a much lower bound!
4. **Deep in the tree:** If we eventually find a solution taking Item 0 and 1 `profit=90`, `max_profit = 90`.
5. Now, we go back to evaluate a node in the "Skip Item 0" branch. Its bound is 70. Is 70 > 90? No! We instantly PRUNE that entire half of the search tree!

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(N)$ |
| **Average** | Much faster than 2^N | $O(2^N)$ |
| **Worst** | $O(2^N)$ | $O(2^N)$ |

In the worst possible mathematical case where the bounds perfectly trick the algorithm, it degenerates into checking every subset, taking $O(2^N)$ time and space (because of the Queue storing the wide BFS level).
However, in average real-world cases, Branch and Bound prunes over 99% of the tree, making it incredibly fast.

## Variants & optimizations

- **Best-First Search (LC-Search):** Instead of using a standard FIFO Queue (which evaluates the tree layer by layer), we use a Priority Queue (Max-Heap) sorted by the `bound`! This means we always explore the most mathematically promising branches first, allowing us to find the optimal `max_profit` much earlier, which vastly increases pruning! (See `bb_03`).

## Real-world applications

- **Integer Linear Programming Solvers:** Tools like Gurobi and CPLEX use heavily optimized Branch and Bound engines to solve scheduling and logistics problems for Fortune 500 companies.

## Related algorithms in cOde(n)

- **[approx_05 - Fractional Knapsack](../approximation/approx_05_fractional-knapsack-greedy.md)** — The $O(N)$ calculation used as the bounding function.
- **[bb_03 - Least Cost B&B Knapsack](bb_03_0-1-knapsack-least-cost-b-b.md)** — The Priority Queue optimization.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
