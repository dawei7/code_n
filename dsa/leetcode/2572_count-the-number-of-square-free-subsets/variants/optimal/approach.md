## General

**Represent used primes with ten bits.** Every allowed value is at most $30$, so its prime factors come from the ten primes $2,3,5,7,11,13,17,19,23,29$. Assign one bit to each prime. A value divisible by a prime square can never participate and receives no mask; every other value receives the mask of its distinct prime factors.

**Compress equal values.** Let $U=30$ be the value-domain size and $P=10$ the number of relevant primes. Count the occurrences of every value before running the subset DP. For a valid value greater than `1`, a square-free subset can choose at most one occurrence because choosing two repeats all of that value's prime factors. If its frequency is $f$, adding that mask therefore has $f$ distinct index choices.

Maintain `dp[mask]` as the number of ways to select processed values whose product uses exactly the primes in `mask`, including the empty selection at mask zero. For each valid value mask, copy the current table to preserve choices that omit it. Whenever a state is disjoint from the value mask, add its count multiplied by the value's frequency to their union mask. Disjointness is exactly the condition that the combined product repeats no prime, so every transition is valid. Processing each value once also ensures every valid index subset is counted once.

The value `1` has no prime factors and any number of its occurrences may accompany any DP selection. If there are $c$ ones, multiply the total by $2^c$ for their independent index choices. Finally subtract one to remove the selection that chooses neither a non-one value nor a one.

## Complexity detail

Counting the $n$ inputs takes $O(n)$ time. At most $U$ frequency groups scan $2^P$ masks, so the total time is $O(n + U \cdot 2^P)$. The mask table and DP require $O(2^P)$ space because $U \le 30 \le 2^P$. Under this contract, $U=30$ and $P=10$.

## Alternatives and edge cases

- **Element-by-element bitmask DP:** Updating all $2^P$ states for every array position is correct but costs $O(n \cdot 2^P)$ time and repeats identical work for duplicate values.
- **Enumerating all index subsets:** Directly testing each product takes exponential time in $n$ and is infeasible for $n=1000$.
- **Values with square factors:** Numbers divisible by `4`, `9`, or `25` are excluded before DP because their individual product is already not square-free.
- **Repeated valid values:** Equal values greater than `1` cannot be selected together, but each occurrence is a distinct one-element choice, which is why transitions are multiplied by frequency.
- **The value one:** Any subset of the one-valued indices is compatible with every prime mask, including the subset containing only ones.
- **Empty selection:** The DP deliberately starts with one empty way; subtracting one after applying the choices for ones removes it from the requested non-empty count.
- **Modulo arithmetic:** Apply the modulus during every transition and use modular exponentiation for the $2^c$ choices contributed by ones.
