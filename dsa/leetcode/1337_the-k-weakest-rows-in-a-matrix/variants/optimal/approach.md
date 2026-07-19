## General
**Locate each row's boundary**

Because every row changes at most once from 1 to 0, its soldier count is the position of its first 0. Use binary search over the half-open interval from 0 through $n$: when the middle cell is 1, move the lower boundary right; otherwise move the upper boundary left. The converged position is 0 for an all-civilian row and $n$ for an all-soldier row.

Pair that count with the row index. Sorting the pairs lexicographically first compares soldier counts and then indices, exactly matching the definition of weaker. Return the indices from the first `k` pairs.

Binary search yields the exact prefix length because positions before the boundary are 1 and positions at or after it are 0. The sorted pair order therefore represents every row's true strength and applies the required tie rule, making its first `k` entries precisely the requested rows.

## Complexity detail
Binary search costs $O(\log n)$ for each of $m$ rows, and sorting the $m$ pairs costs $O(m\log m)$. The total is $O(m\log n+m\log m)$. The strength pairs and returned indices use $O(m)$ space.

## Alternatives and edge cases
- **Sum every row:** Since cells are binary, `sum(row)` obtains the same strength simply, but reads all $mn$ cells and takes $O(mn+m\log m)$ time.
- **Size-$k$ heap:** Maintaining only the weakest candidates can reduce ordering work when $k$ is much smaller than $m$, at the cost of more involved tie handling.
- **All civilians:** Binary search returns a strength of zero.
- **All soldiers:** The boundary falls just after the final column, giving strength $n$.
- **Equal strengths:** The smaller row index must appear first.
- **Return every row:** When $k=m$, the result is the complete strength ordering.
