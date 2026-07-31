## General

**Model the passes as a functional graph**

Each player has exactly one outgoing edge, from $i$ to `receiver[i]`. Starting from any player therefore determines one unique walk, but simulating `k` edges is impossible when $k$ may reach $10^{10}$. Binary lifting replaces that long walk with a logarithmic number of precomputed power-of-two blocks.

For a current block length $2^b$, maintain two arrays:

- `jump[x]` is the player reached after exactly $2^b$ passes from `x`.
- `gain[x]` is the sum of the $2^b$ receiver indices visited during those passes. It excludes the starting `x` but includes the endpoint.

At $b=0$, one pass from `x` reaches `receiver[x]`, so both `jump[x]` and `gain[x]` begin with `receiver[x]`.

**Compose two adjacent blocks**

Two blocks of length $2^b$ form one block of length $2^{b+1}$. If `middle = jump[x]`, the second block starts where the first ends. Therefore

`next_jump[x] = jump[middle]`

and

`next_gain[x] = gain[x] + gain[middle]`.

The two gain intervals are consecutive and non-overlapping: the first includes the player reached on passes $1$ through $2^b$, while the second includes those reached on the following $2^b$ passes. Thus the composed arrays describe exactly twice as many passes.

**Evaluate every starting player together**

Initialize `positions[start] = start` and `scores[start] = start`, because the starting player contributes before any pass. Process the bits of `k` from least significant to most significant. Whenever the current bit is set, append that power-of-two block to every start's accumulated walk:

- add `gain[positions[start]]` to its score;
- replace its current position with `jump[positions[start]]`.

The selected blocks appear in increasing bit order, but they are concatenated in time: each lookup begins at the endpoint of all previously selected blocks. After processing any prefix of bits, `positions[start]` is exactly the player reached after the represented number of passes, and `scores[start]` is exactly the sum of all touched indices through that point. The composition formulas preserve this invariant for the next bit. Once all bits are consumed, every score represents exactly `k` passes, so their maximum is the required answer.

Only the current `jump` and `gain` arrays are needed. Replacing them with their doubled versions after each bit avoids storing a full sparse table.

## Complexity detail

Let $n$ be the number of players. There are $\lfloor\log_2 k\rfloor+1$ relevant bits. Each level advances or composes arrays with $n$ entries, giving $O(n\log k)$ time. The current positions, scores, jump destinations, gains, and two replacement arrays each contain $n$ values, so the auxiliary space is $O(n)$.

The benchmark uses $n$ as `size`, fixes a large `k`, and builds legal permutation-style functional graphs. The optimal rolling tables scale linearly in $n$ for the fixed bit count. A correct calibration implementation redundantly sorts the receiver list $O(n)$ times before performing the same lifting updates. It completes every tier and returns the same answers, but fails with $O(n^2\log n+n\log k)$ scaling.

## Alternatives and edge cases

- **Full sparse tables:** Store `jump[b][x]` and `gain[b][x]` for every player and bit. This has the same $O(n\log k)$ time but uses $O(n\log k)$ space instead of rolling arrays.
- **Direct simulation:** Follow `receiver` once per pass from every start. It is straightforward and correct but requires $O(nk)$ time.
- **Cycle decomposition:** Every functional-graph walk eventually enters a cycle, so tails, cycle prefix sums, and modular arithmetic can answer long walks. This can achieve strong bounds but is substantially more intricate across all starts.
- **Self-loops:** A player may pass to themself; the lifting formulas naturally count that index once for every touch.
- **Duplicate receivers:** Many outgoing edges may meet at one player, so `receiver` is not necessarily a permutation.
- **Repeated visits:** A player's index contributes every time the ball returns to that player, not only on its first visit.
- **Starting contribution:** Each score begins with the start index; `gain` contains only players reached after passes, preventing either omission or double counting.
