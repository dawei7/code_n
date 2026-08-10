## General

**Why a room’s printed height is not its full capacity**

A box cannot be teleported directly into a room. If it enters from the left, it must pass every room to that room’s left; if it enters from the right, it must pass every room to that room’s right. A short room along the route can therefore block a box from reaching a taller room farther inside.

For each warehouse position, the solution computes the tallest box that can reach and occupy that room when the better of the two entrances is chosen. Once those effective capacities are known, the geometric insertion problem becomes a simpler matching problem between box heights and room capacities.

The arrays `left` and `right` summarize the route bottlenecks. For index `i`:

- `left[i]` is the minimum height among rooms strictly to the left of `i`;
- `right[i]` is the minimum height among rooms strictly to the right of `i`.

The word “strictly” matters because the room’s own height is incorporated separately. The assignments `left[0] = inf` and `right[-1] = inf` represent an empty route before the first room or after the last room. An infinite outside bottleneck imposes no restriction, so an endpoint can be entered directly up to its own height.

**Building the two bottleneck arrays**

The left scan starts at index one. To reach room `i` from the left, a box passes room `i - 1` and every room before that. The recurrence

`left[i] = min(left[i - 1], warehouse[i - 1])`

therefore extends the previous route minimum with exactly the newly encountered room. After the assignment, `left[i]` is the minimum of `warehouse[0]` through `warehouse[i - 1]`.

The right scan is symmetric. It starts at `n - 2` and moves down to zero. The recurrence

`right[i] = min(right[i + 1], warehouse[i + 1])`

makes `right[i]` the minimum height from `warehouse[i + 1]` through `warehouse[n - 1]`.

These scans do not yet include `warehouse[i]` itself. That design makes it easy to compare the two entry directions before applying the room’s own final ceiling.

**Deriving the effective room capacity**

If a box approaches room `i` from the left, its maximum permissible height is

`min(warehouse[i], left[i])`.

From the right, its maximum permissible height is

`min(warehouse[i], right[i])`.

The box may enter from either side, so the better capacity is the maximum of those two quantities. The code writes the equivalent expression

`warehouse[i] = min(warehouse[i], max(left[i], right[i]))`.

The identity is valid because the room’s own height limits both routes:

$$
\max(\min(h,L),\min(h,R))=\min(h,\max(L,R)).
$$

This assignment overwrites each original warehouse height with its effective two-sided capacity. The mutation is intentional. After preprocessing, the original raw height is no longer needed.

For example, consider `warehouse = [3, 4, 1, 2]`. The room of height four at index one is reachable from the left only through height three, but it is reachable from the right only through the height-one room. Its best effective capacity is therefore three. The height-one room remains capacity one because its own ceiling is the limiting factor, no matter which side is used.

**Why the capacities can be sorted**

After effective capacities are computed, the method sorts both `boxes` and `warehouse`. This deliberately discards the positional order of the capacities. The preprocessing already encoded the best route to every individual room, and the resulting multiset of effective capacities admits a feasible placement matching.

One way to understand this is to imagine filling rooms from the restrictive bottlenecks outward. A room with a certain effective capacity can accept any box no taller than that capacity, and choosing the side represented by its better route allows it to be reached before rooms that would block that route are consumed in an incompatible order. The established two-sided preprocessing converts each room into one usable slot for maximum-cardinality matching.

Sorting now lets the algorithm make the safest possible match: use the smallest room that can hold the current box. Saving a larger room for a taller box can never reduce the number placed, while wasting a larger room on a shorter box might.

**The ascending two-pointer match**

Boxes are considered from shortest to tallest. The pointer `i` identifies the smallest effective room capacity not yet discarded or occupied.

For a box of height `x`, the inner `while` skips every remaining room with `warehouse[i] < x`. Because boxes are in ascending order, the current box is the shortest box not already processed. If such a room cannot hold this box, it cannot hold this box or any later, taller box. Discarding that room cannot sacrifice a future placement.

When the loop finds `warehouse[i] >= x`, the current box fits. The code increments both `ans` and `i`, matching the box to the smallest still-available room that can contain it. If `i == n`, no room remains. Since later boxes are at least as tall as the current box, none can be placed either, so `break` is correct.

The `for` loop automatically advances to the next box. A box is effectively skipped only if all capacities below it are first discarded and then no capacity remains; otherwise it is matched. In this ascending formulation there is no reason to reject a fitting box: using the smallest adequate room leaves every larger capacity available.

**Why the greedy matching is maximum**

Consider the current shortest unmatched box `x`. Every room skipped by the `while` loop has capacity below `x` and therefore cannot match any remaining box. Removing those unusable rooms changes no feasible answer.

If an adequate room exists, let it be the smallest adequate capacity. Any maximum matching either uses that room, leaves it unused, or gives it to some box at least as tall as `x`. If `x` is matched to a larger room, the two room assignments can be exchanged: put `x` in the smaller adequate room and retain the larger room for the other box. If `x` was omitted while a later box used the room, replacing the later box with `x` preserves the matching size. Thus there is always a maximum solution consistent with the greedy choice.

Applying this exchange argument at every step shows that the algorithm never lowers the best achievable count. The final `ans` is therefore the maximum number of boxes that can be stored.

## Complexity detail

Let $B$ be the number of boxes and $W$ the number of warehouse rooms.

Creating and filling `left` and `right` takes $O(W)$ time. Replacing all raw room heights with effective capacities takes another $O(W)$. Sorting the boxes costs $O(B\log B)$, and sorting the capacities costs $O(W\log W)$. During matching, the box loop advances at most $B$ times and pointer `i` advances at most $W$ times across both skipped and occupied rooms, so matching costs $O(B+W)$.

The sorting terms dominate, giving total time $O(B\log B+W\log W)$.

The two explicit bottleneck arrays each contain $W$ values, so the algorithm-managed auxiliary space is $O(W)$. The code mutates and sorts the caller-provided `boxes` and `warehouse` lists rather than creating sorted copies. The manifest’s $O(W)$ bound follows the conventional treatment that excludes implementation-specific scratch space inside an in-place library sort. For exact Python runtime accounting, Timsort can temporarily use space proportional to the list being sorted, so peak auxiliary memory can be $O(B+W)$ in the worst case. This qualification does not change the data structures explicitly created by the solution.

## Alternatives and edge cases

- **Simulating every push:** Trying insertion orders and moving boxes room by room repeats route checks and creates a combinatorial ordering problem. Prefix and suffix minima summarize all route bottlenecks once.
- **Using only prefix minima:** That solves the one-sided warehouse version but misses rooms that are easier to reach from the right. This solution takes the better of the left and right route capacities.
- **Sorting raw room heights:** Raw heights ignore blocking rooms. A tall interior room may be unreachable by a tall box, so the capacities must be preprocessed before sorting.
- **Largest-box endpoint greedy:** The editorial also describes testing boxes from largest to smallest against the currently exposed left and right rooms. That can use less explicit preprocessing, but the checked-in solution instead materializes effective capacities and performs ascending matching.
- **Endpoint rooms:** `left[0]` and `right[n - 1]` are infinity because no room precedes the corresponding entrance. The room’s own height still caps its effective value.
- **Single-room warehouse:** Both outside bottlenecks are infinite, so the effective capacity remains the room height. The shortest fitting box is placed, and the answer cannot exceed one.
- **More boxes than rooms:** Pointer `i` reaches `n` after at most $W$ placements or discards. The algorithm stops even if boxes remain.
- **More rooms than boxes:** Every box that finds a capacity is counted, and unused rooms are harmless. The answer cannot exceed $B$.
- **Room too short for the shortest remaining box:** It is skipped permanently because all future boxes are at least as tall.
- **Duplicate heights:** Sorting preserves every occurrence as a separate box or room. Equal-height boxes fit equal-height capacities because the comparison rejects only capacities strictly below `x`.
- **Mutation of inputs:** The solution overwrites `warehouse` with effective capacities and sorts both lists. A caller needing the original orders must pass copies; the LeetCode contract does not require preserving them.
- **Large heights:** The comparisons and minima do not depend on the magnitude beyond ordering. Python integers safely hold values up to and beyond the stated limit, while `inf` acts only as an unconstraining sentinel.
