## General

Each row is independent. For `[a, b, c, m]`, first compute
`inner = pow(a, b, 10)`, which is exactly $a^b\bmod 10$ without materializing
$a^b$. Then compute `pow(inner, c, m)` and compare that residue with `target`.
Append the row index on equality.

Binary modular exponentiation maintains the accumulated result and squared base
modulo the relevant modulus after every multiplication. Reducing intermediate
products is valid because congruent values remain congruent after
multiplication. Thus the two modular calls produce exactly the nested formula's
value while keeping all stored numbers bounded. Testing every row once includes
all and only good indices, and scanning in order returns one permitted ordering.

## Complexity detail

Let $V=\lvert\texttt{variables}\rvert$, let $B$ be the maximum `b` value, and
let $C$ be the maximum `c` value. Binary modular exponentiation takes
$O(\log B+\log C)$ time per row, for $O(V(\log B+\log C))$ total time. The
returned indices can contain all $V$ positions, so output space is $O(V)$;
auxiliary space excluding the result is $O(1)$.

## Alternatives and edge cases

- **Repeated modular multiplication:** Multiplying one exponent step at a time stays numerically bounded but takes $O(V(B+C))$ time.
- **Materialize full powers:** Computing `a ** b` and then the outer power is mathematically correct but creates unnecessarily large integers before reduction.
- **Modulus one:** Every integer is congruent to zero modulo one, so only `target = 0` can match such a row.
- **Intermediate zero:** A base ending in zero produces inner residue zero, which remains zero because `c` is positive.
- **Target outside a row's residue range:** A row cannot match when `target >= m`, except that different rows may have larger moduli.
- **Index order:** Any answer order is accepted; a left-to-right scan naturally returns increasing indices.
