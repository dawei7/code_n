## General

Collisions depend on spatial order, not input order, so first sort robot indices by `positions`. While scanning from left to right, a robot moving left can collide only with still-surviving right-moving robots already encountered. Keep those unmatched right movers on a stack; the nearest one is on top and must be the left mover's next possible opponent.

For a left mover, repeatedly compare its health with the stack top. If the left mover is stronger, remove the right mover, decrement the left mover, and continue toward the next stack entry. If the right mover is stronger, decrement it and remove the left mover. Equal health removes both. Mark removed robots with zero health, while surviving right movers stay on the stack for later left movers.

The stack contains exactly the right-moving survivors to the left of the scan position, in spatial order. Same-direction robots never meet because speeds are equal, and a left mover cannot reach any robot behind the nearest unmatched right mover without resolving that collision first. Each stack transition therefore matches the next physical collision. Every robot is pushed at most once and popped at most once. Finally, filtering the mutated health array directly preserves original input order.

## Complexity detail

Let $n$ be the number of robots. Sorting indices takes $O(n\log n)$ time; the amortized stack simulation takes $O(n)$ because each robot enters and leaves the stack at most once. The sorted index list and stack use $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Event-by-event time simulation:** Repeatedly locating the next meeting and updating positions can require $O(n^2)$ work and introduces unnecessary time arithmetic.
- **Sort complete robot records:** Storing `(position, health, direction, index)` tuples is correct but duplicates more data than sorting indices.
- **Use a queue of right movers:** A left mover meets the nearest preceding right mover first, so last-in-first-out order is essential.
- Robots moving only left or only right never collide.
- Equal-health collisions remove both robots and do not decrement another survivor.
- A strong robot may survive several collisions, losing one health each time.
- Input positions are distinct but unsorted; survivor output follows input identity, not spatial order.
- A single robot always survives with unchanged health.
