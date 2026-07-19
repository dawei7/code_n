## General
**Replace each room height by its reachable clearance**

A tall room behind a short doorway cannot accept a tall box. For room `i`, the largest box that can reach it is therefore limited by the minimum room height from the entrance through `i`. Scan from left to right and record these prefix minima in `clearance`. This sequence is non-increasing, so reading it from the deepest room back toward the entrance visits capacities from smallest to largest.

**Give the tightest useful room the smallest remaining box**

Sort the boxes in ascending order and keep an index at the smallest box not yet placed. Visit rooms from deepest to shallowest. If the current smallest box fits the room's effective clearance, place it and advance the index. If it does not fit, no remaining box fits because all remaining boxes are at least as tall, so this room stays empty.

This choice is safe by exchange: whenever a feasible arrangement uses a taller remaining box in the current room, replacing it with the smallest remaining box preserves that placement and leaves a no-taller set of boxes for all later rooms. Conversely, when the smallest box cannot fit, the room cannot contribute to any feasible arrangement. Applying these observations room by room proves that the greedy count is maximal.

## Complexity detail
Sorting $B$ box heights costs $O(B \log B)$ time. Building the $W$ prefix clearances and matching rooms to boxes each take $O(W)$ time, for $O(B \log B + W)$ total time.

The sorted copy holds $B$ heights and the clearance array holds $W$ values, so auxiliary space is $O(B + W)$. The input lists are not modified.

## Alternatives and edge cases
- **Sort effective room capacities:** after computing prefix minima, sort or reverse those capacities and greedily match them against sorted boxes. Reversal is sufficient because prefix minima are already non-increasing; sorting them again adds unnecessary work.
- **Repeated insertion simulation:** try each box and scan the warehouse for its deepest reachable empty room. This can be correct, but repeated scans require $O(BW)$ time.
- **Heap-based selection:** process rooms and maintain candidate boxes in a heap. It is more machinery than needed because sorting once exposes the exact greedy order.
- **Tall room behind a bottleneck:** its physical height is irrelevant when an earlier room is shorter; the prefix-minimum clearance captures this constraint.
- **Smallest box does not fit:** then no remaining box can use the current room, so skipping the room cannot lose a placement.
- **More boxes than rooms:** at most $W$ boxes can be placed because every room holds at most one.
- **More rooms than boxes:** the scan stops as soon as every box has been placed.
- **Equal heights:** equality is allowed, and duplicate box or room heights require no special handling.
