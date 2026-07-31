## General

Because the matrix is binary, the sum of a row is exactly its number of ones. Scan rows from index zero upward, compute each row sum, and retain the index and count whenever the new count is strictly greater than the best count seen so far.

Using a strict comparison is what enforces the tie rule: a later row with an equal count does not replace the earlier winner. After processing row $i$, the stored pair therefore describes the maximum count among rows $0$ through $i$ and the smallest index attaining it. This remains true after the final row, so the pair is the required answer.

## Complexity detail

The scan visits all $mn$ matrix entries once, giving $O(mn)$ time. It stores only the winning row index, its count, and the current row count, so auxiliary space is $O(1)$. The returned two-element array is also constant size.

## Alternatives and edge cases

- **Sort rows by count:** Sorting decorated rows can recover the answer but costs $O(m \log m)$ additional comparison work and $O(m)$ storage after the unavoidable counting pass.
- **Pairwise row comparison:** Recomputing counts while comparing every row pair is correct but takes $O(m^2n)$ time.
- **Binary search:** It cannot count ones correctly because individual rows are not promised to be sorted.
- If every entry is zero, all rows tie with count zero and row zero must be returned.
- A single-row matrix always selects row zero.
- Updating only on a strictly larger count preserves the smallest index across any tie.
