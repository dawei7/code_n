## General

**Define health needed before entering each room**

A tempting forward strategy is to choose the path with the largest running
health or largest total sum. That is not sufficient: survival depends on the
lowest prefix health along the path, and a later large power-up cannot revive
the knight after health has already fallen to zero.

The selected dynamic program works backward. `dp[i][j]` means the minimum
health the knight must have immediately before entering `dungeon[i][j]` so
that some right-and-down path from that room reaches the princess alive.

This state summarizes the complete future requirement in one number. The
answer is `dp[0][0]`.

**Derive the recurrence from the next room**

From `(i,j)`, the knight may next enter `(i+1,j)` or `(i,j+1)`. If those
positions require certain entry health values, the better path is the one with
the smaller requirement:

`next_need = min(dp[i + 1][j], dp[i][j + 1])`.

Entering the current room changes health by `dungeon[i][j]`. To leave it with
at least `next_need`, the incoming amount would algebraically be:

`next_need - dungeon[i][j]`.

A positive room lowers the required incoming health; a negative room raises
it. However, health must always be a positive integer, even when a large
power-up would make the expression zero or negative. Therefore:

`dp[i][j] = max(1, next_need - dungeon[i][j])`.

This one formula handles demons, empty rooms, and orbs.

**Use sentinels to handle the destination**

The source allocates an `(m + 1) x (n + 1)` table filled with positive
infinity. Those extra bottom and right boundaries represent impossible exits
from the grid.

It then sets exactly two boundary positions to one:
`dp[m][n - 1]` below the destination and `dp[m - 1][n]` to its right.

When the destination `(m-1,n-1)` is processed, the minimum of those two values
is one. The recurrence becomes:

$$
\max(1,1-\texttt{dungeon}[m-1][n-1]),
$$

which is precisely the health needed to survive the final room.

For every other edge cell, one neighbor is infinity and the valid neighbor is
finite, so `min` automatically ignores the impossible direction. This removes
separate last-row and last-column branches.

**Fill in reverse movement order**

Each state depends on the room below and the room to the right. The nested
loops therefore visit rows bottom-to-top and columns right-to-left. At the time
`dp[i][j]` is calculated, both dependencies already contain final values.

Filling top-to-bottom would read unresolved future states. The reverse order is
not cosmetic; it follows the dependency graph created by allowed movement.

**Trace the destination and nearby rooms**

In the main example, the destination contains negative five. It requires six
health on entry: five is lost, leaving one.

The room above it contains positive one. Choosing the downward move requires
six afterward, so entering that room with five is sufficient; the orb raises
health to six.

The room left of the destination contains positive 30. Entering with only one
raises health far above the six needed next, so its state is clamped to one.

At the room containing negative ten, the algorithm compares the requirements
of its right and down continuations, chooses the smaller, then adds enough
health to absorb ten damage. Repeating this calculation backward produces
seven at the top-left cell.

**Why locally choosing the smaller next requirement is safe**

Both possible moves begin after the same current-room effect. If one successor
can guarantee rescue from a smaller entry health than the other, it can never
require more initial health at the current room. Subtracting the same dungeon
value and applying the same lower bound preserves that ordering.

Thus the optimal suffix choice has optimal substructure, and a single minimum
is sufficient instead of preserving all paths.

**Prove the state meaning**

At the destination, the sentinel recurrence gives exactly the smallest health
that remains at least one after its value is applied.

Assume the below and right states are correct. Choosing their minimum selects
a feasible suffix with the least required exit health. The recurrence computes
the least current entry health that, after the current gain or loss, meets that
requirement while remaining at least one. Any smaller amount either dies in the
current room or enters every possible successor below its proven need.

Backward induction establishes every state, including `dp[0][0]`.

**Exact-source dependencies**

The source uses `List` and `inf` without imports. Standalone execution needs
`from typing import List` and a definition such as `from math import inf`.

## Complexity detail

There are $mn$ real cells, and each is processed once with constant work, so
time is $O(mn)$.

The exact source allocates $(m+1)(n+1)$ table entries, so auxiliary space is
$O(mn)$, not the manifest's $O(n)$. The extra sentinel row and column do not
change that order. A one-dimensional rolling table is needed to realize the
declared space bound.

## Alternatives and edge cases

- **One-row dynamic programming:** Reuse an array of column requirements while scanning bottom-up and right-to-left, reducing space to $O(n)$.
- **Binary search initial health plus reachability DP:** Correct with a monotone feasibility test but adds a logarithmic factor.
- **Forward maximum-sum path:** Incorrect because total gain does not capture fatal early deficits.
- **Single room:** The sentinel formula returns one for a nonnegative value or `1 - value` for damage.
- **Positive start room:** Initial health still cannot be below one.
- **Negative destination:** Its damage must be survived before rescue completes.
- **One row or one column:** Infinity sentinels force the only valid direction.
- **Large power-up:** The requirement is clamped at one, never zero.
- **Rectangular guarantee:** Every row has the same `n` columns used by the table.
- **Manifest mismatch:** Full-matrix storage is $O(mn)$ despite the declared $O(n)$.
