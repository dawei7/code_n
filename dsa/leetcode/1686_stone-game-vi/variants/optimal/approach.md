## General
**Measure both the gain and the denial**

A stone's strategic importance is not just its value to the player whose turn it is. Taking stone `i` also prevents the opponent from receiving their value for it. Define its combined priority as

$$
p_i = \texttt{aliceValues[i]} + \texttt{bobValues[i]}.
$$

Consider two stones `i` and `j` assigned across one Alice turn and one Bob turn. If Alice gets `i` and Bob gets `j`, their score difference contribution is `aliceValues[i] - bobValues[j]`. Reversing the assignments gives `aliceValues[j] - bobValues[i]`. The first assignment improves Alice's score difference over the second by exactly $p_i-p_j$.

Thus Alice prefers the larger-priority stone to be hers. Bob reaches the same choice from the opposite objective: taking the larger-priority stone minimizes Alice's attainable difference across that exchange. Both optimal players therefore choose a remaining stone with maximum combined priority, and equal-priority stones may be ordered arbitrarily without changing the exchange value.

**Sort once and alternate ownership**

Sort the stone indices by decreasing $p_i$. Traverse that order. Even-numbered turns belong to Alice, so add her value to a running score difference; odd-numbered turns belong to Bob, so subtract his value. The exchange result shows that any inversion with a smaller priority before a larger one can be corrected without hurting the player moving first in that pair. Repeatedly removing inversions yields the greedy order, proving it represents optimal play.

Finally, only the sign of the score difference matters: positive means Alice wins, negative means Bob wins, and zero means a tie.

## Complexity detail
Computing priorities takes $O(n)$ time, sorting their indices takes $O(n \log n)$ time, and the scoring pass takes $O(n)$. The sorted index list occupies $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Priority queue:** inserting all combined priorities into a max-heap and popping once per turn also takes $O(n \log n)$ time and $O(n)$ space.
- **Repeated maximum search:** scanning all untaken stones on every turn implements the same choice but takes $O(n^2)$ time.
- **Sort by the current player's value:** this ignores the value denied to the opponent and can choose a strategically inferior stone.
- **Equal combined priorities:** either order gives the same two-turn exchange difference, so stable tie-breaking is unnecessary.
- **One stone:** Alice takes it and wins because all values are positive.
- **Winner encoding:** return only the sign comparison, not either player's score or their numeric difference.
