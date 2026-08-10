## General

**Translate the balance condition into two arithmetic sums**

A candidate `x` is a pivot when the inclusive sum from 1 through `x` equals the inclusive sum from `x` through `n`. The pivot appears in both sums; it must not be removed from either side.

The sum of consecutive integers from 1 through `x` is

$$
\frac{x(x+1)}{2}.
$$

The sequence from `x` through `n` has $n-x+1$ terms. Its first and last terms are `x` and `n`, so the arithmetic-series formula gives

$$
\frac{(x+n)(n-x+1)}{2}.
$$

Equality between these fractions is equivalent to

$$
x(x+1)=(x+n)(n-x+1),
$$

because multiplying both sides by two preserves equality. The exact solution uses this denominator-free equation:

`(1+x)*x == (x+n)*(n-x+1)`.

Avoiding division means there is no floating-point rounding and no question about integer truncation.

**Check candidates in increasing order**

The `for` loop tries every integer `x` from 1 through `n`. These are exactly all allowed pivot values: a pivot cannot lie outside the sequence it divides.

For each candidate, the left product is twice the sum from 1 to `x` and the right product is twice the sum from `x` to `n`. If the products are equal, the original sums are equal, so the method immediately returns `x`.

If the loop ends, every allowed integer has failed the exact balance test. Returning `-1` is then correct.

For `n=8`, candidate `x=6` produces

$$
(1+6)\cdot6=42
$$

and

$$
(6+8)\cdot(8-6+1)=14\cdot3=42.
$$

Both products are twice 21, so 6 is returned.

**Why there can be at most one answer**

The balance equation can be simplified. The total sum from 1 through `n` is

$$
T=\frac{n(n+1)}{2}.
$$

The left and right sums together count every number once, except `x` is counted twice. If both side sums equal some value $S$, then $2S=T+x$. More directly, subtracting the prefix through `x-1` from the total and equating it to the prefix through `x` yields

$$
\frac{x(x+1)}{2}
=
\frac{n(n+1)}{2}-\frac{(x-1)x}{2}.
$$

After simplification,

$$
x^2=\frac{n(n+1)}{2}=T.
$$

For positive `x`, $x^2$ strictly increases as `x` increases. It can equal the fixed total $T$ for at most one integer. This validates the problem's uniqueness guarantee and explains why returning the first match is safe.

The exact code does not use this simplified perfect-square formula to skip the loop. It evaluates the equivalent arithmetic-series equality for each candidate. Documentation must follow that actual control flow even though the branch summary describes the mathematical shortcut.

**Endpoint behavior**

When `n=1`, the only candidate is `x=1`. Both products equal two, corresponding to the equality $1=1$, so one is returned.

For `x=1` with larger `n`, the left sum is one while the right includes the entire sequence and cannot match. For `x=n`, the left includes the entire sequence while the right contains only `n`. The loop nevertheless checks endpoints uniformly, which keeps the code simple and ensures the valid singleton case is covered.

**Why positive integers matter**

The monotonic uniqueness argument relies on candidates being positive. The contract supplies `n>=1` and the loop creates only positive candidates. Products are also small under `n<=1000`, although Python would support larger integers without overflow.

## Complexity detail

The loop may examine all `n` candidates, and each examination performs a constant number of arithmetic operations. The exact implementation therefore takes $O(n)$ time in the worst case. It may return earlier when a pivot exists, but worst-case analysis includes inputs with no pivot.

Only `x` and a fixed number of temporary arithmetic values are needed, so auxiliary space is $O(1)$.

The manifest describes an $O(1)$ perfect-square test, but that is not what the protected Optimal solution executes. Its loop makes the runtime linear. Under the given maximum of 1000, this is still easily fast enough.

## Alternatives and edge cases

- **Perfect-square test:** Compute $T=n(n+1)/2$, take its integer square root, and return the root only if its square is $T$. This follows the simplified identity and avoids scanning, but it is not the exact implementation explained above.
- **Binary search:** Search for an integer whose square equals $T$. It costs $O(\log n)$ time and constant space.
- **Running left and right sums:** Update prefix totals while scanning. This is also linear but carries more state than evaluating the closed formulas.
- **Nested summation:** Recomputing both ranges for every candidate costs $O(n^2)$ and is unnecessary.
- **`n=1`:** The pivot is one because the same single element belongs to both inclusive ranges.
- **No perfect-square triangular sum:** No integer pivot exists, so the loop returns `-1`.
- **Inclusive pivot:** `x` is counted on both sides; interpreting one range as exclusive changes the problem.
- **Integer arithmetic:** Cross-multiplication avoids floating-point comparison and division rounding.
- **First match:** At most one positive candidate can satisfy $x^2=T$.
- **Manifest mismatch:** Complexity should be reasoned from the loop in the actual solution, not inferred from its mathematical summary.
