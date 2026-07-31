## General

**Keep indices tied to the original string**

The entries in `spaces` refer to positions in the unchanged input, so do not mutate `s` after each insertion. Instead, keep `previous`, the first original index not yet copied, and process the strictly increasing insertion indices in order.

For each `index`, append the untouched slice `s[previous:index]`, then append one space and set `previous = index`. After all requests, append `s[previous:]`. Joining the collected pieces produces the result in one final construction.

Each slice covers exactly the original characters between two consecutive insertion positions. No ranges overlap or are skipped, and the space following a slice is immediately before the requested original index. The final suffix accounts for every remaining character, proving that the joined result contains precisely the requested insertions.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$ and $m=\lvert\texttt{spaces}\rvert$. The disjoint slices contain $n$ characters in total, and each insertion index is processed once, so the time is $O(n+m)$. The returned string and collected pieces contain $n+m$ characters and use $O(n+m)$ space.

## Alternatives and edge cases

- **Character scan with an index pointer:** Walk through `s` and append a space whenever the character index equals the next entry of `spaces`. This has the same $O(n+m)$ bounds.
- **Search all insertion indices per character:** Testing each character against `spaces` from the beginning is correct but can require $O(nm)$ time.
- **Repeated string insertion:** Mutating or rebuilding the growing result after every requested position risks quadratic copying and requires compensating for shifted indices.
- An insertion at index $0$ creates a leading space.
- Adjacent indices place spaces before adjacent original characters; they do not create an empty original-character segment in the output beyond the requested separators.
- The last legal index is $n-1$, which inserts a space before the final character rather than after it.
- Strictly increasing indices guarantee that each requested position is processed exactly once.
