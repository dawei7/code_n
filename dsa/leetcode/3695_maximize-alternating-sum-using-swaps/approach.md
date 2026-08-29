## General

The alternating sum assigns a sign to each position:

- an even index contributes its value positively;
- an odd index contributes its value negatively.

Allowed swaps concern positions, and each listed swap may be used any number of times in any order. Treat indices as vertices of an undirected graph and allowed pairs as edges. Values can be rearranged freely inside one connected component, but can never cross between different components.

The algorithm therefore has two layers:

1. use disjoint-set union to find the connected components of swappable indices;
2. inside each component, place its largest values into even-indexed positions and its smallest values into odd-indexed positions.

**Why connected indices allow arbitrary permutations**

A listed edge lets the values at its two endpoints be transposed. Because swaps may be repeated and reversed, a value can be moved along a path through the component.

More strongly, edge transpositions of a connected graph can generate any permutation of values over its vertices. One way to see this is to use a spanning tree: a desired value can travel along tree edges to its target position, and repeated such moves can arrange every position. Intermediate disruptions can be repaired because every swap is reversible.

Thus direct adjacency is not required. If index zero can swap with two and index two can swap with one, values can ultimately move among all three indices. This transitive freedom is why connected components, rather than individual swap pairs, are the correct units of optimization.

No operation connects two different components, so their sets of values remain independent. The total alternating sum is the sum of each component's contribution, allowing every component to be optimized separately.

**Building components with disjoint-set union**

Initially, every index is its own root:

`parent = list(range(len(nums)))`

and every component has size one.

The local `find` function follows parent pointers until it reaches a root. During this walk, it applies path halving:

`parent[node] = parent[parent[node]]`

which moves the current node two levels upward. Repeated searches make the trees increasingly flat and future root queries faster.

For each allowed pair `left, right`, the source finds both roots. If they already match, the edge lies inside one known component and no merge is needed.

Otherwise, union by size attaches the smaller root below the larger root. The `size` entry of the surviving root is increased accordingly. Combining union by size with path compression gives almost constant amortized work per operation.

**Collecting exactly the information each component needs**

After all unions, the source scans the original positions. For index `index` with `value`, it finds the final root and performs two updates:

- append `value` to `values_by_root[root]`;
- if `index` is even, increment `even_positions_by_root[root]`.

For a component, it is unnecessary to remember which particular even position receives which selected large value. Every even position has coefficient $+1$, and every odd position has coefficient $-1$. Only the number of positive slots matters.

Suppose a component contains $c$ positions and $E$ of them are even. It necessarily has $c-E$ odd positions. Its values may be assigned to these sign slots in any order.

**Why the largest values belong to positive slots**

Assume a current assignment places value $a$ in a positive slot and a larger value $b>a$ in a negative slot. Their contribution is:

$$
a-b.
$$

Swapping them is reachable within the component and changes their contribution to:

$$
b-a.
$$

The improvement is:

$$
(b-a)-(a-b)=2(b-a)>0.
$$

Therefore, an optimal assignment cannot leave a larger value in a negative slot while a smaller value occupies a positive slot. Repeatedly correcting every such inverted pair places the $E$ largest component values into even positions and all remaining values into odd positions.

Values assigned among slots with the same sign can appear in any order because exchanging two positive slots or two negative slots does not change the sum.

**How the sorted list implements that assignment**

The source sorts each component's values in ascending order. If its length is $c$ and it has `positive_count = E` even positions, then:

`positive_start = len(values) - positive_count`

is the index where the largest $E$ values begin.

The slice `values[positive_start:]` contains exactly the values assigned positive signs.

Let $P$ be the sum of those largest values and let $T$ be the sum of every value in the component. The negatively assigned values sum to $T-P$. The component contribution is:

$$
P-(T-P)=2P-T.
$$

That is the source expression:

`2 * sum(values[positive_start:]) - sum(values)`.

The formula also handles extreme sign distributions.

- If every component position is even, `positive_count == len(values)`, the slice is the whole list, and the contribution is $T$.
- If every component position is odd, `positive_count == 0`, the slice is empty, and the contribution is $-T$.

**Tracing a connected example**

For `nums = [1, 2, 3]` and swaps `[[0, 2], [1, 2]]`, all indices form one component. Indices zero and two are even, so there are two positive slots and one negative slot.

The sorted values are `[1, 2, 3]`. The two largest, $2$ and $3$, receive positive signs, while $1$ receives the negative sign. The maximum contribution is:

$$
2+3-1=4.
$$

The actual order can be `[2,1,3]` or `[3,1,2]`; both have the same optimized sign assignment.

For `nums = [1,2,3]` with only swap `[1,2]`, index zero is an isolated positive component contributing $1$. The other component has one negative slot at index one and one positive slot at index two. Assigning $3$ positively and $2$ negatively gives $1-2+3=2$, the same value as performing no swap.

**Why summing component optima is globally optimal**

Every reachable arrangement preserves the multiset of values in each connected component. The exchange argument gives the largest possible signed contribution for that fixed multiset and sign count.

Operations in one component cannot alter positions or values in another. Therefore, choosing an optimal assignment independently in every component is simultaneously reachable, and the sum of those component maxima is an upper bound attained by a global arrangement. The accumulated `answer` is the maximum alternating sum.

## Complexity detail

Let $n$ be the number of values and $m$ be `len(swaps)`.

Disjoint-set initialization takes $O(n)$ time. The union loop and later root queries perform $O(n+m)$ `find` operations. With path compression and union by size, their amortized total is:

$$
O((n+m)\alpha(n)),
$$

where $\alpha$ is the inverse Ackermann function and grows so slowly that it is effectively constant for practical inputs.

If component sizes are $c_1,c_2,\ldots$, sorting costs:

$$
\sum_i O(c_i\log c_i)\le O(n\log n).
$$

Collecting and summing component values is $O(n)$. The precise overall bound is:

$$
O((n+m)\alpha(n)+n\log n).
$$

The manifest's `O((n + m) log n)` time is a valid coarser upper bound, though it does not expose the near-constant union-find cost.

The `parent` and `size` arrays use $O(n)$ space. Component value lists collectively store all $n$ input values, and the root dictionaries contain at most $n$ keys. Sorting and slicing can use additional linear temporary storage. Total auxiliary space is $O(n)$.

The alternating sum can have magnitude near $n\cdot10^9$, so fixed-width implementations should use 64-bit arithmetic. Python integers handle it automatically.

## Alternatives and edge cases

- **Apply beneficial listed swaps greedily:** A locally improving direct swap can prevent recognizing a better sequence of swaps, and values can travel through intermediate vertices. Component-level permutation freedom is the correct abstraction.
- **Build graph components with DFS or BFS:** An adjacency list plus traversal also finds components in $O(n+m)$ time and space. Disjoint-set union avoids storing every edge after processing it.
- **Sort all values globally:** Values cannot cross disconnected components, so a global rearrangement may be unreachable and overestimate the answer.
- **Use a heap per component:** Selecting the largest $E$ values with a heap is possible, but sorting also identifies the remaining negative values and remains within $O(n\log n)$.
- **No allowed swaps:** Every index is a one-value component. Even positions contribute positively and odd positions negatively, reproducing the original alternating sum.
- **Component containing only one parity:** Rearrangement inside it cannot change the contribution because all its positions have the same sign.
- **Equal values:** Their relative assignment is irrelevant; sorting and the exchange argument allow equality without requiring a strict order.
- **Repeated or cyclic connectivity:** An edge whose endpoints already share a root is skipped. Extra paths do not enlarge the component twice.
- **Indirect swaps:** Two indices need not appear in one listed pair. Any path between them places them in the same permutation component.
- **Input order:** The source sorts copied component lists, not `nums` itself, so the original input array is not reordered.
