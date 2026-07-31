## General

**Follow the replacement process to its fixed point**

For any current value, compute the sum of its prime factors with multiplicity and use that sum as the next value. A prime maps to itself. A composite value's prime-factor sum never exceeds the value, and it is strictly smaller unless the value is `4`, whose factorization `2 * 2` also sums to `4`. The sequence therefore cannot increase and must eventually reach a fixed point. Returning when the newly computed sum equals the current value gives the smallest value the process will visit.

**Factor only while a small divisor can still exist**

Start with candidate factor `2`. Whenever it divides the remaining value, add it to the sum and divide it out; repeating this step records multiplicity exactly. Move through larger candidates until `factor * factor > remaining`.

At that point the remaining value, if greater than `1`, must itself be prime. If it were composite, at least one of its factors would be no larger than its square root and would already have been removed. Add that final prime once. This constructs precisely the complete prime factorization's sum without scanning all integers up to the current value.

## Complexity detail

Let $n$ denote the original input. Factoring one current value by trial division takes $O(\sqrt{n})$ time as an upper bound. Every non-fixed replacement strictly decreases the value, and the sequence has at most $O(\log n)$ such replacements, so a conservative bound for the full simulation is $O(\sqrt{n}\log n)$. Only the current value, candidate factor, remainder, and sum are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Scan factors through the entire current value:** Repeatedly trying every candidate until the remainder becomes `1` is correct, but a prime input requires $O(n)$ candidate checks instead of stopping at its square root.
- **Precompute smallest prime factors:** A sieve can make repeated factorizations fast, but allocating an $O(n)$ table is unnecessary for one input and loses the constant-space advantage.
- **Prime input:** Its factor sum is the prime itself, so the first iteration detects the fixed point immediately.
- **The composite fixed point `4`:** Its factors are `2` and `2`, whose sum is again `4`; stopping on equality handles it without assuming every terminal value is prime.
- **Repeated prime factors:** Each division contributes the factor once, so a value such as `8` contributes `2 + 2 + 2`, not merely the distinct factor `2`.
