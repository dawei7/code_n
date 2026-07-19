## General
**Recognize the only direction pattern that can collide**

Asteroids preserve their relative order unless destroyed. Two survivors can approach each other only when the left one moves right and the right one moves left. Thus a newly read negative asteroid can collide only with positive asteroids at the end of the survivor stack.

**Resolve one incoming asteroid through a collision chain**

Keep the current asteroid alive initially. While it is negative, the stack top is positive, and the incoming asteroid is still alive, compare magnitudes. If the top is smaller, pop it and continue because the incoming asteroid may reach another positive survivor. If sizes match, pop the top and destroy the incoming asteroid. If the top is larger, only the incoming asteroid is destroyed.

**Append only after all threats are settled**

If the current asteroid survives the loop, append it. At that point the stack contains no adjacent positive-then-negative collision: either there was no opposing positive top, or the current asteroid itself was positive. This leaves a fully resolved prefix for the next input value.

**Why the stack gives the final order**

Before processing each asteroid, the stack is exactly the collision-free result for the processed prefix. Any collision involving the new asteroid must start at the stack's right edge, because all earlier survivors are shielded by that top survivor. The loop applies the physical size rule at that edge until the new asteroid is destroyed or no collision remains. Therefore the invariant holds for the enlarged prefix, and after the final input the stack is precisely the complete survivor sequence.

## Complexity detail
Every asteroid is pushed at most once and popped at most once. Although one input can trigger many pops, there are only `n` pops over the whole run, so time is $O(n)$. The survivor stack can hold all `n` asteroids, giving $O(n)$ space.

## Alternatives and edge cases
- **Repeated adjacent-pair simulation:** find one colliding pair, edit the array, and restart the scan; it mirrors the story but can take $O(n^2)$ time because collision chains repeatedly traverse the same prefix.
- **Linked-list event simulation:** removals are constant-time once a collision is located, but maintaining candidate events adds unnecessary machinery for this ordered process.
- **All asteroids move the same way:** no pair approaches, so the input remains unchanged.
- **Left movers precede right movers:** a negative followed by a positive moves apart and does not collide.
- **Equal magnitudes:** both opposing asteroids disappear, which may expose no new incoming asteroid to continue.
- **Long destruction chain:** one large left-moving asteroid may pop many smaller right movers before surviving.
- **Larger blocker:** when the positive stack top is larger, the incoming negative asteroid disappears immediately.
