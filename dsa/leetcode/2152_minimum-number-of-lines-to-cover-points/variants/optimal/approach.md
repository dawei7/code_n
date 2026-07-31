## General

**Represent covered points with a bitmask**

For every pair of distinct points $i$ and $j$, compute a mask containing every
point collinear with them. Use the cross-product equality

$$
(x_k-x_i)(y_j-y_i)=(y_k-y_i)(x_j-x_i)
$$

so vertical lines require no special slope representation.

Memoize the minimum additional lines for each covered-point mask. Choose the
first uncovered point $i$. If it is the only uncovered point, one arbitrary
line covers it. Otherwise, pair $i$ with each other uncovered point $j$, add
the precomputed mask of their line, and recurse. Choosing the first uncovered
point removes symmetric choices: every solution must cover it, and any useful
line covering at least two uncovered points is represented by pairing it with
one of those other points. Taking the least recurrence value therefore covers
every optimal possibility.

## Complexity detail

Let $n$ be the number of points. Precomputing all pair-defined masks costs
$O(n^3)$ time and $O(n^2)$ space. There are at most $2^n$ covered masks with
at most $n$ transitions each, giving total time $O(n^3+n2^n)$. The memo table
uses $O(2^n)$ additional space, and recursion depth is at most $n$.

## Alternatives and edge cases

- **Enumerate every collinear subset:** Subset-partition DP is correct but can
  examine $3^n$ state/subset combinations.
- **Greedy largest line first:** Covering the most currently uncovered points
  need not minimize the total number of lines.
- **Floating-point slopes:** Normalized slopes can work, but cross products
  avoid precision errors and handle vertical lines uniformly.
- One or two remaining points always need exactly one more line.
- Duplicate coordinates do not occur.
- Several selected lines may intersect or cover the same point; overlap does
  not invalidate a cover.
