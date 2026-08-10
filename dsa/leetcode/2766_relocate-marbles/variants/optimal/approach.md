## General

**Track occupied positions, not individual marbles**

The output asks only which positions are occupied after all moves. It does not ask how many marbles occupy each position. That distinction allows the exact solution to represent the entire state with a set of coordinates.

`pos = set(nums)` removes duplicate initial coordinates. If several marbles start at position 3, the set stores 3 once, which is sufficient to answer whether position 3 is occupied. The number of marbles at that coordinate never affects future decisions because each operation moves all marbles from its source together.

This is the main compression: potentially many physical marbles at the same coordinate have identical movement histories until they merge with others, and the required result treats any positive count identically.

**Simulate one move as a set transfer**

The paired loops `for f, t in zip(moveFrom, moveTo)` process operations in their given chronological order. For each source `f` and destination `t`:

1. `pos.remove(f)` marks the source unoccupied.
2. `pos.add(t)` marks the destination occupied.

The contract guarantees that at least one marble is at `f` when the operation is applied. Therefore `f` must be present in the set, and `remove` will not raise an error on valid input.

If `t` is already occupied, adding it again changes nothing. That is exactly right: the moved marbles join the marbles already there, but the output still needs only one copy of the coordinate.

If `f == t`, removal temporarily clears the coordinate and addition immediately restores it. The net occupied set is unchanged, matching the fact that moving all marbles from a position to the same position has no observable effect.

**Why multiplicities can never become relevant later**

It may seem dangerous to forget counts because a later operation could move marbles away again. However, every later move also transfers all marbles at its source. Whether one marble or a thousand occupy that coordinate, after that move the source is empty and the destination is occupied. The transition on occupied positions is identical:

$$
P' = (P \setminus \{f\}) \cup \{t\}.
$$

There is no operation that moves only one marble, tests a count, or splits the marbles at a coordinate across destinations. Therefore counts have no influence on any future occupied-set transition.

**An invariant across the operation sequence**

After processing the first `q` moves, let `P_q` be the set held in `pos`. The useful invariant is:

`p` belongs to `P_q` if and only if at least one real marble occupies position `p` after those `q` moves.

It is true initially because `set(nums)` contains exactly the distinct occupied starting positions. Suppose it is true before the next move from `f` to `t`. The guarantee says `f` is occupied, and moving all its marbles makes it unoccupied, which `remove(f)` records. The destination becomes occupied whether it was empty or occupied already, which `add(t)` records. Every other position is unchanged. The invariant therefore remains true after the move.

By induction, the final set exactly represents the final occupied positions.

**Why operation order matters**

Moves cannot be applied as a collection of independent replacements. A destination from an early step can become the source of a later step. In the first reference example, marbles move from position 1 to 2, and a later operation moves all marbles from 2 to 5. Processing the arrays in order causes the newly occupied 2 to be available and then removed at the correct time.

The use of `zip` aligns `moveFrom[q]` with `moveTo[q]`. Their equal length is guaranteed, so no operation is lost due to one iterable ending early.

**Produce the required ordering only once**

A Python set has no sorted iteration guarantee. After all state changes are complete, `sorted(pos)` returns a new list of distinct final coordinates in increasing numerical order.

Sorting after the simulation is more direct than maintaining a sorted structure during every move. The operations require only membership removal and insertion; ordering becomes relevant only for the final output. This gives constant expected-time updates and pays the comparison-sorting cost once.

**A merging walkthrough**

For `nums = [1, 1, 3, 3]`, the initial set is `{1, 3}`. Moving from 1 to 2 changes it to `{2, 3}`. This represents two marbles at 2 and two at 3, although counts are not stored. Moving from 3 to 2 removes 3 and adds the already-present 2, leaving `{2}`. Sorting returns `[2]`, exactly the only occupied coordinate.

The set did not need to know that four marbles ended at 2. It only needed to preserve the fact that at least one did.

## Complexity detail

Let `n` be `nums.length`, `m` be the number of moves, and `k` be the number of final occupied positions. Building `set(nums)` takes `O(n)` expected time. Every move performs one hash-set removal and one insertion, each `O(1)` expected, for `O(m)` expected simulation time. Sorting the final `k` distinct coordinates costs `O(k log k)`. Total expected time is

$$
O(n + m + k \log k).
$$

The occupied set never contains more distinct coordinates than the number of initially distinct coordinates: a move removes one occupied source and adds at most one destination, and merging can reduce the size. Thus it stores at most `n` entries and uses `O(n)` auxiliary space. The returned sorted list contains `k` entries. If output storage is counted separately, working space remains `O(n)`; including output does not exceed `O(n)` because `k <= n`.

Hash-set bounds are expected rather than comparison-tree worst-case bounds. Python's built-in set is the exact data structure used by the solution.

## Alternatives and edge cases

- **Frequency map of marble counts:** It can simulate exact quantities, but counts are never queried and every move transfers the complete source count. A set contains all information needed for the output and future transitions.
- **Move every marble individually:** This repeats work for duplicates and can become much more expensive when many marbles share a coordinate.
- **Maintain a sorted set throughout:** It supports ordered output but makes each update logarithmic. Hash updates plus one final sort are simpler and match the exact code.
- **Sort after every move:** Intermediate order is irrelevant, so repeated sorting wastes work.
- **Destination already occupied:** `add` is idempotent; the two marble groups merge into one occupied coordinate.
- **Source equals destination:** Remove followed by add restores the same set.
- **Duplicate initial positions:** `set(nums)` intentionally collapses them because occupation is Boolean.
- **Later move uses an earlier destination:** Sequential processing preserves that dependency exactly.
- **Large or negative coordinate considerations:** The given coordinates are positive up to `10^9`, and hashing avoids allocating an array indexed by coordinate.
- **Guaranteed occupied source:** `remove` is appropriate because invalid absence need not be handled; `discard` would silently hide a broken precondition.
- **Equal move-array lengths:** `zip` covers every operation under the contract. Unequal arrays would be truncated, but that input is excluded.
- **Final set has one coordinate:** Sorting returns a one-element list, including after many merges.
