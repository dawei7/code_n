# The Earliest and Latest Rounds Where Players Compete

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1900 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming, Memoization |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [The Earliest and Latest Rounds Where Players Compete](https://leetcode.com/problems/the-earliest-and-latest-rounds-where-players-compete/) |

## Problem Description

### Goal

Players numbered $1$ through $n$ stand in their original order. In every round, the first remaining player faces the last, the second faces the second-last, and so on. An unpaired middle player advances automatically. Winners are then reordered by their original player numbers before the next round.

`firstPlayer` and `secondPlayer` defeat every other opponent, so both remain until they face each other. For a match between any two other players, either winner may be chosen. Across every possible assignment of those results, return the earliest and latest round in which the two distinguished players can meet.

### Function Contract

**Inputs**

- `n`: the initial number of players, where $2 \le n \le 28$.
- `firstPlayer` and `secondPlayer`: distinct original player numbers satisfying $1 \le \texttt{firstPlayer} < \texttt{secondPlayer} \le n$.

**Return value**

Return `[earliest, latest]`, the minimum and maximum possible one-based round numbers in which the distinguished players compete.

### Examples

**Example 1**

- Input: `n = 11, firstPlayer = 2, secondPlayer = 4`
- Output: `[3, 4]`
- Explanation: Choosing different winners in unrelated matches can make the two players meet in round three or postpone their meeting until round four.

**Example 2**

- Input: `n = 5, firstPlayer = 1, secondPlayer = 5`
- Output: `[1, 1]`
- Explanation: The first and last players are paired immediately, so no other outcome can change their meeting round.

**Example 3**

- Input: `n = 5, firstPlayer = 1, secondPlayer = 3`
- Output: `[2, 3]`

### Required Complexity

- **Time:** $O(n^5)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Retain only the relevant state.** At the start of a round, future pairings depend on the number of remaining players and the current row positions of the two distinguished players, not on the identities of everyone else. Memoize a state `(player_count, first, second)`. If `first + second == player_count + 1`, they are paired in the current round, so both extrema are one.

**Enumerate attainable next positions.** Process each front-back match while maintaining a set of pairs `(before_first, before_second)`: the numbers of chosen winners whose original row positions lie before each distinguished player. A match containing a distinguished player has a forced winner. Every other match contributes either endpoint, and an odd middle player advances automatically. After all matches, adding one to the two counts gives one attainable pair of positions for the next round.

**Combine child extrema.** Recursively evaluate every distinct attainable next state with $\lceil\texttt{player_count}/2\rceil$ players. The earliest result is one plus the smallest child earliest value; the latest is one plus the largest child latest value. The transition enumerates every legal unrelated-match outcome, while collapsing outcomes that produce identical distinguished positions, so the extrema are complete without tracking entire survivor rows.

#### Complexity detail

At a fixed round size there are $O(n^2)$ distinguished-position states. For one state, at most $O(n^2)$ count pairs are carried through $O(n)$ matches, giving a conservative $O(n^3)$ transition bound. Across memoized states this yields $O(n^5)$ time. The memo and the largest transition set contain $O(n^2)$ entries; recursion has only $O(\log n)$ levels, so auxiliary space is $O(n^2)$.

The legal domain ends at $n=28$, only five elimination rounds. A strictly validated `bounded_domain` certificate therefore replaces runtime scaling with exhaustive contract-domain comparison against an independent transition oracle.

#### Alternatives and edge cases

- **Enumerate complete survivor subsets:** This is conceptually direct but distinguishes many rows that lead to the same two relevant positions and grows exponentially.
- **Minimize or maximize greedily each round:** A locally favorable placement can restrict later pairings, so both extrema require exploring all attainable next states.
- **Immediate opponents:** Positions whose sum is `player_count + 1` meet in the current round with result `[1, 1]`.
- **Odd player count:** The middle player advances without a match and still affects each distinguished player's next position.
- **Original ordering:** Winners are sorted by their original numbers, not by match order or by which side of a pair won.
- **Symmetric placements:** Reflecting both distinguished positions across the row preserves the answer, a useful regression property.

</details>
