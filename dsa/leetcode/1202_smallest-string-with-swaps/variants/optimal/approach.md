## General

View string indices as vertices of an undirected graph and each allowed swap pair as an edge. Because an edge may be used any number of times, characters can travel along paths. Thus every connected component can rearrange its characters arbitrarily, while characters can never move between different components.

The solution finds components with a disjoint-set union structure, collects each component’s characters, sorts them, and assigns the smallest available character to each component index as indices are visited from left to right.

**Build connectivity with parent links**

The parent list `p` begins as `[0, 1, ..., n - 1]`, so every index starts in its own component.

`find(x)` follows parent pointers to a root whose parent is itself. During the recursive return, `p[x] = find(p[x])` performs path compression, redirecting visited vertices straight to the root.

For every allowed pair `[a, b]`, the code executes `p[find(a)] = find(b)`. This connects the root of `a`’s component to the root of `b`’s component. Once all pairs are processed, two indices have the same representative exactly when a path of allowed swaps connects them.

The union step does not use rank or component size. Path compression still shortens traversed paths, but the exact data structure should not be credited with the strongest inverse-Ackermann bound that requires a balancing heuristic as well.

**Why a connected component permits any permutation**

Along one graph edge, the two endpoint characters can swap directly. Along a path, a character can be moved step by step to another vertex. More generally, swaps along edges of a connected graph generate every permutation of the component’s positions. One constructive view is to use a spanning tree and move desired characters along tree paths.

Therefore, only the multiset of characters in each component matters; their original positions inside that component do not restrict the final arrangement.

**Collect and reverse-sort component characters**

The loop over `enumerate(s)` finds each index’s root and appends its character to `d[root]`. Afterward, every dictionary list contains exactly the characters movable among that component’s indices.

Each list is sorted with `reverse=True`, putting its largest character first and smallest character last. This direction is chosen because Python list `pop()` removes the last element in $O(1)$ amortized time. The code can therefore retrieve the smallest remaining character efficiently.

**Fill positions in global index order**

The result expression visits indices from zero through `n - 1`. At position `i`, it finds the component root and pops that component’s smallest remaining character.

Lexicographic order is decided at the first position where two strings differ. Assigning the smallest available character to the earliest index of each component is therefore optimal. A character from another component cannot be used there, so components do not compete for the same position.

After the earliest component index receives its smallest character, the same reasoning applies to the next index with the remaining multiset. This greedy assignment produces the lexicographically smallest arrangement for each component and hence for the whole string.

For `s = "dcab"` with pairs connecting zero to three and one to two, component zero-three has characters `d` and `b`, assigned as `b` at index zero and `d` at index three. Component one-two has `c` and `a`, assigned as `a` then `c`. The result is `"bacd"`.

**Why dictionary roots remain valid during output**

All unions finish before characters are grouped. Later `find` calls may compress paths but do not change a component’s ultimate representative because there are no more unions. Thus the root keys used to build `d` remain the same keys used while popping.

Every original character is appended once and popped once. Components never exchange characters, and every component’s earliest positions receive its smallest choices. The joined result is both reachable and lexicographically minimal.

## Complexity detail

Let $n$ be the string length and $p$ be the number of swap pairs.

The code uses path compression but no union-by-rank or union-by-size. A conservative standard bound for a sequence of arbitrary linking operations with path compression alone is logarithmic amortized overhead per operation, so the DSU work is safely bounded by $O((n+p)\log n)$.

Sorting component character lists costs

$$
\sum_C O(\lvert C\rvert\log\lvert C\rvert)\leq O(n\log n).
$$

The final pops and join are linear aside from the find calls. A safe total bound for the exact implementation is $O((n+p)\log n)$. With a balancing heuristic added to union, DSU work would improve to $O((n+p)\alpha(n))$, matching the stronger editorial-style bound, while sorting would still contribute $O(n\log n)$.

The parent list, component dictionary lists, and output construction each use $O(n)$ space. Sorting lists in Python may also use linear temporary memory across the largest component. Overall auxiliary and output storage is $O(n)$.

## Alternatives and edge cases

- **Balanced DSU:** Track rank or size and attach the smaller tree beneath the larger. Together with path compression, this provides the inverse-Ackermann amortized bound.
- **DFS or BFS components:** Build an adjacency list, traverse each component, sort its indices and characters, and assign them together. This uses $O(n+p)$ graph storage.
- **No swap pairs:** Every index is a singleton component. Each list contains one character, so the original string is returned.
- **One fully connected component:** All characters can be permuted, and the result is the globally sorted string.
- **Duplicate characters:** Component lists preserve multiplicity; equal values are popped into consecutive eligible positions as needed.
- **Indirect swaps:** A path is enough. The DSU merges transitive connectivity even when an endpoint pair is not listed directly.
- **Reverse sort plus `pop`:** Sorting ascending and popping from the end would assign largest characters first and be wrong. Reverse sorting makes the end hold the smallest.
- **Input string immutability:** The method constructs a new string and does not attempt to modify `s` in place.
- **Representative stability:** Character grouping occurs only after all unions, so later path compression cannot move a component to a different root.
- **Recursive `find` depth:** Arbitrary unbalanced linking can create deep parent chains before compression. A balanced union or iterative find can reduce operational recursion risk.
