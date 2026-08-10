## General

**Think in powers of `x`**

Without parentheses, multiplication and division form terms before addition and subtraction combine them. Powers of `x` are cheap: `x` uses zero operators, `x * x` uses one, and `x^k` uses `k - 1` multiplications.

The recursion asks for the minimum operator count to express positive value `v`. It compares building upward from the largest power below `v` with overshooting to the smallest power above it and subtracting the excess.

**Base values from one**

When `v <= x`, there are two constructions.

First, create `v` copies of one using `x / x` and add them. Each copy needs one division, and joining `v` terms needs `v - 1` additions. Total is `2v - 1`.

Second, start with `x` and subtract `x - v` copies of one. Each removed one requires a division to form and a subtraction to attach, totaling `2(x - v)`.

The code returns the smaller. Expressing `x` costs zero, while expressing one costs one through `x / x`.

**Find neighboring powers**

For `v > x`, the code starts `k = 2` and increases it until `x^k >= v`.

Then `x^(k-1) < v` is the largest lower power and `x^k` is the smallest upper power. These are the natural anchors for a signed base-`x` representation.

**Build upward from the lower power**

Write `v = x^(k-1) + (v - x^(k-1))`.

The power needs `k - 2` multiplications, and attaching the remainder needs one addition. Anchor cost is `k - 1`, giving:

`k - 1 + dfs(v - x^(k-1))`.

The remainder is smaller than `v`, so this branch always progresses.

**Overshoot and subtract**

Alternatively, write `v = x^k - (x^k - v)`.

Power `x^k` needs `k - 1` multiplications, and subtraction adds one. The candidate is:

`k + dfs(x^k - v)`.

This can be much better when `v` lies just below the upper power. A difference of one is expressible cheaply as `x / x`.

**Why the overshoot guard exists**

The code considers overshoot only when `x^k - v < v`.

The recursive helper must move to a smaller positive target. If the excess were at least `v`, that branch would not reduce the problem and could create circular or unhelpful recursion.

When the guard fails, only the always-smaller lower remainder is used.

**Operator accounting**

The recursive result counts a complete expression for the remainder. The outer plus or minus is already included in `k - 1` for the lower route or `k` for the upper route.

No parentheses are required conceptually because multiplications inside powers and divisions forming one bind before addition and subtraction.

Unary negation is never used. A negative contribution appears only through a binary subtraction from a positive power.

**Example around a power**

For `x = 3` and target nineteen, neighboring powers are nine and twenty-seven. The lower route represents nineteen as nine plus ten. Recursive choices eventually discover two copies of nine plus one, corresponding to `3 * 3 + 3 * 3 + 3 / 3`.

The operator count is two multiplications, one addition between the nine terms, one division, and one more addition: five.

For an exact power such as `x = 100` and target `100^4`, upper gap is zero and only three multiplications are needed.

**Why the recurrence is correct**

At the highest relevant power scale, an optimal signed representation either starts from the lower power and adds the remaining positive amount or starts from the upper power and subtracts its excess.

The recurrence considers both whenever both reduce the target. The base case gives the cheapest construction at or below `x`. Memoized induction over decreasing targets yields the minimum count.

**Role of caching**

Different lower and upper choices can reach the same remainder. `@cache` solves each distinct `v` once.

## Complexity detail

Let `L = floor(log_x(target)) + 1` be the number of base-`x` positions.

The recurrence moves through neighboring power scales and has `O(L)` relevant memoized values in the standard analysis. Power searching over these scales gives `O(L)` high-level work for the bounded target domain, with integer arithmetic treated as constant.

The recursion stack and cache use `O(L)` space. The manifest states `O(1)`, but the exact Python code contains cache entries and recursive frames, so logarithmic space is the honest bound.

## Alternatives and edge cases

- **Base-`x` digit DP:** Process digits with carry and no-carry costs iteratively. It gives a formal `O(L)` solution with constant state.
- **Breadth-first search over values:** The state range is too large and branching is high.
- **Use only lower powers:** This misses cheap expressions immediately below an upper power.
- **Target equals `x`:** Zero operators are needed.
- **Target equals one:** `x / x` uses one operator.
- **Exact higher power:** Its multiplication count is returned.
- **Upper gap not smaller than target:** Overshoot is skipped to preserve decreasing recursion.
- **Rational division:** Forming one with `x / x` is valid.
- **No unary minus:** Every negative part is attached by binary subtraction.
- **Large target:** Power-scale recursion depends logarithmically on magnitude.
