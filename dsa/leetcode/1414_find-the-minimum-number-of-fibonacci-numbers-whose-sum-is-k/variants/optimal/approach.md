## General
**Build the usable Fibonacci values.** Generate the increasing Fibonacci sequence up to the largest value not exceeding `k`. There are only $O(\log k)$ such values because Fibonacci numbers grow exponentially.

**Take the largest affordable term.** Traverse those values from largest to smallest. Whenever a value does not exceed the remaining sum, subtract it and increment the answer. Continue until the remainder is zero.

The Fibonacci recurrence gives the greedy choice its special structure. If a representation of a remainder omits its largest affordable Fibonacci number, the smaller chosen terms can be exchanged through identities induced by $F_i=F_{i-1}+F_{i-2}$ until that largest term appears without increasing the number of terms. Applying the same exchange to the new remainder yields the canonical nonconsecutive Fibonacci representation, which uses the fewest terms. Therefore each greedy subtraction is compatible with an optimal complete representation.

After choosing $F_i$, the remainder is smaller than $F_{i-1}$, so the scan never needs to choose the same value twice even though repetition is permitted by the contract.

## Complexity detail
The number of Fibonacci values at most `k` is $O(\log k)$. Generating and scanning them therefore takes $O(\log k)$ time, and the stored sequence uses $O(\log k)$ space.

## Alternatives and edge cases
- **Generate downward with two variables:** Fibonacci identities can recover preceding values and reduce auxiliary space to $O(1)$, but storing the short sequence is simpler.
- **Dynamic programming through every sum:** Coin-change DP up to `k` is correct but uses pseudo-polynomial time and space.
- **Search downward for a Fibonacci number:** Testing every integer below the remainder can take $O(k)$ time despite there being only logarithmically many useful values.
- **Exact Fibonacci input:** One greedy choice immediately finishes, so the answer is `1`.
- **Repeated values:** The duplicate initial `1` need only be stored once.
- **Large input:** Generate with integer addition; do not use floating-point logarithms to decide membership.
