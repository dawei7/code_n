## General

**Track the XOR difference.** Let $X$ be the XOR of all values. Flipping bit
$b$ in any one element toggles bit $b$ of $X$ and no other XOR bit. Therefore
the bits that must change are exactly the set bits of $X\oplus k$.

Initialize `difference` with `k` and XOR every value into it, producing
$X\oplus k$. Return its population count. Each differing bit needs at least
one operation, and one flip in any element fixes it, so this count is minimal.

## Complexity detail

The array is scanned once, giving $O(N)$ time. XOR accumulation and the final
bounded-width population count use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Per-bit parity counts:** This is equivalent but more verbose than reducing the XOR.
- **Recompute prefix XORs:** This obtains the same final XOR with $O(N^2)$ work.
- **Already equal:** A zero difference needs no operation.
- **Leading zero bit:** A target bit absent from every value still costs one flip.
- **Zeros and duplicates:** Zeros contribute nothing and equal values may cancel, but all rows remain part of the reduction.
