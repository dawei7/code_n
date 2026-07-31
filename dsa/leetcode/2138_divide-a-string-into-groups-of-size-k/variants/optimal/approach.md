## General

**Consume the string in fixed-size slices**

Visit starting indices `0`, `k`, `2 * k`, and so on. Take the slice of at most
$k$ characters beginning at each index. Every slice except possibly the last
already has length $k$. If the last is short, append exactly
`k - len(group)` copies of `fill`, then add the completed group to the result.

The starting indices partition the original positions into consecutive,
nonoverlapping intervals, so every character appears once and order is
preserved. Padding occurs only after the last original character and supplies
precisely the missing positions. The returned groups therefore satisfy the
required construction.

## Complexity detail

Let $n$ be the length of `s`. Slicing, padding, and storing all output
characters take $O(n)$ time, with at most $k-1$ additional padding characters.
The required returned groups occupy $O(n)$ space.

## Alternatives and edge cases

- **Rebuild every growing group prefix:** Repeatedly copying characters already
  placed in the current group is correct but can take $O(n^2)$ time.
- **Pad the whole string first:** Computing the required suffix and then
  slicing is also $O(n)$ and valid, but creates an extra padded string.
- When $k=1$, each character forms its own group and `fill` is unused.
- If $k$ exceeds the string length, the result contains one padded group.
- Original occurrences equal to `fill` remain ordinary source characters;
  only newly appended copies are padding.
