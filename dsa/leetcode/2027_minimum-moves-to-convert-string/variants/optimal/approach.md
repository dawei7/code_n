## General
**Act at the earliest uncovered `X`**

Scan from left to right. An `O` needs no action, so advance one position. Upon
reaching an `X`, one move is unavoidable because no earlier move has covered
it. Use that move to cover this position and the next two positions, then skip
all three because they are now effectively `O`.

If the earliest remaining `X` lies among the final two positions, the actual
length-three move can start farther left and end at the string boundary.
Previously scanned positions are already `O`, so this still costs exactly one
move and creates no new work.

Every counted move is necessary for the earliest `X` present when it is chosen.
Placing the move as far right as possible from that point covers the greatest
amount of unprocessed suffix without sacrificing any already processed
position. The next uncovered `X` is therefore at least three positions later,
and repeating this exchange-optimal choice produces a minimum-size set of
moves.

## Complexity detail
The scan index only moves forward and visits or skips each of the $N$
positions once, so the time is $O(N)$. The index and move counter use
$O(1)$ space.

## Alternatives and edge cases
- **Repeated string reconstruction:** Find the first `X`, replace its
  three-character region in a new string, and repeat. This is correct but
  copying the string for many moves can take $O(N^2)$ time.
- **Boolean coverage array:** Mark every position affected by selected moves;
  this mirrors the greedy scan but unnecessarily uses $O(N)$ space.
- An all-`O` string requires no moves.
- Existing `O` characters inside a selected block do not change the move cost.
- Adjacent groups of `X` fewer than three positions apart may be covered by
  the same move.
- A final `X` is coverable by a move ending at the final string position.
