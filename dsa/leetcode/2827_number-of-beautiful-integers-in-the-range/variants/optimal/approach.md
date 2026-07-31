## General

Counting each integer in the range would make the running time depend on `high - low + 1`, which can approach one billion. Instead, define $F(b)$ as the number of beautiful positive integers at most $b$. The requested inclusive-range answer is then $F(\texttt{high}) - F(\texttt{low} - 1)$.

Compute $F(b)$ with digit dynamic programming. Scan the decimal digits of $b$ from left to right and memoize five pieces of state:

- the current digit position;
- the prefix remainder modulo `k`;
- the number of chosen even digits minus the number of chosen odd digits;
- whether the prefix still equals the corresponding prefix of $b$; and
- whether a non-leading digit has started the represented positive integer.

For each permitted next digit, update the remainder as `(remainder * 10 + digit) % k`. A real even digit increases the balance by one, while a real odd digit decreases it by one. A zero chosen before the number starts is only padding for the fixed-width traversal: it must not affect the remainder or parity balance. Once the number has started, however, `0` is an ordinary even digit.

**Why the terminal state identifies exactly the beautiful integers**

Every positive integer at most $b$ has exactly one path through the digit choices after adding traversal-only leading zeros. The tight flag admits precisely those paths that do not exceed $b$. The modular transition maintains the represented prefix's remainder, and the balance is zero exactly when its even- and odd-digit counts agree. Requiring a started number, remainder zero, and balance zero at the final position therefore accepts every beautiful positive integer at most $b$ once and rejects every other path.

Subtracting the prefix counts removes every accepted integer below `low`, while retaining a qualifying lower or upper endpoint, so it gives the exact inclusive-range count.

## Complexity detail

Let $D$ be the number of decimal digits in `high`. There are $D$ positions, $k$ possible remainders, $O(D)$ possible parity balances, and two possibilities for each Boolean flag. Each state considers the ten decimal digits, a constant alphabet size. The time complexity is therefore $O(D^2 k)$, and memoized states plus recursion use $O(D^2 k)$ space.

The benchmark uses range width as its scaling variable. Digit dynamic programming depends on the endpoint digit count rather than enumerating that width, whereas the principal direct method inspects every integer in the range.

## Alternatives and edge cases

- **Enumerate the range:** Check divisibility and digit parity for every integer from `low` through `high`. This is straightforward and correct but takes $O((\texttt{high}-\texttt{low}+1)D)$ time.
- **Combinatorial counting by length:** Count digit patterns with balanced parity and then impose divisibility. The remainder couples digit positions, so this ultimately needs states equivalent to digit dynamic programming; the tight prefix is also necessary for arbitrary bounds.
- **Leading zeros:** Traversal padding before the first real digit is not part of the represented integer and must not change either balance or remainder.
- **Zero digits after the start:** The decimal digit `0` is even and increases the parity balance once the number has begun.
- **Odd digit lengths:** A number with an odd number of decimal digits cannot have equal even- and odd-digit counts, so such terminal paths cannot reach balance zero.
- **Positive-number requirement:** The all-padding path represents zero and is excluded by requiring that the number has started.
- **Inclusive endpoints:** Using $F(\texttt{high}) - F(\texttt{low}-1)$ includes either endpoint exactly when it is beautiful.
- **Smallest lower bound:** When `low` is `1`, the second prefix count is $F(0)=0$.
