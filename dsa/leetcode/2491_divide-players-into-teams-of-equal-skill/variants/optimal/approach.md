## General

**The extremes are forced partners.** After sorting, let the smallest remaining skill be $a$ and the largest be $b$. In any valid division, $a$ cannot pair with a value smaller than $b$: if it did, its team sum would be below $a+b$, while $b$ would have to pair with a value at least $a$, producing a team sum at least $a+b$. Equality of all team sums therefore forces the smallest and largest remaining values to pair.

Remove that pair conceptually and apply the same argument to the next smallest and next largest values. Thus the sorted array has only one possible multiset of equal-sum pairings: symmetric positions from its two ends.

Sort `skill` and set the required sum from the first and last values. Walk inward with symmetric indices. If any pair has a different sum, the forced-pair argument proves that no alternative arrangement can succeed, so return `-1`. Otherwise add that pair's product to the chemistry total. When every value has been consumed, all teams share the target sum and the accumulated products are exactly the requested result.

## Complexity detail

Let $n = \lvert\texttt{skill}\rvert$. Sorting costs $O(n\log n)$ time and the symmetric scan costs $O(n)$, for $O(n\log n)$ overall. Python's in-place sort may use $O(n)$ auxiliary storage in the worst case; the subsequent scan uses only constant additional state.

## Alternatives and edge cases

- **Frequency table:** Because skill values are at most $1000$, counts can pair complements in $O(n+U)$ time and $O(U)$ space for value bound $U=1000$, but the sorting method directly exposes the forced pairing and generalizes beyond the fixed bound.
- **Quadratic partner search:** Repeatedly scanning unused players for the required complement is correct but can take $O(n^2)$ time.
- **Two players:** The only possible team is automatically valid, and its product is returned.
- **Repeated skills:** Equal values remain separate players; symmetric positions consume every occurrence exactly once.
- **Nonintegral implied target:** Such an input necessarily produces a mismatched symmetric pair and returns `-1`.
- **Equal total sum but incompatible counts:** A global average alone is insufficient; every symmetric pair is still checked.
- **Large chemistry:** Products are accumulated in an integer wide enough for the full sum; Python integers grow automatically.
