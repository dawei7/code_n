## General

Represent each word by the differences between consecutive alphabet positions. Adding the same offset to every character of a word leaves this representation unchanged, which is why visibly different words can share a pattern.

Because there are at least three words and exactly one outlier, at least two of the first three difference vectors must be the common one. Compute those three vectors and choose the first if it matches either of the others; otherwise the second and third match, so the second is common.

Scan every word and compute its difference vector. The first vector unequal to the inferred common vector identifies the required word. The majority argument proves that the selected reference cannot be the unique pattern, and the problem guarantee ensures exactly one scan entry differs from it.

## Complexity detail

Let $p=\lvert\texttt{words}\rvert$ and let $m$ be the common word length. Building a difference vector costs $O(m)$, and at most $p+3$ vectors are built, so total time is $O(pm)$.

Only a constant number of length-$(m-1)$ tuples are retained at once, giving $O(m)$ auxiliary space.

## Alternatives and edge cases

- **Frequency map of vectors:** Counting every difference tuple and then selecting the frequency-one entry is also $O(pm)$ time but stores $O(pm)$ difference data in the worst case.
- **Compare every pair:** Determining which vector agrees with the most others is correct but takes $O(p^2m)$ time.
- **Normalize to the first character:** Subtracting the first letter's position from every later letter produces an equivalent signature with the same asymptotic costs.
- **Outlier among the first three:** Majority selection is specifically needed so the first word is not assumed to be common.
- **Two-letter words:** Each signature has one difference, and the same comparison logic applies.
- **Negative differences:** Descending letters produce negative entries and must not be converted to absolute distances.
- **Shifted words:** Words such as `"abc"` and `"bcd"` share a vector even though no characters match.
- **Equal-length guarantee:** Every signature has the same length, so tuple equality compares corresponding transitions directly.
