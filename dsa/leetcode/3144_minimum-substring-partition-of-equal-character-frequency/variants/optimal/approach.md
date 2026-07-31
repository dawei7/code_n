## General

Let `dp[end]` be the minimum number of balanced parts covering the prefix `s[:end]`. The empty prefix needs zero parts. If `s[start:end]` is balanced, it can be appended to an optimal partition of `s[:start]`, giving the transition

$$
\texttt{dp[end]} = \min\bigl(\texttt{dp[end]},\ \texttt{dp[start]} + 1\bigr).
$$

**Recognize a balanced substring incrementally**

For each fixed `end`, move `start` from right to left and update a 26-entry frequency array. Also maintain the number $d$ of distinct characters and the greatest frequency $f$ currently present.

The substring is balanced exactly when its length equals $d \cdot f$. If every positive frequency equals $f$, their sum is clearly $df$. Conversely, all positive frequencies are at most $f$ and there are $d$ of them, so a total of $df$ is possible only when every one equals $f$. This single equality avoids rescanning the alphabet for every candidate substring.

Each balanced suffix considered by the inner loop supplies a valid last part. Taking the minimum over all starts examines every possible final cut, so induction on `end` shows that every `dp[end]` is optimal. The requested answer is `dp[n]`.

## Complexity detail

There are $n$ choices of ending position and at most $n$ starts for each one. Every extension updates constant-size state in $O(1)$ time, so the total running time is $O(n^2)$.

The dynamic-programming array uses $O(n)$ space. The 26-entry frequency array is fixed-size and does not change the bound.

## Alternatives and edge cases

- **Recount every substring:** Testing each candidate by rebuilding all of its frequencies is straightforward but costs $O(n^3)$ time; it is the principal slower benchmark comparison.
- **Memoized recursion:** Trying every balanced prefix from each position has the same $O(n^2)$ state-transition work when frequencies are updated incrementally, but recursion adds call-stack overhead.
- **Precomputed prefix counts:** Twenty-six prefix arrays make every frequency query constant-time per letter, yielding $O(26n^2)$ time and extra $O(26n)$ storage without improving the asymptotic result.
- Any one-character substring is balanced, so a valid partition always exists and `dp[end]` is never unreachable.
- A substring containing only one distinct character is balanced regardless of its length.
- Equal frequencies matter only among characters that actually occur in the substring; zero entries are excluded from the distinct count.
- The whole string may already be balanced, in which case the answer is one even if several smaller balanced partitions also exist.
