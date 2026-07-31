## General

For two letters with alphabet indices $x$ and $y$, let

$$
d(x,y)=\min\bigl(\lvert x-y\rvert,\ 26-\lvert x-y\rvert\bigr).
$$

This is the minimum total number of cyclic single-letter operations needed to make the two letters equal. Moving one letter along the shorter arc until it reaches the other proves the cost is attainable; no sequence can use fewer steps than their cyclic distance. Operations on positions omitted from the subsequence never help, so the problem becomes selecting ordered pairs of positions and paying this cost for each mirrored pair.

Define $F(i,j,b)$ as the maximum palindromic-subsequence length obtainable from `s[i:j + 1]` with at most $b$ operations. An optimal subsequence either omits the left endpoint, omits the right endpoint, or uses both endpoints as a mirrored pair. Therefore,

$$
F(i,j,b)=\max\left(
F(i+1,j,b),
F(i,j-1,b),
2+F(i+1,j-1,b-d)
\right),
$$

where the third choice is available only when $d=d(s[i],s[j])\le b$. An empty interval contributes zero and a one-character interval contributes one. These alternatives cover every possible subsequence: if it does not use both endpoints, at least one skip state contains it; if it uses both, palindromic symmetry requires them to become equal and leaves an independent palindromic subsequence inside. Thus the recurrence also proves that every computed choice is attainable and that no optimal choice is omitted.

The full three-dimensional table can be compressed across `i`. Process `left` from right to left and `right` from left to right. Before updating a `right` row, `dp[right]` still stores $F(i+1,j,*)$, while the already updated `dp[right - 1]` stores $F(i,j-1,*)$. A saved `diagonal` row stores $F(i+1,j-1,*)$. Replacing `dp[right]` after all budgets are computed preserves exactly the three dependencies needed by the next interval.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. There are $O(n^2)$ intervals, and each interval evaluates all $k+1$ budgets in constant time, for $O(n^2k)$ time. The rolling table contains $n$ budget rows of length $k+1$, plus two temporary rows, so it uses $O(nk)$ space. A direct table indexed by both interval endpoints would use $O(n^2k)$ space without improving the running time.

## Alternatives and edge cases

- **Full three-dimensional interval DP:** It applies the same recurrence transparently but stores every $F(i,j,b)$ state, increasing space to $O(n^2k)$.
- **Memoized recursion:** Top-down evaluation can skip unreachable states, but recursion overhead and a depth of up to $n$ make the iterative order more predictable while retaining the same worst-case bounds.
- **Enumerate subsequences:** Testing every subsequence and summing mirrored-pair costs is correct but takes exponential time in $n$.
- **Alphabet wraparound:** Pair cost must use the shorter cyclic direction; for example, matching `'a'` and `'z'` costs one, not twenty-five.
- **Odd-length palindrome:** Its middle character has no partner and costs no operations, which is represented by the singleton base case.
- **Unused budget:** States mean at most the given budget, so an already palindromic subsequence remains valid without spending the remaining operations.
- **Single character:** The initialized singleton row returns one for every legal budget.
