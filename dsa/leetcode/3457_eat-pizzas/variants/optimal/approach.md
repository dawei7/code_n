## General

**Separate score-producing pizzas from fillers.** Every day consumes four pizzas. On an odd day, only the largest selected weight $Z$ contributes. The other three can be smaller fillers. On an even day, the second-largest $Y$ contributes, so that day also needs one pizza at least as large as $Y$ to serve as the non-scoring $Z$.

Let

`days = len(pizzas) // 4`.

Among 1-indexed days, the number of odd days is `odd = (days + 1) // 2`, and even days number `even = days - odd`.

**Sort weights to expose the optimal roles.** After ascending sort, use the absolute largest `odd` pizzas as odd-day winners. Each scores its full weight and needs only three low fillers, so no larger pizza must be sacrificed above it.

This is `sum(pizzas[-odd:])`.

For every even-day winner, one larger remaining pizza must be consumed as that day's $Z$. Among the weights below the odd winners, take the largest as a sacrificial $Z$ and the next largest as scoring $Y$. Repeating this means selecting every second weight while moving downward.

The first even winner index is

`len(pizzas) - odd - 2`.

The element one position above it is its required larger companion. After scoring this winner, decrementing by two skips that companion pair and finds the next even winner.

For sorted `[1,2,3,4,5,6,7,8]`, there is one odd and one even day. Weight $8$ is the odd winner. Of the remaining high weights, $7$ is sacrificed as even-day $Z$ and $6$ scores as $Y$, producing $14$. The remaining four small values fill unused $W$ and $X$ roles and odd-day fillers.

**Why odd days receive the very largest weights.** An odd score consumes one high-value resource per scored pizza: its winner itself. An even score consumes two ordered high resources: the winner and a no-smaller sacrifice. If an absolute-largest weight were used as an even sacrifice while a smaller value scored on an odd day, swapping the largest into the odd scoring role cannot reduce any day's feasibility and increases or preserves total score.

After reserving odd winners, pairing remaining high values consecutively is optimal for even days. The scoring $Y$ should be as large as possible, but it must have some unused larger $Z$. Taking the top pair and scoring its smaller member dominates pairing that $Z$ with any smaller winner. Repeating the exchange establishes the every-second selection.

**Why all leftover pizzas can be assigned as fillers.** Each odd day needs three non-scoring pizzas, and each even day needs two pizzas no larger than $Y$ in addition to its selected $Y,Z$ pair. The algorithm consumes exactly `odd + 2 * even` high-role pizzas. The remaining count is

$$
4\cdot\textit{days}-(\textit{odd}+2\cdot\textit{even}),
$$

exactly enough for the low filler slots. Because these remaining values lie no higher than the chosen role values in sorted order, they can be distributed without changing which pizza is $Y$ or $Z$.
Any schedule can be viewed only by the sorted ranks assigned to scoring and sacrifice roles; day order within odd or even classes does not matter. Moving larger values into odd scoring roles and pairing the next remaining ranks as even sacrifice/winner never lowers the score. The source implements precisely this canonical optimal allocation.

The method sorts `pizzas` in place, so the caller's list remains reordered after return.

Day numbering matters only through how many days use each scoring rule. Once roles are assigned, the selected odd winners and even pairs can be distributed among days of the same parity in any order without changing the total.

## Complexity detail

Let $n=\lvert\texttt{pizzas}\rvert$. Sorting dominates with $O(n\log n)$ time. Summing odd winners and iterating over at most $n/8$ even days take $O(n)$ additional time.

Python's sort may use $O(n)$ temporary space; scalar indices use $O(1)$. The manifest's $O(n)$ space bound is safe. The input list itself is mutated rather than copied.

## Alternatives and edge cases

- **Simulate all daily groupings:** The number of partitions into groups of four is enormous. Only sorted role ranks affect the score.
- **Use the four largest pizzas every day:** This wastes valuable weights in non-scoring roles and can reduce later scores.
- **Score the largest remaining pizza on an even day:** It cannot be $Y$ without an even larger $Z$ in the same group.
- **One day:** It is odd, so the largest pizza is the answer and the other three are fillers.
- **No even days:** The loop is empty and only the largest odd-count weights score.
- **Duplicate weights:** Any equal copies can exchange roles without changing feasibility or score.
- **All weights equal:** Every day scores that common weight, and the formula selects exactly one score per day.
- **In-place sorting:** Callers needing original order must pass a copy.
- **Odd-day count:** Ceiling division reflects days $1,3,5,\ldots$.
- **All pizzas consumed:** The role-and-filler count accounts for exactly four pizzas per day.
