## General

**Process robots in physical left-to-right order**

Input order is unrelated to position, but collisions depend on spatial order. The code sorts original indices by `positions[i]` and processes robots from leftmost to rightmost.

Keeping indices rather than rearranging robot records preserves access to directions and mutable health values at their original indices. It also makes final input-order output easy.

**Which direction pattern can collide**

Two robots with equal speed can approach only when the left robot moves right and the right robot moves left. Same-direction robots maintain their separation. A left-moving robot followed spatially by a right-moving robot moves away from it.

Therefore, when scanning left to right, only previously seen unmatched right movers can collide with a current left mover.

**Stack stores pending right movers**

Whenever direction is `R`, append its index to `stk`. These robots are ordered by position, and the top is the nearest pending right mover to the current scan position.

A current left mover must collide with that nearest right mover before it could reach any earlier one. This last-in-first-out collision order is exactly what a stack represents.

**Right robot has greater health**

Let current left robot be `i` and stack top right robot be `j`.

If `healths[j] > healths[i]`, robot `i` is destroyed by setting its health to zero. Robot `j` survives but loses one health.

It remains on the stack because the code only inspected `stk[-1]` rather than popping it. The while loop stops because current health is now zero. That surviving right mover may collide with a later left mover.

**Left robot has greater health**

If `healths[j] < healths[i]`, the right robot is destroyed. Current left health decreases by one, `healths[j]` becomes zero, and `j` is popped.

If current health remains positive, it immediately faces the next-nearest pending right mover, so the while loop continues.

This models a strong left mover passing through a sequence of weaker right movers, losing one health per victory.

**Equal health**

Equal health destroys both robots. Their health values become zero, the right robot is popped, and the loop breaks because current robot no longer exists.

The explicit break is consistent with setting current health zero; it also makes the terminal collision clear.

**Why a surviving left mover is not pushed**

If the stack becomes empty while current left robot remains alive, there is no earlier right mover left to meet it.

Future robots in the scan lie to its right. A future left mover travels in the same direction at the same speed, and a future right mover travels away to the right. Neither can collide with this survivor. It needs no further tracking.

**Trace a chain collision**

Suppose two right movers lie to the left of one strong left mover. The nearer right mover is on top and collides first. If destroyed, it is popped and current left health decreases. The next stack top is then the next robot encountered physically by the continuing left mover.

This order would be wrong with a queue, which would compare the farthest right mover first.

**Mutating healths records survival**

Destroyed robots receive health zero. Survivors retain their final possibly decreased health. After all collision processing, the list comprehension:

`[h for h in healths if h > 0]`

scans healths in original input order and returns only survivors. This satisfies the required original robot order, not spatial order.

The exact source mutates the caller-provided `healths` array.

**Why every robot is processed efficiently**

A right mover is pushed once. It may survive several collisions without being popped, but every such collision destroys a distinct left mover that then exits. Or it is eventually popped exactly once. Each collision permanently destroys at least one robot, so total collision iterations are $O(n)$.


In spatial order, the only unresolved collision for a left mover is with the nearest unmatched right mover to its left, which is the stack top. The three health comparisons update both robots exactly according to the rules and either terminate the current robot or expose the next physically possible collision. Right movers remain pending only while alive; surviving left movers cannot meet future scanned robots. Thus all collisions occur in correct chronological pairing. Positive final healths identify exactly the survivors, and scanning the original health array returns them in required order.

## Complexity detail

Sorting the $n$ original indices by position costs $O(n\log n)$. After sorting, every index is pushed at most once and popped at most once, and every collision destroys at least one robot. The simulation is $O(n)$, so total time is $O(n\log n)$.

The sorted index list and stack each use $O(n)$ space. Python sorting may also use $O(n)$ temporary space. Overall auxiliary space is $O(n)$.

The output list can contain up to $n$ health values. `healths` is modified in place.

## Alternatives and edge cases

- **Simulate positions over time:** Inefficient and difficult because collision times may be fractional.
- **Queue of right movers:** Incorrect because the nearest, most recently seen right mover collides first.
- **All move right:** Every index stays on the stack and all healths survive unchanged.
- **All move left:** The stack stays empty and all survive unchanged.
- **Equal-health collision:** Both become zero and disappear.
- **One strong left mover:** May pop several weaker right movers, losing one health for each.
- **Right mover survives:** It stays on the stack with health decreased by one.
- **Unsorted input:** Sorted indices establish correct physical order without losing original identity.
- **No survivors:** Final filtering returns an empty list.
- **Input mutation:** The original `healths` list contains zeros and reduced survivor healths after execution.
