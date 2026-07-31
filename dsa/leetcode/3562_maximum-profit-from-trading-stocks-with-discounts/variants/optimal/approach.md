## General

Root the hierarchy at employee `1`. For each employee $u$, compute two exact-spend tables:

- `without_discount[c]` is the maximum profit obtainable from $u$'s subtree with total buying cost exactly $c$ when $u$'s parent did not buy.
- `with_discount[c]` is the analogous value when $u$'s parent bought, so $u$ may buy for $\lfloor\texttt{present}[u]/2\rfloor$.

Unreachable costs carry negative infinity. Two intermediate tables combine the children. If $u$ is skipped, every child receives its `without_discount` state. If $u$ is bought, every child receives its `with_discount` state because $u$ is their direct boss. Each child is merged by a knapsack convolution over how the current cost is divided between the already processed children and the new child's subtree.

After all children are combined, skipping $u$ copies the first intermediate table into both parent-state results. Buying $u$ starts from the second intermediate table, adds the appropriate current price for the parent state, and adds `future[u] - actual_price` to the profit. Keeping both choices is essential: a stock with negative individual profit can still be optimal when its purchase unlocks larger discounts for its children.

Every table entry represents exactly the best feasible choice for its state and cost. The child convolution considers every allocation of that cost among disjoint subtrees, and the final skip/buy transition covers the only two possibilities for $u$. Induction from leaves to the CEO therefore covers every valid stock subset with its correct direct-boss discounts. The answer is the largest value in the CEO's `without_discount` table for any cost at most $B$.

## Complexity detail

Let $B=\texttt{budget}$. Merging one child uses $O(B^2)$ time, and the tree has $n-1$ child edges, so total time is $O(nB^2)$. Each node produces two arrays of length $B+1$; including recursion and child results awaiting combination, the worst-case auxiliary space is $O(nB)$.

## Alternatives and edge cases

- **Enumerate every purchase subset:** Checking all $2^n$ subsets can calculate discounts correctly but is infeasible for $n=160$.
- **Ordinary one-dimensional knapsack:** A single table loses whether the subtree root's direct boss bought, yet that state changes both the root's cost and all downstream choices.
- **Greedy by individual profit or ratio:** Buying a locally losing boss can unlock a larger child discount, so stocks do not have independent values.
- **Reuse tomorrow's profit:** Profit is earned only after all purchases; today's total cost alone must remain within `budget`.
- **Direct boss only:** A purchased grandparent does not discount a stock when its direct parent was skipped.
- **Odd current price:** The discounted cost uses floor division.
- **Negative-profit stock:** It may be skipped, but it must not be discarded before considering its effect on descendants.
- **No profitable feasible purchase:** The empty selection has cost and profit zero, so the answer is zero.
