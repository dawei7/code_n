## General

Within any row, a route either has just entered from below (or selected its starting cell on the bottom row) or has used one same-row move. A second same-row transition is forbidden, so only the first state may generate the optional horizontal move. After combining the zero-horizontal and one-horizontal possibilities, every resulting route may move upward to the next row.

Let `entered[c]` count routes that start or arrive at available column `c` before any same-row move in the current row. A horizontal move may cover column difference at most `d`. The routes ending at available column `c` after zero or one horizontal move are therefore the sum of `entered[x]` over `c - d <= x <= c + d`, including `x = c` for the zero-move choice. A column prefix sum evaluates every such interval in constant time.

For an upward move, the row difference is one, so a horizontal difference $x$ is legal exactly when $1+x^2\leq d^2$. Hence the upward column radius is $\lfloor\sqrt{d^2-1}\rfloor$. Apply another prefix-sum interval query to the completed routes of the row below, zeroing blocked destination cells. Then perform the horizontal combination for the new row. Initialize `entered[c] = 1` at every available bottom cell, process rows upward, and sum the completed route counts in the top row.

Every transition represents a legal move between available cells within the distance bound. The two-stage row state permits at most one horizontal move before the mandatory upward move, while retaining both the choice to skip it and the choice to use it as the final top-row move. Conversely, every valid route has exactly this decomposition on each visited row, so it is counted once.

## Complexity detail

Let $N$ and $M$ be the grid dimensions. Each row uses a constant number of prefix-sum constructions and interval queries across $M$ columns, so the time complexity is $O(NM)$. Only the route arrays and one prefix array for the current transition are retained, giving $O(M)$ auxiliary space. All counts are reduced modulo $10^9+7$.

## Alternatives and edge cases

- **Scan every source column:** Summing all horizontally reachable states separately for each destination is correct but costs $O(NM^2)$ time.
- **One DP state:** Combining arrived and horizontal-move states before generating another horizontal transition incorrectly permits two same-row moves in succession.
- **Use radius `d` for upward moves:** A vertical displacement of one consumes part of the Euclidean budget; the horizontal radius must be $\lfloor\sqrt{d^2-1}\rfloor$.
- **Count staying in place as a move:** The interval sum includes the same column only as the choice to make no horizontal move, not as a second cell visit.
- **Single-row grid:** Every available cell is already a complete route, and one legal same-row move may also end a route.
- **Blocked boundary row:** If the bottom or top row has no available cell, the answer is zero.
