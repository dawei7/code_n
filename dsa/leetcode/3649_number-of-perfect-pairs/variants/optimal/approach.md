## General

**Remove the signs algebraically.** For any integers $a$ and $b$,

$$
\max(\lvert a-b\rvert,\lvert a+b\rvert)=\lvert a\rvert+\lvert b\rvert
$$

and

$$
\min(\lvert a-b\rvert,\lvert a+b\rvert)=\bigl\lvert\lvert a\rvert-\lvert b\rvert\bigr\rvert.
$$

The maximum is always at least both individual magnitudes, so the second required inequality holds automatically. Write $x$ for the smaller magnitude and $y$ for the larger. The first inequality becomes $y-x\le x$, or equivalently $y\le2x$. Thus only the two magnitudes and their ratio matter.

Sort all absolute values. For each right endpoint with magnitude `y`, advance `left` while `y > 2 * magnitudes[left]`. Every index from `left` through `right - 1` then forms a perfect pair with `right`, contributing `right - left`. As `right` increases, the smallest valid left endpoint never moves backward, so the scan is linear after sorting.

## Complexity detail

Sorting $n$ magnitudes takes $O(n\log n)$ time, and the two-pointer scan takes $O(n)$ because each pointer moves at most $n$ times. The magnitude list uses $O(n)$ auxiliary space.

The benchmark sets size $N=n$ and keeps all magnitudes between 1000 and 1500, making every pair perfect. Tiers 32, 128, and 512 span 16x. The accepted sort-and-scan method is $O(N\log N)$; checking the original inequalities for every pair is $O(N^2)$ and must finish every tier but fail scaling.

## Alternatives and edge cases

- **Binary search per endpoint:** Lower-bound search for each sorted magnitude also takes $O(n\log n)$ time, but the monotone pointer avoids repeated searches.
- **Test every pair:** Directly applying the two original inequalities is simple but quadratic.
- **Two zeros:** They form a perfect pair because both sides of both inequalities are zero.
- **One zero and one nonzero:** The larger magnitude cannot be at most twice zero, so the pair is not perfect.
- **Opposite signs:** Only absolute values matter after the identities are applied.
- **Inclusive factor two:** Magnitudes `x` and `2x` qualify because the inequality is non-strict.
- **Duplicate magnitudes:** Every distinct pair of indices is counted, even when their values or magnitudes match.
