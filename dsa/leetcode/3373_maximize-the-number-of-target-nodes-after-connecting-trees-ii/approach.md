## General

**Distance parity is exactly a two-color relation.** Every tree is bipartite. Color an arbitrary root zero, give each neighbor the opposite color, and continue alternating. Along any path, color flips once per edge. Therefore two nodes have:

- even distance when they have the same color;
- odd distance when they have different colors.

This turns a path-parity question into class-size lookup.

**Build both undirected trees.** Helper `build` allocates `len(edges)+1` adjacency lists and inserts each edge in both directions. The tree guarantee means every node is reachable and there is one unique path between every pair.

**Color and count one tree in one DFS.** Helper `dfs` receives current color `d`, writes it into array `c`, and increments `cnt[d]`. Each child receives `d ^ 1`, which toggles zero to one and one to zero. Parent `fa` is skipped to avoid walking back over the undirected edge.

After the traversal:

- `c[v]` is node `v`'s bipartition color;
- `cnt[0]` and `cnt[1]` are the two class sizes.

The numeric choice of which class is zero is arbitrary, but equality and inequality of colors are invariant.

**Count targets already in the first tree.** For queried node `i`, all first-tree nodes at even distance are precisely those sharing `c1[i]`. Their number is `cnt1[c1[i]]`.

Adding one bridge cannot create a shorter alternative path between two first-tree nodes. There is only one bridge into the second tree, so a simple path cannot leave the first tree and return through a different edge. The first-tree parity contribution therefore remains fixed.

**Understand the parity introduced by the bridge.** Connect queried node `i` directly to some second-tree node `j`. For a second-tree node `v`,

$$
\operatorname{dist}(i,v)=1+\operatorname{dist}_2(j,v).
$$

This total is even exactly when the internal second-tree distance is odd. Odd-distance nodes from `j` are those in the color class opposite `c2[j]`.

Thus choosing a bridge endpoint of color zero contributes all color-one nodes, while choosing a color-one endpoint contributes all color-zero nodes.

**Choose the larger second-tree class.** Both color classes are nonempty because the tree has at least two nodes. By selecting `j` from the class opposite the desired target class, the query can add either `cnt2[0]` or `cnt2[1]` second-tree targets. The best reusable contribution is

`t = max(cnt2)`.

It is independent of `i`. Queries are independent and remove their temporary edge, so every query may choose whichever second-tree endpoint realizes the larger class.

**Why connecting directly from `i` is sufficient.** If the bridge starts at another first-tree node `a`, the parity from `i` to the second tree includes `dist1(i,a)` in addition to the bridge. This merely decides which second color class becomes even-distance. Directly connecting from `i` already lets us choose either second-tree class by selecting `j`'s color. Moving the first endpoint cannot offer a class larger than `max(cnt2)` or alter the first-tree target set.

**Assemble each answer.** The list comprehension returns

`t + cnt1[c1[i]]`

for every first-tree node. The two terms count disjoint node sets in different trees, so ordinary addition is exact.

**Trace a star.** In a five-node first-tree star rooted at its center, the center's color class has size one and the four leaves share the other color. The center has one even-distance first-tree target— itself—while any leaf has four: all leaves are mutually distance two. This explains why output entries vary solely by `c1[i]`.

**Why coloring proves optimality.** Every target relation inside a tree is completely determined by color equality. The bridge flips parity once, so it exposes exactly one entire second-tree color class and no mixture. The source counts the fixed first class and chooses the larger obtainable second class, which exhausts every possible connection.

**A valid-input recursion defect.** Both traversals are recursive. A path-shaped tree with $10^5$ nodes creates call depth $\Theta(10^5)$, far beyond normal Python's default recursion limit. The exact source does not raise that limit and does not use an iterative stack, so it can raise `RecursionError` on legal inputs even though the coloring logic is correct.

## Complexity detail

Building and traversing both trees touches every node and edge a constant number of times, giving $O(n+m)$ time. Producing the $n$ answers is included in that bound.

Adjacency lists, color arrays, counts, output, and the theoretical DFS stack use $O(n+m)$ space. The asymptotic bounds match the manifest, but the recursive implementation is not operationally safe at the maximum depth.

## Alternatives and edge cases

- **Iterative DFS or BFS:** It produces the same colors and avoids recursion-limit failure.
- **Run a distance search per query:** It repeats parity work and can cost quadratic time.
- **Connect from a different first node:** It only flips which second color is targeted; direct connection already offers both choices.
- **Balanced bipartition:** Either class supplies the same second-tree contribution.
- **Unbalanced bipartition:** Choose a bridge endpoint in the smaller/opposite class to target the larger class.
- **First-tree query colors:** Nodes of the same color receive identical answers.
- **Self target:** Distance zero is even, so `cnt1[c1[i]]` always includes `i`.
- **Two-node tree:** Both color classes have size one.
- **Star tree:** Center and leaves can have very different first-tree contributions.
- **Path tree:** Colors alternate, but recursive execution is hazardous at large size.
- **Independent queries:** The maximizing endpoint can be reused.
- **Root color choice:** Swapping color labels swaps counts and color entries consistently, leaving answers unchanged.
- **Tree guarantee:** Parent exclusion is sufficient only because cycles are absent.
- **Manifest bounds:** Linear time and space are mathematically correct despite the recursion defect.
- **Required import:** `List` must be available.
