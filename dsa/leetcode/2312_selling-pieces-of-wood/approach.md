## General

**Ask the same optimization question for every rectangle size**

After any sequence of legal cuts, each remaining piece is itself a rectangle with some height `h` and width `w`. The best revenue obtainable from that piece depends only on those two dimensions. It does not depend on where the piece came from or on the order of cuts that produced it.

The memoized function `dfs(h, w)` therefore has a precise meaning:

> the maximum revenue obtainable from one `h x w` piece using any number of full horizontal or vertical cuts and selling any resulting pieces whose ordered dimensions appear in `prices`.

The dimensions are ordered. `dfs(2, 3)` describes height 2 and width 3, while `dfs(3, 2)` describes height 3 and width 2. They are not automatically interchangeable because rotation is forbidden by the wood grain.

**Start with the option of making no cut**

The dictionary `d` maps an offered height to another dictionary from width to sale price. For every input triple `[h, w, p]`, the assignment `d[h][w] = p` records the direct price for exactly that orientation.

When `dfs(h, w)` begins, it initializes

`ans = d[h].get(w, 0)`.

If this shape has a listed price, selling the whole piece immediately is one valid plan. If it has no listed price, making no cut and earning zero is still a legal baseline because the statement does not require every piece to be sold. Later cut options may improve this baseline.

The input guarantees that listed shapes are pairwise distinct, so there is no conflict between multiple prices for the same ordered dimensions. The use of `defaultdict(dict)` means that looking up an unseen height produces an empty inner dictionary; `get(w, 0)` then supplies the zero baseline.

**Try every different full horizontal cut**

A horizontal cut across the entire width splits an `h x w` rectangle into pieces `i x w` and `(h - i) x w`. Once the first cut is made, the two pieces can be optimized independently. Their best combined revenue is

`dfs(i, w) + dfs(h - i, w)`.

The first loop tries `i` from 1 through `h // 2` and keeps the maximum candidate. It does not need to try larger values. A cut at `i` and a cut at `h - i` create the same unordered pair of rectangles; reversing which piece is called “top” does not change their independent revenues or sum. Restricting to half the positions removes this duplicate work without losing a distinct partition.

If `h` is even, `i = h // 2` creates two equal-height pieces and is included once. If `h = 1`, the range is empty because no positive horizontal split exists.

**Try every different full vertical cut**

The second loop applies the same reasoning to width. Cutting after `i` columns creates `h x i` and `h x (w - i)`, so its candidate is

`dfs(h, i) + dfs(h, w - i)`.

Only positions through `w // 2` are required because the complementary positions produce the same two widths in reverse order. If `w = 1`, there is no legal vertical split and this loop is empty.

Every transition represents a cut across the entire current piece, exactly matching the guillotine-cut rule. The recursion never combines shapes through an illegal partial or L-shaped cut.

**Why considering only the first cut covers every plan**

Any plan for an `h x w` piece has one of two forms. It either makes no cut before selling or discarding the whole piece, or it has a first cut. That first cut must be horizontal at some positive height `i < h` or vertical at some positive width `i < w`.

For a horizontal first cut, all later work takes place independently inside the two resulting rectangles. By definition, `dfs(i, w)` is at least as profitable as the plan's choices for the first child, and `dfs(h - i, w)` is at least as profitable as its choices for the second. Thus the recurrence's candidate for that first cut is at least as large as the revenue of the original plan. The vertical case is identical.

Conversely, every candidate evaluated by the recurrence is achievable: make the represented full cut, then use the optimal plans returned for its two children. The direct-price baseline is also achievable by selling without cutting, and zero is achievable by not selling an unpriced remainder.

The recurrence therefore compares an achievable candidate corresponding to every possible form of an optimal plan. Its maximum is exactly the best revenue for `h x w`. Since every recursive child has a smaller height or width, this reasoning bottoms out at rectangles that cannot or need not be cut. Calling `dfs(m, n)` consequently gives the answer for the original board.

**Memoization makes repeated subboards cheap**

Different cutting sequences often produce the same dimensions. For example, a `2 x 3` rectangle might arise after a horizontal cut of one board or a vertical cut of another. Without caching, the recursion would solve its entire cutting problem again each time.

The `@cache` decorator stores the result for each ordered pair `(h, w)`. The first call explores all direct-sale and split options; every later call with the same dimensions returns the stored maximum. Caching is valid because prices and dimensions do not change during the recursion, so `dfs(h, w)` is a pure value for the lifetime of this method call.

**Rotation remains forbidden throughout**

The price lookup uses `d[h].get(w, 0)` and never also checks `d[w][h]`. Horizontal and vertical transitions preserve the actual orientation of their child rectangles. Therefore a listed `1 x 4` price is not applied to a `4 x 1` piece unless that second orientation has its own listing.

## Complexity detail

There are at most `m \cdot n` distinct ordered states `(h, w)` with `1 <= h <= m` and `1 <= w <= n`. Memoization evaluates each state at most once. State `(h, w)` tries `\lfloor h/2 \rfloor` horizontal cuts and `\lfloor w/2 \rfloor` vertical cuts. Summed over all states, this is `O(m^2n + mn^2) = O(mn(m+n))` time.

The cache stores up to `mn` integer results, giving `O(mn)` space. The price dictionary stores one entry per listed shape; because shapes are distinct and lie within the `m` by `n` dimension domain, it also uses at most `O(mn)` space. The recursive call stack can follow a sequence that reduces one dimension at a time and may reach `O(m+n)` depth, which is dominated asymptotically by `O(mn)` storage for nontrivial dimensions.

The returned revenue may exceed a fixed 32-bit range after selling many pieces, but Python integers expand automatically. Each arithmetic transition is constant time under the bounded problem values in the usual analysis.

## Alternatives and edge cases

- **Bottom-up two-dimensional dynamic programming:** Fill `dp[h][w]` in increasing height and width using the same direct-price and cut recurrence. It has the same asymptotic time and space and avoids recursion, but the memoized version computes only states actually reached from `(m, n)`.
- **Try every cut position instead of only half:** This remains correct but evaluates each unordered two-piece split twice, once from each side. The complementary halves always have the same summed optimal revenue.
- **Greedily sell the highest price-per-area shape:** A locally attractive density may not tile the current dimensions under full-cut restrictions, and a combination with lower individual density can yield greater total revenue. The state recurrence respects geometry and compares complete plans.
- **Treat rotation as free:** Looking up `d[w][h]` for an `h x w` piece would violate the explicit grain rule. Ordered dimension keys prevent this.
- **Require every final piece to have a price:** The contract allows unsold shapes. A zero baseline lets the method discard an unprofitable remainder when that enables valuable pieces elsewhere.
- **A directly priced rectangle that is better uncut:** The initial `ans` preserves its sale value, and no cut replaces it unless the two optimized children earn more.
- **A directly priced rectangle that is better cut:** Direct sale is only one candidate. The loops correctly replace it when a split gives a larger sum.
- **No direct price for the original board:** The zero lookup does not imply the answer is zero. The recursion still tries all cuts and can assemble revenue from smaller priced shapes.
- **Height or width equal to one:** Cuts in that dimension are impossible, so its loop is empty. Cuts along the other dimension remain available.
- **Equal halves:** An even dimension's central cut is included once by the inclusive `dimension // 2` endpoint.
- **Multiple pieces of the same shape:** Separate recursive branches may return the same cached state many times and add its revenue repeatedly. Caching the value does not restrict how many physical pieces of that shape may be sold.
- **Pairwise-distinct listed shapes:** The input guarantee means `d[h][w] = p` never has to decide between duplicate offers. If duplicates existed, the dictionary assignment would keep only the last one rather than explicitly taking the maximum.
- **Input mutation:** The method reads `prices` and builds a separate dictionary. It does not reorder or modify the input list.
