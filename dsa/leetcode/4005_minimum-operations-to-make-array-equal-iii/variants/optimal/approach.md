## General

Fix a candidate common value $x>1$. An entry already equal to $x$ costs zero operations. Any other entry costs one operation exactly when it divides $x$ and can be multiplied to it, or when it is divisible by $x$ and can be divided to it. Every remaining value costs two operations: multiply it to the product with $x$, then divide by the original value.

An absent target costs at least one operation for every array entry. A common multiple of all entries is always reachable in exactly $n$ multiplications, so $n$ is a universal upper bound and no absent target can improve it. It is therefore sufficient to initialize the answer to $n$ and test distinct values already present in the array. The all-equal case is handled immediately, which also resolves an array containing only ones. A mixed array never needs target $1$: the strict inequality on a division factor prevents a value greater than one from being divided directly to one.

For a present target $x>1$, let $M_x$ be the number of array entries divisible by $x$, including entries equal to $x$, and let $D_x$ be the number of entries that divide $x$, again including equals. If $e_x$ entries equal $x$, then $M_x+D_x-2e_x$ non-equal entries cost one operation, while $n-M_x-D_x+e_x$ entries cost two. The total simplifies to

$$
2n-M_x-D_x.
$$

Count these quantities without comparing every pair of distinct values. Sieve all primes through $\sqrt V$, where $V$ is the maximum input value. Factor each distinct value and generate all of its positive divisors. Its frequency contributes to $M_d$ for every generated divisor $d$ that is also a present candidate. Summing the stored frequencies of those same generated divisors gives $D_x$ for the current value $x$. Evaluating the formula for each present target then yields the global minimum.

## Complexity detail

Let $U$ be the number of distinct values, $V=\max(\texttt{nums})$, and

$$
D=\sum_{v\text{ distinct}}\tau(v),
$$

where $\tau(v)$ is the number of positive divisors of $v$. Let $P=\sqrt V\log\log V$ denote the prime-sieve work. Trial division is bounded by $O(U\sqrt V)$, and generating and processing divisors costs $O(D)$, for total time $O(P+U\sqrt V+D)$. The sieve, frequency maps, score maps, and one value's divisor list use $O(\sqrt V+U)$ space because the divisor list is bounded by the sieve term over the stated value range.

## Alternatives and edge cases

- **Every candidate against every value:** Direct divisibility testing is simple and correct but takes $O(U^2)$ time in the worst case.
- **Choose the greatest common divisor:** The best target need not be the global GCD, and a target absent from the array cannot beat the universal $n$-operation upper bound.
- **Target one:** A value greater than one cannot be divided to one because that would require choosing `k == nums[i]`, which the contract forbids.
- **All entries equal:** Return zero before excluding target one; this covers singleton arrays and arrays consisting only of ones.
- **Duplicate values:** Frequencies, rather than distinct-value counts, must contribute to both divisibility totals.
- **Absent common multiple:** It supplies the $n$ upper bound but never needs to be constructed or factorized.
- **Large prime values:** Prime trial division stops once the tested prime squared exceeds the remaining factor.
