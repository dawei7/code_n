# Stone Game VI

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1686 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Greedy, Sorting, Heap (Priority Queue), Game Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/stone-game-vi/) |

## Problem Description
### Goal

There are $n$ stones. Stone `i` is worth `aliceValues[i]` points if Alice takes it and `bobValues[i]` points if Bob takes it; the same physical stone may therefore have different values to the two players. Alice and Bob alternate taking one remaining stone, Alice moves first, and the chosen stone is removed. The game ends after all stones have been taken.

Both players choose optimally to determine the winner from their personal score totals. Return `1` when Alice finishes with more points, `-1` when Bob finishes with more points, and `0` when the totals are equal. Taking a stone both earns its current player's value and permanently denies the other player that stone's value.

### Function Contract
**Inputs**

- `aliceValues`: a length-$n$ list giving Alice's value for each stone
- `bobValues`: a length-$n$ list giving Bob's value for the corresponding stones

**Return value**

`1` if optimal play makes Alice win, `-1` if it makes Bob win, or `0` for a tie.

### Examples
**Example 1**

- Input: `aliceValues = [1, 3], bobValues = [2, 1]`
- Output: `1`

Alice takes stone 1 for three points; Bob then receives two points from stone 0.

**Example 2**

- Input: `aliceValues = [1, 2], bobValues = [3, 1]`
- Output: `0`

Optimal play gives both players one point.

**Example 3**

- Input: `aliceValues = [2, 4, 3], bobValues = [1, 6, 7]`
- Output: `-1`

Bob can force a strictly larger total.

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

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

#### Complexity detail

Computing priorities takes $O(n)$ time, sorting their indices takes $O(n \log n)$ time, and the scoring pass takes $O(n)$. The sorted index list occupies $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Priority queue:** inserting all combined priorities into a max-heap and popping once per turn also takes $O(n \log n)$ time and $O(n)$ space.
- **Repeated maximum search:** scanning all untaken stones on every turn implements the same choice but takes $O(n^2)$ time.
- **Sort by the current player's value:** this ignores the value denied to the opponent and can choose a strategically inferior stone.
- **Equal combined priorities:** either order gives the same two-turn exchange difference, so stable tie-breaking is unnecessary.
- **One stone:** Alice takes it and wins because all values are positive.
- **Winner encoding:** return only the sign comparison, not either player's score or their numeric difference.

</details>
