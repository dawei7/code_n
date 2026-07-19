## General
**Sort to expose the best exchange at each end.** After sorting token values, keep `left` at the cheapest unplayed token and `right` at the most expensive. Also track the current score and the greatest score seen.

If the current power can pay for `ordered[left]`, play that token face-up, advance `left`, and increase the score. Among all affordable face-up choices, the cheapest token gives the same one-point gain while leaving at least as much power for every future action, so choosing it cannot reduce the best attainable score.

If the cheapest token is unaffordable, no remaining token can be bought. When the score is positive and at least two tokens remain, play `ordered[right]` face-down and retreat `right`. Every face-down play costs the same one score, so selling the largest token supplies at least as much power as selling any other token and dominates those alternatives. If neither action is possible, or only one unaffordable token remains, stop.

These exchange arguments allow an optimal play sequence to be transformed so that every face-up play uses the current minimum and every necessary face-down play uses the current maximum. The two-pointer simulation therefore explores an optimal canonical sequence. Record the maximum after face-up plays because a later power trade temporarily lowers the current score.

## Complexity detail
Sorting $n$ token values costs $O(n\log n)$ time, and the two pointers consume each token at most once in $O(n)$ additional time. The sorted copy contains $n$ values, giving $O(n)$ space.

## Alternatives and edge cases
- **Sort the input in place:** The same greedy scan can avoid the explicit copied list when mutation is allowed, though the language's sorting implementation may still use auxiliary memory.
- **Search all play sequences:** Dynamic programming or backtracking over token subsets can find the optimum but has exponential state growth.
- **Repeatedly scan for extremes:** Find the cheapest affordable and largest sellable token by scanning all unplayed tokens before every move. It preserves the greedy choices but takes $O(n^2)$ time.
- **Empty bag:** No move is available, so the score remains zero.
- **Zero-valued tokens:** Each can be played face-up without reducing power and contributes one score.
- **Cannot make the first purchase:** With score zero, no face-down play is legal, so the answer is zero.
- **One unaffordable token remains:** Selling it would lower the score without leaving another token to buy, so stopping preserves the maximum.
- **Maximum versus final score:** A valid strategy may trade away a point after reaching its best score; the returned value is the peak, not necessarily the score after every chosen play.
