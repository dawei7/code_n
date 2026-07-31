## General

**Reduce the two witnesses to global extrema**

Let the smallest array value be $m$ and the greatest be $M$. An occurrence
with value $x$ has a strictly smaller witness exactly when $m < x$, and it has
a strictly greater witness exactly when $x < M$. The required condition is
therefore equivalent to

$$
m < x < M.
$$

This equivalence also proves that array order and the multiplicities of the
extreme values do not matter. Find $m$ and $M$, then count every occurrence
whose value lies strictly between them. Each counted occurrence has both
required witnesses, while an excluded occurrence equals an extreme and is
missing at least one strict witness.

## Complexity detail

Let $n$ be the length of `nums`. Finding the two extrema and counting the
qualifying occurrences takes $O(n)$ time. Only the extrema and the counter are
stored, so the extra space is $O(1)$.

## Alternatives and edge cases

- **Sort the array:** After sorting, the counts of the minimum and maximum can
  be removed from $n$, but sorting costs $O(n \log n)$ time and may modify the
  input.
- **Compare every pair:** Searching separately for smaller and greater
  witnesses is direct but takes $O(n^2)$ time in the worst case.
- A one-element array, a two-element array, or an all-equal array has no
  qualifying occurrence.
- Duplicate interior values are counted once per occurrence.
- Strict inequalities exclude every occurrence equal to the minimum or
  maximum, including repeated extrema.
