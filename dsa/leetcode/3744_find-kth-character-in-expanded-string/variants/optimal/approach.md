## General

Each source character represents one contiguous block in `t`. The character at zero-based position `p` within its word contributes a block of length `p + 1`; a separator contributes a block of length one and resets the next word's position.

Scan those blocks in source order while maintaining the conceptual expanded length reached so far. After adding the current block length, `k` belongs to that block exactly when it is smaller than the new cumulative length. Every character inside the block is identical, so the current source character is then the answer. The guarantee that `k` is valid ensures that some block will contain it.

This reasoning also explains why the expanded text need not be built: only block boundaries matter for locating one index.

## Complexity detail

At most all $n$ source characters are inspected once, giving $O(n)$ time. The scan stores only counters and the current character, so it uses $O(1)$ auxiliary space. A single word of length $n$ could expand to $n(n+1)/2$ characters, which is deliberately excluded from the storage bound.

## Alternatives and edge cases

- **Materialize `t`:** Repeating and joining every character is simple but can require $O(n^2)$ time and space for one long word.
- **Precompute word lengths:** Prefix lengths plus binary search can answer multiple queries efficiently, but one query needs only the direct scan and extra storage is unnecessary.
- **First expanded index:** `k = 0` always selects the first character of `s`.
- **Separator index:** A space occupies exactly one expanded position and resets the repetition count for the next word.
- **One-letter words:** Their only character is repeated once, even when many such words appear.
- **Large valid index:** Fixed-width languages need a 64-bit counter because `t.length` can be on the order of $n^2$.
