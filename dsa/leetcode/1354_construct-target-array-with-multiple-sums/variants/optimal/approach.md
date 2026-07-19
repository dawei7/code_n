## General
**Reverse the final operation.** In any noninitial reachable state, the value most recently replaced by the previous array sum is at least as large as every unchanged value. Thus the largest current element is the only candidate to reverse. Keep all values in a max-heap and track their total.

Pop `largest` and let `rest = total - largest`, the sum of all other values. If every value is already one, or if `rest == 1`, reversal can always reach the initial state. Otherwise, a valid previous value must be positive and smaller than `largest`.

**Compress repeated reversals with modulo.** One reverse operation would replace `largest` by `largest - rest`. While that same position remains largest, `rest` does not change, so many identical subtractions can be skipped at once: the earliest positive predecessor is `largest % rest`. Push that predecessor and update the total.

If `rest == 0`, `rest >= largest`, or the remainder is zero, no positive smaller predecessor exists and the target is impossible. Each accepted reversal recreates the unique prior state that could lead to the current one. Repeating until an all-one condition succeeds therefore recognizes exactly the constructible targets.

## Complexity detail
Building the heap takes $O(n)$ time. Each compressed reverse step performs one heap removal and insertion in $O(\log n)$ time. Modulo reduction shrinks the dominant magnitude in the Euclidean-algorithm manner, yielding at most a logarithmic number of reductions per value scale; the standard bound is $O(n \log n \log M)$ time. The heap stores $n$ values, so auxiliary space is $O(n)$.

## Alternatives and edge cases
- **Single reverse subtraction:** Replacing `largest` with `largest - rest` is correct but may require $\Theta(M)$ iterations when `rest` is small.
- **Forward search:** Branching over every index from the all-ones state creates an enormous state space and values grow rapidly.
- **One-element target:** No operation changes the sole value from one, so only `[1]` is reachable.
- **Remaining sum of one:** The largest value can always be reduced to one by repeated subtraction.
- **Zero remainder:** A previous value of zero is illegal, so this state cannot be reached.
- **Largest not greater than the rest:** It could not have been the sum produced by the preceding positive array.
