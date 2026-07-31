## Function Contract

**Inputs**

- `hp`: The health available at the beginning of each separate dungeon run.
- `damage`: The health loss applied upon entering each room.
- `requirement`: The minimum post-damage health needed to earn that room's point.

The two arrays have the same nonzero length $N$. Each run resets health to `hp`, begins at one selected index, and then visits every remaining room in increasing index order.

**Return value**

Return the sum of the points earned over all $N$ starting positions. A single room can contribute to several runs, and the total may require a 64-bit integer in fixed-width languages.
