## General
**Preserve the three states needed by the recurrence.** At the start of an iteration for index $i$, keep `first`, `second`, and `third` equal to $T_{i-3}$, $T_{i-2}$, and $T_{i-1}$. No earlier term can affect $T_i$ except through those three values, so storing the complete prefix is unnecessary.

**Advance the rolling window.** Handle `n = 0`, `n = 1`, and `n = 2` directly. For every later index, perform `first, second, third = second, third, first + second + third`. The right side is evaluated from the old state, producing the next Tribonacci value before the three positions shift together.

The initialization holds the required values $T_0,T_1,T_2$. If the rolling variables hold three consecutive terms before an update, the recurrence makes the new `third` exactly the following term while the other assignments retain the two needed predecessors. By induction, after processing index `n`, `third` equals $T_n$.

## Complexity detail
The loop performs one constant-time update for each index from `3` through `n`, so it takes $O(n)$ time. Only three rolling sequence values and a loop index are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Bottom-up array:** Store every term through $T_n$ and apply the same recurrence in $O(n)$ time, but this uses unnecessary $O(n)$ space.
- **Memoized recursion:** Cache each computed term for $O(n)$ time and $O(n)$ cache and call-stack space; it is more machinery than the rolling recurrence needs.
- **Naive recursion:** Expanding all three recursive branches repeats subproblems exponentially and is unsuitable even though the public index bound is small.
- **Base indices:** `n = 0`, `n = 1`, and `n = 2` must return their definitions without entering the recurrence loop.
- **Exact arithmetic:** No modulus is requested; return the full value, with the input guarantee keeping it within signed 32-bit range.
