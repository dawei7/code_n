## General

A number is magical when it is divisible by `a` or by `b`. Listing magical numbers one by one would be far too slow when `n` can be $10^9$. Instead, the solution asks a monotonic counting question:

> How many magical numbers are less than or equal to a candidate value $x$?

As $x$ increases, this count never decreases. Binary search can therefore find the smallest $x$ whose count is at least $n$. That smallest boundary is exactly the $n$-th magical number.

**Count with inclusion-exclusion.** There are $\lfloor x/a\rfloor$ positive multiples of $a$ up to $x$ and $\lfloor x/b\rfloor$ positive multiples of $b$ up to $x$. Numbers divisible by both were counted twice. A number is divisible by both exactly when it is a multiple of

$$
c=\operatorname{lcm}(a,b).
$$

Subtracting their count once gives

$$
\operatorname{count}(x)
=
\left\lfloor\frac{x}{a}\right\rfloor
+
\left\lfloor\frac{x}{b}\right\rfloor
-
\left\lfloor\frac{x}{c}\right\rfloor.
$$

The exact solution computes `c = lcm(a, b)` and uses this formula as the `key` for `bisect_left`.

For $a=2$, $b=3$, and $x=6$, the separate counts are three multiples of 2 and two multiples of 3. The number 6 belongs to both lists, so subtracting the one multiple of 6 gives $3+2-1=4$ distinct magical numbers: 2, 3, 4, and 6.

**Why lower-bound search returns the requested ordinal.** Suppose $X$ is the $n$-th magical number. Fewer than $n$ magical numbers are at most $X-1$, so `count(X - 1) < n`. At least $n$ magical numbers are at most $X$, so `count(X) >= n`. Therefore $X$ is precisely the first integer where the count reaches the target $n$.

The code calls

```text
bisect_left(range(r), x=n, key=count)
```

Conceptually, `bisect_left` searches the nondecreasing sequence `count(0), count(1), ..., count(r - 1)` for the first entry not less than `n`. Its returned index is also the candidate integer itself because `range(r)` contains values equal to their indices.

Unlike the boolean search in some binary-search solutions, the search target here is the integer `n`. Python applies `key` to range elements, then compares the resulting counts with `n`. It does not apply `key` to `n`.

**Why the upper range is large enough.** The solution sets `r = (a + b) * n`. A much tighter upper bound would be $n\min(a,b)$, since every multiple of the smaller divisor is magical. The chosen bound is larger because

$$
n\min(a,b) < n(a+b).
$$

Thus the true answer is strictly below `r` and is present in `range(r)`. The looser bound changes only a constant amount inside the logarithm and keeps the correctness proof simple.

The lower end includes zero. `count(0) = 0`, and $n\ge1$, so zero can never be selected. Including it makes range indices line up directly with numeric candidates.

**Apply the modulus only after finding the exact answer.** The ordering and divisibility structure must be evaluated on actual integers. Taking candidate values modulo $10^9+7$ during the search would destroy monotonicity and could merge distinct values. The solution first obtains the exact $n$-th magical number and then returns it modulo `mod`.

**Why the count predicate is monotonic.** Increasing $x$ can only add new multiples of $a$ or $b$; it never removes earlier ones. Each floor-division count is nondecreasing, and the inclusion-exclusion expression equals the size of a growing union. Therefore there is a well-defined first candidate reaching count $n$.

## Complexity detail

The search range has size $r=n(a+b)$. Binary search evaluates the constant-time count formula $O(\log r)$ times. Computing the least common multiple is constant time under the standard fixed-width arithmetic model for these bounded inputs.

- **Time complexity:** $O(\log(n\min(a,b)))$ in the standard tighter-bound expression; the exact chosen bound gives $O(\log(n(a+b)))$, which is the same logarithmic scale under the stated bounds.
- **Space complexity:** $O(1)$. `range` is lazy, and only a fixed number of integers are stored.

Python's arbitrary-precision integers safely hold the upper bound and intermediate products. The final modulo is one constant-time operation under the problem's arithmetic model.

## Alternatives and edge cases

- **Generate and merge multiples:** Repeatedly choose the next multiple of `a` or `b`. This takes $O(n)$ time and is infeasible for $n$ near $10^9$.
- **Use a heap:** A heap can generate divisible numbers but still performs work proportional to the requested ordinal and must suppress duplicates.
- **Period-based mathematics:** Magical numbers repeat a pattern modulo the least common multiple. One can count a full period and locate the remainder, but binary search is shorter and already logarithmic.
- **Tighter upper bound:** Using `n * min(a, b)` reduces the numeric interval. The exact solution's `n * (a + b)` is still guaranteed and preserves the stated asymptotic bound up to logarithmic constants.
- **Forget inclusion-exclusion:** Adding `x // a` and `x // b` alone double-counts common multiples and can return an answer that is too small.
- **`a == b`:** Then `c == a`, and the formula becomes one copy of `x // a`. The answer is simply `n * a`.
- **One divisor divides the other:** Every multiple of the larger divisor is already counted among multiples of the smaller. Inclusion-exclusion removes the duplicate contribution correctly.
- **First magical number:** For `n = 1`, the lower boundary is `min(a, b)`.
- **Common multiple at the boundary:** The subtraction by `x // c` ensures that a value divisible by both advances the union count by one, not two.
- **Modulo timing:** Apply modulo only to the final exact ordinal value, never to the search coordinate or count.
- **Zero in the range:** It has count zero and cannot satisfy positive `n`, so it is a harmless lower sentinel.
- **Large result:** The broad range and Python integer arithmetic avoid overflow; the returned value is reduced as required.
