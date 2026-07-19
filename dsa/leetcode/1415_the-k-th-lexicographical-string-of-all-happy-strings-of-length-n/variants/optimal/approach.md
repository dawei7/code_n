## General
**Count the strings under a prefix.** There are three choices for the first character and two choices at every later position, so the total number is $3 \cdot 2^{n-1}$. If `k` exceeds this value, the requested string does not exist.

After a prefix has chosen its last character, each allowable next character begins a lexicographically contiguous block. If $r$ positions remain after that choice, every block contains exactly $2^r$ completions, because each later position has two choices different from its predecessor.

**Unrank one block at a time.** At each position, list the allowable characters in `a`, `b`, `c` order. The zero-based block containing rank `k` is `(k - 1) // block_size`. Append that block's character, subtract the number of strings in all earlier blocks from `k`, and continue.

Every valid completion belongs to exactly one next-character block, and the blocks occur in the same order as their first differing character. Selecting the block containing the current rank therefore preserves the requested global ordering. Once all positions are fixed, the sole remaining completion is exactly the original `k`-th string.

## Complexity detail
The algorithm makes at most three constant-time character checks at each of the $n$ positions, for $O(n)$ time. The constructed answer and its short choice lists use $O(n)$ space in total.

## Alternatives and edge cases
- **Backtracking enumeration:** Generate happy strings in lexical order and stop at the `k`-th. It is simple but spends $O(kn)$ time constructing earlier strings.
- **Generate and sort all strings:** This performs unnecessary exponential generation and sorting.
- **Length one:** The only results are `"a"`, `"b"`, and `"c"`.
- **Rank out of range:** Compare with $3 \cdot 2^{n-1}$ before indexing a block.
- **One-indexed rank:** Subtract one before integer division to avoid selecting the following block at an exact boundary.
- **Adjacent characters:** Remove the previously chosen character before determining the next block order.
