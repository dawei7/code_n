## General

**Retain only factors shared with `k`**

For a value $x$, factors not present in $k$ cannot affect whether a product is
divisible by $k$. Replace $x$ by $g_x=\gcd(x,k)$. For any two values $x$ and
$y$,

$$
k\mid xy \quad\Longleftrightarrow\quad k\mid g_xg_y.
$$

The forward direction holds because every prime-power requirement of $k$
supplied by $x$ or $y$ also appears in the corresponding gcd. The reverse
direction follows because each gcd divides its original value.

**Count compatible earlier classes**

Scan `nums` from left to right and count how many prior values produced each
gcd class. For the current class $g$, add the counts of all earlier classes
$h$ satisfying $k\mid gh$, then record $g$.

Every added occurrence belongs to an earlier index, and the gcd equivalence
proves that its product with the current value is divisible by `k`. Conversely,
every valid pair is encountered when its later endpoint is processed, and its
earlier gcd class passes the compatibility test. Thus every valid pair is
counted exactly once.

## Complexity detail

Every gcd class is a divisor of $k$, and $k$ has $O(\sqrt{k})$ divisors.
Scanning the present classes for each of $n$ values therefore takes
$O(n\sqrt{k})$ time. The counter stores at most $O(\sqrt{k})$ divisor classes.

## Alternatives and edge cases

- **Enumerate all pairs:** Test every product directly. This is simple and
  correct but takes $O(n^2)$ time.
- **Factor every value:** Tracking prime exponents can also determine
  compatibility, but gcd classes provide a smaller and more direct state.
- When `k = 1`, every index pair qualifies and the answer is
  $\binom{n}{2}$.
- A value divisible by `k` pairs successfully with every other positive
  value.
- Neither value needs to be divisible by `k`; their factors can complement
  each other, as with `2` and `3` when `k = 6`.
- Duplicate values at different indices form distinct pairs.
- The answer may exceed 32-bit range for a large array.
