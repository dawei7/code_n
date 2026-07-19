## General
**Encode coverage, not team order.** Assign each required skill one bit. Convert every person's skills into an $s$-bit mask, so bitwise OR gives the combined coverage of a team. The target is `full_mask = (1 << s) - 1`.

**Keep the smallest team for each coverage state.** Start with coverage `0` represented by the empty team. Process people one at a time. For every state that existed before considering person `i`, OR its coverage with that person's mask. If the new coverage has no recorded team, or adding `i` produces fewer selected people, replace the state. Iterating over a snapshot prevents one person from being selected repeatedly during the same update.

**Why dominated teams can be discarded.** Two teams with the same skill mask are interchangeable for every future person: any later mask adds exactly the same new coverage to both. Therefore only the smaller team can belong to an optimum. Inductively, after processing each prefix of `people`, every stored state has minimum size among teams drawn from that prefix. The state for `full_mask` at the end is consequently a globally smallest sufficient team.

The implementation stores a selected team as a $p$-bit integer. `team.bit_count()` gives its size, and the set bits are converted back to person indices only once for the final answer.

## Complexity detail
There are at most $2^s$ coverage masks. Each of the $p$ people updates a snapshot of those states with constant-time mask operations, giving $O(p2^s)$ time under the bounded machine-word model used by the constraints. Up to $2^s$ team bitsets are stored, each containing up to $p$ bits, for $O(p2^s)$ bits of space.

## Alternatives and edge cases
- **Enumerate subsets of people:** Testing all $2^p$ teams is correct but depends exponentially on as many as $60$ people instead of at most $16$ skills.
- **Backtracking with pruning:** Skill rarity and dominance pruning can work well on some inputs, but its worst case remains exponential in the number of people and is harder to bound.
- **Person with no skills:** Their mask is zero, so adding them never improves coverage or team size and they can be skipped.
- **Duplicate person masks:** Both indices may be considered, but the DP retains only a minimum-size representative for each resulting coverage.
- **One person covers every skill:** Processing that person creates the full mask with a one-person team, which is immediately optimal.
- **Multiple minimum teams:** The semantic contract accepts any sufficient team whose size is minimum; neither index order nor a particular tie-breaking choice is required.
