## General

**Turn each section into a binary choice**

Winning section $k$ requires exactly `aliceArrows[k] + 1` useful arrows and yields $k$ points. Spending fewer does not win, while spending more cannot increase the score. Therefore every optimal allocation corresponds to a subset of sections Bob chooses to win at their minimum costs.

Enumerate all $2^{12}$ subsets. For each mask, sum its arrow cost and score and retain the highest-scoring affordable subset. Construct its allocation using the minimum winning count at each selected section.

**Place arrows that do not affect the optimum**

The selected subset may use fewer than `numArrows` arrows. Put every leftover arrow into section zero. Section zero is worth no points, so this cannot reduce Bob's selected score or create a more valuable unaccounted win.

Every legal allocation wins some subset of sections and spends at least the enumerated minimum cost for that subset. Consequently, if the allocation is affordable, the enumeration considers the same subset with no greater cost and the same score. Choosing the best affordable mask is therefore globally optimal, and adding leftovers preserves feasibility.

## Complexity detail

Let $s=12$ be the fixed section count. Evaluating $s$ bits for all $2^s$ masks takes $O(2^s s)$ time, and one candidate allocation uses $O(s)$ space.

Because the legal contract fixes $s$ at twelve, this is bounded work: exactly 4,096 masks and at most 49,152 section inspections. The complexity certificate records why runtime scaling is not meaningful for this fixed domain.

## Alternatives and edge cases

- **Backtracking:** Include-or-skip recursion explores the same subset space and can carry cost incrementally.
- **Knapsack by arrow count:** A budget-indexed dynamic program depends on `numArrows` up to $10^5$, despite there being only twelve choices.
- **Greedy by score or ratio:** A high-value section can consume too many arrows; neither score nor score-per-arrow ordering guarantees the best subset.
- **Tied optima:** Any allocation with the maximum score and the exact arrow total is valid.
- **Section zero:** Winning it adds no score, making it a safe destination for leftover arrows.
- **Unbeatable section:** If its minimum winning cost exceeds `numArrows`, that section cannot appear in any affordable mask.
