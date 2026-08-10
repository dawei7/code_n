## General

**Connected components determine reachability.** Ignoring blocked cells, four-direction movement partitions the positive cells into connected components. Every cell in one component can reach every other cell in that component and cannot reach any cell in another component.

If component $C$ has size $t_C$ and value sum $s_C$, every cell in $C$ has remoteness equal to the sum of values in all other components.

**The exact source uses a dual counting formula.** A direct component contribution would be

$$
t_C\left(S-s_C\right),
$$

where $S$ is the sum of all positive cell values.

The code does not calculate $S$. It first counts the total number of positive cells, stored as `cnt`. For component $C$, it adds

`(cnt - t) * s`.

This appears reversed: it multiplies the component's value sum by the number of cells outside it. Yet the total over all components is identical.

The requested total can be expanded as

$$
\sum_C\sum_{D\ne C} t_Cs_D.
$$

The source computes

$$
\sum_C\sum_{D\ne C} s_Ct_D.
$$

The ordered component pairs $(C,D)$ cover both directions. Renaming $C$ and $D$ shows the double sums are equal. Conceptually, instead of asking how much outside value each cell sees, the source asks how many outside cells count each component's values.

**Explore one component recursively.** `dfs(i, j)` starts with the current positive cell's value as `s` and one as `t`. It then writes zero into the grid cell to mark it visited.

For each four-direction neighbor that is in bounds and still positive, recursion returns that neighbor subtree's sum and size. These are added to the current pair. When traversal finishes, the helper returns the complete component value sum and cell count.

Blocked cells stay negative one and are never entered. Visited cells are zero and are also excluded by the strict positivity test.

**The outer scan finds each component once.** When the row-major loops encounter a positive cell, no previous DFS has visited it, so it begins a new component. That DFS changes every cell in the component to zero. Later scan positions therefore skip the component.

After obtaining `s, t`, the source adds the dual contribution and continues.
The DFS visits exactly the positive cells reachable from its start: every recursive edge follows a valid adjacency, and every reachable positive neighbor is eventually explored. Zero marking prevents repeats. Summing values and counts over recursive subtrees therefore yields exact component statistics.

The outer scan covers every component once. The double-sum identity proves the source's contribution formula equals the requested total remoteness. Blocked cells correctly contribute zero because they are absent from both component counts and sums.

**Input mutation is significant.** Every nonblocked cell is overwritten with zero. After the method, the caller's grid no longer contains its original positive values. This is how the source avoids a separate visited matrix, but it must be documented if input reuse matters.

**Recursive depth can exceed standard Python limits.** A $300$ by $300$ connected grid can create a depth-first call chain far longer than Python's usual recursion limit of roughly one thousand, especially with the direction order producing long paths. The asymptotic algorithm is correct, but the exact recursive implementation may raise `RecursionError` on a legal large component unless the environment raises the limit. An iterative stack or BFS is safer for the full constraint.

## Complexity detail

Let $N=n^2$ be the number of grid cells. The initial positive-cell count scans $N$ cells. Across all DFS calls, each positive cell is visited once and four neighbors are checked. The outer scan is also $O(N)$. Total time is $O(n^2)$.

No separate visited matrix is allocated because the grid is mutated. However, recursive DFS can retain one frame per cell in the worst case, using $O(n^2)$ call-stack space. Scalar state is constant per frame.

Thus, the exact auxiliary-space worst case is $O(n^2)$, consistent with the manifest but accompanied by a practical recursion-limit risk. An iterative queue or stack also uses $O(n^2)$ worst-case storage but does not consume the language call stack.

## Alternatives and edge cases

- **Iterative BFS per component:** Compute size and sum with a queue, then use either contribution formula. It avoids recursion overflow and is the safest direct replacement.
- **Direct total-sum formula:** Precompute total positive value sum `S` and add `t * (S - s)` per component. This is easier to relate to the definition than the source's dual formula.
- **Disjoint set union:** Merge adjacent positive cells, aggregate component sums and sizes, then compute contributions. It uses extra arrays and is useful when connectivity is built incrementally.
- **All positive cells connected:** There are no unreachable positive cells, so the only component contribution is zero.
- **Every positive cell isolated:** Each cell's remoteness is the sum of all other cell values; the dual formula counts the same ordered pairs.
- **Single-cell grid:** Its component has no outside cells, yielding zero.
- **Blocked cells:** They are excluded from `cnt`, DFS, and contribution, matching remoteness zero.
- **Visited marker zero:** It is safe because valid cell values are strictly positive and blocked values are negative one.
- **Grid mutation:** Callers needing original values must pass a copy or use a separate visited structure.
- **Deep component:** The exact recursion can fail on standard Python despite correct asymptotic reasoning.
- **Dual contribution identity:** `(total_count - component_size) * component_sum` is valid only after summing over every component, not as the remoteness of that component's own cells.
