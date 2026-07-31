## General

For fewer than five teams, no schedule exists. With two or three teams, every two matches share a team. With four teams, a two-team set is disjoint only from its unique complementary set, so the graph of possible consecutive matchup sets is disconnected and cannot cover every fixture.

**Partition every matchup into disjoint rounds.** For $n\ge5$, apply the circle method for round-robin tournaments. When $n$ is odd, temporarily add one dummy team and omit its match from every round. Rotating all teams except one fixed position produces $O(n)$ rounds, each containing pairwise disjoint matches, and covers every unordered pair exactly once.

Place each round immediately beside a copy whose home and away roles are reversed. This supplies both directed fixtures for every team pair. Inside one round block, the games can appear in any order because they are mutually disjoint; only the last game of one block and first game of the next require coordination.

**Choose block boundaries with compact dynamic programming.** For each block, record which game can be last and retain a parent consisting of a compatible previous last game and a different current first game. A current game uses two teams, while the prior block is a matching, so it can conflict with at most two prior games. Testing any three reachable prior endings is therefore sufficient to find a compatible one whenever one exists. Supported first games have distinct indices, so each possible last needs to inspect at most the first two supports to choose a different first.

Backtrack one final state to recover the first and last game of every block. Emit the chosen first, all remaining games, and the chosen last. Internal neighbors are disjoint because they belong to one matching, and every boundary is disjoint by its recorded parent. The round-robin factorization and reversed copies guarantee that every ordered pair appears exactly once.

## Complexity detail

The output itself contains $n(n-1)=\Theta(n^2)$ matches. Constructing and flattening the rounds takes $O(n^2)$ time. There are $O(n)$ block boundaries and $O(n)$ games per block; each first game tests at most three prior states, and each last game tests at most two supported firsts, so boundary reconstruction also takes $O(n^2)$ time. The rounds, states, and output use $O(n^2)$ space.

The benchmark defines its size as the team count $n$. The accepted construction matches the output-size lower bound. A calibrated correct alternative examines every reachable prior ending for every possible first game at each block boundary, adding one factor of $n$ while producing the same valid schedules.

## Alternatives and edge cases

- **Backtrack individual fixtures:** It can find small schedules but explores a huge search space and offers no practical guarantee near 50 teams.
- **Unoptimized boundary compatibility:** Scanning every prior ending for every next first game is correct but takes $O(n^3)$ time.
- **Independent round-robin games:** Concatenating arbitrary rounds is insufficient because the last game of one round may share a team with the next round's first game.
- **Odd team count:** The dummy participant creates a standard even-sized rotation; omit every dummy fixture before scheduling.
- **Home and away roles:** Reversing every round supplies the second directed fixture without changing disjointness.
- **Distinct first and last games:** Each block has at least two games for $n\ge5$, allowing all internal and boundary neighbors to remain separate fixtures.
- **Multiple valid outputs:** Correctness depends on fixture coverage and adjacency, not equality with one reference ordering.
