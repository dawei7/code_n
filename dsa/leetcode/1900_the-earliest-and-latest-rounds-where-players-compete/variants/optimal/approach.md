## General

**Represent only current positions, not original labels.** `dfs(l, r, n)` describes a round with `n` surviving players, where the two unbeatable players occupy zero-based row positions `l` and `r`. Everyone remains ordered by original label, so after a round only the number of winners appearing before each special player matters. The identities of ordinary players are irrelevant because their match outcomes are freely selectable.

**Detect their meeting immediately.** Positions `l` and `r` are paired this round exactly when they are symmetric: `l + r == n - 1`. In that case both the earliest and latest possible meeting are the current round, so the state returns `[1, 1]`. This base case runs before outcome enumeration and prevents trying to force both players to win the same match.

**Enumerate all ordinary match outcomes.** There are `m = n >> 1` matches formed by front/back pairs. Integer mask `i` ranges through `0` to `(1 << m) - 1`. For pair number `j`, a set bit selects front position `j` as winner; an unset bit selects back position `n - 1 - j`. Boolean list `win` records advancing positions. If `n` is odd, middle position `m` advances automatically.

This enumeration includes every possible choice among ordinary players. It also includes redundant mask choices for matches involving a special player, because those results are overwritten next. Redundancy costs time but does not omit or falsify any reachable next state.

**Force the two best players to survive.** The assignments

`win[n - 1 - l] = win[n - 1 - r] = False`

clear their opponents, and `win[l] = win[r] = True` marks both special players as winners. Since the base case already excluded a direct meeting, these positions belong to different matches. This enforces the guarantee that each beats any ordinary opponent regardless of the mask.

**Translate winners into next-round positions.** Winners are lined up in original order, which is the same left-to-right order of current positions. Variable `c` counts winners encountered during a scan. When scan index reaches `l`, `a = c` records how many winners precede the first special player. Likewise `b = c` at `r`. After all positions, `c` is the next round's player count. Therefore `dfs(a, b, c)` is exactly the state reached by this outcome.

Notice that `a` and `b` are captured before incrementing `c` for the special player itself. They are consequently zero-based positions, consistent with the recursive state definition.

**Combine earliest and latest futures.** Recursive result `[x, y]` counts rounds starting with the next round. The current round adds one. `res[0]` keeps the minimum `x + 1` across all outcome masks, while `res[1]` keeps the maximum `y + 1`. Thus ordinary winners are chosen once to make the meeting as early as possible and separately to delay it as long as possible.

**Memoize equivalent tournament states.** Many different masks lead to the same triple `(a, b, c)`. The module-level `@cache` evaluates each distinct state only once, returning its stored earliest/latest pair thereafter. State meaning depends only on positions and survivor count, so this merging of histories is valid.

**Convert the public one-based positions.** The method calls `dfs(firstPlayer - 1, secondPlayer - 1, n)`. Initial labels equal initial row positions, and subtraction changes them to the zero-based convention used by symmetric indexing. The recursive ordering always preserves `l < r` because winners remain in original order.

**Why exhaustive outcomes prove correctness.** Every legal round chooses one winner from each ordinary match, automatically advances a middle player, and forces the two special players to win. One mask represents that choice, and the winner scan derives its exact next state. Conversely, every mask after special-player overrides describes a legal round. Recursion therefore covers every possible tournament history. Taking minima and maxima across this complete set yields precisely the earliest and latest meeting rounds.

## Complexity detail

The exact source is exponential, despite the polynomial labels in the variant manifest. A state with `n` players enumerates $2^{\lfloor n/2\rfloor}$ masks. For each mask it initializes/scans arrays and matches in $O(n)$ time. Memoization limits repeated states; at a fixed survivor count there are $O(n^2)$ possible special-position pairs, and only $O(\log n)$ survivor counts arise as the field halves.

A conservative bound is $O(n^3 2^{n/2})$ time, with the exponential work dominated by larger rounds; a more refined sum over shrinking round sizes is smaller but remains exponential. It is not the manifest's $O(n^5)$ executed behavior. The constraint $n\le28$ is what makes mask enumeration plausible.

Cached states occupy up to $O(n^2\log n)$ pairs in a broad bound. Each active call temporarily allocates a length-$n$ `win` list, and recursion depth is $O(\log n)$. This also differs from a simple manifest $O(n^2)$ label when all distinct survivor sizes and temporary state are counted.

The cache is module-level and is not cleared after a call. Results are pure functions of `(l, r, n)`, so reuse across calls is semantically safe and can retain memory between invocations.

## Alternatives and edge cases

- **Combinational position DP:** Count possible winners in regions around the two special players instead of enumerating every match mask. This yields polynomial state transitions and is the intended route to the manifest-style bound, but it is not the checked-in source.
- **Simulate original player labels:** Keeping complete winner lists for every history creates enormous duplication. Current positions are sufficient because original ordering is preserved.
- **Players paired immediately:** The symmetric-position base case returns `[1, 1]` before any forced-winner override.
- **Odd number of players:** The middle position is marked as an automatic winner. If it is a special player, setting it true again is harmless.
- **Masks involving a special match:** Their chosen ordinary winner is overwritten so the unbeatable special player advances. Different mask bits may then lead to duplicate next states, which caching absorbs later.
- **Earliest equals latest:** Some configurations force the meeting round even when it is not round one; minimum and maximum converge naturally.
- **One-based versus zero-based:** The public arguments must be decremented once. The meeting equation `l + r == n - 1` is specifically zero-based.
- **Input limit:** Exponential enumeration relies strongly on `n <= 28`. It should not be described as a scalable polynomial algorithm.
- **Persistent cache:** Sharing cached pure states is correct, but long-lived processes retain entries. Clearing would control memory at the cost of losing cross-call reuse.
