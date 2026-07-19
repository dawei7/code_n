## General
**A bulb is toggled once for each divisor of its position**

Bulb `k` changes state during exactly those rounds `i` for which `i` divides `k`. It begins off, so it finishes on precisely when the number of divisors of `k` is odd.

Divisors normally form distinct pairs: if `d` divides `k`, then it pairs with $k / d$. The only time both members of a pair are the same is when $d \cdot d = k$. Therefore non-square positions have an even number of divisors and finish off, while perfect-square positions have one unpaired square-root divisor and finish on.

**Count squares instead of simulating toggles**

The bulbs left on are exactly $1^2,2^2,3^2,\ldots$ not exceeding $n$. If $r^{2} \le n < (r + 1)^{2}$, there are exactly $r$ such bulbs, so the answer is $\lfloor \sqrt{n} \rfloor$.

For $n = 3$, only position one is square. For $n = 16$, positions `1`, `4`, `9`, and `16` remain on. An integer square-root operation computes the count directly and avoids floating-point rounding near a large square.

**The divisor parity argument covers every round**

Every toggle of bulb `k` corresponds one-to-one with a positive divisor of `k`, because round `i` toggles it if and only if $i | k$. Pairing divisors proves that parity is even for every nonsquare and odd for every square. Consequently the final on-set is exactly the set of square indices, and its cardinality is the integer square root of `n`.

## Complexity detail
Under the problem's bounded machine-integer model, integer square root is a direct constant-space numeric operation, giving $O(1)$ time and $O(1)$ space with respect to the number of bulbs. No bulb states or rounds are materialized.

## Alternatives and edge cases
- **Toggle an explicit bulb array:** takes at least linear space and roughly $O(n \log n)$ total toggles.
- **Test every position for being square:** uses constant space but takes $O(n)$ time.
- **Increment square roots until exceeding `n`:** is correct but takes $O(\sqrt{n})$ time.
- $n = 0$ has no bulbs and returns zero. Exact square boundaries increase the result by one; values immediately below the next square do not.
