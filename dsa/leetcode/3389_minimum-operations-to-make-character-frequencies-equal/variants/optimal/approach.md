## General

**A good final string chooses one common positive frequency.** For a target `target`, every letter either appears zero times or exactly `target` times. The source tries every target from one through the largest original frequency.

Deleting every character is retained separately as initial `answer = len(s)`. This covers the all-absent outcome and ensures a finite baseline.

**Compress the string to 26 counts.** `frequencies[c]` stores occurrences of each lowercase letter in alphabet order. Alphabet order matters because the only substitution operation changes a letter to its immediate successor.

**Cost of handling one letter alone.** For frequency `f`, two independent choices exist:

- remove the letter completely, costing `f` deletions;
- keep it at target, costing `abs(f-target)` insertions or deletions.

`individual_cost = min(f, abs(f-target))` selects the cheaper goal among zero and target.

**Dynamic program over alphabet positions.** `dp[p]` is the minimum cost for the first `p` letters. From `dp[index]`, the source can handle current letter individually and update `dp[index+1]`.

It may instead handle current and next letters as a pair, updating `dp[index+2]`. Pairing captures the saving from changing surplus copies of the current letter into deficient copies of its immediate successor.

**Evaluate all zero/target goals for a pair.** `current_goal` and `next_goal` each take values zero or target. Without substitutions, adjusting both counts costs

$$
|f-g_1|+|h-g_2|.
$$

Current surplus is `max(f-current_goal,0)` and next deficit is `max(next_goal-h,0)`. One change operation simultaneously removes one current occurrence and supplies one next occurrence, replacing a delete-plus-insert pair of cost two by one operation. The saving is

`min(surplus, deficit)`.

The formula subtracts that saving and takes the cheapest of the four goal combinations.

**Why pairing only adjacent letters matches the operation.** A single change sends letter `c` only to `c+1`. It cannot directly fill a deficit two alphabet positions away. The DP tiles the alphabet with individual positions and disjoint adjacent interactions so each count is assigned once.

**Prevent overlapping pair decisions.** A pair transition jumps from `index` to `index+2`. The next state cannot reuse either letter in another pair. Individual transition advances one. This is the standard path-DP structure for choosing non-overlapping beneficial adjacent edges.

**Try every plausible target.** A target above the maximum original count cannot improve over a smaller boundary target: it requires only additional insertions and offers no new surplus-based conversion savings. Trying one through the maximum is therefore sufficient.

For each target, `dp[26]` is the best cost under the recurrence. The global answer keeps its minimum.

**Interpret the DP as a tiling of the alphabet line.** At position `index`, an individual transition places a one-letter tile. A pair transition places a two-letter tile spanning `index` and `index+1`. Every complete route from `dp[0]` to `dp[26]` covers each alphabet position exactly once. This makes the state meaning concrete and explains why an unreachable infinity entry cannot contribute to a valid full assignment.

**Trace a useful substitution.** If letter `a` has three copies and goal one while `b` has zero copies and goal one, adjusting separately costs two deletions plus one insertion. Changing one surplus `a` to `b` saves one operation, giving cost two.

**Why the source is mathematically organized.** Every final letter count is zero or target. Independent changes use insertion/deletion costs; immediate-successor changes are the only coupling and are priced by pair transitions. The DP minimizes a complete non-overlapping selection for each target, then minimizes over targets and deletion-all.

**Generated-source caveat.** There is no local editorial. This explanation follows the exact recurrence. Its disjoint-pair formulation is a substantive algorithmic assumption; the file contains no separate proof addressing longer chains of successive changes across multiple alphabet positions.

## Complexity detail

Counting characters costs $O(n)$. There are at most `max(frequencies) <= n` target values. Each runs a 26-position DP with constant-size four-goal pair loops, so additional time is $O(26n)=O(n)$ for the fixed alphabet.

The frequency and DP arrays have 26 and 27 entries. Auxiliary space is $O(1)$ with respect to string length, matching the manifest.

## Alternatives and edge cases

- **Delete every character:** Baseline cost `len(s)` is always available.
- **Ignore substitution coupling:** It can overpay by separately deleting surplus and inserting the next letter.
- **All frequencies already equal:** Choosing that target yields zero.
- **One distinct character:** Keeping its existing frequency yields zero.
- **Absent letter:** It may remain zero or be filled to target.
- **Letter `z`:** It has no successor and only receives the individual transition.
- **Surplus without next deficit:** No substitution saving exists.
- **Next deficit without current surplus:** Insertions remain necessary.
- **Target one:** Every retained letter occurs once.
- **Target above maximum:** It is unnecessary and not enumerated.
- **Non-overlapping pairs:** Jumping by two prevents double-use of a count.
- **Complete alphabet coverage:** Every DP path ends at 26 after covering all letters.
- **Delete-versus-adjust:** `individual_cost` explicitly chooses zero count or target count.
- **Counter order:** Counts are copied into fixed alphabet positions before DP.
- **Floating infinity:** It marks unreachable prefixes and cannot beat finite costs.
- **Generated source:** No editorial evidence exists beyond the exact implementation.
