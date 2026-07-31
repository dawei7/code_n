## General

Treat equal coordinate triples as one available point because the contract forbids pairing identical coordinates. Store every available triple in the hash set `known`, and store only the points first produced in the latest generation in a second set, `frontier`.

At the start of generation $k\ge1$, a pair needs to be considered for the first time exactly when at least one endpoint belongs to generation $k-1$:

- a pair whose endpoints are both older was already available and processed in an earlier generation;
- a pair involving a point produced during generation $k$ is not legal until the next generation because production is simultaneous.

Therefore pair each frontier point with every point in the snapshot of `known`. Skip a point paired with itself. When both endpoints belong to the frontier, use their tuple order to process that unordered pair only once. Insert every midpoint not already in `known` into a separate `produced` set; do not mutate `known` while the generation is being formed.

If `target` is in `produced`, the current generation is the answer. Otherwise, an empty `produced` set means the reachable closure is stable and the target is impossible. For a non-empty result, add the complete produced set to `known`, make it the next frontier, and advance the generation.

Initially, `known` and `frontier` are exactly generation $0$. By induction, each loop enumerates precisely the pairs that first become legal in that generation and delays every new midpoint until the next loop. Thus `produced` is exactly the set of previously unseen points in the source-defined generation. The first target detection is its minimum generation, and stabilization proves that no ungenerated point can ever appear later.

## Complexity detail

Creating the initial set takes $O(n)$ time. Across the whole simulation, every unordered pair among the $U$ reachable points is processed at most once, so midpoint work totals $O(U^2)$. Hash-set membership and insertion are expected $O(1)$ operations. The total expected time is $O(n+U^2)$ and the sets use $O(U)$ auxiliary space. Here $U\le343$.

## Alternatives and edge cases

- **Rescan every available pair each generation:** This direct simulation is correct but repeats pairs whose endpoints are both old, taking $O(GU^2)$ time for $G$ generations.
- **List-based duplicate detection:** Keeping points in lists and linearly checking whether each midpoint is known preserves the generation semantics but can take $O(U^3)$ time.
- **Asynchronous insertion:** Adding a midpoint to the available collection immediately lets it participate in its own generation and can return a generation that is too small.
- **Identical coordinates:** Never pair a point with itself, even if the same midpoint could be produced by a different legal pair.
- **Duplicate production:** Many pairs may produce the same midpoint; the produced set must keep only one coordinate triple without changing its generation.
- **Initial target:** Check generation $0$ before attempting to form any pair.
- **Singleton input:** Unless its sole point is the target, no legal pair exists and the answer is `-1`.
- **Floored coordinates:** Apply integer floor independently to all three coordinate sums.
- **Stable closure:** Once a generation contributes no unseen point, repeating the same pairs cannot create anything later.
