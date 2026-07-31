## General

**Track lengths instead of characters.** Scan `s` once and store the conceptual result length after every prefix. A letter increases the length by one, a successful `*` decreases it by one, `#` doubles it, and `%` leaves it unchanged. If `k` is at least the final stored length, return `'.'` immediately. An all-letter input has no index transformation, so the app adapter may answer it directly.

**Invert each operation around the requested index.** Walk `s` backward while maintaining the index of the same logical character in the preceding prefix.

- For `#`, the two halves are identical, so replace `k` by `k % previous_length`.
- For `%`, reversal maps index `k` to `previous_length - 1 - k`.
- For `*`, every surviving index is unchanged because only the previous last character was removed.
- For a letter, the appended character occupied index `previous_length`. If the tracked index equals that value, this letter is the answer; otherwise the index already belonged to the preceding prefix.

The forward pass records the exact length transition for every operation. Each backward rule is the inverse mapping from a surviving position after that operation to its unique source position before it. Therefore the maintained index always identifies the requested final character in the current prefix. The first appended letter whose new position matches it is precisely the character that created that position.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. The algorithm performs one forward and at most one backward pass, taking $O(n)$ time. The prefix-length array contains $n+1$ integers and uses $O(n)$ space. It never allocates the conceptual result, whose length may reach $10^{15}$.

The benchmark uses a one-letter result followed by many reversals. The stored-length method remains linear. A calibrated correct alternative recomputes the entire preceding prefix length at every backward step and therefore takes $O(n^2)$ time.

## Alternatives and edge cases

- **Materialize the result:** Repeated duplication can create up to $10^{15}$ characters, making direct construction impossible.
- **Recompute prefix lengths during the backward pass:** This avoids stored lengths but repeats work and can take $O(n^2)$ time.
- **Out-of-range `k`:** Compare against the final conceptual length before any backward modulo or reflection.
- **Deletion from empty:** The length remains zero; no character exists to trace through that prefix.
- **Duplication of empty:** The length remains zero. A valid tracked character must have been appended later, so backward tracing returns at that later letter before needing to fold through the empty duplicate.
- **Reversal:** Length is unchanged, but index `k` must be reflected around both ends of the prefix.
- **Second duplicated half:** Modulo maps it to the matching position in the first half.
- **Very large length:** Python integers safely store the conceptual lengths; fixed-width implementations need 64-bit arithmetic under the $10^{15}$ guarantee.
