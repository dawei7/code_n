## General

**Recognize the balanced-parentheses structure**

Treat `1` as an opening parenthesis and `0` as a closing parenthesis. Equal total counts mean the complete string is balanced, while the prefix rule means the balance never becomes negative.

This analogy reveals that a special string is built from primitive balanced blocks. A primitive block begins with `1`, ends at the first later position where its balance returns to zero, and contains another special string between those outer characters.

**Split at every return to balance zero**

The solution scans left to right with `cnt`, adding one for `1` and subtracting one for `0`. Variable `j` records the beginning of the current top-level block.

Whenever `cnt == 0` at index `i`, substring `s[j:i + 1]` is one complete consecutive special block. Because this is the first return for that block, its first and last characters are the outer `1` and `0`. Its interior is `s[j + 1:i]` and is itself special.

After recording the block, `j` moves to `i + 1` so scanning can identify the next top-level block.

**Optimize the interior recursively**

Swaps may also occur inside a primitive block. Removing its required outer `1` and `0` leaves an independent special string, so the method recursively computes the lexicographically largest form of that interior.

It then rebuilds the primitive block as

`"1" + optimized_interior + "0"`.

The empty interior is valid. The recursive base case returns the empty string unchanged, so the smallest primitive block `"10"` is reconstructed correctly.

**Sort top-level blocks in descending order**

Every top-level block is a nonempty special string, and consecutive special substrings may be swapped. Repeated adjacent swaps can therefore arrange the top-level blocks in any order.

For concatenated strings, lexicographic maximum is obtained by sorting these special blocks in reverse lexicographic order. A block beginning with a longer or lexicographically stronger pattern of leading ones should occur first.

The same reasoning applies recursively at every nesting level: optimize each block’s interior, then order sibling blocks from largest to smallest.

**Trace `"11011000"`**

The entire string is one outer primitive block because balance does not return to zero until the end. Its interior is `"101100"`.

That interior splits into top-level blocks `"10"` and `"1100"`. Their recursively optimized forms are unchanged. Reverse sorting places `"1100"` before `"10"`, producing interior `"110010"`.

Wrapping it with the original outer characters gives `"11100100"`, the requested maximum.

**Why primitive boundaries are safe**

A return to zero separates two complete special strings. No valid prefix dependency crosses that boundary: both sides independently have equal counts and nonnegative relative balance. They may therefore be rearranged as units without breaking specialness.

Inside one primitive block, the outer `1` and `0` cannot be moved outside while preserving its nested role in this decomposition, but all legal optimization of its special interior is captured recursively.

The decomposition also preserves every character. Each top-level slice is rebuilt from its original outer pair plus a rearrangement of its interior, and the final join merely changes sibling order. The returned string therefore has exactly the same number of zeroes and ones as the input.

**Why descending order is optimal**

Suppose two adjacent optimized blocks `A` and `B` appear as `AB` while `B > A` lexicographically. Swapping them gives `BA`, whose first differing position is better, so the complete string increases. Therefore no maximum can contain an increasing adjacent inversion.

Sorting removes every such inversion. Since adjacent special blocks are legally swappable, the sorted arrangement is reachable and is lexicographically maximal.


Induct on string length. The empty string is already optimal. For a nonempty special string, balance scanning uniquely decomposes it into top-level primitive blocks. By induction, each recursive call makes a block’s interior maximal.

Every legal top-level rearrangement is an ordering of these optimized blocks, and reverse sorting gives the greatest ordering. Conversely, all recursive transformations and sibling swaps are permitted special-substring operations. The returned string is therefore reachable, remains special, and is lexicographically largest.

## Complexity detail

Let `n` be the string length. Across recursive levels, scanning, slicing, sorting component strings, and joining can revisit characters. A conservative bound for the exact Python implementation is `O(n^2)` time.

Recursive substrings, component lists, and constructed strings can hold `O(n^2)` total character data over deeply nested calls. The recursion depth is `O(n)`, so the stated auxiliary bound is `O(n^2)`.

## Alternatives and edge cases

- **Try every legal swap:** The reachable-state space grows rapidly and repeats equivalent arrangements.

- **Sort individual characters:** This destroys the prefix-balance structure and may produce an unreachable string.

- **Sort before recursively optimizing:** Sibling comparison should use their best attainable forms; optimize interiors first.

- **Single block `"10"`:** Its interior is empty and it remains unchanged.

- **Several identical blocks:** Their relative order does not matter.

- **Deep nesting:** Recursion follows the natural primitive structure and eventually reaches empty interiors.

- **Top-level balance returns:** Every return to zero ends exactly one independently swappable special component.
