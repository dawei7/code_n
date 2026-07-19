## General
**Represent every possible combined stone by a prefix sum**

After any sequence of moves, the leftmost stone equals the sum of some original prefix. Convert `stones[i]` in place to the prefix total through index `i`. A move that expands the combined prefix through `i` scores exactly this stored value, so the full changing row no longer needs to be simulated.

**Express a move as current gain minus the opponent's advantage**

If the current player takes prefix total $P_i$, the opponent then controls the continuation and can obtain its own optimal score difference. From the current player's perspective, that choice is $P_i$ minus the opponent's advantage. Choosing the entire row gives $P_{N-1}$ with no reply, which initializes `best`.

**Collapse all later choices while scanning backward**

When considering prefix endpoint `i`, the best difference available from endpoints later than `i` is already stored in `best`. The newly available choice produces `P_i - best`; alternatively, the player can retain the previous later choice. Therefore update `best = max(best, P_i - best)` from `i = N-2` down through `1`. Endpoint zero is illegal because a move must remove at least two stones. The final `best` is Alice's optimal difference.

## Complexity detail
Building prefix sums and scanning them backward each take $O(N)$ time. Both transformations reuse the input array, and the recurrence keeps only one scalar, so auxiliary space is $O(1)$. If preserving the caller's array is required, copying it first changes auxiliary space to $O(N)$ without changing time.

## Alternatives and edge cases
- **Quadratic game DP:** Evaluating every later prefix choice for every state follows the minimax definition directly but costs $O(N^2)$ time.
- **Recursive simulation:** Materializing each changed stone row creates many overlapping game states and can become exponential without the prefix-state reduction.
- **Two stones:** Only the whole-row move is legal, so the answer is their sum.
- **All-negative values:** A player may still prefer a less negative strategic choice; greedy selection by immediate score is unsafe.
- **Take every stone:** This is always a legal option and supplies the recurrence's base value.
- **Minimum prefix:** Index `1` is the earliest legal endpoint; index `0` must never be considered.
- **Input mutation:** In-place prefix sums are intentional for constant auxiliary space.
