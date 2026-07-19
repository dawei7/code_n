## General
**Place shorter people while taller slots are still empty**

Sort by increasing height and, for equal heights, decreasing `k`. When a person is processed, every unplaced person is at least as tall. Therefore the person's required `k` tall-enough predecessors correspond exactly to `k` empty queue positions before their own slot.

**Represent empty slots with a Fenwick tree**

Initialize every one of the `n` queue positions with value one. Fenwick prefix sums count remaining empty positions. Locate the $(k + 1)$th empty slot by binary lifting over those sums, place the person there, and update that position from one to zero.

**Order equal heights by decreasing k**

Equal-height people count one another. Processing larger `k` first leaves their positions empty when a smaller-`k` peer chooses its slot; after placement, that peer no longer appears as an empty future tall person. This tie order makes the empty-slot rank model exact.

**Why every placed person ends with the requested count**

At placement, exactly `k` empty slots precede the chosen slot, and all eventual occupants of those slots are at least as tall. Already occupied slots contain shorter people, which do not count. Later placements only fill the empty slots without changing order, so the final number of qualifying predecessors remains exactly `k`.

## Complexity detail
Sorting `n` people costs $O(n \log n)$. Each Fenwick rank lookup and removal costs $O(\log n)$, for $O(n \log n)$ total time. The tree and output arrays use $O(n)$ space.

## Alternatives and edge cases
- **Sort tall-first and insert at index k:** is concise and correct, but array insertion can shift $O(n)$ entries per person for $O(n^2)$ time.
- **Segment tree of empty counts:** supports the same `k`th-slot strategy with $O(n \log n)$ time and more tree storage.
- **Try every permutation:** grows factorially and ignores the structure supplied by heights.
- People with $k = 0$ choose the first currently suitable empty slot.
- Equal heights require the specified reverse-`k` tie order.
- Duplicate pairs represent distinct people and must retain multiplicity.
- A one-person queue is already valid.
