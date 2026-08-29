## General

**Measure each stone’s total strategic importance**

Taking stone `i` has two effects: the current player gains their own value, and the opponent permanently loses the chance to gain their value for that same stone. If Alice takes it, the swing in Alice’s score minus Bob’s score is `aliceValues[i]` compared with letting Bob later gain `bobValues[i]`. Its combined strategic importance is therefore

$$
\texttt{aliceValues[i]}+\texttt{bobValues[i]}.
$$

Both optimal players should prioritize the remaining stone with the largest combined value. The source builds `vals` as pairs of this sum and the original index, then sorts them in descending order.

**Why descending combined value is the correct game order**

Consider two stones `i` and `j` that will be taken on consecutive turns, first by Alice and then by Bob. If the order is `i` then `j`, their contribution to Alice-minus-Bob is

$$
a_i-b_j.
$$

If the order is reversed, it is

$$
a_j-b_i.
$$

The first order is at least as good for Alice precisely when

$$
a_i-b_j \ge a_j-b_i,
$$

which rearranges to

$$
a_i+b_i \ge a_j+b_j.
$$

Thus a larger combined-value stone belongs earlier. The same comparison reflects Bob’s optimal denial objective on Bob’s turn: choosing a large combined value prevents Alice from receiving a valuable stone as well as collecting Bob’s own value.

Repeated adjacent exchanges transform any take order into descending combined value without worsening the player whose turn owns the earlier position. This gives the optimal-play ordering.

**Assign alternating positions**

Alice moves first, so she receives stones at sorted positions zero, two, four, and so on. Bob receives positions one, three, five, and so on.

The source computes:

`a = sum(aliceValues[i] for _, i in vals[::2])`

and

`b = sum(bobValues[i] for _, i in vals[1::2])`.

The stored original index is necessary because the combined priority is not either player’s actual score. Once a stone is assigned to a turn, its owner receives the value from their own array.

**Why ties in combined value do not matter**

`vals.sort(reverse=True)` sorts tuple pairs, so equal combined values are secondarily ordered by index descending. That tie rule is incidental.

If two stones have equal sums, then

$$
(a_i-b_j)-(a_j-b_i)
=(a_i+b_i)-(a_j+b_j)
=0.
$$

Swapping their adjacent Alice/Bob assignments leaves the final score difference unchanged. Any deterministic tie order therefore produces the same winner, even if individual totals differ.

**Determine only the requested outcome**

After summing scores, the method returns one if `a > b`, minus one if `a < b`, and zero otherwise. The exact totals are intermediate information; the contract asks only which player wins or whether they tie.

For `aliceValues = [1, 3]` and `bobValues = [2, 1]`, combined values are three and four. The second stone is first, so Alice gets three points; Bob receives the first stone for two, and Alice wins.

**Why the strategy is globally optimal**

The two-stone exchange establishes that whenever a smaller combined-value stone precedes a larger one, swapping them improves or preserves the outcome for the player occupying the earlier turn relative to the alternating zero-sum score difference. Sorting removes all such inversions.

Once stones are in this order, neither player can improve the eventual score difference by choosing a lower-priority remaining stone over the highest-priority one: doing so creates exactly such an inversion with the opponent’s next opportunity. Therefore optimal play follows the sorted sequence, and alternating ownership computes the resulting scores correctly.

## Complexity detail

Let `n` be the number of stones. Building `vals` takes $O(n)$ time and $O(n)$ space. Sorting takes $O(n\log n)$ time.

The two slices `vals[::2]` and `vals[1::2]` create lists containing the alternating tuples, and the generators sum their referenced player values in $O(n)$ total time. These slices use $O(n)$ additional temporary space. Total auxiliary space remains $O(n)$.

The overall time bound is $O(n\log n)$, dominated by sorting.

## Alternatives and edge cases

- **Sort indices by combined value:** This avoids storing the sum in each tuple but still needs an $O(n)$ index list and $O(n\log n)$ time.
- **Priority queue:** Repeatedly pop the largest combined value for alternating turns. It has the same $O(n\log n)$ time and more per-operation overhead.
- **Sort by Alice’s value alone:** This ignores the value denied to Bob and can choose a strategically inferior stone.
- **Sort by value difference:** The pairwise exchange derives the sum, not `a_i-b_i`; using the difference is incorrect.
- **One stone:** Alice takes it and wins because all values are positive.
- **Even number of stones:** Both players take the same count, but their scores can still differ.
- **Odd number of stones:** Alice receives one extra stone because she starts.
- **Equal combined priorities:** Any order among them gives the same Alice-minus-Bob contribution across their turn slots.
- **Equal final scores:** The source returns zero exactly for a draw.
- **Positive values:** Scores are nonnegative and every stone is taken; no pass action is available or useful.
- **Input preservation:** The source sorts a new `vals` list and does not reorder either value array.
- **Slice allocation:** A more memory-conscious loop could iterate through `vals` once and add to Alice or Bob by parity, but the exact source materializes the two slices.
