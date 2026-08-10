## General

There is only one heap, each turn removes between one and three stones, and the player who takes the final stone wins. Because both players choose their moves optimally, the question is not whether the first player *might* win after a convenient reply. The question is whether the first player has a move that guarantees a win even when the second player always gives the strongest possible response.

The exact solution is the constant-time test `n % 4 != 0`. To understand why that tiny expression completely solves the game, it helps to classify a position by what the player whose turn it is can force from that position.

**Winning and losing positions**

A position is *winning* when the current player has at least one legal move that leaves the opponent in a losing position. A position is *losing* when every legal move leaves the opponent in a winning position. This distinction is about the player whose turn it is; it does not permanently label one person as the winner or loser.

Start with the smallest heap sizes:

- With one stone, the current player removes one stone and wins immediately.
- With two stones, the current player removes both stones and wins immediately.
- With three stones, the current player removes all three stones and wins immediately.
- With four stones, no immediate win is possible. Removing one, two, or three stones leaves respectively three, two, or one stone. The opponent can remove everything that remains and win.

Thus, sizes one through three are winning, while size four is losing. The next few positions reveal the pattern. From five stones, remove one and leave four. From six, remove two and leave four. From seven, remove three and leave four. Each of those moves hands the opponent the losing four-stone position. With eight stones, however, every legal move leaves five, six, or seven stones, all of which are winning for the next player.

So the classifications repeat in blocks of four:

| Stones modulo 4 | Status for the current player | Useful move |
| --- | --- | --- |
| $0$ | Losing | No legal move reaches another multiple of four |
| $1$ | Winning | Remove 1 |
| $2$ | Winning | Remove 2 |
| $3$ | Winning | Remove 3 |

**Why every nonmultiple of four is winning**

Suppose the heap contains

$$
n = 4q + r,
$$

where the remainder $r$ is one of $1$, $2$, or $3$. Removing exactly $r$ stones is legal, because the game permits removing any amount from one through three. That move leaves

$$
n-r = 4q,
$$

which is a multiple of four. Therefore, from any positive heap size that is not divisible by four, the current player can deliberately move to a multiple of four.

This is not merely a locally convenient move. It establishes control over every later round. If the opponent removes $x$ stones, where $x\in\{1,2,3\}$, the controlling player removes $4-x$ stones. The response is also in the legal range, and the two moves together remove exactly four stones. Consequently, after each such pair of turns, the opponent again receives a multiple of four.

For example, begin with ten stones. The first player removes two, leaving eight. If the opponent then removes one, the first player removes three; if the opponent removes two, the first player removes two; and if the opponent removes three, the first player removes one. In every case the combined removal is four. Repeating this response eventually makes the opponent face four stones. Whatever that opponent removes, the first player removes the remaining stones and wins.

**Why every positive multiple of four is losing**

Now suppose the current heap has $4q$ stones. Any legal move removes a number $x$ in $\{1,2,3\}$, leaving $4q-x$. Its remainder modulo four is respectively three, two, or one, so it is not a multiple of four. The opponent can then use the strategy above: remove $4-x$ stones and restore a multiple-of-four heap for the original player.

This proves both necessary directions. A nonmultiple has a move into the losing class, whereas a multiple has no move that stays in the losing class. The two classifications therefore support one another all the way down to the base position of four stones. There is no unexplored type of position, because every positive integer has exactly one remainder in $\{0,1,2,3\}$ when divided by four.

**How the implementation represents the strategy**

The method does not need to simulate the moves. The return value asks only whether a forced win exists, not which stones should be removed on each turn. `n % 4` computes the remainder after division by four. A zero remainder identifies exactly the losing positions, so `n % 4 != 0` returns `False` for those positions and `True` for all winning ones.

Although the function contains no loop or explicit opponent model, the modulo proof has already accounted for every legal response by both players. The implementation is short because the repeating game structure has been summarized as an invariant, not because moves have been ignored.

## Complexity detail

The solution performs one remainder operation and one comparison, independent of the numeric value of $n$. Under the problem's fixed-width integer model, both operations take constant time, so the time complexity is $O(1)$.

The algorithm creates no array, table, recursion stack, or simulated game history. It keeps only the input and the temporary result of the arithmetic expression, so the auxiliary space complexity is $O(1)$.

It is also useful to distinguish the complexity of the *reasoning* from the complexity of the executed method. We may inspect several small positions and prove a response strategy to discover the pattern, but the final program does not repeat that discovery for each input. Once the invariant has been established, every valid input is classified by the same single modulo calculation.

## Alternatives and edge cases

- **Dynamic programming over every heap size:** Mark sizes one through `n` as winning or losing according to whether they can reach a losing predecessor. This can rediscover the four-position pattern, but it requires $O(n)$ time and $O(n)$ space if the whole table is stored, which is unnecessary for a value as large as $2^{31}-1$.
- **Constant-space iterative classification:** Track only a few recent winning and losing states while advancing from one to `n`. This reduces auxiliary space to $O(1)$ but still spends $O(n)$ time reproducing a pattern that the modulo invariant expresses directly.
- **Recursive game search:** Try each removal and ask recursively whether the opponent loses. Without memoization it repeats many states; with memoization it becomes a slower form of dynamic programming. Neither version is suitable when the mathematical structure already gives a constant-time answer.
- **Always removing three stones:** This does not preserve the winning invariant. The correct first removal depends on the current remainder, and later responses must complement the opponent's removal so that each pair totals four.
- **Confusing this game with general Nim:** Classical multi-heap Nim uses the bitwise XOR of heap sizes. This problem has exactly one heap and permits removing only one to three stones, so the relevant invariant is divisibility by four, not a multi-heap XOR calculation.
- **`n = 1`, `n = 2`, or `n = 3`:** The first player removes the entire heap in one legal move. Their nonzero remainders correctly produce `True`.
- **`n = 4`:** This is the first losing position. Every legal first move gives the opponent a heap small enough to take completely, so the zero remainder correctly produces `False`.
- **A larger multiple of four:** Values such as 8, 12, and 16 remain losing under optimal play. The opponent can complement every removal to make the two turns remove four stones in total.
- **A value immediately after a multiple of four:** For values such as 5 or 9, removing one stone leaves a losing multiple of four. The modulo test correctly returns `True`.
- **The maximum allowed input:** The method neither allocates memory proportional to `n` nor loops `n` times. It handles $2^{31}-1$ with the same constant amount of work as a small input.
- **Positive-input guarantee:** The constraints begin at one, so the implementation does not need to define a game with an initially empty heap. If zero were introduced under the usual rules, it would be losing for the player to move and would also have remainder zero, but that case is outside the stated contract.
- **Optimal-play assumption:** A winning position guarantees that a winning strategy exists. A player can still lose by choosing a poor move, but the requested Boolean assumes that the player follows the force-win strategy.
