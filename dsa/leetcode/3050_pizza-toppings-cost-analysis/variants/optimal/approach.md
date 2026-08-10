## General

**Assign each topping an alphabetical position.** The CTE `T` reads every topping and computes

`RANK() OVER (ORDER BY topping_name) AS rk`.

Because `topping_name` is the primary key, names are unique. There are no rank ties, so `rk` behaves as an alphabetical position from 1 through $N$.

The rank is not needed to display the answer; it provides a convenient numeric condition for constructing combinations in a canonical order.

**Join three ordered copies of the topping table.** Aliases `t1`, `t2`, and `t3` represent the first, second, and third topping. Join conditions require

$$
\texttt{t1.rk}<\texttt{t2.rk}<\texttt{t3.rk}.
$$

These strict inequalities accomplish three goals at once.

First, no topping can repeat because one rank cannot be strictly less than itself. Second, names appear alphabetically in the selected triple because rank follows `topping_name`. Third, every unordered set of three toppings appears exactly once: among its six permutations, only the increasing-rank order satisfies both joins.

**Build the requested columns.** `CONCAT` joins the three already ordered names with commas, producing strings such as `Chicken,Pepperoni,Sausage`. The cost expression adds the corresponding three decimal values.

No grouping is needed because each joined row is already one distinct three-topping combination.

**Apply the two-level output order.** `ORDER BY 2 DESC, 1 ASC` uses select-list ordinals. Column 2 is `total_cost`, so expensive pizzas come first. Column 1 is `pizza`, so equal-cost combinations are ordered alphabetically ascending.

Using aliases instead of ordinals would be more self-documenting, but the semantics are identical.

**Why the join covers all possibilities.** Take any three distinct toppings. Their unique alphabetical ranks can be sorted as $r_1<r_2<r_3$. The join produces the row with those toppings as `t1`, `t2`, and `t3`. No other arrangement passes the inequalities. Conversely, every produced row contains three distinct toppings and is alphabetically ordered. The output is therefore a one-to-one enumeration of valid pizzas.

**Rounding behavior of the exact query.** The contract explicitly asks for total cost rounded to two decimal places. The source returns

`t1.cost + t2.cost + t3.cost`

without an explicit `ROUND(..., 2)`. If the MySQL column's actual decimal scale is two, decimal addition naturally retains an appropriate exact scale and the displayed result meets the examples. But the local schema says only `decimal` and does not state scale. With higher-scale inputs, this query does not explicitly enforce two-decimal rounding. That is a fidelity caveat in the protected source.

**Why rank rather than row number still works.** `RANK` can create gaps when sort keys tie. The primary-key guarantee makes equal names impossible, so it produces the same ordering relation needed here. Even with gaps, strict rank order would still distinguish different names; uniqueness is what prevents equal-ranked distinct toppings.

## Complexity detail

Let $N$ be the number of toppings and

$$
K=\binom{N}{3}.
$$

Ranking requires ordering names, typically $O(N\log N)$. The joins logically produce $K=O(N^3)$ rows. Sorting those rows for final output costs $O(K\log K)$, which is $O(N^3\log N)$ after simplification.

The result itself contains $K$ rows, so materialization and sorting may require $O(K)=O(N^3)$ space. Actual database execution depends on indexes, optimizer join plans, memory limits, and whether temporary data spills to disk; these bounds describe logical worst-case output processing.

The query is read-only and does not alter `Toppings`.

## Alternatives and edge cases

- **Compare names directly in joins:** Conditions `t1.topping_name < t2.topping_name` and `t2.topping_name < t3.topping_name` can enforce the same uniqueness and alphabetical order without a ranking CTE.
- **Cross join then deduplicate:** Generating all $N^3$ ordered triples and applying `DISTINCT` wastes work and makes repeated-topping exclusion harder to reason about.
- **Recursive combination generation:** It is unnecessary for a fixed combination size of three.
- **Fewer than three toppings:** No triple satisfies the joins, so the result is empty.
- **Exactly three toppings:** Exactly one increasing-rank triple is returned.
- **Equal costs:** The secondary pizza ordering determines deterministic ascending output.
- **Unique names:** The primary key guarantees rank ties cannot merge distinct toppings.
- **Names containing commas:** `CONCAT` would make the display ambiguous, but the reference does not define escaping; the source follows the required literal format.
- **Decimal rounding:** The exact source relies on MySQL decimal scale propagation and does not explicitly call `ROUND(...,2)`, so higher-scale costs expose a contract gap.
- **Output ordering:** Ordinals 2 and 1 correctly mean cost descending, then pizza ascending.
- **Why `UNION` or grouping is unnecessary:** The strict rank chain already makes every selected set unique. Adding duplicate elimination would impose extra work without changing valid output.
- **Output-size lower bound:** Any correct query must emit $\binom N3$ rows when $N\ge3$. Consequently cubic result production is unavoidable even if indexes make the joins themselves efficient.
- **Lexicographic ordering basis:** Alphabetical order follows the database collation used by `ORDER BY topping_name`. The concatenated name order and rank comparisons use that same collation consistently.
