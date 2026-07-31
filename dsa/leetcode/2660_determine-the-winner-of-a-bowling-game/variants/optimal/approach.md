## General

Score each player's turns independently. At index `i`, the current pin count is doubled exactly when `rolls[i - 1]` is `10` or, when it exists, `rolls[i - 2]` is `10`. No other earlier turn can influence the current value, so checking these two positions completely implements the rule.

Add the weighted value to a running total and repeat for every index. The first turn can never be doubled because it has no predecessor; the second turn can depend only on index `0`. Consecutive strikes do not multiply a turn more than twice: the condition asks whether either qualifying predecessor is a strike, not how many are strikes.

For every turn, the algorithm applies multiplier two precisely under the stated condition and multiplier one otherwise, so the accumulated total is the player's score. Comparing the two independently correct totals directly yields `1`, `2`, or `0` as required.

## Complexity detail

Let $n$ be the number of turns. Each of the two arrays is scanned once and every turn uses constant work, so the total running time is $O(n)$. Only scalar totals and indices are stored, giving $O(1)$ auxiliary space.

The benchmark scales `size` as $n$. A correct alternative that scans the entire earlier history at every turn while filtering for the last two indices completes all legal tiers but takes $O(n^2)$ time.

## Alternatives and edge cases

- **Two-turn bonus counter:** Track how many future turns remain doubled, decreasing the counter after each score and resetting it to two after a strike. This is also linear but requires careful update ordering when strikes are consecutive.
- **Rescan all prior turns:** Searching the whole prefix for a qualifying strike is correct if older turns are filtered out, but unnecessarily costs $O(n^2)$ time.
- A strike is not automatically doubled on the turn in which it occurs; only earlier strikes affect it.
- Either or both of the preceding two turns may be strikes, but the multiplier remains exactly two.
- A strike's effect expires after two later turns.
- Equal total scores return `0`, regardless of how differently the players obtained them.
