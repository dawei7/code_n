## General

**Reverse the game**

Forward choices are awkward because an increment made before a double has more
effect than one made afterward. Starting at `target` removes that ambiguity.
The reverse of an increment is subtracting one, and the reverse of a double is
halving an even value.

**Use every beneficial reverse double greedily**

While the current value exceeds `1` and a double remains, an odd value cannot
have resulted from doubling, so subtract one. An even value should be halved:
replacing that halving with reverse increments would require subtracting half
the current value and could not use fewer moves.

Thus every reverse step is forced or no worse than its alternative. Halving
also preserves all smaller future possibilities, so applying it immediately
cannot prevent an optimal continuation.

**Finish after the doubling budget is exhausted**

Once no double remains, the only permitted forward operation represented in
reverse is subtraction. Reaching `1` then costs exactly `target - 1` additional
moves. Adding that distance at once avoids iterating through it.

## Complexity detail

Each loop iteration either consumes a doubling allowance or changes an odd
value to the next even value. At most a constant number of iterations occurs
per binary digit of `target`, so the running time is
$O(\log \texttt{target})$. The algorithm stores only counters and uses $O(1)$
space.

## Alternatives and edge cases

- **Forward dynamic programming:** Recording the best move count for every
  reachable score is correct but takes $O(\texttt{target})$ time and space.
- **Forward greedy choices:** Doubling whenever possible can overshoot the
  target or spend a scarce double before the most valuable position.
- If `target` is `1`, no move is required regardless of the doubling allowance.
- If `maxDoubles` is zero, the answer is exactly `target - 1`.
- An odd reverse value must first be decremented because no integer double can
  produce it.
