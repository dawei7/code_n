## General

**Represent one way as a pair of quantities**

A purchase plan is determined by two nonnegative integers:

- `x`, the number of pens;
- `z`, the number of pencils.

It is affordable exactly when

$$
x \cdot \texttt{cost1} + z \cdot \texttt{cost2}
\le \texttt{total}.
$$

The quantities may be zero, and money may remain unused. The task is to count all integer pairs satisfying this inequality.

**Enumerate one quantity and count the other arithmetically**

The solution loops over every affordable pen count:

`for x in range(total // cost1 + 1)`.

The maximum is `total // cost1`. Adding one to the range endpoint includes that maximum and also includes `x = 0`.

After buying `x` pens, the remaining money is

`total - x * cost1`.

The largest affordable pencil count is its floor division by `cost2`. If that maximum is `q`, then every pencil quantity from zero through `q` is valid, giving `q + 1` choices. The exact code calculates

`y = (total - x * cost1) // cost2 + 1`

and adds `y` to `ans`.

The local name `y` is the number of pencil-quantity choices for this pen count, not one selected pencil quantity.

**Why every counted pair is affordable**

For fixed `x`, the code counts only pencil quantities `z` satisfying

`0 <= z <= floor((total - x * cost1) / cost2)`.

Multiplying that upper-bound relation by positive `cost2` proves `z * cost2` does not exceed the remaining budget. Adding the already spent pen cost keeps the total purchase within `total`.

The pen loop itself contains only affordable `x` values, so the remaining budget is never negative.

**Why every affordable pair is counted**

Take any affordable pair `(x, z)`. Affordability implies `x * cost1 <= total`, so `x` lies in the loop range. For that exact iteration, rearranging the budget inequality gives

`z <= (total - x * cost1) // cost2`.

Therefore, `z` is one of the pencil quantities represented by the added `y` count. Every valid pair is included.

Different iterations have different pen quantities, and pencil quantities within one iteration are distinct. No pair is counted twice. This proves `ans` is exactly the number of ways.

**Trace the example**

With `total = 20`, `cost1 = 10`, and `cost2 = 5`:

- `x = 0` leaves twenty and permits pencil counts zero through four, five ways;
- `x = 1` leaves ten and permits zero through two, three ways;
- `x = 2` leaves zero and permits only zero, one way.

The sum is nine.

If both costs exceed the budget, the loop still includes `x = 0`. The remaining budget cannot buy a pencil, but the `+ 1` counts pencil quantity zero. Thus, buying nothing is always represented.

**Partially spending money is intentional**

Floor division counts quantities whose cost is at most the remaining budget. It does not require the remainder to be zero. For instance, six dollars remaining with a five-dollar pencil permits zero or one pencil, even though one dollar stays unused.

**Exact implementation versus the manifest wording**

The manifest summary says to enumerate quantities of the more expensive item, which would minimize the number of iterations. The stored Python solution does not compare or swap the costs; it always enumerates pens using `cost1`.

Its correctness is unaffected because either item can be the enumerated dimension. Its precise runtime depends on `cost1` rather than `max(cost1, cost2)`. An optimized variant could swap costs first, but that is not part of this exact solution.

**Integer safety and input behavior**

All costs are positive, so floor divisions are defined and loop bounds are finite. Python integers safely hold the answer, which can be large when both costs are small. Inputs are scalars and cannot be mutated.

## Complexity detail

The loop executes `floor(total / cost1) + 1` times. Each iteration performs constant-time arithmetic under the standard bounded-integer model. Exact time complexity is

`O(total / cost1)`.

If the costs were swapped so the enumerated one were larger, the bound would be `O(total / max(cost1, cost2))` as stated in the manifest, but this stored code does not perform that swap.

The method stores only `ans`, `x`, and `y`, using `O(1)` auxiliary space.

## Alternatives and edge cases

- **Enumerate the more expensive item:** Swap `cost1` and `cost2` when needed before looping. This preserves the count and can reduce iterations, matching the manifest summary.
- **Nested loops over both quantities:** It explicitly visits every pair but can take quadratic pseudo-polynomial time; arithmetic counting removes the inner loop.
- **Dynamic programming by budget:** Coin-change DP uses `O(total)` space and is unnecessary with only two unlimited item types and an at-most budget.
- **Require exact spending:** That would count solutions to equality rather than the stated inequality and would incorrectly discard plans with leftover money.
- **Buy nothing:** `(0, 0)` is always one valid way.
- **Neither item affordable:** The result is exactly one.
- **Only pens affordable:** Every affordable pen quantity pairs with zero pencils.
- **Only pencils affordable:** The single `x = 0` iteration counts all pencil quantities.
- **Equal costs:** Different pen/pencil quantity pairs remain distinct even if their total costs match.
- **Remaining money below `cost2`:** Floor division is zero and the `+ 1` counts only zero pencils.
- **Cost exactly divides remaining money:** The maximum pencil quantity is included.
- **Positive-cost guarantee:** It prevents division by zero and infinite quantities.
