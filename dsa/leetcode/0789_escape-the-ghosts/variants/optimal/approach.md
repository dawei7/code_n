## General

**Measure shortest grid travel with Manhattan distance**

On each turn, a participant may change one coordinate by one unit or stay still. The fewest turns between points `(x1, y1)` and `(x2, y2)` is therefore:

$$
\lvert x1 - x2 \rvert + \lvert y1 - y2 \rvert.
$$

This is Manhattan, or taxicab, distance. Every horizontal move can reduce the horizontal difference by at most one, and every vertical move can reduce the vertical difference by at most one, so at least this many turns are necessary. Moving along the two axes achieves exactly that bound.

The player's shortest time from origin `(0,0)` to `(tx,ty)` is:

`abs(tx) + abs(ty)`.

A ghost at `(x,y)` needs:

`abs(tx - x) + abs(ty - y)`

turns to reach the target.

**Reduce the adversarial game to a race to the target**

At first, it may seem necessary to simulate every possible player path and every coordinated ghost pursuit. The key observation is that a ghost can defeat the player simply by reaching the target no later than the player.

If a ghost's distance to the target is less than or equal to the player's distance, it travels along a shortest route to the target. It arrives before or at the same turn. The player cannot escape, because arriving simultaneously with a ghost does not count.

Thus every successful strategy requires the player to have strictly smaller target distance than every ghost.

**Why a farther ghost cannot intercept a shortest player path**

The converse needs proof. Suppose the player follows a shortest path to target `T` from start `S`. Assume some ghost starting at `G` could meet the player at point `X` before or at the player's arrival there.

That means:

$$
\operatorname{dist}(G,X)
\le
\operatorname{dist}(S,X).
$$

By the triangle inequality:

$$
\operatorname{dist}(G,T)
\le
\operatorname{dist}(G,X)+\operatorname{dist}(X,T).
$$

Because `X` lies on a shortest player path:

$$
\operatorname{dist}(S,X)+\operatorname{dist}(X,T)
=
\operatorname{dist}(S,T).
$$

Combining the relations would give:

$$
\operatorname{dist}(G,T)
\le
\operatorname{dist}(S,T).
$$

Therefore any ghost capable of intercepting a shortest player path must also be able to reach the target no later than the player. The contrapositive is exactly what is needed: if every ghost is strictly farther from the target, none can intercept the player on a shortest route.

This proves that comparing only target distances is sufficient; no grid search or pursuit simulation is missing a more dangerous strategy.

**Understand the strict inequality**

The generator tests:

`ghost_distance > player_distance`.

Equality must fail. All movements happen simultaneously, and the statement says sharing any square at the same time—including the target—is not an escape.

If a ghost needs fewer turns, it can reach the target first and wait, because staying still is allowed. If it needs exactly the same turns, it can arrive simultaneously. Only a strictly larger ghost distance guarantees the player arrives alone first.

**Use `all` to express the universal condition**

The method evaluates the comparison for every pair `(x,y)` in `ghosts`. Python's `all` returns true only if every ghost satisfies the strict inequality.

It short-circuits on the first dangerous ghost. Once one ghost can reach the target no later than the player, the overall answer is false regardless of all other ghosts.

If all comparisons succeed, the shortest-player-path argument proves one strategy that beats all ghosts simultaneously.

**Trace the first example**

The target is `(0,1)`, so the player distance is one.

Ghost `(1,0)` has distance two to the target. Ghost `(0,3)` also has distance two. Both are strictly greater than one, so the method returns true.

The player moves north once and arrives before either ghost.

**Trace a blocking ghost**

For target `(2,0)`, the player needs two turns. A ghost at `(1,0)` needs one turn to reach the target. The inequality fails.

It does not matter whether the ghost physically starts between the player and target or chooses a direct collision route. Reaching the target first and waiting already prevents escape.

**Trace simultaneous arrival**

For target `(1,0)`, the player distance is one. A ghost at `(2,0)` also has distance one. Equality fails the strict comparison, so the answer is false exactly as required.

**Why negative coordinates need no special case**

Absolute differences handle every quadrant. A target at negative coordinates has player distance `abs(tx) + abs(ty)`, and a ghost's formula measures its independent horizontal and vertical differences in the same way.

The infinite grid has no walls or boundaries, so Manhattan distance is always achievable.


If the algorithm returns false, some ghost can reach the target no later than the player and can force failure by going there directly.

If it returns true, the player takes any shortest path. Were a ghost able to intercept that path, triangle inequality would imply that ghost could also reach the target no later, contradicting the checked strict inequality. Therefore the player arrives safely before every ghost, and escape is guaranteed.

## Complexity detail

Let $g$ be the number of ghosts. The player distance is computed once. Each ghost contributes a constant number of arithmetic and absolute-value operations, so time is $O(g)$.

The generator and `all` stream the ghost positions without building another collection. Only scalar coordinates and distances are used, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Breadth-first search on the grid:** The grid is infinite and obstacles do not exist, so BFS replaces a constant-time distance formula with an unbounded search.

- **Simulate simultaneous turns:** There are many possible adversarial moves, but the direct-to-target proof makes simulation unnecessary.

- **Check collision only on one chosen path:** Target-distance comparison is stronger and proves safety for a shortest path through triangle inequality.

- **Equal distance:** The ghost can arrive simultaneously, so equality must return false.

- **Ghost closer than the player:** It can arrive and wait at the target.

- **Multiple ghosts at one location:** Each produces the same comparison; duplicates do not change correctness.

- **Negative coordinates:** Absolute differences already cover them.

- **Ghost initially at the target:** Its distance is zero, so escape is impossible.

- **Player initially at the target:** The player distance is zero; under the given nonempty ghost list, success requires every ghost to have positive target distance.
