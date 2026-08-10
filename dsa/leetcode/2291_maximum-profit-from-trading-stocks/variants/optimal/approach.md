## General

**Recognize a zero-one knapsack problem**

Buying stock `i` costs `present[i]` units of the current budget and yields profit

$$
\texttt{future}[i]-\texttt{present}[i].
$$

Each stock may be bought at most once. The total purchase cost may not exceed `budget`, and the objective is to maximize the sum of profits. These are exactly zero-one knapsack choices: each item is either skipped or selected once.

Future sale proceeds cannot fund current purchases. The budget constraint applies to the sum of present prices chosen now.

**Define the table state**

`f[i][j]` is the maximum profit obtainable using only the first `i` stocks with a spending capacity of at most `j`.

The table has `len(present)+1` rows and `budget+1` columns. Row zero contains zeros because no profit can be made from zero stocks. Column meanings include unused budget; a solution is never required to spend exactly `j`.

**Start every state with the skip choice**

For stock `i-1`, the code first assigns

`f[i][j] = f[i - 1][j]`.

This carries forward the best result without buying the current stock. It guarantees that adding another available stock can never reduce the stored optimum.

It also allows any amount of budget to remain unused.

**Consider buying a profitable stock**

The stock can be selected only when `j >= w`, where `w` is its present price. The remaining capacity is `j-w`.

The candidate profit is

`f[i - 1][j - w] + future[i - 1] - w`.

Using the previous row is essential: it prevents the current stock from being selected repeatedly. The maximum between this candidate and the skip state implements the two exhaustive choices.

**Why nonpositive-profit stocks are ignored**

The source also requires `future[i - 1] > w` before evaluating the buy transition. If future value equals present price, buying adds zero profit while consuming budget; skipping is at least as good. If future value is smaller, buying produces a loss and can never help maximize profit when purchases are optional.

Therefore, excluding zero and negative profit items cannot remove an optimal solution.

**Handle a zero-price stock**

Present prices may be zero. If such a stock has positive future value, `j >= w` is true for every budget and `j-w=j`.

The transition still reads from row `i-1`, so the free stock is added exactly once to every capacity state. Zero cost does not turn the zero-one item into an unlimited item.

**Why the recurrence is correct**

Consider an optimal selection from the first `i` stocks under capacity `j`. Either it omits stock `i-1`, in which case its profit is bounded by `f[i-1][j]`, or it includes that stock. In the second case, the remaining chosen stocks come from the first `i-1` and fit within `j-w`, so their best profit is `f[i-1][j-w]`.

The recurrence evaluates both exhaustive cases whenever buying is feasible and worthwhile. Induction over rows proves every table entry is optimal.

**Read the final answer**

`f[-1][-1]` is the state using all stocks with capacity `budget`. Since capacities mean “at most,” it includes every feasible purchase set, including the empty set. The empty set has profit zero, so the method never returns a negative value.

For the first example, the selected costs five, two, and three exactly fill budget ten, and their profits three, one, and two total six.

**Account for the exact table shape**

The branch manifest describes a one-dimensional budget DP, but the executable source stores all `n+1` rows. This makes the previous-row dependency visually explicit and guarantees zero-one behavior without reverse capacity iteration.

Row compression is a valid alternative, not the code being explained.

## Complexity detail

Let `n` be the number of stocks and `B` the budget. The nested loops fill `(n)(B+1)` states with constant work per state, so time is `O(nB)`.

The full table contains `(n+1)(B+1)` integers, giving `O(nB)` auxiliary space for the exact implementation. This differs from the manifest's `O(B)` optimized-space summary.

The input arrays are read but not modified.

## Alternatives and edge cases

- **One-dimensional knapsack:** Update capacities from `B` down to the item's price to achieve `O(B)` space. Descending order is required to avoid reusing a stock.
- **Ascending one-dimensional update:** It would allow the same positive-profit stock to be selected multiple times and solve an unbounded problem incorrectly.
- **Greedy by profit:** A high-profit stock may consume too much budget compared with several smaller choices.
- **Greedy by profit-to-cost ratio:** Zero-one knapsack does not generally admit the fractional-knapsack ratio rule.
- **Negative-profit stock:** It is skipped because buying is optional and would reduce the objective.
- **Zero-profit stock:** Ignoring it is harmless because it cannot raise profit.
- **Zero-price profitable stock:** It is included at most once through the previous-row transition.
- **Zero budget:** Only profitable zero-price stocks can contribute.
- **Stock price above budget:** No capacity state can select it.
- **Unused budget:** State `j` means cost at most `j`, so exact spending is unnecessary.
- **All trades unprofitable:** The zero-initialized skip path returns zero.
- **Equal array lengths:** The index `i-1` safely pairs each present and future price.
- **No reinvestment:** Future revenue affects profit value only, not current capacity.
- **Input preservation:** The DP table is separate from both price arrays.
