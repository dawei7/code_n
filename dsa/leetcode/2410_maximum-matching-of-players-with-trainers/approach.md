## General

**Give the weakest player the smallest trainer that works**

Sort players by increasing ability and trainers by increasing capacity. Process players from weakest to strongest. For each player, discard trainers that are too weak, then match the first trainer whose capacity is sufficient.

This preserves larger trainers for harder players. Giving the current weak player a stronger trainer while a smaller sufficient one exists cannot increase future options.

**Advance a monotone trainer pointer**

`j` is the index of the first trainer not already consumed or discarded. For current player ability `p`, the loop skips:

```python
while j < n and trainers[j] < p:
    j += 1
```

A skipped trainer cannot serve `p`. Since later players have ability at least `p`, it cannot serve any later player either. Discarding it permanently is safe.

If `j < n` after skipping, `trainers[j] >= p`. This is the smallest remaining sufficient capacity because trainers are sorted. Incrementing `j` consumes it for exactly one match.

**Why players are processed weakest first**

Suppose a valid matching pairs a weak player with a large trainer while a smaller sufficient trainer is unused or assigned to a no-stronger player. Swapping assignments so the weak player takes the smaller trainer does not invalidate either match and leaves at least as much capacity for harder players.

Repeated exchanges transform an optimal matching into the greedy form. Therefore, taking the smallest feasible trainer for each weakest remaining player loses no possible match.

**Interpret the early return**

The loop uses `enumerate(players)`. Before processing player index `i`, every earlier player has been matched, so exactly `i` matches exist.

If `j == n` after skipping weak trainers, no trainer remains for the current player. Later players are at least as demanding, so none can be matched either. Returning `i` is therefore the final maximum count.

If the loop matches every player, it returns `len(players)`. Extra trainers are irrelevant.

**Trace the first example**

Sorted players are `[4,7,9]` and sorted trainers are `[2,5,8,8]`.

- Capacity two is too small for player four and is discarded. Capacity five matches four.
- Capacity eight matches player seven.
- The last capacity eight is too small for player nine. No trainer remains, so the function returns two.

Using an eight for player four would waste capacity five and still leave no trainer for nine, demonstrating why the smallest sufficient choice is sensible.

**Why original identities do not matter**

The output asks only for the number of matches, not the actual index pairs. Sorting changes identity order but preserves the multiset of abilities and capacities, which fully determines whether a one-to-one match is feasible.

Each pointer increment consumes one distinct trainer, and each loop iteration attempts one distinct player, so one-to-one constraints are automatic.

**Formal greedy correctness**

Consider the weakest unmatched player `p`. If no trainer can handle `p`, no stronger player can use the remaining weaker trainers, and failure is final. Otherwise, let `t` be the smallest sufficient trainer.

Take any maximum matching of the remaining participants. If it leaves `p` unmatched while matching a stronger player to some trainer, replacing that stronger player with `p` preserves a match. If `p` is matched to a trainer `u > t`, then either `t` is unused, in which case swap `p` to `t`, or `t` serves another player whose ability is at most `t`; assigning `u` to that player preserves validity. Hence, an optimum exists using greedy pair `(p,t)`.

Removing them leaves the same smaller problem. Induction proves every greedy match is compatible with an optimum, so the final count is maximum.

**Input mutation**

Both `players.sort()` and `trainers.sort()` reorder the caller's lists in place. Original order is not needed by the algorithm. Copy before sorting if external preservation is required.

## Complexity detail

Let $p$ be the number of players and $t$ the number of trainers. Sorting costs $O(p\log p+t\log t)$ time.

The player loop advances its index once per processed player, while trainer pointer `j` advances at most $t$ times total. The scan is $O(p+t)$, dominated by sorting.

Python's in-place sorting may use $O(p+t)$ temporary space in the worst case, matching the manifest. The explicit pointer state is $O(1)$.

## Alternatives and edge cases

- **Largest-first greedy:** Match the strongest player with the smallest capable trainer from the high end. It can also be formulated correctly, but weakest-first two pointers are simpler.
- **Bipartite matching:** General maximum matching is unnecessary because feasibility is totally ordered by numeric thresholds.
- **Trainer too weak for current player:** It is also too weak for every later stronger player and can be discarded.
- **No trainer fits the weakest remaining player:** No later player can be matched, so early return is safe.
- **Equal abilities or capacities:** Sorting and non-strict `<=` matching handle duplicates naturally.
- **More players than trainers:** The answer cannot exceed trainer count, and pointer exhaustion enforces this.
- **More trainers than players:** All players may be matched; extras are unused.
- **Exact equality:** Capacity equal to ability is sufficient.
- **Input mutation:** Both arrays are sorted in place.
