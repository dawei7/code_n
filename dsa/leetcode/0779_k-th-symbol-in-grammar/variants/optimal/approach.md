## General
**Follow the implicit ancestry**

Each symbol produces a left child equal to itself and a right child equal to its complement. For the zero-based position $k - 1$, a zero bit in its binary representation selects a left child at that level, while a one bit selects a right child and flips the inherited symbol.

**Count flips instead of building rows**

Start with symbol `0`. Repeatedly inspect the lowest bit of $k - 1$: toggle the symbol when that bit is one, then shift the position right. The final symbol is the parity of the number of right-child choices, equivalently the parity of the set-bit count of $k - 1$.

The root symbol is zero, and every step along its unique descendant path either preserves or complements it exactly as the corresponding position bit indicates. Toggling once per right edge therefore reproduces every grammar expansion on that path, so the parity returned after all position bits are consumed is precisely the requested symbol.

## Complexity detail
The loop consumes one binary digit of $k - 1$ per iteration, taking $O(\log k)$ time. It stores only the current position and one bit of parity, for $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Built-in population count:** Return `(k - 1).bit_count() % 2`; this expresses the same parity rule directly.
- **Recursive parent lookup:** Move to parent position $\lceil k/2 \rceil$ and complement the result for an even $k$; this takes $O(n)$ time and recursion space.
- **Construct every row:** Applying the substitutions literally is correct but requires exponential time and space in `n`.
- **First position:** $k = 1$ has zero right-child choices, so its symbol is always zero.
- **Last position:** Its zero-based index consists entirely of ones, so the answer is the parity of $n - 1$.
- **Role of `n`:** Once `k` is guaranteed to lie in row `n`, the ancestry and answer are determined by $k - 1$; no row storage is needed.
