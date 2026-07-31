## General

**The resolved prefix behaves like a stack**

Process the original values from left to right. The stack stores the final form of the prefix seen so far: it contains no adjacent equal values, and it is exactly what literal leftmost merging would leave before the next untouched input value.

Treat the next input as a current value. If it differs from the stack top, no merge crosses the boundary between the resolved prefix and this value, so append it. If the values are equal, remove the top and double the current value. That merge can expose another equal stack top, so repeat the comparison until the current value differs or the stack becomes empty, then append it.

**Why cascading at the boundary preserves leftmost order**

Before the current value arrives, the stack prefix has already exhausted every merge wholly inside that prefix. Therefore any newly available leftmost merge must be the pair formed by the stack top and the current value. After merging that pair, all earlier stack positions are still resolved; the only possible new merge is again at the same boundary. The loop performs exactly this forced cascade before any later input is considered.

By induction over the processed input, the stack after each iteration is precisely the result of literal leftmost merging on that prefix. Once all values have been processed, no untouched suffix remains and the stack contains no equal neighbors, so it is the required final array.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Each original value is appended once. Every successful loop iteration removes one previously appended stack value, so at most $N-1$ removals occur across the complete run. The total time is therefore $O(N)$, even when one input triggers a long cascade. The returned stack can contain $N$ values, giving $O(N)$ space.

The benchmark defines size as $N$ and uses power-of-two runs of the maximum legal input value. Every tier collapses to one sum and exercises repeated cascades. The accepted stack and an independent run-stack formulation scale linearly, while literal repeated scanning and array reconstruction performs quadratic total work.

## Alternatives and edge cases

- **Literal repeated scanning:** Find the first equal pair, rebuild the array, and restart. This directly mirrors the statement but may shift or copy a linear number of values for each of $O(N)$ merges, producing $O(N^2)$ time.
- **Linked list plus eligible-position tracking:** Neighbor links can support local removals efficiently, but maintaining the globally leftmost eligible pair requires additional ordered bookkeeping and is more complex than the stack.
- **Single element:** No adjacent pair exists, so the sole value is returned unchanged.
- **No equal neighbors:** Every value is appended once and the output equals the input.
- **Cascading merge:** In `[2,1,1]`, merging the `1` values creates a `2` beside the existing `2`, so both merges are required and the result is `[4]`.
- **Simultaneous eligible pairs:** In `[1,1,2,2]`, the left pair must merge first; the correct final array is `[4,2]`, not the result of choosing the right pair first.
- **Output magnitude:** Although each input is at most $10^5$, their sum can reach $10^{10}$, so fixed-width implementations need 64-bit result values.

