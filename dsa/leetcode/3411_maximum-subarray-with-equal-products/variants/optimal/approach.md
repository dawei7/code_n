## General

Consider one prime $p$ and let $e_i$ be its exponent in the $i$th element of a candidate subarray. The exponent of $p$ in the three quantities is respectively

$$
\sum_i e_i,\qquad \min_i e_i,\qquad \max_i e_i.
$$

Product equivalence therefore requires $\sum_i e_i=\min_i e_i+\max_i e_i$ for every prime.

Every two-element array satisfies this identity because its two exponents are exactly their minimum and maximum. For a subarray of length at least three, suppose $p$ divides two elements. If another element is not divisible by $p$, then the minimum exponent is zero while the sum exceeds the maximum. If every element is divisible by $p$, the third positive exponent makes the sum exceed the minimum plus the maximum. Either way the identity fails. Conversely, when $p$ divides at most one element, the minimum is zero and the sum equals the maximum. Thus every subarray of length at least three is product equivalent exactly when no prime factor occurs in two different elements.

The only possible prime factors of values from 1 through 10 are 2, 3, 5, and 7. Encode the distinct prime factors of each value as a four-bit mask; `1` has mask zero. Maintain a sliding window and the union of its factor bits. Before adding a value, repeatedly remove elements from the left while its mask intersects the union. The maintained window then contains each prime in at most one element.

Because that invariant makes every active factor bit unique, removing the left element with XOR safely clears precisely its bits. Each left and right pointer advances at most $n$ times. The longest maintained window supplies every valid length of at least three, while initializing the answer to 2 covers the universal two-element case.

## Complexity detail

The right pointer visits each element once and the left pointer removes each element at most once. Factor lookup and four-bit operations are constant time, so the total time is $O(n)$. The lookup table, bit mask, and pointers use $O(1)$ space.

The benchmark defines `size` as $n$ and uses legal all-one arrays of lengths 10, 40, and 100, spanning 10x. The accepted sliding window is linear. A correct enumerator that incrementally computes product, GCD, and LCM for every subarray takes $O(n^2)$ time and must fail only the scaling verdict.

## Alternatives and edge cases

- **Enumerate every subarray:** Incremental product, GCD, and LCM updates are correct, but examining all endpoints costs $O(n^2)$ time.
- **Pairwise GCD checks:** Testing all element pairs inside each growing window repeats work and can reach $O(n^3)$ time.
- **Length two:** Any positive pair satisfies `product = gcd * lcm`, even when both values share every prime factor.
- **Value one:** It contributes no factor bits and may extend a valid window without restriction.
- **Composite values:** A value such as 6 claims both the 2 and 3 bits, so later multiples of either prime conflict with it.
- **Repeated conflict removal:** The left pointer may need to discard several values before every bit in the incoming mask is free.
- **Bounded value domain:** The four-bit representation is complete only because the contract limits values to at most 10.
