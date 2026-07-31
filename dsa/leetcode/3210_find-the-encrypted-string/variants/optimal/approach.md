## General

**Reduce the circular distance**

Moving by the string length returns to the same position, so offsets that differ by a multiple of $n$ are equivalent. Compute `offset = k % n`. The encrypted character at result index $i$ is then `s[(i + offset) % n]`.

**Recognize the rotation**

Those source indices appear in two contiguous ranges: `offset` through `n - 1`, followed by `0` through `offset - 1`. Therefore the complete result is the left rotation

`s[offset:] + s[:offset]`.

This uses every original position exactly once. For indices before $n-\textit{offset}$, the first slice supplies index $i+\textit{offset}$. Remaining indices wrap to the second slice and supply $(i+\textit{offset})\bmod n$. Hence every result character matches the stated circular replacement.

## Complexity detail

Creating the two slices and concatenating them copies $n$ characters, so time complexity is $O(n)$. The returned encrypted string requires $O(n)$ output space; beyond that output, only the offset is stored.

Languages with constant-time substring views may construct intermediate views differently, but producing the length-$n$ result still requires linear work.

## Alternatives and edge cases

- **Index every output character:** Joining `s[(i + k) % n]` for all indices is also $O(n)$ time, but rotation slices state the transformation more directly.
- **Walk `k` steps per position:** Simulating every circular step takes $O(nk)$ time and repeats unnecessary full cycles.
- **Alphabet shift:** Encryption uses later positions in `s`, not later letters of the alphabet.
- **Offset multiple of length:** When `k % n == 0`, the encrypted string equals `s`.
- **Offset larger than length:** Modulo removes all complete cycles before rotating.
- **Single character:** Every positive offset returns the same character.
- **Repeated characters:** Equal symbols may make different rotations look identical, but the positional rule remains unchanged.
- **Original values:** Replacements are simultaneous; a previously produced output character must not feed a later position.
