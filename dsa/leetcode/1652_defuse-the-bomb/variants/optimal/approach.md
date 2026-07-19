## General
**Choose the first directed window.** Allocate the output before doing any sums so the original `code` remains unchanged. For positive $k$, the window for position 0 spans logical indices 1 through $k$. For negative $k$, it spans indices $n+k$ through $n-1$, which are exactly the previous $\lvert k\rvert$ circular positions. If $k=0$, the initialized zero output is already complete.

**Slide without recomputing.** Sum the first window once. After storing it for the current output position, remove the value at the window's left boundary, advance both boundaries, and add the new right-boundary value. Apply modulo $n$ only when indexing `code`; letting the logical boundaries increase makes the same update work across every wraparound.

**Why direction and simultaneity are preserved.** The initial boundaries select precisely the required side of position 0. Advancing both boundaries by one rotates that same relative block to the next position, so induction gives the correct directed neighbors for every index. Because every sum reads only the untouched input array and writes into a separate result, all replacements have simultaneous semantics.

## Complexity detail
The initial sum touches at most $n-1$ elements, and the window then advances through $n$ positions with constant work per position, for $O(n)$ total time. The returned list uses $O(n)$ space; beyond that output, the window requires $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Direct modular summation:** For every position, loop through all $\lvert k\rvert$ required neighbors. This is simple and correct but costs $O(n\lvert k\rvert)$, which becomes $O(n^2)$.
- **Doubled array plus prefix sums:** Prefix sums over `code + code` answer each directed interval in constant time after $O(n)$ preprocessing, but use another $O(n)$ array.
- **Mutate in place:** Replacing `code[i]` before later sums are computed violates the simultaneous-replacement rule.
- When $k=0$, return $n$ zeros without reading any neighbor.
- When $n=1$, the legal key can only be zero.
- With $\lvert k\rvert=n-1$, each result is the total array sum minus the element at that position, regardless of direction.
- Positive windows wrap from the end to the beginning; negative windows wrap from the beginning to the end.
- The legal key range prevents a window from including the current position or circling more than once.
