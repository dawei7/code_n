## General

**Rewrite road importance as city contributions**

If city $i$ receives value $v_i$ and has degree $d_i$, its value appears once
in the importance of every incident road. Therefore the total importance is

$$
\sum_{i=0}^{n-1} d_i v_i.
$$

Only the degree of each city matters; the individual road pairings do not
affect the assignment step.

**Pair larger degrees with larger values**

Count every city's degree, sort the degree multiset in ascending order, and
pair it with the values $1,2,\ldots,n$ in ascending order. Sum each
degree-value product.

For the exchange argument, suppose two cities have degrees $d_a<d_b$ but
values $v_a>v_b$. Swapping their values changes the total by

$$
(d_b-d_a)(v_a-v_b)>0.
$$

Thus any assignment containing such an inversion is not optimal. Removing all
inversions produces the sorted pairing, which therefore achieves the maximum.
Equal degrees may receive their tied values in any order.

## Complexity detail

Let $n$ be the number of cities and $r$ the number of roads. Degree counting
takes $O(r)$ time, sorting takes $O(n \log n)$ time, and the weighted sum takes
$O(n)$ time, for $O(n \log n+r)$ total. The degree array and sorting storage
use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Repeated minimum selection:** Removing the smallest remaining degree for each next value is correct but takes $O(n^2)$ time with an array.
- **Min-heap:** Heap removal produces the same ordering in $O(n \log n)$ time but is less direct than sorting.
- **Assign by city index:** Numeric city labels carry no importance information; degree determines how often a value contributes.
- **Isolated cities:** Degree-zero cities should receive the smallest values because their assignments add nothing.
- **Equal degrees:** Swapping their assigned values leaves the total unchanged.
- **One road:** Its two endpoints receive the two largest useful values, while any isolated cities receive smaller values.
- **Large total:** The answer may exceed 32-bit integer range even though each assigned value is at most $n$.
