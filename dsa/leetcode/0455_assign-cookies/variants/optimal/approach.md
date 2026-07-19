## General
**Consider the least demanding child first**

Sort greed requirements and cookie sizes. Maintain one pointer to the smallest unsatisfied greed. Scan cookies from smallest to largest, discarding a cookie when it is too small and assigning it when it meets the current requirement.

**Use the smallest cookie that can work**

When a cookie can satisfy the least greedy remaining child, assigning it is safe. Any feasible assignment that gives this child a larger cookie can swap in the current smaller cookie; the larger cookie remains available for a child with an equal or greater requirement. Thus the greedy assignment cannot reduce the number achievable by an optimum.

**Why an undersized cookie can be skipped**

If a cookie is smaller than the least remaining greed, it is also too small for every later child because the requirements are sorted. No future assignment can use it, so advancing only the cookie pointer loses nothing.

## Complexity detail
Sorting takes $O(g \log g + s \log s)$ time for `g` children and `s` cookies. The two-pointer scan is $O(g + s)$. Sorted copies use $O(g + s)$ auxiliary space; in-place sorting reduces explicit copy space.

## Alternatives and edge cases
- **Match from largest to largest:** satisfying the greediest child with the largest adequate cookie is the symmetric greedy strategy.
- **Repeatedly search for the smallest adequate cookie:** is correct but removing one match at a time can cost $O(g \cdot s)$.
- **Maximum bipartite matching:** models all valid assignments but is unnecessary because the threshold relation is totally ordered.
- **No children or no cookies:** the answer is zero.
- **Extra cookies:** once every child is satisfied, remaining cookies do not change the result.
- **Equal sizes and requirements:** each cookie can satisfy only one child, so duplicates retain their multiplicity.
- **Exact boundary:** a cookie whose size equals the greed requirement is sufficient.
