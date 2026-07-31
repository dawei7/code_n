## General

For an index `i`, first form its ordinary decimal representation. Suppose that representation has `d` characters. Any substring equal to it must also have length `d`. Because the substring must end at `i`, its start is forced to be `i - d + 1`. Thus there is only one possible witness for each index; searching over all earlier starting positions is unnecessary.

Scan the indices from left to right. At each index, compare its representation with `s[i - d + 1 : i + 1]`. Append the index exactly when those strings are equal. Processing positions in their natural order also produces the required increasing output order without a later sort.

Whenever an index is appended, the tested slice is contiguous, ends at that index, and equals its decimal representation, so the index is good. Conversely, suppose an index is good. Its witnessing substring must have the same length as the representation and must end at the index; therefore it is precisely the unique slice tested by the scan. The comparison succeeds and the index is appended. The returned array consequently contains every good index and no other index.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$, and let $D$ be the greatest decimal width of an index in the string. Constructing and comparing the representation at index `i` costs at most $O(D)$. Across all indices, the running time is $O(ND)$.

The legal bound $N\le 10^5$ gives $D\le 5$, so the work grows linearly with the legal string length with a small fixed digit factor. The transient representation and slice use $O(D)$ auxiliary space; the returned array is not counted as auxiliary storage.

The benchmark defines size as $N$ and uses an all-zero string. Only index `0` is good, but the direct method still performs the required single candidate check at every position. A slower search that tries every possible substring start for every ending position performs $O(N^2)$ candidate visits on the same inputs.

## Alternatives and edge cases

- **`endswith` with an explicit endpoint:** `s.endswith(str(i), 0, i + 1)` expresses the same unique-candidate test without materializing the slice and has the same $O(ND)$ worst-case character work.
- **Enumerate all ending substrings:** Trying every start position can reproduce the definition directly, but it wastes $O(N^2)$ candidate visits because equality already determines the required length.
- **Rolling decimal window:** Maintaining the numeric value of the current digit-width suffix can remove repeated string conversion, but it adds boundary bookkeeping at powers of ten and is unnecessary for the live five-digit limit.
- **Index zero:** Zero is represented by the single character `"0"`; it is good exactly when `s[0]` is `'0'`.
- **Powers of ten:** At indices `10`, `100`, and later powers, the candidate width increases by one and the start position must move accordingly.
- **Leading zeros:** A substring such as `"01"` is not equal to the representation `"1"` or `"11"`; comparison is textual, not numeric.
- **Overlapping candidates:** Ending substrings for neighboring indices may overlap, and each must still be checked independently.
- **Empty answer:** If every forced ending slice differs from its index representation, return an empty array.
