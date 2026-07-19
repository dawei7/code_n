## General
**Closest factors surround the square root.** For a fixed product $x$, write a factor pair as $a\le b$ with $ab=x$. As $a$ increases toward $sqrt{x}$, its partner $b=x/a$ decreases, so their difference becomes smaller. Consequently, the largest divisor no greater than $sqrt{x}$ produces that product's closest pair.

**Evaluate both permitted products.** For each of `num + 1` and `num + 2`, begin at $lfloor\sqrt{x}\rfloor$ and scan downward until finding a divisor. Pair it with the exact quotient. Compare the two resulting absolute differences and return the better pair.

The downward scan finds the largest possible lower factor for each product, which proves optimality within that product. Since the contract permits only those two products, selecting the better of their two optimal pairs proves global optimality.

## Complexity detail
Each downward search examines at most $O(sqrt{x})$ candidate divisors, and both products are at most $n$. The total running time is $O(sqrt{n})$. Only the current divisor, quotient, and best pair are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Enumerate every divisor:** Test all integers through each complete product and retain the closest factor pair. This is correct but takes $O(n)$ time.
- **Prime factorization:** Factor each candidate and combine prime powers to approach its square root. This adds complexity without improving the worst-case trial-division bound here.
- **Perfect square:** When either candidate is a square, its equal factors have difference zero and are globally optimal.
- **Prime candidate:** Its only positive pair is `[1, x]`; the other candidate may therefore win by a wide margin.
- **Smallest input:** Factor one is always legal, so both candidates always have at least one pair.
- **Output order:** Returning the smaller factor first is convenient but not required by the contract.
