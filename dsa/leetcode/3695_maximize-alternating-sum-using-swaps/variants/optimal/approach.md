## General

Treat every array index as a graph vertex and every allowed swap pair as an undirected edge. Reusing and composing edge swaps allows values to follow paths. Consequently, the values initially located in one connected component can be permuted arbitrarily among that component's indices, while no value can cross between components.

**Optimize each component independently.** Suppose a component contains $e$ even indices and $o$ odd indices. Exactly $e$ of its values will be added and the remaining $o$ will be subtracted. If a smaller value $a$ occupies a positive position while a larger value $b$ occupies a negative position, exchanging them changes the component's contribution by $2(b-a)\ge0$. Repeating that exchange argument shows that a maximum assigns the component's $e$ largest values to its even indices and its $o$ smallest values to its odd indices.

**Build components and assign signs.** Use disjoint-set union to merge the endpoints of every allowed pair. Group `nums[index]` by the final representative and count the even indices belonging to each group. After sorting one component's values, its contribution is the sum of the largest `even_count` values minus the sum of all earlier values. Equivalently, it is twice the positive sum minus the sum of the complete component. Adding the independently maximal contributions gives the global maximum because swaps never couple different components.

## Complexity detail

Let $n=\lvert\texttt{nums}\rvert$ and $m=\lvert\texttt{swaps}\rvert$. Disjoint-set operations take $O((n+m)\alpha(n))$ time, and sorting all component values costs at most $O(n\log n)$. The combined bound is $O((n+m)\log n)$. The disjoint-set arrays, grouped values, and counters use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Graph traversal components:** Building adjacency lists and running DFS or BFS is also correct in $O(n+m)$ component-discovery time, but stores $O(n+m)$ graph entries rather than the disjoint-set's $O(n)$ arrays.
- **Try allowed swaps greedily:** A locally improving direct swap can miss a better permutation that requires intermediate moves through a path; connectivity, not the listed-edge order, determines reachability.
- **Search all reachable arrays:** A connected component of size $c$ can realize $c!$ permutations, making explicit state search infeasible.
- **No allowed swaps:** Every index forms a singleton component, so the computation returns the original alternating sum.
- **Edges within one parity:** A component containing only even indices or only odd indices cannot change which sign its values receive, although their internal order may change.
- **Large result magnitude:** The answer can exceed 32-bit integer range because up to $10^5$ values of size $10^9$ contribute with signs.
