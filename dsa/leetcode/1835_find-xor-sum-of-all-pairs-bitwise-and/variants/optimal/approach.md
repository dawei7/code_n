## General
**Distribute AND over XOR**

For any values $x$, $y$, and $z$, bitwise operations satisfy

$$
(x \mathbin{\&} z) \mathbin{\oplus} (y \mathbin{\&} z)
= (x \mathbin{\oplus} y) \mathbin{\&} z.
$$

This can be checked independently at each bit: the AND results contribute a 1 to the XOR exactly when $z$ has that bit and an odd number of the other operands have it.

**Collapse one dimension at a time**

Fix one value $b$ from `arr2`. XORing `a & b` over every $a$ in `arr1` distributes to

$$
\left(\bigoplus_{a \in \texttt{arr1}} a\right) \mathbin{\&} b.
$$

XOR these collapsed values over all $b$. Applying the same identity again yields

$$
\left(\bigoplus_{a \in \texttt{arr1}} a\right)
\mathbin{\&}
\left(\bigoplus_{b \in \texttt{arr2}} b\right).
$$

Thus only the XOR aggregate of each input array is needed. Compute both in separate scans and return their bitwise AND.

**Why multiplicities remain correct**

XOR records the parity of set-bit occurrences. A value repeated an even number of times cancels, while an odd repetition contributes once. Each aggregate therefore retains exactly the parity information that every pair contributes at every bit, so the algebraic collapse does not discard any required multiplicity.

## Complexity detail
Scanning the $p$ values of `arr1` and the $q$ values of `arr2` takes $O(p+q)$ time. The two XOR accumulators use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate every pair:** It directly follows the definition but evaluates $pq$ AND operations and takes $O(pq)$ time.
- **Count set bits per position:** Parity counts can derive the same result in $O((p+q)B)$ for a fixed bit width $B$, but aggregate XOR already performs those parity updates natively.
- **Materialize pair results:** Besides quadratic time, storing the Cartesian product requires $O(pq)$ space and is unnecessary.
- **Single-element arrays:** The result is simply the AND of the two elements.
- **Zeros:** A zero XOR aggregate makes the final result zero.
- **Duplicate values:** Even multiplicities cancel within an array's XOR aggregate.
- **Equal arrays:** Do not pair matching indices only; every cross-array index pair belongs to the definition.
- **Maximum values:** Ordinary integer bitwise operators handle values through $10^9$ without special cases.
- **Zero pair results:** XORing zero has no effect, but those pairs are still represented by the identity.
