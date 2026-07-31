## General

**Encode uniqueness and alphabetical order in the joins.** Treat three aliases
of `Toppings` as the first, second, and third positions of a pizza. Join them
under `first.topping_name < second.topping_name` and
`second.topping_name < third.topping_name`. The strict inequalities prevent a
topping from repeating and choose exactly one ordering for every three-row
set. Because that chosen ordering is increasing, the concatenated names are
already alphabetized inside `pizza`.

**Compute one row per combination.** Concatenate the three names with commas
and add their three decimal costs. Apply `ROUND(..., 2)` to the sum so the
projected `total_cost` follows the required two-decimal rule. Every selected
row uses three distinct toppings, and every possible distinct triple has one
unique increasing name order, so the joins produce all and only the required
pizzas exactly once.

**Apply both output priorities explicitly.** Sort first by `total_cost` in
descending order. Add `pizza` in ascending order as the tie-breaker; without
that second key, equal-cost combinations could appear in an arbitrary order.

## Complexity detail

Let $n$ be the number of toppings and $K = \binom{n}{3}$ the output row count.
Generating each combination once takes $O(K)=O(n^3)$ work. Sorting the result
takes $O(K\log K)=O(n^3\log n)$ time, which dominates the query. Materializing
all returned rows uses $O(K)=O(n^3)$ space, although a database engine may
stream parts of the join or sort through external storage.

The output itself can contain $\Theta(n^3)$ rows, and arbitrary decimal costs
determine their required order. This output-and-ordering lower bound is why a
faster principal complexity class is not available for an honest scaling
comparison.

## Alternatives and edge cases

- **Generate all ordered triples and use `DISTINCT`:** This examines six permutations of every combination and then removes duplicates, doing avoidable work and making name ordering less direct.
- **Rank rows before joining:** Assigning an alphabetical row number and joining increasing ranks is correct, but direct primary-key comparisons express the same invariant without a window CTE.
- **Group concatenation:** Aggregating arbitrary groups of three requires extra machinery to enumerate those groups and can make deterministic within-group order database-specific.
- Fewer than three input rows produce no joined row and therefore an empty result.
- Strict name comparisons are safe because `topping_name` is a primary key and therefore unique.
- The `pizza` string uses commas without added spaces, matching the required output shape.
- Rounding applies after all three costs are added, not to each input cost separately.
- Equal totals must use ascending `pizza` order; the secondary `ORDER BY` key is mandatory.
