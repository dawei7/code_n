## General

Sort the values. For the value at rank $i$ to be the maximum of a subsequence of size $j+1$, that subsequence must include this occurrence and choose its other $j$ indices from the $i$ smaller-or-equal ranked occurrences before it. Index occurrences remain distinct even when values tie, so the count is $\binom{i}{j}$. Across every allowed size, its maximum coefficient is

$$
W_i=\sum_{j=0}^{k-1}\binom{i}{j},
$$

where terms with $j>i$ are zero.

The minimum calculation is symmetric. The value at rank $n-1-i$ has exactly $i$ occurrences to its right and is therefore the minimum of $W_i$ eligible subsequences. Consequently, one coefficient can contribute both extremes at once:

$$
W_i\bigl(\texttt{values[i]}+\texttt{values[n-1-i]}\bigr).
$$

Generate the coefficients of Pascal's triangle incrementally. Before processing rank $i$, the compact array stores $\binom{i}{0},\ldots,\binom{i}{k-1}$. Its sum is $W_i$. Updating entries from right to left applies Pascal's identity without overwriting a value still needed by the current row. Reducing every update and contribution modulo $10^9+7$ keeps all stored values bounded.

Every eligible subsequence has one well-defined selected minimum occurrence and maximum occurrence. The coefficient argument counts it once in each role, which proves that the accumulated result is exactly the requested total.

## Complexity detail

Sorting takes $O(n\log n)$ time and stores $O(n)$ values. Updating at most $k$ binomial coefficients and summing them for every rank costs $O(nk)$ time. The Pascal row uses $O(k)$ space, so total auxiliary space is $O(n+k)$ with the sorted copy.

## Alternatives and edge cases

- **Enumerate subsequences:** Direct generation is exponential and becomes infeasible long before $n=10^5$.
- **Factorials and inverse factorials:** Precomputation supports constant-time individual binomial coefficients, but summing up to $k$ sizes for every rank still takes $O(nk)$ time and uses $O(n)$ tables.
- **Only singletons:** When `k = 1`, every coefficient is `1`, so every array value contributes twice.
- **Duplicate values:** Sorting equal occurrences into separate ranks is correct because subsequences are distinguished by selected indices.
- **Zero values:** They contribute zero when selected as an extreme but still affect the number of subsequences containing other extremes.
- **Maximum values and large totals:** Modular reduction is required throughout the coefficient updates and weighted sum.
