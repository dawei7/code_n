## General
Sort all values in non-increasing order. Starting from the largest, append values to the answer and maintain their selected sum. Stop as soon as the selected sum is strictly greater than the total sum minus the selected sum.

For any fixed length $k$, the $k$ largest values have at least as much total satisfaction as any other $k$-element selection. Therefore, if this prefix does not exceed the remaining sum, no length-$k$ selection can qualify. The first prefix that does qualify consequently has minimum length.

The same dominance also resolves the tie rule: among selections of that minimum length, the largest-value prefix has maximum possible sum. It is already in the required non-increasing order.

## Complexity detail
Sorting takes $O(n\log n)$ time and the prefix scan takes $O(n)$. The sorted copy and returned subsequence use $O(n)$ space in the worst case.

## Alternatives and edge cases
- **Repeated maximum extraction:** Find and remove the maximum one element at a time. It produces the same order but costs $O(n^2)$ time.
- **Subset enumeration:** Testing combinations can establish minimality directly but takes exponential time.
- **Strict inequality:** Stop only when the selected sum is greater than the remainder; equality is insufficient.
- **Single element:** The only value must be returned.
- **Equal values:** More than half of the elements are necessary, and any occurrences yield the same output values.
- **Tie by length:** The required maximum-sum tie break is achieved by taking the largest values.
