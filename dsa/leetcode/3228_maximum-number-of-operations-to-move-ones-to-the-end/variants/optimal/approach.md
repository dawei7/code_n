## General

**Count crossings of zero blocks.** A move carries one `1` across one maximal block of zeroes. For each zero block, every `1` originally to its left can cross that block at most once: after crossing, that character is on the block's right side and moves only farther right.

These crossings are simultaneously attainable by processing movable `1` characters from right to left as needed. Moving a rightmost eligible `1` across a block does not prevent any earlier `1` from crossing it later. Repeating this across successive blocks realizes one operation for each pair consisting of a zero block and a `1` to its left.

Scan the string from left to right while counting seen `1` characters. A zero block begins exactly at a `"10"` transition. At that boundary, add the number of seen ones; this is precisely the number of operations contributed by the whole block. Interior zeroes add nothing separately because one operation crosses the complete block.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. The scan examines each character once, taking $O(n)$ time. The ones counter and accumulated answer use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Recount every prefix at each zero block:** This computes the same sum but takes $O(n^2)$ time in strings with many alternating blocks.
- **Simulate string moves:** Repeated deletion and insertion can also be quadratic and obscures the invariant.
- Leading zeroes contribute no operations because no `1` precedes them.
- Trailing ones contribute no new zero block.
- A zero block of any positive length contributes only once per preceding `1`.
- The same `1` may contribute to several distinct zero blocks as it moves rightward.
- All-zero and all-one strings both have answer zero.
