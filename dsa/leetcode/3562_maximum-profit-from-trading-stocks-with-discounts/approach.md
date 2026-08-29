## General

The hierarchy is a rooted tree, and buying one employee’s stock affects only the purchase price of that employee’s **direct children**. This local parent-to-child dependency makes tree dynamic programming possible.

The other constraint is a global budget. Subtrees compete for that budget, so their solutions must be merged like knapsack items. The source combines these ideas into a two-state tree knapsack:

- one state says the current employee’s parent was not purchased;
- the other says the parent was purchased, so the current employee may buy at half price.

For every budget capacity from zero through `budget`, the DP stores the best achievable profit without exceeding that capacity.

**Why the hierarchy can be processed as a tree**

The directed adjacency list `g[u]` contains the direct reports `v` from hierarchy edges `[u, v]`. The guarantees say the hierarchy is acyclic, contains `n-1` edges, and every employee is reachable from employee `1`. Together these properties make it a rooted tree with CEO `1` as the root.

Each non-root employee belongs to exactly one child subtree, so sibling subtrees are disjoint. Once the decision to buy or skip their common boss is known, those subtrees interact only through how the budget is divided among them. This is precisely the independence needed for knapsack merging.

**The returned table f**

For a node `u`, `dfs(u)` returns a table `f` with rows `0` through `budget` and two columns.

`f[j][pre]` is the maximum profit obtainable from the subtree rooted at `u` while spending **at most** `j`, where:

- `pre = 0` means `u`’s direct boss was not purchased, so `u` has no discount;
- `pre = 1` means `u`’s direct boss was purchased, so `u` may buy at half price.

This is an at-most-capacity table, not an exact-spend table. Its entries start at zero even for positive capacities, and unused budget is allowed. That matches the problem: there is no requirement to spend every available unit.

The manifest summary calls these “exact-spend tables,” but the executable recurrence and initialization implement “best profit with spending at most `j`.” The at-most interpretation is the faithful one and is also what makes zero-initialized unreachable exact-spend states harmless.

**The child-only table nxt uses a different meaning for its state**

Before deciding whether to buy `u` itself, the source recursively solves and combines all child subtrees into `nxt`.

`nxt[j][state]` is the best combined profit from the already merged children with at most `j` budget, where:

- `state = 0` means `u` is **not** purchased, so every direct child receives `pre = 0`;
- `state = 1` means `u` **is** purchased, so every direct child receives `pre = 1`.

This distinction is subtle. In returned table `f`, the state describes whether the **parent of `u`** was bought. In child aggregate `nxt`, it describes whether **`u` itself** will be bought, because that is the fact relevant to the children’s discounts.

The source reuses the variable name `pre` in the merge loops, but its contextual meaning is the second one there.

**Merging one child by budget splitting**

Suppose some children have already been merged into `nxt` and the next child `v` returns table `fv`. For total capacity `j`, the code tries every allocation `jv` from zero through `j`:

- capacity `j-jv` is reserved for previously merged children;
- capacity `jv` is offered to child `v`.

For each purchase state of `u`, the candidate is

`nxt[j - jv][pre] + fv[jv][pre]`.

The same `pre` is used on both sides because all direct children either receive the discount from a purchased `u` or do not receive it from an unpurchased `u`.

Taking the maximum over all splits considers every way to distribute the available money between the child subtrees. Since each component may spend less than its offered capacity, their actual combined spending is still at most `j`.

The outer capacity loop runs downward from `budget` to zero. When `jv > 0`, `j-jv < j`, and that smaller `nxt` row has not yet been updated for the current child. Thus it still represents only the earlier children, preventing child `v` from being merged more than once. The `jv = 0` case references the current row, but `fv[0][pre]` cannot add a positive-cost purchase; under the positive present-price constraints its profit is zero, so it does not create repeated benefit.

After all children are processed, `nxt` contains the optimal child contribution for both possibilities: skipping `u` or buying `u`.

**Deciding whether to buy the current employee**

For every capacity `j` and incoming parent state `pre`, the current purchase cost is

`cost = present[u - 1] // (pre + 1)`.

If `pre = 0`, the denominator is one and the full present price is used. If `pre = 1`, the denominator is two and integer division implements `floor(present/2)`.

There are two decisions.

**Skip u.** The current employee contributes no cost and no profit. Because `u` was not purchased, its children receive no discounts, regardless of whether `u` itself was eligible for a discount. The value is

`nxt[j][0]`.

**Buy u.** This is possible only if `j >= cost`. The purchase leaves capacity `j-cost` for the children. Since `u` was purchased, every direct child may use its discounted state, giving

`nxt[j - cost][1] + future[u - 1] - cost`.

The source takes the maximum of these decisions. A stock with negative individual profit is not automatically rejected: buying a boss at a loss can still be optimal if the discounts unlocked for children create a larger total gain. The recurrence evaluates the complete subtree effect.

**Why profits cannot fund purchases**

Only present-day purchase costs are subtracted from the budget index. Future sale proceeds appear solely in the objective term `future - cost`. They never increase `j` or the remaining capacity.

Therefore every selected set has total buying cost at most the original budget, and future profit cannot be reinvested. This exactly enforces the note in the statement.

**Root state and final answer**

Employee `1` has no parent, so no parent purchase can discount the CEO’s stock. The answer is

`dfs(1)[budget][0]`.

Using the full budget as a capacity does not force full spending because the table means “at most.” It simply makes every affordable strategy available.

**Why the recurrence is complete**

For a fixed node, any feasible strategy either buys `u` or skips it. That choice uniquely determines which state all direct children receive. Once that state is fixed, each child subtree is independent except for its allocated share of the budget, and the knapsack merge tries every possible share.

By induction, each child table already contains the best strategy for every capacity and parent state. The merge therefore finds the best combination of child strategies, and the final two-way decision finds the best complete strategy for `u`’s subtree. The base case of a leaf is included naturally: its zero-initialized `nxt` represents having no child profit.

## Complexity detail

Let `B` be `budget`. Merging one child loops over total capacity `j`, child capacity `jv`, and two states. The number of budget pairs is `O(B^2)`. Every non-root node is merged once into its parent, so all child merges cost `O(nB^2)` time.

Constructing each node’s final `f` table adds `O(B)` work, which is dominated. Total time is `O(nB^2)`.

Each DP table contains `2(B+1) = O(B)` values. The recursive implementation creates a `nxt` table in every active stack frame before descending. On a chain, `O(n)` frames can coexist, each retaining `O(B)` state, so the worst-case auxiliary space is `O(nB)`. Recursion depth is at most `n \le 160`, below Python’s usual recursion limit.

The returned table of a completed child may be released after it is merged, but that rolling behavior does not improve the worst-case chain bound because the ancestors’ `nxt` tables remain live.

## Alternatives and edge cases

- **Flat subset knapsack:** Treating employees as independent items fails because a child’s price depends on whether its direct boss is selected. The tree state is necessary to preserve that dependency.
- **Enumerate all purchase subsets:** There are `2^n` subsets, far too many for `n=160`. Tree knapsack compresses subsets that share the same subtree, budget, and parent-purchase state.
- **Exact-spend DP:** It can work if unreachable states are initialized to negative infinity and the final answer takes the best spend up to `B`. The exact source instead uses at-most-capacity states initialized to zero.
- **Cap tables by subtree cost:** Limiting each subtree’s budget dimension to its maximum useful purchase cost can reduce practical work. The source uses the global `B` everywhere for simpler transitions.
- **Skip an unprofitable boss automatically:** This greedy rule is unsafe because buying that boss may unlock discounts that make descendant purchases highly profitable.
- **Discount propagation:** Buying `u` discounts only its direct children. A grandchild receives a discount only if its own direct parent is also bought; the recursive state transition enforces this one edge at a time.
- **Discount eligibility without buying:** If `u`’s parent was bought but `u` is skipped, `u`’s children do not receive discounts. The skip transition deliberately uses `nxt[j][0]`.
- **Odd present price:** Integer division in `present // 2` implements the required floor, so a price of five becomes two.
- **Unused budget:** At-most states allow leftover money, which is essential when no remaining stock is beneficial or affordable.
- **Zero selected stocks:** All tables begin with profit zero, so buying nothing is always available and the answer cannot be forced negative.
- **One employee:** The root chooses between skipping and buying at full price; no child merge occurs.
- **Chain hierarchy:** Discounts can propagate down the chain only through a consecutive sequence of purchased bosses, exactly as the state passed from parent to child records.
- **Wide hierarchy:** Sibling subtrees share no discount dependency; only their budget allocation interacts, which is handled by the grouped-knapsack merge.
- **Future proceeds:** They raise profit but never capacity, so the algorithm never spends money that becomes available only tomorrow.
- **Built-in name shadowing:** The local lambda named `max` replaces Python’s built-in only inside this method and still compares the two transition values correctly; it does not change the algorithm.
