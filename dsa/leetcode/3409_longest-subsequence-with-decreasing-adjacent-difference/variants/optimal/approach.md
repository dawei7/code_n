## General

Let $V=300$, the largest permitted value. The index of the last chosen element is relevant only through its value and the last difference already used. Define `dp[x][d]` as the maximum length of a processed subsequence that ends at value $x$ and whose most recent absolute difference is exactly $d$.

Suppose the next input value is $v$ and a preceding chosen value is $x$. Their new difference is

$$
\delta=\lvert v-x\rvert.
$$

The preceding state may be extended exactly when its last difference $d$ satisfies $d\ge\delta$. Rechecking every such $d$ for every value would add another factor of $V$. Instead, maintain

$$
\texttt{suffix\_best[x][delta]}
=
\max_{d\ge\delta}\texttt{dp[x][d]}.
$$

This makes the best extension through a seen value $x$ available in constant time. If no longer state exists, any earlier occurrence of $x$ and the current $v$ form a new length-two subsequence. The candidate length for difference $\delta$ is therefore the greater of 2 and `suffix_best[x][delta] + 1`.

Compute every candidate for the current array element into a temporary `updates` row before changing `dp[v]`. That separation is essential when $v$ has appeared earlier: otherwise the current element could update a state and then immediately reuse itself as its own predecessor. Merge the completed row into `dp[v]`, rebuild that row's suffix maxima from large differences down to zero, and mark $v$ as seen.

By induction over processed positions, `dp` contains the best subsequence for every exact ending state. Every legal extension is considered through its previous ending value, and the suffix maximum includes exactly the allowed prior differences $d\ge\delta$. Conversely, every created state appends a later array element while satisfying that inequality. The largest stored length is therefore the requested optimum.

## Complexity detail

For each of the $n$ array elements, the algorithm scans the $V$ possible previous values, merges a row of $V$ differences, and rebuilds one suffix row of $V$ differences. The time is $O(nV)$. The exact-state table and its suffix maxima each use $O(V^2)$ space; the temporary row and seen flags use $O(V)$ additional space.

The benchmark defines `size` as $n$ and uses legal 50-, 200-, and 400-element alternating-boundary tiers, spanning 8x. The accepted value-domain DP performs $O(nV)$ work. A correct index-based DP with one suffix row per index examines every preceding index for every new element, requiring $O(n^2+nV)$ time, and fails only the scaling verdict.

## Alternatives and edge cases

- **Three nested loops over indices and differences:** Tracking every ending index is natural, but scanning all eligible previous differences for every pair takes $O(n^2V)$ time.
- **Index-based suffix DP:** Precomputing difference suffix maxima per index improves that to $O(n^2+nV)$, but it still ignores the small value domain that permits state compression.
- **Memoized subsequence search:** Choosing or skipping each element has exponential raw state and does not exploit the bounded values.
- **Equal differences:** The relation is non-increasing, so suffix queries must include the current difference rather than start at the next larger one.
- **Difference zero:** Repeated equal values may extend a zero-difference chain through the entire array.
- **Two elements:** Any pair is valid because it has only one adjacent difference.
- **Repeated current value:** Build a temporary update row before mutating that value's stored states, preventing reuse of the same position.
- **Boundary values:** Values 1 and 300 produce the maximum difference 299, which fits the allocated difference domain.
