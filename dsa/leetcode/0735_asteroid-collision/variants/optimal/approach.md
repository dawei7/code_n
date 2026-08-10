## General

**Identify the only direction pattern that can collide**

All asteroids move at the same speed. Two moving in the same direction keep their distance. A left-moving asteroid followed by a right-moving asteroid also separates: the left one moves farther left and the right one farther right.

A collision is possible only when an asteroid on the left moves right and a later asteroid moves left. In signs, that is a positive value followed somewhere to its right by a negative value, with no surviving asteroid between them that prevents contact.

The exact solution processes input from left to right and stores the already resolved surviving prefix in `stk`. Only the stack’s top can collide next with the current asteroid because it is the nearest surviving asteroid on the current one’s left.

**Positive asteroids can be pushed immediately**

When the current value `x` is positive, it moves right. Every asteroid already processed lies to its left:

- A positive stack asteroid moves in the same direction.
- A negative stack asteroid moves left, away from the new positive asteroid.

Neither case creates an immediate collision, so the positive asteroid is appended.

It may collide later with a future negative asteroid, which is why it remains available on the stack.

**A negative asteroid may trigger a collision chain**

For `x < 0`, collision is possible while the stack is nonempty and its top is positive. The current asteroid’s size is `-x`.

The loop pops while

`stk[-1] > 0 and stk[-1] < -x`.

Each popped positive asteroid is smaller than the incoming negative one and therefore explodes. The negative asteroid survives that collision and continues left, so it must be compared with the new stack top. This is how one large left-moving asteroid can destroy several smaller right-moving asteroids.

**Resolve the first asteroid that is not smaller**

After all smaller positive tops have been removed, three cases remain.

- If the top is positive and equal in size, `stk[-1] == -x`, both asteroids explode. The solution pops the top and does not append `x`.
- If the top is positive and larger, no branch appends `x`. The incoming asteroid explodes while the stack survivor remains.
- If the stack is empty or its top is negative, no collision is possible. The current negative asteroid is appended.

The final condition `not stk or stk[-1] < 0` expresses the third case. Two negative asteroids move left together and never meet.

**Why the stack always represents a stable prefix**

After each input asteroid is processed, no pair remaining in `stk` can collide with one another. If such a pair existed, it would contain a positive asteroid immediately before a negative asteroid somewhere in survivor order. That negative asteroid would have been resolved against the positive top when it was processed.

The stack also preserves original relative order because values are appended in input order and only destroyed values are popped.

**Trace `[10, 2, -5]`**

Push 10, then push 2. When -5 arrives:

1. Top 2 is positive and smaller than size 5, so 2 explodes and is popped.
2. New top 10 is positive but larger than size 5. The while loop stops.
3. It is not equal to 5, and the stack is neither empty nor topped by a negative value, so -5 is not appended.

The final stack is `[10]`.

For `[8, -8]`, the while loop does not pop because 8 is not smaller than 8. The equality branch pops 8, and -8 is not appended, leaving an empty result.

**Why only the top needs comparison**

Asteroids maintain their one-dimensional order until collisions remove some of them. The current left-moving asteroid encounters the nearest surviving asteroid on its left before any farther one. If that nearest asteroid survives, it blocks the current asteroid permanently. If it explodes, the next stack top becomes the new nearest possible collision.

This physical order is exactly the last-in, first-out behavior of a stack.

**Why the result is correct**

The algorithm resolves every possible collision involving the current asteroid in the same order those collisions would physically occur. It removes the smaller participant, removes both on equality, and stops when the current asteroid is destroyed or no opposing positive survivor remains.

By induction, the stack after each step contains exactly the survivors of the processed prefix in their original order and contains no internally colliding pair. After the final input value, the processed prefix is the whole array, so the stack is exactly the stable final state.

## Complexity detail

Let `n` be the number of asteroids. Each asteroid is considered once in the outer loop and appended at most once. Once popped, it never returns to the stack. Although one negative asteroid may execute many while-loop iterations, all pops across the complete run total at most `n`.

The amortized time complexity is therefore `O(n)`.

In the no-collision case, all `n` asteroids remain in `stk`, so auxiliary space is `O(n)`. The stack itself becomes the returned list; no second output copy is constructed.

## Alternatives and edge cases

- **Repeatedly scan adjacent pairs:** Simulate one collision, rebuild or rescan, and continue. This can revisit large portions of the array and degrade to `O(n^2)`.

- **Linked list of live asteroids:** Removing neighbors can be made constant time, but selecting and revisiting collision candidates adds complexity. The stack directly matches the one-sided processing order.

- **Treat every opposite-sign pair as colliding:** A negative asteroid to the left of a positive one moves away from it. Only a positive-left, negative-right arrangement collides.

- **Equal sizes:** Both values disappear. Popping the positive top without appending the current negative implements exactly that rule.

- **Incoming negative destroys many positives:** The while loop continues after every smaller top is popped.

- **Larger positive blocks the incoming asteroid:** The loop stops and the negative is not appended, leaving the positive survivor intact.

- **Empty stack after a collision chain:** The negative asteroid has survived all opponents and is appended.

- **Negative top:** Both the top and current asteroid move left, so the current one is appended without collision.

- **All asteroids move the same direction:** Every asteroid is appended, and the original array order is returned.

- **Nonzero guarantee:** The sign always identifies a direction; there is no stationary asteroid case to define.
