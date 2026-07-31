## General

**Identify the cars that can escape**

A left-moving car can avoid every collision only while it belongs to the initial run of `L` cars: nothing lies to its left that can stop it. Symmetrically, only the final run of `R` cars can move right forever. Remove those two boundary runs.

**Count stopped moving cars**

Inside the remaining interval, every moving car eventually stops in a collision. A right-moving car cannot escape through the right boundary, and a left-moving car cannot escape through the left boundary; an opposing car or an existing stationary site must stop it.

Each such moving car contributes exactly one unit to the score when it first becomes stationary. An `RL` meeting stops two moving cars and scores two, while a moving car hitting `S` stops one and scores one. Cars initially marked `S` contribute nothing. Therefore the total is simply the number of non-`S` characters after trimming the escaping prefix and suffix.

## Complexity detail

Let $n$ be the length of `directions`. Trimming the boundary runs and counting stationary characters each scan at most $n$ characters, for $O(n)$ time.

Python's trimmed substring may contain up to $n$ characters, so this implementation uses $O(n)$ auxiliary space. An index-based version can achieve $O(1)$ extra space.

## Alternatives and edge cases

- **Event simulation:** Repeatedly resolving adjacent collisions is harder to synchronize and can take $O(n^2)$ time.
- **Stack simulation:** A stack can model pending right-moving cars in $O(n)$ time, but stores state that the boundary invariant makes unnecessary.
- **All escaping:** A string consisting of some leading `L` cars followed by trailing `R` cars has zero collisions.
- **All stationary:** No character contributes to the result.
- **Opposite-direction meeting:** `RL` scores two because both moving cars stop, consistent with counting moving participants.
- **Collision chain:** Once a stationary point forms, every later moving car that reaches it adds one.
