## General

**Manhattan distance is the best of four signed directions.** At position $(x,y)$,

$$
\lvert x\rvert+\lvert y\rvert
=
\max(x+y,x-y,-x+y,-x-y).
$$

Each signed expression corresponds to moving outward toward one of four diagonal quadrants. For example, in one expression two movement letters contribute $+1$ and the opposite two contribute $-1$.

The helper `calc(a, b)` evaluates one such quadrant. Letters `a` and `b` are the two favorable directions. The four calls use `("S","E")`, `("S","W")`, `("N","E")`, and `("N","W")`, covering every choice of vertical sign and horizontal sign.

**For one quadrant, changing an unfavorable move gains two.** Without changes, a favorable character adds $1$ to the signed displacement and an unfavorable character subtracts $1$. Changing an unfavorable direction into either favorable direction turns $-1$ into $+1$, improving the signed value by $2$. Changing a favorable move cannot help.

For any prefix containing $g$ favorable and $u$ unfavorable moves, the best score using at most $k$ changes is

$$
g-u+2\min(k,u).
$$

Equivalently, the first $\min(k,u)$ unfavorable moves may be treated as $+1$ and all later unfavorable moves as $-1$.

That is exactly what `calc` simulates. `cnt` records how many changes have been spent. A favorable character increments `mx`. An unfavorable character also increments `mx` while `cnt < k` and consumes one change; after the budget is exhausted, it decrements `mx`.

`ans` stores the largest `mx` over all prefixes because the problem asks for maximum distance at any time, not only after the complete movement string.

**Why greedily changing the earliest unfavorable moves is safe.** For a fixed prefix, only the number of unfavorable moves changed matters; every such change contributes the same improvement of two. Spending changes on the first encountered unfavorable moves ensures that, simultaneously for every prefix, as many bad moves as possible have already been converted. Delaying a change cannot improve an earlier prefix and gives the same score for later prefixes once the same count is used.

For `"NWSE"` and $k=1$, consider the northwest quadrant with favorable directions `N` and `W`. The first two moves give score $2$. The following `S` is unfavorable but is converted with the one change, raising the prefix score to $3$. This corresponds to changing `S` to `N` or `W` and reaches the example's maximum.

**Why four independent helper runs are legitimate.** The best prefix and chosen changes may differ between quadrants. That is allowed: the algorithm is comparing possible strategies, not trying to apply all four sets of changes simultaneously. Whichever helper returns the global maximum supplies one concrete quadrant, prefix, and set of at most $k$ character changes achieving that value.

For any modified prefix position, its Manhattan distance equals one of the four signed expressions, so its value cannot exceed the corresponding helper optimum. Conversely, each helper score is a signed displacement achieved by legal changes, and Manhattan distance is at least that signed expression. Taking the maximum therefore gives exact equality.

Changes to characters after the prefix attaining `ans` are unnecessary. The operation budget applies to the whole string, but leaving later characters unchanged preserves the distance already achieved at that earlier time.

**The helper state is a score, not literal coordinates.** It never needs separate north, south, east, and west counts. Once a quadrant is fixed, favorable versus unfavorable is the only distinction relevant to its signed expression. This is why each scan stays constant-space.

## Complexity detail

Let $n=\lvert\texttt{s}\rvert$. Each of four helper calls scans all $n$ characters with constant work, so total time is $O(4n)=O(n)$.

Each helper stores only `ans`, `mx`, `cnt`, and loop variables. The outer method stores four results. Auxiliary space is $O(1)$, matching the manifest.

## Alternatives and edge cases

- **Track coordinates and use the closed formula:** For each prefix, `min(prefix_length, original_distance + 2k)` also yields the optimum. The four-quadrant scan provides a constructive signed interpretation.
- **Try every changed character set:** There are exponentially many choices. All unfavorable changes have identical signed benefit within a fixed quadrant.
- **Change favorable moves:** This cannot increase that quadrant's score and wastes budget.
- **\(k=0\):** Every unfavorable move subtracts one, so the four scans reduce to the original prefix Manhattan distances.
- **\(k\ge\) prefix length:** Every move in that prefix can point outward, and the score reaches the prefix length, the largest possible distance after that many unit moves.
- **Maximum at an early time:** `ans` is updated on every character, so later movement back toward the origin cannot erase the recorded maximum.
- **Same movement string, different quadrants:** Each call is an alternative strategy; their change counters are intentionally independent.
- **One-character string:** A single move already has distance one, and every helper containing its direction records it.
- **At most \(k\):** Unused changes are harmless when no unfavorable move remains.
- **Infinite grid:** No boundary checks are required; only displacement matters.
