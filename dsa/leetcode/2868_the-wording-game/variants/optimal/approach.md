## General

**Discard dominated words within one initial-letter group**

Fix a player and a first letter. If that player decides to use a word from this group, only the lexicographically greatest word in the group can be useful. It leaves the opponent the smallest possible set of legal replies while keeping the same first letter. Any response legal after the greatest word was also available after a smaller choice; if no such response exists, the greatest word wins immediately. Because every later threshold is larger, skipped smaller words can never become playable again.

Scan both sorted lists and retain the final, therefore greatest, word for each of the 26 possible first letters. Along with Alice's forced opening `a[0]`, these at most 52 representatives contain every strategically relevant move.

**Solve the reduced acyclic game**

Define `can_win(player, last)` as whether the player whose turn it is can force a win after `last` was played. If `last` begins with letter index `c`, the rules permit only two representative candidates for that player: the greatest word beginning with `c`, and the greatest word beginning with `c + 1`. A candidate is legal only when it is lexicographically greater than `last`.

The state is winning if at least one legal candidate leaves the opponent in a losing state. It is losing when neither candidate has that property, including the case where no legal move exists. Memoize results by `(player, last)`.

Every transition strictly increases the played word, so the game graph is acyclic. The recurrence examines both distinct strategic choices rather than always advancing to the next initial: for example, after `"aa"`, Bob should play `"ab"` instead of `"ba"` when Alice holds `"ca"`.

Alice's opening is forced rather than chosen optimally. Evaluate the position with Bob to move after `a[0]`; Alice wins exactly when that state is losing for Bob.

## Complexity detail

Let $S$ be the combined number of characters in all input words. Reading the lists and recording one representative per player and first letter takes $O(S)$ time. The reduced game contains at most $2 \cdot 52$ memoized states, each with two transitions. Its string comparisons are bounded by the same total input representation, so the full time is $O(S)$.

The two 26-entry tables, memo, and recursion depth are bounded by the lowercase English alphabet and therefore use $O(1)$ auxiliary space.

The benchmark uses combined character count $S$ as `size` and supplies fixed-width distinct words from 96 through 1536 characters. The representative-state method scales linearly. A correct implementation that constructs a pairwise word-comparison table completes every tier but exhibits quadratic scaling.

## Alternatives and edge cases

- **Full minimax over every word:** Memoizing every possible last word but scanning an entire list for each state is correct, yet can take quadratic time in the number of words.
- **Pairwise comparison table:** Precomputing which words may follow which others makes transitions explicit but uses quadratic time and space unnecessarily.
- **Always choose the lexicographically greatest legal word:** This can be wrong because advancing to the next initial may unlock a response from the following letter; the two possible initial groups must be evaluated separately.
- **Forced opening:** Alice cannot replace `a[0]` with her greatest word from that initial group on the first turn.
- **Same initial:** A response must still be strictly lexicographically greater; sharing the first letter alone is insufficient.
- **Skipped initial:** A word whose first letter is more than one position after the previous initial is illegal even when the whole word is lexicographically greater.
- **Final letter:** A word beginning with `z` has no next-letter group, leaving only greater `z` words as possible replies.
- **Distinctness:** No tie can occur between Alice's and Bob's representative words because every input word is globally distinct.
