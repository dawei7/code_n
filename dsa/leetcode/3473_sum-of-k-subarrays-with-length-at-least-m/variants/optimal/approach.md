## General

Let `prefix[j]` be the sum of the first `j` elements, and let $D_t(j)$ be the maximum total for selecting exactly $t$ valid subarrays entirely within those first `j` elements. For zero selections, $D_0(j)=0$ for every prefix. States that cannot contain $t$ minimum-length subarrays are unreachable rather than zero, which matters when all available sums are negative.

For $t>0$, an optimal solution within the first `j` elements has two possibilities. It may leave position `j - 1` unused, giving $D_t(j-1)$. Otherwise, its last subarray ends at `j - 1` and starts at some prefix boundary `p` with $p\le j-m$. The earlier $t-1$ subarrays must lie within the first `p` elements, so this choice has value

$$
D_{t-1}(p)+\texttt{prefix[j]}-\texttt{prefix[p]}.
$$

Rearranging separates the only `j`-dependent term:

$$
D_t(j)=\max\left(D_t(j-1),\ \texttt{prefix[j]}+\max_{p\le j-m}\bigl(D_{t-1}(p)-\texttt{prefix[p]}\bigr)\right).
$$

As `j` advances, exactly one new start boundary, `p = j - m`, becomes legal. Maintain the inner maximum as `best_start`; each state then takes constant time. The first alternative covers every solution whose last selected position occurs earlier. The second considers every possible start of a subarray ending at the current boundary, and $D_{t-1}(p)$ guarantees non-overlap while still allowing adjacent subarrays. These exhaustive alternatives prove that the recurrence returns the optimum for exactly `t` selections.

Only the preceding selection-count row is needed to build the current row. Initialize that previous row to zero for zero selections, mark every new row unreachable, and scan `end` from `chosen * m`, the earliest prefix that can hold the required number of subarrays. After processing all `k` rows, the state for the full array is the required answer.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$. Prefix construction takes $O(n)$ time. Each of the $k$ dynamic-programming rows scans at most $n$ end boundaries and performs constant work per boundary, so total time is $O(nk)$. The prefix array plus the previous and current rows use $O(n)$ space. The fixed negative sentinel is below every legal total because the magnitude of any possible sum is at most $2\times10^7$.

## Alternatives and edge cases

- **Enumerate every start boundary:** Directly evaluating all `p <= j - m` for every state is correct but costs $O(kn^2)$ time.
- **Store the full DP table:** Keeping every $D_t(j)$ row also takes $O(nk)$ time but increases space from $O(n)$ to $O(nk)$.
- **All-negative values:** Unreachable states must not default to zero, and exactly `k` subarrays must still be selected.
- **Adjacent subarrays:** Using the previous row at prefix boundary `p` allows an earlier subarray to end at `p - 1`, so selections may touch without overlapping.
- **Lengths greater than `m`:** Retaining the best start across later end boundaries naturally extends the last subarray beyond its minimum length.
- **Tight capacity `n == k * m`:** Every selected subarray must have length exactly `m`, and together they cover the entire array.
- **Minimum length one:** The same recurrence permits singleton subarrays and still handles gaps and longer profitable extensions.
