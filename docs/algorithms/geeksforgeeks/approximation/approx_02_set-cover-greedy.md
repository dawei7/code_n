# Set Cover (Greedy Approximation)

| | |
|---|---|
| **ID** | `approx_02` |
| **Category** | approximation |
| **Complexity (required)** | $O(S * N)$ |
| **Difficulty** | 4/10 |
| **Interview relevance** | 5/10 |
| **Wikipedia** | [Set cover problem](https://en.wikipedia.org/wiki/Set_cover_problem) |

## Problem statement

Given a "universe" of elements U, and a family S of subsets of U, find the minimum number of subsets from S whose union equals the entire universe U.
This is a classic NP-Hard problem. You must implement a greedy approximation algorithm that guarantees an approximation ratio of H_n (where H_n is the n-th harmonic number, roughly \ln(N)).

**Input:** A list of elements representing the universe `U`, and a list of lists `S` representing the subsets.
**Output:** A list of indices of the selected subsets that cover `U`.

## When to use it

- Whenever you face a resource allocation problem where you must "cover" a set of requirements using the fewest number of predefined packages.

## Approach

While Vertex Cover had a clever 2-approximation (pick both endpoints of an edge), Set Cover does not have a constant-factor approximation. The best polynomial-time approximation we can achieve is bounded by $O(\ln N)$.

**The Greedy Approach:**
The logic is highly intuitive. At every step, we want to pick the subset that covers the **maximum number of elements that we haven't covered yet**.

1. Maintain a `uncovered` set of elements, initially equal to `U`.
2. While `uncovered` is not empty:
   - Iterate through all available subsets in `S`.
   - For each subset, count how many elements in it are *also* in the `uncovered` set (i.e., the size of the intersection).
   - Pick the subset that yields the highest intersection size.
   - Add this subset to our results.
   - Remove all elements of this subset from the `uncovered` set.
3. Return the results.

**Why is it H_n-approximate?**
In the worst case, the greedy choice might get "tricked" into picking many slightly overlapping sets instead of the optimal non-overlapping sets. However, mathematically, each step covers a significant fraction of the remaining uncovered elements, leading to a logarithmic ratio bound: \ln(|U|) + 1.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for approx_02: Set Cover (Greedy).

Each step picks the set covering the most uncovered elements.
"""


def solve(universe, sets, m, k):
    if k == 0:
        return []
    uncovered = set(universe)
    chosen = []
    while uncovered:
        best_idx = -1
        best_count = 0
        for i, s in enumerate(sets):
            count = sum(1 for x in s if x in uncovered)
            if count > best_count:
                best_count = count
                best_idx = i
        if best_idx == -1 or best_count == 0:
            break
        chosen.append(best_idx)
        for x in sets[best_idx]:
            uncovered.discard(x)
    return sorted(chosen)
```

</details>

## Walk-through

`Universe = {1, 2, 3, 4, 5}`
`Subsets = [S0:{1, 2, 3}, S1:{2, 4}, S2:{3, 4}, S3:{4, 5}]`
*(Optimal is S0 and S3 -> covers all 5 elements using 2 sets).*

**Iteration 1:**
`uncovered = {1, 2, 3, 4, 5}`
- `S0` covers 3 elements.
- `S1` covers 2 elements.
- `S2` covers 2 elements.
- `S3` covers 2 elements.
Best is `S0`. Select `S0`.
`uncovered = uncovered - {1, 2, 3} = {4, 5}`.

**Iteration 2:**
`uncovered = {4, 5}`
- `S1` covers {2, 4} \cap {4, 5} = {4} (1 element).
- `S2` covers {3, 4} \cap {4, 5} = {4} (1 element).
- `S3` covers {4, 5} \cap {4, 5} = {4, 5} (2 elements).
Best is `S3`. Select `S3`.
`uncovered = uncovered - {4, 5} = {}`.

Loop finishes! Selected: `[S0, S3]`. ✓
*(In this case, the greedy algorithm actually found the absolute optimal answer).*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(S * N)$ | $O(S * N)$ |
| **Average** | $O(S * N^2)$ | $O(S * N)$ |
| **Worst** | $O(S * N^2)$ | $O(S * N)$ |

*Where N is the size of the Universe and S is the number of subsets.*
In the worst case, we might only cover 1 new element per iteration, causing the outer `while` loop to run N times. Inside, we loop over all S subsets, taking $O(N)$ time for intersection. Worst-case time is $O(S \cdot N^2)$.
Space complexity is $O(S \cdot N)$ to store the sets in memory.

## Variants & optimizations

- **Weighted Set Cover:** If each subset has a "cost", instead of picking the subset that covers the absolute maximum elements, you pick the subset that has the lowest **cost-effectiveness** ratio: `cost(s) / elements_covered`. This maintains the exact same \ln(N) approximation ratio!
- **Dancing Links (Algorithm X):** If you need the *exact* minimum cover (or specifically, an Exact Cover where no elements overlap), Donald Knuth's Algorithm X using Dancing Links solves it brilliantly via backtracking, though still in exponential time.

## Real-world applications

- **Software Dependencies:** A package manager (like `npm` or `pip`) trying to satisfy a universe of requested libraries by installing the absolute minimum number of meta-packages.
- **Crew Scheduling:** Airlines covering all scheduled flights (universe) using the minimum number of predefined crew shifts (subsets).

## Related algorithms in cOde(n)

- **[approx_01 - Vertex Cover](approx_01_vertex-cover-2-approx.md)** — A special case of Set Cover where every element (edge) appears in exactly two sets (vertices).
- **[greedy_02 - Fractional Knapsack](../greedy/greedy_02_fractional-knapsack.md)** — Shares the "cost-effectiveness" greedy ratio heuristic.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
