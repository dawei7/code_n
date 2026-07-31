## General

A positive integer divides every value in `numsDivide` if and only if it
divides their greatest common divisor. Let

$$
G=\gcd(\texttt{numsDivide[0]},\ldots,\texttt{numsDivide[m-1]}).
$$

This replaces many divisibility constraints with the single test `G % value ==
0`.

**Choose the smallest usable survivor**

Scan `nums` for the smallest value that divides $G$. If none exists, no
deletion plan can succeed. Otherwise call this value $d$. Every occurrence
strictly smaller than $d$ must be deleted, because leaving even one would make
that smaller value the array minimum and it does not divide $G$. No value at
least $d$ needs deletion: retaining $d$ makes it the minimum and it divides
every target.

Thus the number of `nums` values below $d$ is both a necessary lower bound and
an achievable deletion count. Choosing any larger usable divisor could only
add deletions, so the smallest usable divisor yields the global minimum.

## Complexity detail

Let $n$ and $m$ be the two array lengths and let $V$ be their largest value.
Computing a gcd costs $O(\log V)$ per target in the worst case; the two scans
of `nums` are linear. The total bound is $O((n+m)\log V)$ time and $O(1)$
auxiliary space.

## Alternatives and edge cases

- **Sort `nums` first:** After computing $G$, scan sorted values until finding
  a divisor. This directly makes the index equal the deletion count, but adds
  $O(n\log n)$ sorting time and may mutate the input.
- **Test every target for every candidate:** This avoids the gcd observation
  but can take $O(nm)$ divisibility checks.
- **Duplicate smaller values:** Every occurrence below the chosen divisor must
  be deleted and therefore counts separately.
- **Gcd absent from `nums`:** A proper divisor of $G$ is equally valid; the
  selected value need not equal $G$.
- **Value one:** If 1 occurs in `nums`, zero deletions are always sufficient
  because no positive input can be smaller.
