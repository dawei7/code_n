## General

**The groups are connected components, not just direct pairs**

Two strings are directly similar when they are identical or one swap of two positions can make them equal. Group membership is transitive: `A` can share a group with `C` through `B` even if `A` and `C` are not directly similar.

This is exactly an undirected graph problem:

- each string index is a vertex;
- an edge connects two directly similar strings;
- the requested number is the number of connected components.

The solution does not build an explicit adjacency list. It checks every string pair and immediately merges their components with union-find.

**Why at most two mismatched positions is the similarity test**

All input strings have the same length and are anagrams.

If two strings have zero mismatches, they are identical and therefore similar.

If they have exactly two mismatches at positions `p` and `q`, the anagram guarantee forces the two misplaced characters to be exchanged. The character from `p` in one string must appear at `q` in the other, and vice versa. Swapping those two positions makes the strings equal.

One mismatch cannot occur between equal-length anagrams: changing one position would make one character count differ without a compensating mismatch elsewhere.

More than two mismatches cannot be repaired by a single swap, because one swap changes only two positions.

Therefore, under the supplied anagram guarantee,

`sum(s[k] != t[k] for k in range(m)) <= 2`

is necessary and sufficient for direct similarity.

**Check each unordered pair once**

The outer loop processes string `s` at index `i`. The inner loop enumerates `strs[:i]`, so `j` ranges only over earlier indices.

Every unordered pair appears once: when its larger index becomes `i`. A pair is never compared in both orders, and no index is paired with itself.

The generator comparison scans all `m` positions and sums Boolean mismatch indicators. The exact source does not stop early after a third mismatch; it calculates the complete count.

**Union-find represents current groups**

Initially, `p[x] = x` and `size[x] = 1`, so every string is its own component.

`find(x)` follows parent references to the representative root. Path compression assigns traversed nodes directly to that root, making future searches faster.

`union(a,b)` finds both roots:

- if they are already equal, the strings are already connected through previous similarity edges, so no component count changes;
- otherwise, it attaches the smaller component below the larger one and updates the new root's size.

Attaching by size limits tree height, while path compression makes operations nearly constant amortized time.

**Reuse `n` as the component count**

At the start, local variable `n` is the number of strings and therefore the number of singleton components.

When a similar pair is found, `uf.union(i,j)` returns `True` only if two previously different components were actually merged. The condition:

`if similar and uf.union(i, j): n -= 1`

decreases the group count exactly once per successful merge.

If a later similarity edge connects strings already in the same group, `union` returns `False` and `n` does not decrease. This prevents cycles or redundant edges from undercounting components.

**Trace the main example**

For `["tars","rats","arts","star"]`:

- `"tars"` and `"rats"` differ at two positions, so their singleton sets merge and the count drops from 4 to 3.
- `"rats"` and `"arts"` differ at two positions, so `"arts"` joins that component and the count drops to 2.
- `"tars"` and `"arts"` need not be directly similar; union-find already connects them transitively through `"rats"`.
- `"star"` has no direct edge into that component and remains alone.

The final count is two.

**Why the result is correct**

Every directly similar pair is examined, and its endpoints are unioned. Therefore, every path of similarity edges ends inside one union-find set.

Union operations occur only for directly similar pairs, so two union-find sets can merge only when a legitimate graph edge connects them. Union-find consequently represents exactly the graph's connected components.

Starting from one component per vertex and subtracting once per actual merge leaves precisely the number of connected components, which is the requested group count.

## Complexity detail

Let `g = len(strs)` and `\ell` be their common length. There are `g(g-1)/2 = O(g^2)` unordered pairs. The exact mismatch calculation scans all `\ell` positions for each pair, giving `O(g^2\ell)` time.

Union-find operations add `O(\alpha(g))` amortized work per similar pair, dominated by string comparison.

Parent and size arrays use `O(g)` space. The temporary slice `strs[:i]` can contain `O(g)` references at one time, so peak auxiliary space remains `O(g)`. The mismatch generator uses constant iteration state.

## Alternatives and edge cases

- **DFS or BFS on an explicit similarity graph:** It produces the same components but stores up to `O(g^2)` edges. Union-find processes each edge as it is discovered and uses `O(g)` persistent space.

- **Generate every one-swap neighbor:** For shorter strings and many words, hashing generated neighbors can be useful. With both dimensions at most 300, direct pair comparison is straightforward.

- **Stop mismatch counting after three:** This improves constants for dissimilar pairs. The exact source uses `sum` over all positions.

- **Identical strings:** They have zero mismatches and are directly similar. Union merges their indices if needed.

- **Exactly two mismatches:** The anagram guarantee ensures those two characters cross-match and one swap suffices.

- **One mismatch:** It cannot occur for valid anagram inputs, though the `<=2` test would accept it. Correctness relies on the stated anagram contract.

- **More than two mismatches:** One swap cannot repair all differing positions, so no union occurs.

- **Transitive connection:** Strings need not be directly similar to share a final group; a path through other strings is enough.

- **Redundant similarity edge:** `union` detects equal roots and leaves the component count unchanged.

- **One input string:** No pair is checked, and the initial count one is returned.

- **Input order:** Pair enumeration order can change which representative root survives but cannot change the number of groups.

- **No string mutation:** Characters are compared only; union-find stores indices rather than altered strings.
