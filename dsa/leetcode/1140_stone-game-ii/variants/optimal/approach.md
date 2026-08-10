## General

**Describe a game state completely**

At any point, the remaining piles form a suffix of the original array because a move always removes piles from the front of what remains. Two values are enough to describe the future:

- `i` is the index of the first remaining pile;
- `m` is the current value of the game's variable `M`.

The player whose turn it is may choose `x` from one through `2m`, take piles `i` through `i + x - 1`, and pass the state `(i + x, max(m, x))` to the opponent. No earlier move history matters once these two values are known. This makes `dfs(i, m)` a suitable dynamic-programming state.

The function is defined from the viewpoint of the player about to move: `dfs(i, m)` is the maximum number of stones that this current player can eventually collect from piles `i` onward, assuming both players make optimal choices from this point. It does not mean Alice specifically. On Alice's turn it describes Alice's best total from the suffix; on Bob's recursive turn it describes Bob's best total.

**Convert the opponent's best result into the current player's result**

Let the total number of stones remaining at state `(i, m)` be `remaining`. After the current player chooses `x` piles, all remaining stones will eventually be divided between the current player and the opponent. The recursive call

`dfs(i + x, max(m, x))`

returns the maximum number of those stones that the opponent can secure. Therefore, the current player's final share under that move is

`remaining - opponent_best`.

This subtraction includes both the stones taken immediately and any stones the current player may take on later turns. There is no need to add the current move separately. The remaining suffix's total is partitioned between exactly two players, so whatever the opponent eventually gets is precisely what the current player does not get.

Because the current player chooses the move, the recurrence takes the maximum over all legal `x`:

`dfs(i, m) = max(remaining - dfs(i + x, max(m, x)))`.

The opponent's recursive value already assumes optimal opposition. Maximizing over these worst responses is the minimax principle expressed through a zero-sum stone total.

**Use prefix sums for constant-time suffix totals**

The code builds `s = list(accumulate(piles, initial=0))`. Thus `s[t]` is the sum of the first `t` piles, `s[n]` is the total sum, and

`s[n] - s[i]`

is the total number of stones from index `i` through the end. Without this prefix-sum array, calculating a suffix total inside every state would repeatedly scan piles and add avoidable work.

**Recognize the take-everything base case**

If `2m >= n - i`, the current player is allowed to take all `n - i` remaining piles in one move. Every pile contains a positive number of stones, so leaving any pile to the opponent cannot increase the current player's total. Taking everything is immediately optimal, and `dfs` returns `s[n] - s[i]`.

This base case also ensures that recursive calls never choose more piles than remain. The generator is evaluated only when `2m < n - i`, so every `x` from one through `2m` is a legal count. There is no need to clamp the range separately.

The expression `m << 1 | 1` deserves careful reading. Shifting `m` left by one bit gives `2m`. Since `2m` is even, bitwise OR with one produces `2m + 1`. Python's `range(1, 2m + 1)` stops before its upper endpoint, so the generated choices are exactly one through `2m` inclusive.

**Why memoization is necessary**

Different move sequences can reach the same pair `(i, m)`. Once that happens, the remaining game is identical, so recomputing its entire decision tree would be wasteful. The `@cache` decorator stores the result of each argument pair and returns it immediately on later visits.

The recursion terminates because every legal choice has `x >= 1`, making `i + x` strictly larger than `i`. Eventually the number of remaining piles is small enough for the take-everything base case.

**Why the recurrence is correct**

Consider a state with some number of remaining piles. If all can be taken, the base case clearly returns the largest possible collection for the current player. Otherwise, assume the recursive value is correct for every state with fewer remaining piles. Each legal first choice `x` leads to one such smaller state for the opponent. By the induction assumption, the recursive call gives exactly what an optimal opponent can obtain there. Subtracting that value from the fixed remaining total gives exactly what the current player can guarantee after choosing `x`. Examining every legal `x` and selecting the largest guarantee is therefore optimal for the current state.

By induction, `dfs(0, 1)` is the maximum number of stones the starting player can obtain from the entire array under optimal play. Alice starts and the initial rule gives `M = 1`, so that returned value is exactly Alice's answer.

For the example `[2, 7, 9, 4, 4]`, the root considers both legal first moves. It does not greedily prefer the first two piles merely because they contain more stones now. Each candidate subtracts Bob's best possible continuation, capturing that taking two piles lets Bob remove everything else, while taking one can preserve a later turn for Alice.

## Complexity detail

Let `n` be the number of piles. The state is a pair `(i, m)`, and both components are bounded by `n`, so there are at most `O(n^2)` cached states. A non-base state tries up to `2m` choices, which is `O(n)` in the worst case. This gives the documented upper bound of `O(n^3)` time. Prefix-sum construction adds only `O(n)` time.

The cache stores at most `O(n^2)` integer results. The prefix-sum array requires `O(n)` space, and the recursion stack has depth at most `O(n)` because `i` increases on every call. The cache dominates, so the total auxiliary space is `O(n^2)`.

This is a safe upper bound; not every theoretical pair `(i, m)` must be reachable, and large values of `m` often trigger the base case immediately. Those facts improve practical work but do not invalidate the stated worst-case bound.

## Alternatives and edge cases

- **Greedily take the most stones now:** Choosing the locally largest legal prefix ignores how `M` changes and what it allows the opponent to take. The first example directly shows that taking two piles initially gives Alice fewer stones overall than taking one.
- **Plain minimax recursion:** It explores the correct game tree but recomputes identical `(i, m)` states exponentially many times. Memoization is what turns the recurrence into a practical dynamic program.
- **Bottom-up dynamic programming:** The same state and recurrence can be filled iteratively from larger indices toward smaller ones. It has comparable polynomial bounds but requires careful ordering because each state depends on later indices and possibly larger `M` values.
- **Track score difference instead of stones owned:** A recurrence can maximize current-player stones minus opponent stones. Since the remaining total is fixed at every state, the complement formulation used here is simpler and returns Alice's absolute stone count directly.
- **One pile:** At `dfs(0, 1)`, `2M` covers the only pile, so Alice takes it and the suffix sum is returned immediately.
- **All remaining piles fit within `2M`:** Taking every one is optimal because pile sizes are positive. The base case correctly avoids further recursion.
- **Highly uneven pile sizes:** The recurrence uses sums rather than pile counts as the payoff, so a very large late pile is valued correctly even though moves are constrained by counts.
- **`M` never decreases:** The transition `max(m, x)` preserves the old value when a small move is chosen and raises it only when `x` is larger. Using `x` alone would implement a different game.
- **Inclusive move limit:** The player may take exactly `2M` piles. The unusual bit expression constructs a range whose last generated choice is exactly `2m`.
- **Positive pile values:** This guarantee justifies taking all remaining piles whenever legal. If negative piles existed, that base-case argument would not hold, but such inputs are outside the contract.
