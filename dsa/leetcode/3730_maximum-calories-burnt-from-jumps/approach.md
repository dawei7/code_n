## General

**Squared distance rewards jumps between opposite extremes**

All block heights are positive and the start is fixed at zero, below every block. A jump contributes the square of its height difference. Because squaring is convex, one large difference is more valuable than splitting that separation into smaller differences. An optimal route therefore repeatedly crosses between the largest and smallest unvisited heights instead of visiting nearby heights consecutively.

The exact source sorts the heights and keeps two indices:

- `l` points to the smallest unvisited height.
- `r` points to the largest unvisited height.

It begins with `pre = 0`. While at least two heights remain, it jumps first to `heights[r]`, then to `heights[l]`, removes both extremes by moving the pointers inward, and records the low height as the new `pre`.

The resulting order is

$$
\text{largest},\ \text{smallest},\ \text{second largest},\ \text{second smallest},\ldots
$$

If one middle height remains, the final statement jumps to it from `pre`.

**Why the first block is the maximum**

The ground is zero and all heights are positive. Among possible first jumps, the largest height gives the greatest initial square. It also places the route at the high extreme, ready for a maximum-span jump to the smallest remaining height.

Starting from a smaller height would spend that block without gaining the full ground-to-maximum distance. The standard extreme-exchange argument for convex distance shows that moving the largest remaining height into this first position and relocating the displaced height to the later neighbor of the maximum cannot reduce the two affected squared differences. The fixed endpoint outside the height range breaks the symmetry in favor of starting high.

**Why alternating extremes is optimal**

For ordered values `a <= b <= c <= d`, pairing across the range is at least as valuable as pairing nearby values. Expanding squares gives the Monge-style inequality

$$
(d-a)^2+(c-b)^2
\ge
(b-a)^2+(d-c)^2.
$$

The left side uses cross-extreme gaps; the right side uses gaps within the low and high groups. Repeated exchange of adjacent route portions removes any situation in which two still-available extremes are bypassed in favor of closer internal transitions. The route can therefore be transformed, without lowering its score, into one that alternates the high and low ends of the sorted remaining set.

Once the route is at a low chosen extreme, the farthest unvisited point is the current maximum. Once it reaches that maximum, the farthest unvisited point is the current minimum. Choosing those in alternation realizes the cross-extreme form at every layer. With the ground fixed below all values, the high-first version is the maximizing orientation.

This exchange view is important: “choose the farthest next block” is not being used as an unsupported generic greedy rule. On arbitrary metrics it could fail. It works here because points lie on one ordered line and squared distance has the convex cross-extreme inequality.

**How the loop accounts for every jump**

At the beginning of an iteration, `pre` is zero for the first pair or the low extreme visited at the end of the previous pair. The source adds

`(heights[r] - pre) ** 2`

for the jump to the largest remaining height, followed by

`(heights[l] - heights[r]) ** 2`

for the jump from that high to the smallest remaining height.

It then sets `pre = heights[l]` and advances both pointers. Every selected block is used exactly once.

If the original length is odd, the loop eventually reaches `l == r` with one middle block still unvisited. The final statement

`(heights[r] - pre) ** 2`

adds the jump to that remaining block. If the original length is even, the last paired iteration consumes both remaining blocks and leaves `l = r + 1`. In that case `heights[r]` is the low block just visited and equals `pre`, so the same final statement adds zero. For length two, for example, the loop consumes maximum then minimum, and the trailing term is harmless because its two endpoints are identical. No block is given a second positive-cost jump.

For `[1,7,9]`, the sorted extremes produce `9,1`, followed by the remaining seven. The score is

$$
(9-0)^2+(1-9)^2+(7-1)^2=81+64+36=181.
$$

For equal heights, the cross-block differences are zero regardless of order, while the first jump supplies the common height squared.

## Complexity detail

Let `n` be the number of blocks. Sorting takes $O(n\log n)$ time. The two pointers move inward across the array once, so the jump accumulation takes $O(n)$ time. Total time is $O(n\log n)$.

Python's in-place sort may require $O(n)$ temporary memory in the worst case. The pointer and sum variables use $O(1)$ space. Thus the implementation-level auxiliary space bound is $O(n)$, matching the manifest; an in-place comparison-sort model may sometimes describe the explicit state as constant apart from sorting internals.

Squared differences and their sum can exceed 32-bit range, so fixed-width implementations need 64-bit integers.

## Alternatives and edge cases

- **Enumerate every visiting order:** This requires $n!$ permutations. Sorting plus the convex extreme exchange determines an optimal order directly.
- **Visit heights in sorted order:** Consecutive gaps are small and waste the benefit of squaring. Alternating extremes maximizes large cross-range jumps.
- **Start at the smallest height:** Because the fixed ground is below all blocks, this sacrifices the largest possible initial square. The high-first extreme orientation is superior.
- **Alternate extremes but begin low:** This may be optimal for a different free endpoint, but not with the fixed zero start and positive heights.
- **Single block:** The loop is skipped, and the final statement returns its height squared.
- **Two blocks:** The route is maximum then minimum. The bookkeeping's final zero term does not change the correct two-jump score.
- **Odd number of blocks:** One middle height remains after paired extremes and receives the final jump.
- **Duplicate heights:** Sorting retains all positions. Equal-height jumps contribute zero, and every duplicate is still visited exactly once.
- **All heights equal:** The first jump contributes `h²` and every later jump contributes zero.
- **Input mutation:** `heights.sort()` changes the list order. The problem permits arbitrary rearrangement and does not require preserving the input.
- **Ground cannot be revisited:** The sequence includes zero only as `pre` before the first jump; no later transition uses it.
