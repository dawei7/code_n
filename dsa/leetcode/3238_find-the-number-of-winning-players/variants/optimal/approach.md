## General

Maintain one frequency for every player-color pair. When processing `[player, color]`, increment that exact frequency.

Player $i$ becomes a winner at the first moment one frequency reaches $i+1$. A separate boolean records whether the player was already counted. When the threshold is crossed for an uncounted player, mark the player and increment the answer; later picks cannot increment the answer again.

This online check is equivalent to counting all frequencies after processing the input: each winner has at least one threshold-crossing event, and a non-winner has none. The boolean ensures that several winning colors for one player still contribute exactly one.

## Complexity detail

Let $p=\lvert\texttt{pick}\rvert$. Each event performs constant work, so the time complexity is $O(p)$. The fixed 11-color table and winner flags use $O(n)$ auxiliary space.

The contract caps $n$ at $10$ and $p$ at $100$. This is too small for a stable scaling verdict, so the bounded-domain certificate and property regression replace runtime benchmarking.

## Alternatives and edge cases

- **Nested hash maps:** They are correct and useful for an unbounded color domain, but a fixed 11-color table is simpler here.
- **Rescan all picks for each player:** This repeats work and can take $O(np)$ time.
- Player $0$ wins after any one pick because the threshold is strictly more than zero.
- Player $i$ needs exactly $i+1$ same-color picks to reach the winning threshold.
- Picks of different colors do not combine.
- A player winning with several colors is counted once.
- Players with no picks cannot win.
- Colors `0` and `10` are both valid boundary values.
- Event order does not change the final set of winners.
