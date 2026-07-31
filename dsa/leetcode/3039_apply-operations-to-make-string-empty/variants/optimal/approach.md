## General

**How many operations a character survives.** If a letter occurs $f$ times, each operation removes its earliest remaining occurrence. It therefore appears in the string immediately before operations $1$ through $f$, and disappears during operation $f$. The entire process lasts as many operations as the largest original frequency, say $F$.

Consequently, a letter is present immediately before the final operation exactly when its frequency is $F$. A less frequent letter has already disappeared, while every most-frequent letter has exactly one occurrence left.

**Which occurrence remains.** Deletions always remove a letter's occurrences from left to right. The sole surviving occurrence of a most-frequent letter is therefore its last occurrence in the original string. Because deleting characters never reorders the survivors, the answer lists those last occurrences in their original left-to-right order.

Use one pass to record the frequency and final index of every letter. After finding the maximum frequency, scan `s` once more. Append a character precisely when its frequency equals that maximum and the current index is its recorded final index. The preceding observations show that this condition selects every character present before the last operation, exactly once and in the required order.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. The two scans take $O(n)$ time. The frequency and last-index arrays each have 26 entries, so their auxiliary space is $O(1)$ with respect to $n$. The returned string is output space.

## Alternatives and edge cases

- **Literal repeated deletion:** Simulating every operation is straightforward, but a string containing one repeated letter makes it rescan and rebuild successively shorter strings, requiring $O(n^2)$ time.
- **Count, collect, and sort:** A frequency map plus sorting the most-frequent letters by their last indices is correct in $O(n + \sigma\log\sigma)$ time, where $\sigma \le 26$, but the second scan avoids the sort.
- **Backward collection:** Scanning from right to left and taking the first seen occurrence of each most-frequent letter also works, provided the collected answer is reversed afterward.
- **All letters unique:** Every frequency is `1`, so the original string itself is the state before the first and final operation.
- **One distinct letter:** Regardless of its repetition count, only its final occurrence remains before the last operation, so the answer is that one letter.
- **Tied maximum frequencies:** The answer is ordered by the tied letters' last positions, not alphabetically or by their first appearances.
