## General

**Define a prefix state**

For a fixed number of carpets, store the minimum visible-white count in every prefix of `floor`. With zero carpets, this value is simply the prefix count of `1` tiles.

Suppose the current layer permits one more carpet and considers the prefix ending at position `index - 1`. There are two exhaustive choices for that final tile. Leave it uncovered, adding one exactly when it is white to the current layer's answer for the shorter prefix. Or cover it with the rightmost carpet, which also covers the preceding `carpetLen - 1` positions and leaves the previous layer's answer for the prefix ending before that carpet.

**Roll the carpet layers**

Take the smaller of those two choices at every prefix. The recurrence may effectively waste a carpet on an already covered or empty prefix, which is valid because overlap is allowed and ensures using an additional layer never worsens the answer.

The two choices partition all placements according to whether the final position is covered by a selected rightmost carpet. Removing that carpet leaves an optimal subproblem with one fewer carpet; otherwise removing the final uncovered tile leaves the adjacent prefix state. Induction over carpet layers and prefix lengths therefore establishes that every stored value is optimal. Only the preceding layer is needed, so the table can be rolled.

## Complexity detail

Let $n$ be the floor length and $c$ the number of carpets. Each of the $c$ layers evaluates all $n$ prefix positions in constant time, for $O(cn)$ time.

Two arrays of $n+1$ prefix values are sufficient, giving $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Full two-dimensional table:** Storing every carpet-prefix state uses the same $O(cn)$ time but $O(cn)$ space.
- **Enumerate carpet starts:** Trying every combination of starting positions grows exponentially with `numCarpets`.
- **Greedily cover the densest interval:** Locally maximizing newly covered white tiles can block a better combination of later intervals.
- **Enough total reach:** If the carpet intervals can cover all floor positions, the answer is zero even when overlap is necessary at their boundaries.
- **Black tiles:** Leaving a black tile uncovered adds zero to the state.
- **Carpet longer than the current prefix:** The carpet covers the whole prefix, so the prior index is clamped to zero.
