## General

**Always address the leftmost unresolved `X`**

The scan index `i` represents the first position not already handled by an earlier conceptual move. If `s[i]` is `O`, that position needs no work, so the code advances by one.

If `s[i]` is `X`, at least one additional move is unavoidable. Earlier decisions have already handled every index before `i`, and leaving this `X` untouched cannot lead to an all-`O` string. The source counts one move and advances `i` by three.

That jump represents converting the current character and the following two positions to `O`. Their original values do not matter: an `X` becomes `O`, while an `O` remains `O`. Consequently none of those three positions can require another move.

**Why beginning at the current position is the best greedy choice**

Suppose the leftmost unresolved `X` occurs at index `i` and there are at least three positions beginning there. Any successful solution must use some move whose length-three interval covers `i`. Starting the move earlier would spend part of its coverage on positions before `i`, which the scan has already resolved. Starting it at `i` covers `i` and reaches as far to the right as possible, through `i+2`.

There is no penalty for changing an already-`O` character again, so maximizing rightward coverage cannot make a future position harder. This greedy move handles the mandatory current `X` while covering at least as much still-unresolved territory as any alternative move that also covers it.

The code does not construct a mutable copy of the string. The jump is sufficient bookkeeping: after counting the conceptual move, it never inspects the two newly covered positions because their post-move values are known to be `O`.

**The special case near the right boundary**

If the first unresolved `X` is one of the final two characters, a literal window starting at `i` would extend beyond the string. The count is still correct. Because the input length is at least three, choose the last valid window, covering indices `n-3` through `n-1`. It includes the tail `X` and may overlap positions the scan already considered.

That overlap is harmless: applying a move to `O` leaves it `O`, and there are no unprocessed positions beyond the end. The source's `i += 3` should therefore be understood as “this move finishes the remaining tail,” not as constructing an out-of-bounds substring.

**Trace `XXOX`**

At index zero, the character is `X`. One move is mandatory, and the greedy choice conceptually converts indices zero through two, changing `XXO` into `OOO`. The code increments the answer to one and jumps directly to index three.

Index three is another `X`. It lies in the final two positions, so a valid move may select the last three-character window, indices one through three. The first two of those positions are already `O`, and the final `X` becomes `O`. The code increments the answer to two and jumps past the string. This matches the required minimum.

**A lower bound for every counted move**

Whenever the loop encounters an `X` at `i`, that position has not been covered by any previously counted move; otherwise the conceptual result there would already be `O` and the scan would have skipped it as part of a three-position jump. Therefore some new move is necessary to cover it.

Each increment of `ans` can be charged to a different leftmost uncovered `X`. A single future move cannot eliminate the need for two such charged decisions, because the earlier charged position had to be covered before the scan could pass its block. The algorithm's count is thus a lower bound on every valid solution.

**A matching construction for the upper bound**

For each non-tail `X` found by the loop, perform the length-three move starting exactly at that index. For a final-tail `X`, perform the last valid length-three move. These operations are all legal and realize every conceptual jump made by the scan.

After a jump, the covered positions are `O`. After a one-step advance, the inspected position was already `O`. When the index reaches or exceeds the string length, every position has therefore either been originally `O` or covered by one of the counted moves. The counted number of moves is achievable.

Because the same count is both unavoidable and achievable, it is minimum.

**Why runs do not need separate construction**

For a long run of `X` characters, the scan naturally takes one move for each group of up to three positions. A run of length six needs two nonoverlapping moves. A run of length four also needs two moves: the first covers three positions and the second covers the remaining tail position, possibly with overlap.

Separated runs can sometimes be partly covered by one window when the gap is short. The scan already exploits this. For example, encountering an `X` causes a three-position jump even if one of the next positions is `O`, so another `X` within that covered block is resolved without an additional count. Treating runs independently could miss this cross-gap coverage, whereas the left-to-right greedy scan handles it automatically.

**Why no explicit edits are required**

The only future-relevant fact about a chosen move is that its three covered positions no longer contain an unresolved `X`. By jumping over all three, the algorithm never needs to query their modified values. Positions outside the move retain their original characters, which remain available in `s` when the scan reaches them.

This allows the source to preserve the immutable input string and use constant memory.

## Complexity detail

Let $N=\lvert s\rvert$. The index always increases, by one for an `O` or by three for an `X`. No position is revisited by the loop, so there are at most $N$ iterations and the running time is $O(N)$.

Only the integer index `i` and the move counter `ans` are stored. The source does not build a character array, interval list, or dynamic-programming table. Auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Mutate a character array:** Explicitly write `O` into three positions after each move; it is still $O(N)$ but uses $O(N)$ space and performs unnecessary writes.
- **Dynamic programming:** One can model which recent positions are covered, but the forced leftmost-`X` choice makes that machinery unnecessary.
- **Count each run independently:** This can overlook a move that covers `X` characters on both sides of a short `O` gap.
- **All `O` characters:** The loop only takes one-step advances and returns zero.
- **Exactly three `X` characters:** The first iteration counts one move and jumps to the end.
- **A single `X` in the middle:** One move covers it and its two following positions whenever that start is in range.
- **A single `X` at the final index:** Use the final legal three-character window; the source's jump records the correct one move.
- **A tail of one or two unresolved positions:** One final move is enough because it may overlap already resolved positions.
- **Existing `O` inside a chosen block:** It remains `O` and does not waste correctness, even though it occupies coverage.
- **Overlapping moves:** Allowed and sometimes necessary near the end; repeated conversion to `O` has no adverse effect.
- **Long `X` run:** Each move handles the next three unresolved positions, giving the unavoidable ceiling of run length divided by three when no neighboring coverage changes the grouping.
- **Minimum input length:** The guarantee $N\ge3$ ensures a valid final three-character window exists for a tail `X`.
- **Input preservation:** The algorithm reasons about moves without modifying `s`.
