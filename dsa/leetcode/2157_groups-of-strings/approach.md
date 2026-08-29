## General

Each word contains distinct lowercase letters, so its letter set can be encoded as a 26-bit mask. Connected words become adjacent vertices in a graph, and the requested groups are the graph’s connected components. A disjoint-set union structure maintains those components without constructing explicit adjacency lists.

**Encode words and combine duplicates**

For every character `c`, the code sets bit `ord(c) - ord('a')` in mask `x`. Bitwise OR is appropriate because each letter’s presence matters, not order.

Dictionary `p` stores a parent for each distinct mask, while `size` stores how many original words belong to that mask’s component. If multiple words are anagrams, they have the same mask. `size[x]` increases for each occurrence.

The variable named `n` begins as the total number of words and is used as the current group count. Every duplicate after the first causes `n -= 1` because identical masks already belong to one group. `mx` is updated from `size[x]` so a duplicate-only group can become the largest.

All masks are collected before union processing begins. Reassigning `p[x] = x` for a duplicate is safe because no unions have yet occurred.

**Find component representatives**

`find(x)` follows parent pointers. The recursive assignment `p[x] = find(p[x])` compresses the path, making future searches for nodes on that path faster.

**Merge only masks that exist**

`union(a, b)` first returns if `b not in p`. The algorithm generates many neighboring masks that may have no corresponding word; nonexistent graph vertices must not create groups.

For existing masks, representatives `pa` and `pb` are found. If they differ, `pa` is attached under `pb`, their component sizes are added, `mx` is updated, and the group count `n` decreases by one. If they already share a representative, the edge adds no new merge.

**Generate addition and deletion neighbors**

For every bit `i`, `x ^ (1 << i)` toggles that letter:

- when the bit was absent, toggling adds exactly one letter;
- when present, toggling deletes exactly one letter.

Calling `union` for all 26 toggles therefore covers both permitted operations. Connections are undirected, so processing an edge again from its other endpoint is harmless.

**Generate replacement neighbors**

If bit `i` is present, the nested loop considers every absent bit `j`. The mask

`x ^ (1 << i) | (1 << j)`

first removes letter `i` and then adds letter `j`, representing replacement by a different absent letter.

The rule also says a letter may be replaced by itself. That operation leaves the mask unchanged and creates only a self-connection, which never changes components. Omitting an explicit self-union loses nothing.

**Why DSU components equal the required groups**

Every generated union corresponds to one allowed one-step letter-set operation between two input masks. Thus DSU never connects words from different graph components.

Conversely, every allowed addition, deletion, or effective replacement between existing masks appears among the toggles. DSU merges both endpoints of every graph edge. Transitive chains of connections collapse through repeated unions, so final DSU components are exactly the unique groups.

The returned pair `[n, mx]` contains the component count and largest weighted component size. Weights count original words, not merely distinct masks.

## Complexity detail

Let $d$ be the number of distinct masks, with $d\le n$, and let the alphabet size be $A=26$. Encoding all words costs time proportional to their total characters.

For each distinct mask, the code performs $A$ toggle attempts and, for every present bit, up to $A$ replacement attempts. This is $O(dA^2)$ union attempts. Treating the fixed alphabet as a constant gives linear-scale work in the number of distinct words, with path-compressed disjoint-set operations very close to constant amortized time. The manifest summarizes this as $O(n\alpha(n))$.

The implementation uses path compression but not union by rank or size for choosing the parent, so the strongest textbook inverse-Ackermann guarantee normally associated with both heuristics should be read as the intended DSU bound. With $A=26$ and at most 20,000 inputs, the fixed neighbor enumeration dominates practical behavior.

The parent dictionary and size counter store one entry per distinct mask, using $O(d)$ space, bounded by $O(n)$. Recursive `find` uses parent-chain stack frames, shortened by compression.

## Alternatives and edge cases

- **Explicit graph plus DFS:** Generate the same neighbors into adjacency lists, then run component search. This stores potentially many edges; DSU merges them online.
- **Pairwise word comparison:** Testing all pairs costs $O(n^2)$, avoidable because each mask has only a fixed set of one-operation neighbors.
- **Anagrams:** Identical masks are immediately counted in one weighted component even though no union edge is needed.
- **One word:** It forms one group of size one.
- **Addition edge:** Masks whose bit counts differ by one and whose smaller set is contained in the larger are joined by one toggle.
- **Deletion edge:** It is the same undirected edge viewed from the larger mask.
- **Replacement edge:** Masks of equal size differing in exactly two bit positions are joined by remove-then-add.
- **Replace with itself:** The set is unchanged, so it cannot connect two previously separate masks.
- **Generated missing mask:** `union` returns immediately and does not insert a new DSU node.
- **Repeated edge:** Representatives already match, so group count and size do not change.
- **Transitive grouping:** Words need not be directly connected to every member; DSU joins paths into one component.
- **Duplicate group count:** Every occurrence after the first decrements the initial word count, converting it to a distinct-mask component count before unions.
- **Largest duplicate class:** Updating `mx` during mask construction handles many identical words even before any neighbor union.
- **Dictionary iteration safety:** Union changes parent values but never adds or deletes keys, so iterating over `p.keys()` is safe.
- **Input preservation:** Words are encoded without being sorted or modified.
