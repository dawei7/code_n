## General

**Turn the inclusive range into two prefix counts.** Let $F(x)$ be the number of positive good integers at most $x$. The requested answer is

$$
F(\texttt{r})-F(\texttt{l}-1).
$$

This transformation avoids visiting the enormous interval itself. It remains to compute one prefix count from the decimal digits of its bound.

**Describe exactly the information a prefix needs.** Process the bound from its most significant digit to its least significant digit. A memoized state records the current position, the previous real digit, whether the chosen prefix is still equal to the bound's prefix, and whether the number has started. The tight flag determines the largest digit allowed at the current position. Once the number has started, a candidate digit is legal exactly when its difference from the previous digit is at most `k`.

Leading zeroes require separate treatment: they only pad a shorter number to the bound's width and are not adjacent digits of that number. While the number has not started, choosing zero therefore keeps a sentinel previous value and imposes no adjacency check. Choosing the first nonzero digit starts the number. At the end, count the state only if some real digit was chosen, so the artificial all-zero representation does not contribute.

Every positive integer at most the bound has one unique padded digit sequence accepted by these rules, and every accepted sequence removes its padding to produce one such integer. The transition condition checks every adjacent pair exactly when its right-hand digit is chosen. Consequently, the completed states count precisely the good integers in the prefix, and subtracting the two prefix counts gives precisely the good integers in the inclusive range.

## Complexity detail

There are at most $D \cdot 11 \cdot 2 \cdot 2$ memoized states: $D$ positions, ten possible previous digits plus the sentinel, and two values for each Boolean flag. Each state tests at most ten digits. Because the decimal alphabet is fixed, the time complexity is $O(D)$ and the memo table plus recursion stack use $O(D)$ space.

## Alternatives and edge cases

- **Enumerate the interval:** Testing every integer directly takes $O((\texttt{r}-\texttt{l}+1)D)$ time, which is infeasible when the range spans nearly $10^{15}$ values.
- **Generate every good number:** A depth-first generator can prune illegal adjacent digits, but it still explores exponentially many valid prefixes when `k` is large; memoizing equivalent bound states is the essential compression.
- **Bottom-up digit DP:** Iterating over the same state dimensions avoids recursion and has the same complexity, but the top-down form expresses tight and leading-zero transitions more directly.
- **`k = 9`:** Every adjacent pair is allowed, so every integer in the inclusive range is good; the DP naturally reproduces `r - l + 1`.
- **`k = 0`:** Every adjacent pair must be equal. Shorter numbers still use leading padding zeroes that must not be compared with their first real digit.
- **Inclusive lower endpoint:** Subtract $F(\texttt{l}-1)$ rather than $F(\texttt{l})`; otherwise a good value equal to `l` would be lost.
- **Different digit widths:** The started flag lets one bound computation count all shorter positive integers without treating padding as part of their decimal representation.
