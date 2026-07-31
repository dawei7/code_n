## General

Each original array element generates a non-increasing reward chain if it is selected repeatedly:

$$
x,\ \left\lceil\frac{x}{3}\right\rceil,\ \left\lceil\frac{\lceil x/3\rceil}{3}\right\rceil,\ldots
$$

Selecting a reward exposes only the next value from that same chain. At any step, the currently exposed heads are exactly the mutable values in `nums`. Choosing the largest head is optimal: if a proposed solution chooses a smaller exposed reward before a larger one, swap the larger reward into that step. This cannot invalidate later choices from the smaller chain, and it exposes the larger chain's no-greater successor earlier. Repeating the exchange transforms an optimal sequence into one that always chooses the current maximum.

Maintain those exposed heads in a max-heap. For each of the `k` operations, remove the maximum, add it to the score, and insert `(value + 2) // 3`, the exact integer form of $\lceil value/3\rceil$. The heap then represents precisely the array state for the next choice.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. Building the heap takes $O(n)$ time. Each of the `k` operations performs one removal and one insertion in $O(\log n)$ time, for $O(n+k\log n)$ total time. The heap stores $n$ values and uses $O(n)$ space.

## Alternatives and edge cases

- **Linear maximum search:** Scanning all values to find the next maximum preserves the greedy choice but costs $O(kn)$ time.
- **Resort after every operation:** Reordering the full array each time costs up to $O(kn\log n)$ and repeats far more work than heap maintenance.
- **Floating-point ceiling:** Using floating-point division can lose precision in other numeric ranges; `(value + 2) // 3` is exact integer arithmetic.
- **Value one:** Its replacement is still `1`, so large `k` remains well-defined and contributes one per later operation.
- **Tied maxima:** Any tied maximum can be selected because equal exposed rewards produce the same immediate score and successor.
- **Large score:** The total can exceed 32-bit range, so fixed-width implementations need a 64-bit accumulator.
