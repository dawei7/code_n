## General

Let $m\le4$ be the number of targets and represent the satisfied targets by an $m$-bit mask. A single final number can cover a subset of targets exactly when it is divisible by every value in that subset. This is equivalent to being divisible by their least common multiple.

Precompute `subset_lcm[mask]` for every target subset. For a number $x$ and required multiple $L$, the least increment that reaches a multiple of $L$ is `(-x) % L`. Thus every input number offers one transition for each subset it might cover.

Maintain `dp[mask]`, the minimum cost after the already-processed numbers have covered `mask`. For each new number, copy the table to represent leaving it unchanged. From every reachable mask, enumerate only subsets of the still-uncovered bits, pay the corresponding LCM increment, and update the union mask. Restricting the chosen subset to uncovered targets loses nothing: adding an already-covered target can only keep or increase the LCM and therefore cannot yield a cheaper next multiple.

Using a copied table ensures one array element is assigned at most once during its iteration. Inductively, every DP value is the best cost among assignments of processed numbers, and every possible assignment appears through one of the subset transitions. The full mask therefore holds the global minimum.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and $m=\lvert\texttt{target}\rvert\le4$. Computing all subset LCMs costs $O(m2^m)$. Across all covered masks, their disjoint remaining submasks produce $3^m$ state/subset combinations per number, giving $O(m2^m+n3^m)$ time. The LCM and DP tables use $O(2^m)$ space.

## Alternatives and edge cases

- **Handle each target independently:** This can overpay because one incremented number may cover several targets through their LCM.
- **Enumerate every subset from every mask:** This gives $O(n4^m)$ transitions; limiting choices to uncovered bits removes dominated work.
- **Use the product of a subset:** Shared factors make the product unnecessarily large; divisibility by all targets requires their LCM.
- **Already covered targets:** Zero-cost transitions naturally retain existing multiples.
- **Duplicate targets:** Their bits may be covered together by the same unchanged or incremented number.
- **Divisibility relationships:** If one target divides another, reaching a multiple of the larger target can satisfy both bits.
- **Large LCM:** Python integers safely hold the LCM of four values up to $10^4$.
