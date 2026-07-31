## General

**Turn the pair condition into a per-day invariant.** Consider two selected 1-indexed days $a<b$. They may appear consecutively in a linear selection exactly when

$$
\texttt{prices[b]}-\texttt{prices[a]}=b-a.
$$

Rearranging gives

$$
\texttt{prices[b]}-b=\texttt{prices[a]}-a.
$$

Consequently, all indices of a linear selection share the same `price - index` key. The converse is also true: if several indices have that common key, every consecutive pair in their increasing index order satisfies the required equality. Each invariant group therefore describes one valid linear selection.

**Every positive member should be included.** All prices are positive. Within one invariant group, omitting an index can only reduce the score, while retaining it preserves linearity. Thus the best selection for a key contains every day with that key and has score equal to their price sum.

Scan the array once. For each zero-based `index`, add `price` to the hash-table total for `price - index`. Using a zero-based index only shifts every official 1-indexed key by the same constant, so group membership is unchanged. Return the largest accumulated group total. Since the input is nonempty, at least one total exists.

## Complexity detail

Each of the $n$ prices performs one expected-constant-time hash-table update, so the expected running time is $O(n)$. There can be $n$ distinct invariant keys, giving $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Sort keyed prices:** Sorting `(price - index, price)` pairs and summing adjacent equal keys is correct, but takes $O(n\log n)$ time.
- **Rescan for every candidate key:** Summing a candidate group by scanning the whole array for each index can take $O(n^2)$ time when all keys are distinct.
- **Dynamic programming over subsequences:** The equality is transitive after rearrangement, so pairwise subsequence state is unnecessary.
- **Index origin:** Replacing 1-indexed positions by zero-based indices adds the same constant to every key and cannot change which indices share a group.
- **Single-element groups:** Any one day is a valid selection because there is no consecutive-pair condition to check.
- **Large scores:** Although each price is at most $10^9$, a group sum can exceed 32-bit range; use the language's appropriate wide integer type.
