## General

**Reduce a collection to its count**

If a collection contains $c$ numbers ending in `k`, its sum has the same units
digit as $c\cdot k$. The smallest possible sum for that count is $c\cdot k$
when `k` is positive. Any additional amount can be distributed in multiples of
10 without changing a summand's units digit. For `k = 0`, every positive
summand is at least 10, and the same residue test plus the source bound still
rejects impossible small totals.

Thus a positive count $c$ is feasible exactly when `c * k <= num` and
`(c * k) % 10 == num % 10`.

**Check one complete residue cycle**

The units digit of $c\cdot k$ repeats with period at most 10. Test counts from
1 through 10 and return the first feasible one. If none works, later counts
repeat an already rejected residue and are larger, so they cannot become
feasible. Handle `num = 0` first with the empty collection.

Testing counts in increasing order makes the first feasible count minimal.
The residue and lower-bound conditions construct a valid sum, while their
failure across a complete decimal cycle proves that no later count can work.

## Complexity detail

At most ten candidate counts are examined, independent of `num`, so time and
auxiliary space are both $O(1)$.

## Alternatives and edge cases

- **Unbounded-knapsack dynamic programming:** Computing the minimum count for every total through `num` is correct but unnecessary for a decimal residue condition.
- **Enumerate summand values:** Trying every positive value ending in `k` obscures that extra tens can be moved between summands freely.
- **Zero target:** Return zero before requiring any positive summand.
- **Zero units digit:** Positive numbers ending in zero start at 10; `num = 0` is the only case using no values.
- **Repeated values:** Multiple instances of the same integer are explicitly allowed.
- **Lower bound:** Matching the target units digit is insufficient when `count * k > num`.
- **Complete cycle:** Ten tested counts cover every possible decimal residue, including when `k` and 10 share a divisor.
- **Impossible target:** Return `-1`, not zero, for a positive target with no feasible count.
