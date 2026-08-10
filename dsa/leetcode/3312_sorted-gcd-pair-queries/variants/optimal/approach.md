## General

**Count GCD values without generating pairs.** There are $n(n-1)/2$ index pairs, which is far too many to list when $n=10^5$. However, every GCD is an integer from one through `mx = max(nums)`, at most $5\cdot10^4$. The source counts how many pairs have each possible exact GCD and answers order-statistic queries from those counts.

`cnt = Counter(nums)` stores how many input elements equal each value. Array `cnt_g[g]` will eventually store the number of index pairs whose GCD is exactly $g$.

**First count pairs whose two values are divisible by $i$.** For a fixed candidate $i$, the loop visits `i, 2i, 3i, ...` and sums `cnt[j]` into `v`. Thus $v$ is the number of input positions whose values are multiples of $i$. Any two of those positions form a pair whose GCD is itself a multiple of $i$. The number of such pairs is

$$
\binom v2=\frac{v(v-1)}2.
$$

This count includes exact GCD $i$, but also exact GCDs $2i,3i,\ldots$.

**Subtract already-known larger exact GCDs.** Candidate values are processed from `mx` down to one. By the time the algorithm handles $i$, `cnt_g[j]` is already final for every larger multiple $j$ of $i$. Inside the multiples loop, it performs `cnt_g[i] -= cnt_g[j]`. After the loop it adds the all-divisible pair count.

The multiple `j == i` is included, but `cnt_g[i]` is still zero before processing and subtracting itself has no effect. For larger multiples, subtraction removes pairs whose GCD is $2i,3i,\ldots$. The resulting relation is

$$
\texttt{cnt\_g}[i]
=
\binom{\#\{x:i\mid x\}}2
-
\sum_{\substack{j>i\\i\mid j}}\texttt{cnt\_g}[j].
$$

Every pair divisible by $i$ has exactly one exact GCD among those multiples, so this inclusion-exclusion leaves precisely the pairs with GCD $i$.

For `nums = [2,3,4]`, the exact counts become two pairs with GCD one and one pair with GCD two. The algorithm derives this from divisibility totals rather than evaluating three calls to a GCD function.

**Turn exact frequencies into sorted-array boundaries.** `s = list(accumulate(cnt_g))` creates prefix sums. `s[g]` is the number of pairs whose GCD is at most $g$. Conceptually, in sorted `gcdPairs`, indices from `s[g-1]` through `s[g]-1` contain value $g$.

Each query `q` is a zero-based index. The desired GCD is the smallest $g$ for which more than $q$ pairs have GCD at most $g$, or

$$
\texttt{s}[g]>q.
$$

`bisect_right(s, q)` returns the first prefix-sum index whose value is strictly greater than $q$. That index is exactly $g$. Using the strict boundary is important: if `q == s[g]`, index $q$ lies after all GCD-$g$ pairs and belongs to a larger value.
For every $i$, the divisibility count includes exactly pairs whose GCD belongs to the set of multiples of $i$. Descending subtraction partitions those pairs by their unique exact GCD. Therefore `cnt_g` contains correct multiplicities and its total is $\binom n2$. Prefix sums reproduce the block endpoints of the conceptual sorted array, and binary search selects the block containing each legal query index.

No explicit sorting of pair values occurs. The integer value domain is already traversed in ascending order by the prefix array.

## Complexity detail

Let $M=\max(\texttt{nums})$ and $q=\lvert\texttt{queries}\rvert$. Counting input values takes expected $O(n)$ time. The total iterations over multiples are

$$
\sum_{i=1}^{M}\left\lfloor\frac Mi\right\rfloor=O(M\log M).
$$

Prefix accumulation costs $O(M)$. Each query performs binary search over $M+1$ values in $O(\log M)$ time. Total time is $O(n+M\log M+q\log M)$, matching the manifest.

`cnt_g` and `s` each use $O(M)$ space. The counter has at most $\min(n,M)$ keys, and the output uses $O(q)$ result space. Excluding the required answer, auxiliary space is $O(M)$.

## Alternatives and edge cases

- **Enumerate every pair:** It costs $\Theta(n^2\log M)$ time if each GCD uses Euclid's algorithm and cannot handle $n=10^5$.
- **Sort generated GCDs:** Even if GCD calculation were faster, storing $\Theta(n^2)$ values is prohibitive.
- **Möbius inversion:** Number-theoretic Möbius methods can derive exact GCD counts from divisible-pair counts, but descending multiple subtraction is direct and easy to verify.
- **Binary-search boundary:** `bisect_right(s, q)` finds the first cumulative count strictly above the zero-based query. `bisect_left(s, q)` would mishandle block boundaries.
- **Duplicate input values:** Counter frequencies and $\binom v2$ count distinct index pairs correctly, including pairs of equal values.
- **All values equal $x$:** Every pair has GCD $x$, all legal queries binary-search to $x$, and other exact counts are zero.
- **Value one present:** Pairs involving one necessarily have GCD one, and inclusion-exclusion includes them naturally.
- **Repeated query indices:** Each is answered independently and returns the same value without altering state.
- **Zero-count GCD values:** Prefix sums can have repeated values. `bisect_right` skips the entire flat region to the next GCD with a nonempty block.
- **Large pair count:** $\binom n2$ exceeds 32-bit range. Python integers are safe; fixed-width implementations need 64-bit counts and query handling.
- **Counter lookup of absent multiples:** It contributes zero and does not need a dense frequency array, though a dense array could reduce hashing overhead.
- **Including `j == i` in subtraction:** It is harmless only because `cnt_g[i]` is zero before its descending computation. Starting multiples at `2*i` would express the formula more transparently.
- **Query validity:** Constraints guarantee every query is below the total pair count, so binary search always returns a GCD between one and $M$.
