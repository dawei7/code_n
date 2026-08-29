## General

**Model gardens as a graph-coloring problem**

Each garden is a vertex. Every bidirectional path is an undirected edge. Assigning one of four flower types is the same as coloring each vertex with one of four colors so adjacent vertices differ.

General graph coloring can require backtracking and can be computationally difficult. This graph has a decisive guarantee: every garden has degree at most three. When a garden is colored, at most three flower types can be forbidden by its neighbors, while four types are available. At least one choice always remains.

This makes a simple greedy pass sufficient in any garden order.

**Build undirected adjacency**

Input garden labels run from one through `n`, while Python list indices run from zero through `n - 1`. For every path `[x, y]`, the code first subtracts one from both labels.

It then appends `y` to `g[x]` and `x` to `g[y]`. Both insertions are necessary because a path constrains both endpoints.

`g` is a `defaultdict(list)`. A garden with no paths automatically receives an empty neighbor list when accessed; no explicit entry is required during construction.

**Color gardens one by one**

`ans` begins as `[0] * n`. Zero means “not colored yet” and is not a real flower type.

For garden `x`, the set

`used = {ans[y] for y in g[x]}`

collects the current assignments of every neighbor. Previously processed neighbors contribute values one through four. Neighbors that appear later in the loop still contribute zero.

Including zero is harmless because the candidate loop checks only flower types one through four. It can be viewed as an ignored sentinel.

The inner loop tries `c = 1, 2, 3, 4` in order. The first value absent from `used` is assigned, and `break` stops the search.

**Why a color is always available**

A garden has at most three neighbors. Even if all three are already colored and all use different types, they forbid only three of the four candidates. The fourth remains available.

If some neighbors are uncolored, fewer real types are forbidden. If several neighbors share a type because they are not adjacent to each other, the set removes duplicates and again forbids fewer than three distinct candidates.

Therefore, the inner loop always finds a color before it ends. The source's existence guarantee follows directly from the maximum-degree condition.

**Why later assignments cannot break earlier edges**

When garden `x` is colored, it differs from every already colored neighbor because their colors are in `used`.

An uncolored neighbor `y` may later receive a color. At that later time, `x` is already colored, and `ans[x]` appears in `y's` used set. Garden `y` will avoid it.

Thus every edge is enforced when its second endpoint is processed. There is no need to revisit or change the first endpoint.

**A formal edge argument**

Take any path between gardens `u` and `v`. Without loss of generality, suppose `u < v`, so the outer loop colors `u` first.

When `v` is processed, `ans[u]` is a completed real type and `u` is in `g[v]`. The set `used` contains `ans[u]`, and the chosen type for `v` is absent from that set. Hence `ans[v] != ans[u]`.

This argument applies independently to every input path. All adjacent gardens end with different types.

**Trace a triangle**

For paths connecting gardens one, two, and three in a cycle:

- Garden one has only uncolored neighbors at its turn, so it takes type one.
- Garden two sees type one at garden one and takes type two.
- Garden three sees types one and two at its two neighbors and takes type three.

The result `[1,2,3]` is valid. Type four was available but unnecessary because the task accepts any valid assignment.

**Trace disconnected paths**

For four gardens with paths `1-2` and `3-4`:

- Garden one takes type one.
- Garden two avoids one and takes two.
- Garden three has no colored neighbor in its component and can reuse one.
- Garden four avoids garden three's one and takes two.

The output can be `[1,2,1,2]`. Reusing flower types across disconnected components is completely valid.

**Why choosing the smallest type is not an optimization claim**

The loop tries types in numeric order only for deterministic simplicity. It does not minimize the number of distinct flower types as a separate objective, and the problem does not ask for such a minimum.

Any available type would preserve the proof. The four-type palette exists to guarantee greedy progress under degree at most three.

**Why no backtracking is needed**

In some coloring problems, an early choice can leave a later vertex with no available color. Here a later vertex has at most three neighbors total, so it can never see all four types forbidden, regardless of earlier choices.

This local degree bound converts every greedy choice into a permanently safe choice.

**Index conversion and output meaning**

Internal index zero represents garden one. After coloring, `ans[x]` is the type for garden `x + 1`. This matches the output contract directly, so no conversion back to one-based labels is necessary.

The returned values themselves already use the required one-through-four numbering.

## Complexity detail

Let `N` be the number of gardens and `P` the number of paths. Building adjacency appends two entries per path and takes `O(P)` time.

The outer loop visits `N` gardens. Across all used-set constructions, neighbor entries are read twice per path, once from each endpoint. The degree is at most three, and checking at most four candidate types is constant work. Total time is `O(N + P)`, matching the manifest.

The adjacency lists contain `2P` integers, and `ans` contains `N` values. Each temporary `used` set has at most four entries including zero. Total auxiliary and output storage is `O(N + P)`, matching the manifest.

## Alternatives and edge cases

- **Backtracking coloring:** It can solve general graphs but explores unnecessary choices here. Four colors and maximum degree three guarantee a greedy answer.
- **Breadth-first or depth-first component coloring:** Traversing components first is also valid, but the numeric-order pass already ensures every edge is handled when its later endpoint is colored.
- **Use neighbor bitmasks:** Encode used flower types in four bits and choose the first zero bit. This reduces small set allocation but does not change complexity.
- **Only three flower types:** Maximum degree three alone does not guarantee a greedy three-coloring for every graph; a four-vertex clique has degree three and requires four colors.
- **Garden with no paths:** Its used set is empty or contains no real type, so it receives type one.
- **Disconnected graph:** Types may be reused freely between components; adjacency lists isolate the constraints.
- **All three neighbors use distinct colors:** Exactly one of the four types remains, and the loop finds it.
- **Several neighbors share a color:** The set deduplicates that color, leaving even more choices.
- **Uncolored neighbors contribute zero:** Zero is outside candidate range one through four and cannot accidentally block a real type.
- **One-based input labels:** Subtracting one on both endpoints is essential before indexing `ans` and adjacency.
- **Bidirectional path:** Adding both adjacency directions ensures whichever endpoint is colored later sees the earlier one.
- **No self-paths:** The source guarantees `x != y`, so a garden is never asked to differ from itself.
- **Any valid answer:** The deterministic smallest-available choice is convenient but not uniquely required.
- **Large `n`:** No recursion or exponential search is used, so the method scales linearly to `10^4` gardens.
