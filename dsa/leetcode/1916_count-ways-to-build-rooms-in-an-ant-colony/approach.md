## General

**View prerequisites as a rooted tree.** Every room except zero has exactly one direct previous room, and all rooms are reachable from zero. The plan therefore forms a rooted tree. Building a room requires its parent first, while rooms in different child subtrees become independent once their common parent has been built.

**Create child adjacency.** For each room `i >= 1`, the source adds its parent to `ingoing[i]` and adds `i` to `outgoing[parent]`. Only `outgoing` is later used; `ingoing` is redundant state. Sets hold children, although each parent-child edge appears only once.

**Let recursion return subtree size.** `recurse(i)` returns the number of nodes in the subtree rooted at `i`. A leaf has no children and returns one. For an internal room, every recursive child call `cn = recurse(v)` gives that child's subtree size and, as a side effect, has already multiplied `ans[0]` by all ordering choices inside that subtree.

**Interleave completed child-subtree orders.** After room `i` itself is built, valid orders from different child subtrees can be interwoven arbitrarily as long as each subtree's internal parent-before-child order is preserved. If previously processed child subtrees contain `nodes_in_tree` rooms and the next contains `cn`, choose which `cn` of the combined positions belong to the new subtree:

$$
\binom{\textit{nodes\_in\_tree}+cn}{cn}.
$$

The remaining positions automatically hold the earlier subtree sequence. Multiplying by this binomial counts every stable interleaving.

**Why repeated merging produces the multinomial count.** Combining child sizes one at a time yields

$$
\binom{s_1+s_2}{s_2}
\binom{s_1+s_2+s_3}{s_3}\cdots,
$$

whose product equals the multinomial coefficient for distributing all positions among child subtrees. Therefore iteration order of the child set does not change the final count. The first child needs no combination factor, which is why multiplication occurs only when `nodes_in_tree != 0`.

**Accumulate internal and external choices together.** Each child recursion updates shared one-element list `ans` with arrangements inside that child. The parent then multiplies the ways to interleave those already-counted arrangements. Using a list allows the nested function to mutate the outer value without a `nonlocal` declaration.

**Exclude the parent from interleaving.** Room `i` must precede every descendant, so it has a fixed first position within its subtree. `nodes_in_tree` sums only child subtree sizes. After processing them, the function returns `nodes_in_tree + 1` to include `i` for its own parent's combination.

**Apply the modulus after each product.** Binomial coefficients and total orders can be enormous. The source multiplies and reduces modulo $10^9+7$ at every merge. Modular reduction preserves the final product remainder. `comb` itself computes the exact binomial before reduction.

**Trace two chains below the root.** If root zero has child subtrees of sizes two and two, each chain has one internal order. Their four descendant positions can be interleaved in `comb(4,2)=6` ways, matching the second example's structure.

**Why the count is exact.** Recursion counts every valid internal child order by induction. Any parent-subtree order consists uniquely of one valid order from each child plus a choice of their interleaving positions. The binomial product counts exactly those position choices, and the parent remains first. Induction from leaves proves the root result.

No order is counted twice because reading a finished sequence and selecting the positions occupied by each child subtree reconstructs one unique set of interleaving choices. Likewise, no valid order is missed: removing the parent and separating descendants by their first child recovers valid internal sequences that recursion already counted.

## Complexity detail

The graph construction and DFS visit $n$ rooms and $n-1$ edges, giving $O(n)$ structural work under the conventional unit-cost view of arithmetic and combinations. The implementation calls `comb` for child merges; exact big-integer cost depends on operand sizes and is not literally constant, though the manifest reports $O(n)$.

Adjacency sets store $O(n)$ edges, and recursion can reach depth $O(n)$ for a chain. Auxiliary space is $O(n)$. A chain of $10^5$ rooms can exceed Python's default recursion limit, so an iterative postorder implementation is safer at the maximum constraint.

## Alternatives and edge cases

- **Factorial formula:** Compute subtree sizes and use the tree linear-extension formula involving factorials and inverse factorials modulo the prime. This avoids large exact `comb` values.
- **Iterative postorder:** Preserves the same recurrence while avoiding recursion-depth failure.
- **Single chain:** Every parent must precede its only child, every combination factor is one, and the answer is one.
- **Star rooted at zero:** All non-root rooms are independent, giving $(n-1)!$ orders.
- **Child iteration order:** Sets are unordered, but sequential binomial products equal the same multinomial coefficient.
- **Unused `ingoing` map:** It consumes space but does not influence execution after construction.
- **Room zero:** It is already the unique root and must be first; recursion correctly excludes it from sibling interleavings.
- **Modulo timing:** Reducing the running product is safe, but exact `comb` is still computed before reduction.
- **Deep plan:** Correct mathematics does not prevent Python `RecursionError` on a long parent chain.
- **Sibling independence:** Descendants from different child subtrees have no prerequisite edges between them, which is precisely why arbitrary stable interleavings are legal.
