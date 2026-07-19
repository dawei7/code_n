## General
**Retain only the relevant state.** At the start of a round, future pairings depend on the number of remaining players and the current row positions of the two distinguished players, not on the identities of everyone else. Memoize a state `(player_count, first, second)`. If `first + second == player_count + 1`, they are paired in the current round, so both extrema are one.

**Enumerate attainable next positions.** Process each front-back match while maintaining a set of pairs `(before_first, before_second)`: the numbers of chosen winners whose original row positions lie before each distinguished player. A match containing a distinguished player has a forced winner. Every other match contributes either endpoint, and an odd middle player advances automatically. After all matches, adding one to the two counts gives one attainable pair of positions for the next round.

**Combine child extrema.** Recursively evaluate every distinct attainable next state with $\lceil\texttt{player_count}/2\rceil$ players. The earliest result is one plus the smallest child earliest value; the latest is one plus the largest child latest value. The transition enumerates every legal unrelated-match outcome, while collapsing outcomes that produce identical distinguished positions, so the extrema are complete without tracking entire survivor rows.

## Complexity detail
At a fixed round size there are $O(n^2)$ distinguished-position states. For one state, at most $O(n^2)$ count pairs are carried through $O(n)$ matches, giving a conservative $O(n^3)$ transition bound. Across memoized states this yields $O(n^5)$ time. The memo and the largest transition set contain $O(n^2)$ entries; recursion has only $O(\log n)$ levels, so auxiliary space is $O(n^2)$.

The legal domain ends at $n=28$, only five elimination rounds. A strictly validated `bounded_domain` certificate therefore replaces runtime scaling with exhaustive contract-domain comparison against an independent transition oracle.

## Alternatives and edge cases
- **Enumerate complete survivor subsets:** This is conceptually direct but distinguishes many rows that lead to the same two relevant positions and grows exponentially.
- **Minimize or maximize greedily each round:** A locally favorable placement can restrict later pairings, so both extrema require exploring all attainable next states.
- **Immediate opponents:** Positions whose sum is `player_count + 1` meet in the current round with result `[1, 1]`.
- **Odd player count:** The middle player advances without a match and still affects each distinguished player's next position.
- **Original ordering:** Winners are sorted by their original numbers, not by match order or by which side of a pair won.
- **Symmetric placements:** Reflecting both distinguished positions across the row preserves the answer, a useful regression property.
