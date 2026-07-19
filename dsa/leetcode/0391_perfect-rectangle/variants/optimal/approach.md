## General
**Track the only possible outer rectangle**

While scanning the `r` pieces, maintain the minimum lower coordinates and maximum upper coordinates. These extrema define the bounding rectangle that an exact cover would have to fill. Also add every piece's positive area to a running total.

**Cancel corners by parity**

Toggle each of a piece's four corner points in a set: insert an absent point and remove a present one. Along a perfect cover, every interior junction appears an even number of times and cancels. Points on a shared boundary also pair off. Only the four outer bounding corners appear an odd number of times.

**Require both area and corner evidence**

At the end, the unmatched set must equal exactly the bounding rectangle's four corners, and the sum of piece areas must equal its area. Corner parity rules out disconnected boundaries and most local defects; equal area rules out a gap balanced by an overlap that could preserve the same outer corners.

**Why the two conditions are sufficient**

If pieces overlap, their summed area counts the overlap more than once. Equal total and bounding area would then require an equally large gap. Such an overlap-gap arrangement introduces unmatched boundary endpoints away from the four outer corners, contradicting the corner condition. Conversely, a gap without overlap makes total area too small. Therefore satisfying both tests means the bounded region is covered exactly once.

## Complexity detail
Each rectangle contributes constant-time extrema, area, and four set toggles, so processing takes $O(r)$ expected time. The unmatched-corner set can contain $O(r)$ points in an invalid arrangement and therefore uses $O(r)$ space.

## Alternatives and edge cases
- **Sweep line with interval coverage:** can validate every vertical slab in $O(r \log r)$ time and is useful for more general union-area problems.
- **Pairwise overlap checks plus area:** is correct when combined with the bounding area, but checking every rectangle pair costs $O(r^2)$.
- **Rasterize unit cells:** works only for small integer coordinates and scales with coordinate area rather than rectangle count.
- A single valid rectangle is already a perfect cover.
- Rectangles may share edges or corners; only positive-area overlap is forbidden.
- Duplicate rectangles must be rejected as overlap.
- Large or negative coordinates do not change the parity or area reasoning.
