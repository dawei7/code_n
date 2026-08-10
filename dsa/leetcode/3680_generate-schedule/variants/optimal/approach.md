## General

The output must contain one directed match for every ordered pair of different teams. There are therefore

$$
n(n-1)
$$

days in every valid schedule. The difficult condition is not generating those matches; it is ordering them so that the two teams used on one day are both absent from the next day's match.

The exact Optimal source solves the problem in two layers:

1. use the circle method to partition all unordered team pairs into round-robin rounds, where matches inside one round are automatically disjoint; and
2. choose the first and last match of every round block so adjacent blocks also have disjoint boundary matches.

Once those boundary choices are known, all remaining games inside a block can appear in any order because no team occurs twice in the same round.

**Why fewer than five teams cannot work**

The implementation immediately returns an empty list when `n < 5`. This is not an arbitrary construction limit.

With two teams, both required directed matches involve the same two teams, so they cannot occupy consecutive days.

With three teams, every pair of teams intersects every other pair: after one match, only one team remains unused, and a second match needs two teams. Thus no legal next day exists.

With four teams, a match between teams $A$ and $B$ has exactly one possible disjoint unordered match: the match between the other teams $C$ and $D$. After $C$ plays $D$, the next match is forced back to the unordered pair $\{A,B\}$. A legal sequence must therefore alternate one pair and its complement. After using both home/away directions of $A$ versus $B$ and both directions of $C$ versus $D$, those four directed matches are exhausted, yet the schedule still needs the matches involving the other pairings. There is no legal way to continue. Hence no valid complete schedule exists for $n=2,3,4$.

For every permitted `n >= 5`, each constructed round contains at least two real matches. That fact is needed later because a block must be able to choose different matches as its first and last elements.

**Building one copy of every unordered matchup**

The circle method works most naturally with an even number of participants. The code sets

`total = n if n % 2 == 0 else n + 1`.

When $n$ is odd, the extra value is a dummy participant representing a bye. It appears in the rotation like a team, but any pair containing the dummy is omitted from `games`.

The list `teams` initially contains `0, 1, ..., total - 1`. During one round, position `index` is paired with the mirrored position `total - 1 - index`. The loop considers `total // 2` such pairs, so every participant appears in exactly one pair that round. After discarding a possible dummy pair, all remaining matches are pairwise disjoint real-team matches.

After recording a round, the arrangement changes to

`[teams[0], teams[-1], *teams[1:-1]]`.

The first participant stays fixed. The last participant moves directly behind it, and the other nonfixed participants shift one position. Repeating this rotation `total - 1` times is the standard circle construction: every participant is mirrored with every other participant exactly once. Consequently:

- for even $n$, every unordered pair of real teams occurs in exactly one round;
- for odd $n$, every real team meets the dummy once, producing one bye, while every unordered pair of real teams still occurs exactly once.

At this point, `rounds` covers every matchup without home/away direction. A match is stored as `(home, away)` according to its positions in the current arrangement.

**Creating both home and away fixtures**

For each round `games`, the solution appends two blocks to `all_rounds`:

1. the original list of `(home, away)` pairs; and
2. a list containing `(away, home)` for every original pair.

Thus each unordered pair appears once in each direction. Reversing the tuple changes the home team but not the two participating teams, so the disjointness property inside every block is preserved.

Simply concatenating these blocks in their current list order would not be enough. The final match of one block might share a team with the first match of the next block. The rest of the source is devoted to choosing a safe order for each block.

**What a boundary state means**

Suppose one block contains $q$ pairwise disjoint games. If indices `first` and `last` are different, the block can be ordered as:

- game `first`;
- all games whose indices are neither `first` nor `last`, in their existing order; and
- game `last`.

All neighboring games within that order are disjoint because every two different games in the block are disjoint. Therefore, the interior order needs no further search. Only the block's first game must be compatible with the preceding block's chosen last game.

For each block, `states` is a dictionary keyed by a possible `last` game index. An entry

`states[last] = (previous_last, first)`

means there is a valid ordering through this block such that:

- the preceding block ends with game `previous_last`;
- this block begins with game `first`;
- those two boundary games are disjoint; and
- this block ends with game `last`.

The dictionary value is also a parent link. It remembers enough information to reconstruct the actual choices after all blocks have been processed.

The first block has no preceding boundary. For every possible last index, the code selects index $0$ as the first game unless the last game is already index $0$; in that case it uses index $1$. Because `n >= 5` guarantees at least two real games per block, these indices exist and are different.

**Finding supported first games in later blocks**

For a later block, the code examines up to three reachable last-game indices from `previous_states`:

`previous_options = list(previous_states)[:3]`

For every candidate `first` game in the current block, it searches those options for a previous game having no team in common. A successful pair is recorded in `supported_firsts`.

Why can three previous options be enough? All games in the previous block are pairwise disjoint. A current game contains exactly two teams, so it can intersect at most two previous games—at most one containing its first team and at most one containing its second team. Among any three distinct previous games, at least one must therefore be disjoint from the current game.

For `n >= 6`, every block has at least three games. The first block creates a state for every last index. If the previous block has at least three reachable last choices, the argument above gives support to every possible first game in the current block. Since the current block also has at least two games, every desired last index can choose a supported first index different from itself. This restores a state for every last index, so the reasoning continues inductively through all blocks.

The smallest constructive case, `n = 5`, has only two real games per round because the sixth rotating participant is the dummy. The implementation then examines all reachable previous states rather than three. Some blocks retain only one possible ending, but the specific five-team circle sequence preserves a compatible chain. In the generated ten blocks, reconstruction uses game-index order `(0, 1)` for the first six blocks and `(1, 0)` for the final four. This is why the general parent-state machinery also handles the two-game boundary case without a separate hard-coded schedule.

After collecting supported first choices, the solution considers every candidate `last`. It takes the first supported pair whose `first` differs from `last`. That difference is essential: a game cannot occupy both ends of a block unless the block contains only one game, and such blocks were excluded by `n < 5`. The selected tuple is saved as the parent entry for this last index.

**Reconstructing the schedule**

After the forward pass, any key in the final `previous_states` represents a reachable ending. The source selects one with `next(iter(previous_states))`.

It then walks backward through `parents`. If the current chosen ending is `last`, the stored value gives both the block's `first` and the preceding block's required `previous_last`. The pair `(first, last)` is saved in `choices`, and backtracking continues with `previous_last`.

Finally, each block is emitted using its chosen first game, every interior game, and its chosen last game. There are two reasons no consecutive conflict can appear:

- inside a block, every pair of different games is disjoint by the round-robin construction; and
- across a block boundary, the parent state was created only after checking that the preceding last game and current first game have disjoint team sets.

Coverage is also exact. The circle construction generates each unordered real-team pair once, and the two orientation blocks generate each ordered pair once. Reordering a block never creates or removes a match. The returned list therefore contains exactly $n(n-1)$ directed matches, with every team playing every opponent once at home and once away.

## Complexity detail

Let $T$ be `total`, the smallest even integer at least $n$. Since $T$ is either $n$ or $n+1$, $T=O(n)$.

There are $T-1$ circle rounds. Each round examines $T/2$ mirrored pairs, so generating `rounds` takes $O(T^2)=O(n^2)$ time. Creating the original and reversed blocks in `all_rounds` also copies $O(n^2)$ matches.

There are $2(T-1)=O(n)$ blocks, and each contains $O(n)$ games. For one later block, every current game checks at most three previous options, so building `supported_firsts` is $O(n)$. When producing states, the source scans supported first choices only until it finds one different from the desired last. Because first indices are unique, either the first entry already differs or at most the next entry does; if only one supported entry exists, it is checked once. Thus this phase is also $O(n)$ per block, not $O(n^2)$ per block. Across all blocks, the state pass takes $O(n^2)$ time.

Backtracking chooses one boundary pair per block in $O(n)$ time. Emitting the answer visits every match once and therefore takes $O(n^2)$ time. The total time complexity is $O(n^2)$. This is asymptotically optimal because the required output itself contains $n(n-1)=\Theta(n^2)$ matches.

The stored round lists, doubled block lists, parent dictionaries, and final schedule each contain $O(n^2)$ total entries. Consequently, auxiliary storage is $O(n^2)$, and the returned output is also $O(n^2)$. Even an implementation with less temporary storage would still require $\Theta(n^2)$ space for the returned schedule.

## Alternatives and edge cases

- **Naively concatenate circle rounds:** The circle method guarantees disjoint games within a round, but the last game of one round may overlap the first game of the next. Boundary ordering is still required.
- **Backtrack over every match permutation:** Trying arbitrary orders among all $n(n-1)$ directed games creates an enormous factorial search space. Grouping games into disjoint round blocks reduces the only choices that matter to block boundaries.
- **Search every previous ending:** It is valid to compare a current first game with all reachable previous endings, but unnecessary for blocks of at least three games. A two-team current match can conflict with at most two pairwise disjoint previous games, so three candidates suffice.
- **Use a separately derived closed-form order:** A direct constructive formula could avoid parent dictionaries, but it would require its own careful boundary derivation for even and odd $n$. The exact source uses the more explicit reachable-state reconstruction.
- **Odd `n`:** The dummy participant creates one bye per circle round. Dummy pairs are omitted, and no dummy identifier can enter the returned schedule.
- **`n = 5`:** Every block has exactly two real games. The state set can narrow to one ending, but the generated block sequence retains a complete compatible chain, which backtracking recovers.
- **`n = 6`:** This is the first case with three games per block, so the “at most two conflicts among three previous games” argument applies directly.
- **Different home and away days:** The reversed fixture is placed in a separate block. The two directions of a matchup both appear exactly once; they are not treated as interchangeable.
- **First block:** It has no preceding match, so only distinct first and last indices matter. The initialization uses indices $0$ and $1$ to ensure that distinction.
- **Output lower bound:** Because every ordered pair must be written, no valid algorithm can run in asymptotically less than $\Omega(n^2)$ time when output construction is included.
