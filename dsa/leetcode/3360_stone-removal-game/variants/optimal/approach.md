## General

There are no strategic choices: the requested removals are fixed as $10,9,8,\ldots$, and each turn either succeeds or ends the game. Simulate this sequence with `required`, subtracting it whenever the pile contains enough stones and then decreasing the next requirement by one.

Track whether Alice would win with a Boolean that toggles after every successful move. Before any move it is false because Alice loses if she cannot remove $10$. After Alice's first successful move it becomes true; after Bob's response it becomes false; this parity continues for every turn. When the next move is impossible, the Boolean therefore identifies the player who made the last successful move.

For the legal maximum $n=50$, the first seven removals total $49$, leaving one stone when the next requirement is three. Thus every legal game terminates within seven iterations, well before the requested amount could reach zero.

## Complexity detail

The contract restricts $n$ to $1\le n\le50$. At most seven successful moves occur, so both time and auxiliary space are $O(1)$ over the complete legal domain.

Runtime scaling is not meaningful for this bounded scalar domain. The verified `bounded_domain` certificate replaces a benchmark with the seven-iteration proof and exhaustive expected results for all 50 legal inputs.

## Alternatives and edge cases

- **Cumulative-sum intervals:** Precomputing the transition totals $10,19,27,34,40,45,49$ gives an equivalent constant-size lookup, but simulation follows the rules more directly.
- **Recursive turn simulation:** It is correct but adds unnecessary call-stack state for a forced sequence of at most seven moves.
- **Opening failure:** For $n<10$, Alice cannot move and loses.
- **Exact cumulative total:** If a move consumes the last stone, the opponent still loses because the next required positive removal is impossible.
- **Parity boundaries:** Winners change whenever $n$ reaches the next cumulative-removal total.
- **Maximum input:** At $n=50$, seven moves succeed, Alice makes the last one, and the next required removal of three cannot be made from the remaining stone.
