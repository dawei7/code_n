# 0-1 Knapsack (Least Cost Branch & Bound)

| | |
|---|---|
| **ID** | `bb_03` |
| **Category** | branch_and_bound |
| **Complexity (required)** | $O(2^N)$ Worst Case |
| **Difficulty** | 8/10 |
| **Interview relevance** | 3/10 |
| **Wikipedia** | [Best-first search](https://en.wikipedia.org/wiki/Best-first_search) |

## Problem statement

Solve the 0-1 Knapsack Problem using **Least Cost (Best-First) Branch and Bound**.
In `bb_01`, we explored the state-space tree using a standard FIFO Queue (Breadth-First Search). This evaluates all nodes at Level 1, then all nodes at Level 2, etc.
In Least Cost B&B, you must use a Priority Queue to always expand the node with the most promising mathematical bound, regardless of its depth in the tree.

**Input:** A list of `(value, weight)` pairs and a `capacity`.
**Output:** The maximum possible value.

## When to use it

- This is the standard, fully optimized version of Branch and Bound. A simple FIFO Queue is rarely used in production engines because it wastes massive amounts of time exploring mathematically terrible branches just because they are shallow in the tree.
- By using Best-First Search, the algorithm dives straight down the most profitable mathematical path, establishing a massive `max_profit` early, which instantly prunes everything else.

## Approach

Everything from `bb_01` applies (the node structure, the state, the Fractional Knapsack bounding function). The only difference is the traversal order.

Since Python's `heapq` is a Min-Heap, and we want to expand the node with the *highest* possible profit bound, we can simply insert nodes into the Priority Queue with their bounds multiplied by `-1`!

1. Create a Priority Queue.
2. Push the root node into the PQ, prioritized by its upper bound.
3. While the PQ is not empty:
   - Pop the node with the **highest bound**.
   - **Crucial Check:** If the highest possible bound of the best node in the queue is STILL worse than our current `max_profit`, we can **instantly terminate the entire algorithm!** Because it's a priority queue, we mathematically guarantee that no other node remaining in the queue can possibly beat `max_profit` either.
   - Expand the node (Take and Skip branches).
   - If a branch is valid, update `max_profit`.
   - Calculate the bounds for the new branches. If their bounds are > max\_profit, push them into the PQ.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for bb_03: 0/1 Knapsack (Least-Cost B&B).

Solve 0/1 knapsack via Least-Cost (LC) branch and
"""


def solve(values, weights, capacity, n):
    """0/1 Knapsack via Least-Cost Branch and Bound.

    Sort items by value/weight ratio descending. Build a
    priority queue (min-heap by lower bound) of live nodes.
    Each node has level, accumulated value, accumulated weight,
    and an upper bound (fractional knapsack from this level).
    Pop the node with the smallest lower bound; if it is at
    leaf level, update the best. Generate both children
    (exclude and include the next item), compute their bounds,
    and enqueue if they are still promising (UB <= best).
    """
    if n == 0 or capacity <= 0:
        return 0
    # Sort items by value/weight ratio descending.
    order = sorted(range(n), key=lambda i: values[i] / weights[i], reverse=True)
    v_sorted = [values[i] for i in order]
    w_sorted = [weights[i] for i in order]
    # Precompute suffix sums for the fractional upper bound.
    import heapq
    INF = float("inf")
    best = 0

    def upper_bound(level, cur_value, cur_weight):
        """Fractional knapsack UB from `level` onwards."""
        if cur_weight > capacity:
            return -INF
        value = cur_value
        weight = cur_weight
        for i in range(level, n):
            if weight + w_sorted[i] <= capacity:
                weight += w_sorted[i]
                value += v_sorted[i]
            else:
                # Take a fraction of item i.
                frac = (capacity - weight) / w_sorted[i]
                value += v_sorted[i] * frac
                break
        return value

    def lower_bound(level, cur_value, cur_weight):
        """LB: same as UB but break instead of taking fraction."""
        if cur_weight > capacity:
            return -INF
        value = cur_value
        weight = cur_weight
        for i in range(level, n):
            if weight + w_sorted[i] <= capacity:
                weight += w_sorted[i]
                value += v_sorted[i]
            else:
                break
        return value

    # For MAXIMIZATION, the correct LC search is "best-first by
    # upper bound": pop the node with the highest UB. Early-exit
    # when the head's UB is no greater than the current best.
    # We use a max-heap by negating the UB.
    # Each queue entry: (neg_ub, counter, level, cur_value, cur_weight)
    counter = 0
    pq = []
    initial_ub = upper_bound(0, 0, 0)
    heapq.heappush(pq, (-initial_ub, 0, 0, 0, 0, 0))
    while pq:
        neg_ub, _, level, cur_value, cur_weight, _ = heapq.heappop(pq)
        ub = -neg_ub
        # Early-exit: if the highest UB in the queue is no
        # better than our best-known solution, no future node
        # can improve on `best`.
        if ub <= best:
            break
        if level == n:
            # Leaf.
            if cur_value > best:
                best = cur_value
            continue
        # Right child: exclude item at this level.
        right_value = cur_value
        right_weight = cur_weight
        right_ub = upper_bound(level + 1, right_value, right_weight)
        if right_ub > best:
            right_lb = lower_bound(level + 1, right_value, right_weight)
            if right_lb < INF:
                counter += 1
                heapq.heappush(pq, (-right_ub, counter, level + 1,
                                    int(right_value),
                                    int(right_weight), 0))
        # Left child: include item at this level (if it fits).
        if cur_weight + w_sorted[level] <= capacity:
            left_value = cur_value + v_sorted[level]
            left_weight = cur_weight + w_sorted[level]
            left_ub = upper_bound(level + 1, left_value, left_weight)
            if left_ub > best:
                left_lb = lower_bound(level + 1, left_value, left_weight)
                if left_lb < INF:
                    counter += 1
                    heapq.heappush(pq, (-left_ub, counter, level + 1,
                                        int(left_value),
                                        int(left_weight), 0))
    return best
```

</details>

## Walk-through

*(Conceptual)*
`capacity = 10`
`Items: I0(40,4), I1(50,5), I2(20,5)`

1. **Root:** `profit=0`. Bound=94. `PQ = [Root(94)]`.
2. **Pop Root (94):**
   - Take I0: `profit=40`. Bound=94. `max_profit=40`.
   - Skip I0: `profit=0`. Bound=70.
   - `PQ = [Take(94), Skip(70)]`.
3. **Pop Take (94):** *(Notice it ignores the Skip branch completely!)*
   - Take I1: `profit=90, w=9`. Bound=94 (40+50 + 1/5*20). `max_profit=90`.
   - Skip I1: `profit=40, w=4`. Bound=60 (40+20).
   - `PQ = [Take-Take(94), Skip(70), Take-Skip(60)]`.
4. **Pop Take-Take (94):**
   - Take I2: Over capacity! (w=14 > 10). Invalid.
   - Skip I2: `profit=90`. Bound=90.
   - `PQ = [Skip-I2(90), Skip(70), Take-Skip(60)]`.
5. **Pop Skip-I2 (90):**
   - Reached the end. `max_profit` is already 90.
   - `PQ = [Skip(70), Take-Skip(60)]`.
6. **Pop Skip (70):**
   - Wait! `u.bound (70) <= max_profit (90)`. **BREAK LOOP!**

Algorithm terminates instantly! It never even generated the nodes underneath the `Skip(70)` branch! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(N)$ |
| **Average** | Much faster than FIFO B&B | $O(Nodes Generated)$ |
| **Worst** | $O(2^N)$ | $O(2^N)$ |

The Best-First heuristic generally results in generating far fewer nodes than the FIFO approach because it finds the optimal solution (or a very close one) almost immediately, rendering the bounds of all other pending nodes obsolete. However, in the worst mathematical case, it still degrades to exploring the full $O(2^N)$ space.
Space complexity is heavily improved in average cases as fewer nodes sit in the Priority Queue simultaneously.

## Variants & optimizations

- **A* Search:** LC-Search is mathematically identical to A* Search algorithm on graphs! The path cost `g(x)` is the profit collected so far, and the heuristic `h(x)` is the fractional upper bound of the remaining items. Because the fractional knapsack is an admissible heuristic (it never underestimates the max profit), A* guarantees optimality!

## Real-world applications

- **AI Planners:** Best-First Search is the foundation of almost all modern AI action planning and routing logic.

## Related algorithms in cOde(n)

- **[bb_01 - 0-1 Knapsack FIFO](bb_01_0-1-knapsack.md)** — The Breadth-First Search variant of the exact same algorithm.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
