## General
**Measure the tape without constructing it**

Scan the encoding forward while maintaining `decoded_length`. A letter adds one; a digit `d` multiplies the length by `d`. Stop at the first encoding position whose decoded prefix reaches or passes `k`, since later characters cannot affect the requested position.

**Undo the encoding from right to left**

Walk backward through that relevant prefix. When the current character is a digit `d`, the current tape consists of `d` identical copies of the previous tape. First execute `decoded_length //= d`, then map the one-based position into one copy with `k = (k - 1) % decoded_length + 1`.

When the current character is a letter, it was appended at position `decoded_length`. If `k == decoded_length`, that letter is the answer; otherwise, remove its contribution with `decoded_length -= 1` and continue.

The forward pass records the exact length produced by every relevant prefix. Each reverse step maps the requested position to the equivalent position before the last encoding operation. This preserves the identity of the target character until the responsible appended letter is reached, proving the returned character is correct.

## Complexity detail
The algorithm scans at most $q$ characters forward and the same prefix backward, so it takes $O(q)$ time. It stores only indices, lengths, and the target position, requiring $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Build the decoded tape:** Explicit expansion is simple but can require time and memory proportional to a decoded length near $2^{63}$.
- **Recursive expansion:** Recursively forming repeated prefixes has the same prohibitive output-size cost and may also add call-stack depth.
- **Store every prefix length:** A length array supports the reverse pass but uses $O(q)$ space; the stopping index and one running length are sufficient.
- **Position at a repetition boundary:** The one-based mapping `(k - 1) % decoded_length + 1` correctly maps the final position of a copy to the previous tape's final position.
- **No digits before the answer:** Reverse processing simply removes later letters until it reaches the requested appended character.
- **Repeated digits:** Each digit is undone separately, even when the conceptual tape is already extremely large.
- **Single distinct letter:** Every valid position returns that letter regardless of the repetition factors.
- **Wide length arithmetic:** Fixed-width implementations should use a 64-bit type for `decoded_length`, matching the stated decoded-length guarantee.
