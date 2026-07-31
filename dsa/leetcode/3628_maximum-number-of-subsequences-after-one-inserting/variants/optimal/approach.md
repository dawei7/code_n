## General

**Count the subsequences already present.** Scan left to right. Maintain the number of seen `L` characters, the number of `LC` subsequences, and the number of complete `LCT` subsequences. A `C` extends every earlier L, while a `T` extends every earlier LC. In the same scan, count `CT` pairs because they determine the gain from inserting L.

**Reduce the inserted letter to three meaningful choices.** Any letter other than L, C, or T creates no new target subsequence. Inserting L before the string adds one subsequence for every existing CT pair. Inserting T after the string adds one for every existing LC pair. These endpoint positions are optimal for those letters because they maximize the available suffix or prefix.

For an inserted C at a boundary between characters, every L on its left can combine with every T on its right. Scan all boundaries while maintaining the left-L count and remaining-right-T count, and maximize their product. Adding the greatest of the L, C, and T gains to the original LCT count yields the optimum. Each new subsequence uses the inserted character exactly once, so the gain calculations neither omit nor double-count any new choice.

## Complexity detail

Let $n$ be the string length. The first scan computes existing L, C, LC, CT, and LCT counts; the second scan evaluates every possible C boundary. Both take $O(n)$ time. Only a fixed number of integer counters is stored, so auxiliary space is $O(1)$.

The benchmark uses $S=n$. The accepted counting method is $O(S)$, while a correct baseline that inserts each of L, C, and T at every position and recounts LCT subsequences is $O(S^2)$.

## Alternatives and edge cases

- **Try every insertion explicitly:** This is straightforward and correct, but rebuilding or rescanning the string at every position is quadratic.
- **Prefix and suffix arrays:** Arrays of L, LC, T, and CT counts also give $O(n)$ time, but constant-space counters are sufficient.
- **Irrelevant letters:** They preserve relative order but change none of the counters.
- **Insert no letter:** The best gain may be zero, so retaining the original count is allowed.
- **Insert L or T:** The beginning and end respectively dominate every interior position.
- **Insert C:** Its best position may be internal and is determined by the product of left Ls and right Ts.
- **Large result:** The number of length-three subsequences can exceed 32-bit range.

