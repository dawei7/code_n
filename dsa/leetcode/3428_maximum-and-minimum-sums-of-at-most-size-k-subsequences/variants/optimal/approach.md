## General

**Count how often each sorted value is an extreme.** Enumerating subsequences is exponential. Instead, sort the values and add each number's total contribution as a maximum and as a minimum.

Let `values` be `sorted(nums)`. Consider position $i$. To form a non-empty subsequence for which `values[i]` is the distinguished maximum, include this element and choose $j$ additional indices from the $i$ positions before it. If the subsequence may contain at most $k$ elements, then $0\le j\le k-1$. Its number of maximum contributions is

$$
W_i=\sum_{j=0}^{\min(k-1,i)}\binom ij.
$$

Every such chosen earlier value is no greater than `values[i]`.

Duplicates do not cause overcounting. Think of the sorted elements as retaining their original identities. A subsequence's maximum is attributed to its rightmost selected sorted position. All other selected positions are earlier, so that subsequence appears in exactly one $W_i$. Equal numeric values may be interchangeable as values, but different original indices define different subsequences, as the examples require.

**Use symmetry for minimum contributions.** The element at mirrored position `values[n - 1 - i]` has exactly $i$ positions after it. Include it as the leftmost selected sorted position and choose up to $k-1$ of those later positions. It is then the distinguished minimum in the same $W_i$ ways.

Therefore, one loop index contributes

$$
(\texttt{values}[i]+\texttt{values}[n-1-i])W_i.
$$

As $i$ runs from $0$ through $n-1$, every element receives its complete maximum contribution once and its complete minimum contribution once.

For `[1,2,3]` with $k=2$, the maximum weights are $1$, $2$, and $3$: value $1$ is maximum only in `[1]`; value $2$ is maximum in `[2]` and `[1,2]`; value $3$ is maximum in its singleton and the two pairs ending with it. Minimum weights are the reverse. The combined contribution is $24$.

**Maintain one row of Pascal's triangle.** Recomputing binomial coefficients for every $i$ would be expensive. At the start of iteration $i$, the array `combinations` stores

`combinations[j] = C(i, j)`

for $0\le j\le\texttt{limit}$, where `limit = min(k - 1, n - 1)`. It begins as `[1,0,...]`, the row for $i=0$.

The source calculates `ways = sum(combinations) % mod`. Entries beyond $i$ remain zero, so this sum is exactly $W_i$ without a separate bound in the expression.

After using the current row, the loop

`for chosen in range(min(i + 1, limit), 0, -1)`

applies Pascal's identity:

$$
\binom{i+1}{j}
=
\binom ij+\binom i{j-1}.
$$

Descending order is essential. It ensures `combinations[chosen - 1]` still comes from row $i$, rather than from the partially updated row $i+1$. Index zero remains one.

All combination entries, `ways`, and `answer` are reduced modulo $10^9+7$. Because addition and multiplication respect modular arithmetic, reducing intermediate counts does not change the final required residue.

**Why sorting does not violate subsequence identity.** A subsequence normally preserves original index order. But its minimum and maximum depend only on which indexed elements were chosen, not the order in which their values appear. Every subset of original indices determines exactly one subsequence in original order. Sorting the indexed values is only a counting device for assigning that subset's extreme contributions; it does not construct a different set of subsequences.
For every valid non-empty subsequence, select its rightmost position in sorted-by-value order among chosen identities. The maximum is contributed once by that position's formula. Select its leftmost sorted position, and the minimum is contributed once by the mirrored formula. Conversely, every combination counted in $W_i$ chooses at most $k-1$ partners plus the distinguished element, so it represents a valid subsequence of size at most $k$. Thus the accumulated answer is exactly the required sum.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Sorting costs $O(n\log n)$. The combination array has length at most $k$. Each of the $n$ iterations sums it and updates up to $k-1$ entries, costing $O(nk)$. Total time is $O(n\log n+nk)$.

`values` is a sorted copy using $O(n)$ space. `combinations` uses $O(k)$ space. Scalar arithmetic adds constant storage, so total auxiliary space is $O(n+k)$, matching the manifest. Since $k\le70$, the $nk$ factor is tightly bounded.

## Alternatives and edge cases

- **Enumerate subsequences:** Even limiting size to $k$ yields up to $\sum_{j=1}^k\binom nj$ choices, far too many.
- **Precompute a full combination table:** An $n\times k$ table works but uses $O(nk)$ space. One descending Pascal row is sufficient.
- **Factorials and inverses:** They can query each $\binom ij$ in $O(1)$ after $O(n)$ preprocessing, but still require summing up to $k$ terms per index and add larger tables.
- **\(k=1\):** `limit` is zero and `ways` is always one. Every singleton contributes twice its value.
- **\(k=n\):** All non-empty subsequences are allowed; the truncated Pascal sums naturally include every possible partner count.
- **Duplicate values:** Original indices still create distinct subsequences. Rightmost/leftmost sorted identity attribution prevents double counting.
- **Zero values:** Their numerical contribution is zero, though they still affect the number of ways other values become extremes.
- **Modulo arithmetic:** Combination counts are reduced at every update, preventing enormous integers while preserving the final residue.
- **Descending update order:** Updating from low to high would reuse new-row values and corrupt binomial coefficients.
- **Empty subsequence:** It is never counted because every contribution explicitly includes one distinguished element.
