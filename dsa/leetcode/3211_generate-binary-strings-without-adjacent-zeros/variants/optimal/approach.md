## General

**Build only valid prefixes**

Maintain the current prefix as a mutable path. Appending `"1"` is always legal. Appending `"0"` is legal only when the path is empty or its final character is `"1"`. This local rule prevents `"00"` at the moment it could first appear, so no invalid branch is explored further.

When the path reaches length $n$, join its characters and append that complete string to the result. Backtrack after each recursive call so sibling choices start from the same prefix.

**Why the search is exact**

Every emitted path has length $n$, uses only binary characters, and never appends zero after zero, so every output is valid.

Conversely, take any valid length-$n$ string. At each position its next character is either `"1"`, which the search always offers, or `"0"` following the start or a `"1"`, which the search also offers. Its characters therefore define one complete root-to-leaf path. Different strings diverge at their first different character, so no output is duplicated.

The number of leaves satisfies $V_n=V_{n-1}+V_{n-2}$: strings ending in `"1"` extend every valid length-$(n-1)$ string, while strings ending in `"0"` must end in `"10"` and extend every valid length-$(n-2)$ prefix.

## Complexity detail

There are $V_n$ returned strings, and materializing each length-$n$ string costs $O(n)$. Time complexity is $O(nV_n)$, which is output-optimal up to constant factors.

The recursion and mutable path use $O(n)$ auxiliary space. The required returned strings occupy $O(nV_n)$ output space, which is not counted in the manifest's auxiliary-space bound.

## Alternatives and edge cases

- **Generate all masks then filter:** Examining all $2^n$ binary strings is correct after rejecting those containing `"00"`, but it explores exponentially many invalid candidates.
- **Iterative breadth-first prefixes:** Applying the same append rules level by level is correct, but it stores an entire frontier rather than one depth-first path.
- **Bit-mask test:** The expression `mask & (mask << 1)` can detect adjacent one bits; using complemented fixed-width masks can analogously detect zeros, but careful width handling is required.
- **Length one:** Both `"0"` and `"1"` are valid because no adjacent pair exists.
- **Leading or trailing zero:** Either is legal; only consecutive zeros are forbidden.
- **Alternating zeros:** Strings such as `"01010"` remain valid because every zero is separated by a one.
- **Output order:** Choosing the `"1"` branch first or the `"0"` branch first changes only list order.
- **No duplicates:** Each result corresponds to one unique sequence of recursive choices.
