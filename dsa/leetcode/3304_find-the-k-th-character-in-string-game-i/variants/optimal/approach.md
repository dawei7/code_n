## General

Each operation doubles the word. The first half is the previous word, while the second half is the previous word with every character shifted once. For a zero-based position $p=k-1$, descending through these halves adds one shift whenever $p$ lies in a second half.

Those second-half decisions are exactly the `1` bits in the binary representation of $p$. Therefore the character has been shifted `bit_count(k - 1)` times from `a`. Since $k\le500$, the count is at most eight and no alphabet wraparound is needed.

## Complexity detail

Inspecting the binary digits of `k - 1` takes $O(\log k)$ time. The calculation stores only the position and shift count, using $O(1)$ auxiliary space.

## Alternatives and edge cases

- **String simulation:** Repeatedly constructing doubled strings uses $O(k)$ time and space even though only one position is requested.
- **Recursive half selection:** It expresses the same binary decisions in $O(\log k)$ time but uses recursive stack space.
- **First position:** `k = 1` gives zero set bits and returns `a`.
- **Power-of-two boundary:** A zero-based position with one set bit lies in exactly one transformed half and returns `b`.
- **Maximum input:** `k = 500` remains within nine binary digits and safely below alphabet wraparound.
