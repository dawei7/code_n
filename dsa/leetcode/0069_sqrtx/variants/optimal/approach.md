## General

**Turn square root into a boundary search**

The requested value is not necessarily an exact square root. It is the largest integer $a$ whose square does not exceed `x`:

$$
a^2 \le x < (a+1)^2.
$$

This definition exposes a monotone yes-or-no question for a candidate `mid`: is `mid` small enough that $\texttt{mid}^2 \le x$? If a candidate is small enough, every smaller non-negative integer is also small enough. If it is too large, every larger integer is too large. A monotone boundary is precisely what binary search can locate.

The search begins with `l = 0` and `r = x`. This is a deliberately broad interval, but it is always valid. The floor square root of a non-negative `x` cannot be negative and cannot exceed `x`. For `x` equal to zero or one, the interval already has equal endpoints or rapidly resolves without requiring a separate special case.

**Compare without squaring the candidate**

The natural test `mid * mid > x` is mathematically correct, and Python integers would safely hold the product. In a language with fixed-width integers, however, `mid * mid` can overflow before the comparison. An overflowed value could make a too-large candidate appear valid and destroy the search.

For positive `mid`, the relation

$$
\texttt{mid}^2 > x
$$

is equivalent to

$$
\texttt{mid} > \left\lfloor\frac{x}{\texttt{mid}}\right\rfloor.
$$

The source therefore uses `mid > x // mid`. It performs integer division and never creates the potentially large square. There is also no division-by-zero path. The loop runs only while `l < r`, and its upper-middle calculation produces a positive `mid` whenever a nontrivial interval starting at zero exists. When `x == 0`, `l == r` initially and the loop is skipped.

**Maintain an interval that still contains the answer**

The key invariant is that the true floor square root lies within the inclusive interval `[l, r]`. Initially this follows from $0 \le \lfloor\sqrt{x}\rfloor \le x$.

If `mid > x // mid`, then $\texttt{mid}^2>x$, so `mid` and all larger values are impossible. Assigning `r = mid - 1` discards only impossible candidates and keeps the answer inside the interval.

Otherwise, $\texttt{mid}^2 \le x$. The candidate is feasible, as are all smaller values. Because the answer means the largest feasible integer, `mid` is now a valid lower bound. Assigning `l = mid` preserves `mid` rather than discarding it: it may be the answer, and the search still needs to determine whether a larger feasible value exists.

**Why the midpoint is biased upward**

The expression `(l + r + 1) >> 1` is integer division of $l+r+1$ by two, so it chooses the upper middle. For a two-element interval such as `[2, 3]`, it chooses 3 rather than 2.

That bias is essential because the feasible branch assigns `l = mid`. With a lower midpoint, `[2, 3]` could choose 2, set `l` to the same value 2, and repeat forever. The upper midpoint guarantees `mid > l` whenever `l < r`; therefore the feasible branch strictly raises `l`. The infeasible branch strictly lowers `r`. Every iteration shrinks the interval.

**Trace a non-square input**

For `x = 8`, the interval starts as `[0, 8]`. The upper midpoint is 4, and `4 > 8 // 4`, so 4 is too large and `r` becomes 3. The next upper midpoint of `[0, 3]` is 2. Since `2 <= 8 // 2`, 2 is feasible and `l` becomes 2. The upper midpoint of `[2, 3]` is 3; `3 > 8 // 3`, so `r` becomes 2. The endpoints meet at 2, which is returned.

This trace also shows why the algorithm does not need to see an exact square. It seeks the last candidate for which the feasibility predicate is true, not merely a candidate satisfying equality.

**Why returning `l` is correct**

Termination occurs only when `l == r`. The invariant still says that the answer lies in `[l, r]`, but that interval now contains exactly one integer. That integer must be $\lfloor\sqrt{x}\rfloor$. The update rules also guarantee termination because the inclusive interval becomes strictly shorter on every iteration.

The solution uses no built-in power, exponent, or square-root operation. Right shift is used only to divide the non-negative midpoint sum by two, which is ordinary integer binary-search arithmetic.

## Complexity detail

The initial interval contains at most $x+1$ integers. Each comparison removes roughly half of the remaining interval, so the number of iterations is $O(\log x)$. Every iteration performs a constant number of integer arithmetic operations, comparisons, and assignments under the usual word-RAM model for the constrained 32-bit input. This matches the manifest's $O(\log x)$ time bound. For `x == 0`, the loop performs zero iterations, which is still within that bound.

Only `l`, `r`, and `mid` are stored. The search is iterative and creates no recursion stack or size-dependent collection, so auxiliary space is $O(1)$, also matching the manifest.

## Alternatives and edge cases

- **Square-product comparison:** Test `mid * mid <= x`. It is simple and safe with Python's arbitrary-precision integers, but may overflow in fixed-width languages unless the type is widened.
- **Tighter initial upper bound:** For `x >= 2`, search through `[1, x // 2]`. It slightly reduces the initial range but needs explicit handling for zero and one.
- **Newton iteration:** Repeatedly improve a numeric estimate using an average involving `x // estimate`. It converges quickly, but its integer termination condition is less immediately obvious to beginners.
- **Bit-by-bit construction:** Build the root from the most significant bit downward. It avoids multiplication overflow and has bounded steps, but is more specialized and harder to derive.
- **Floating-point square root:** Converting through logarithms or a floating square-root routine violates the stated restriction and can need correction near integer boundaries.
- **`x == 0`:** The initial endpoints are equal, so no division occurs and zero is returned.
- **`x == 1`:** The search recognizes one as feasible and returns one.
- **Perfect square:** Its exact root remains feasible and all larger candidates are eliminated, so the exact root survives.
- **Non-square:** The search returns the greatest feasible candidate rather than rounding to the nearest integer.
- **Maximum input:** Quotient comparison avoids an overflowing square and safely handles $2^{31}-1$.
- **Upper-middle requirement:** It is paired with `l = mid`; changing only one of those choices can cause a non-shrinking two-element interval.
