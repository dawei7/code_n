## General

**Track the active player with one Boolean**

Only the identity of the active player and the current score difference are needed. Initialize the Boolean to indicate that the first player is active. For game `index`, toggle it when the point value is odd, then toggle it again when `(index + 1) % 6 == 0`. Keeping these checks separate preserves the source rule that an odd-valued sixth game swaps twice.

**Update the difference directly**

There is no need to store two score totals. After the swaps, add the game's points to `difference` if the first player is active and subtract them if the second player is active. This signed update has exactly the same effect as adding to one of two totals and subtracting those totals at the end.

Before each iteration, the Boolean names the player left active by all preceding games, and `difference` equals the first player's accumulated score minus the second player's accumulated score. The two conditional toggles reproduce the current game's role changes in their required order. The signed addition then assigns every point from that game to exactly the resulting active player, preserving both facts for the next iteration. After the final game, the maintained difference is therefore the requested result.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. The algorithm performs a constant amount of work for each game, so its time complexity is $O(N)$. It stores only the active-player flag, loop values, and running difference, giving $O(1)$ auxiliary space.

The benchmark defines size as $N$ and repeats a six-game pattern containing both odd and even values. A one-pass simulation retains linear growth, whereas a correct control that recomputes the complete result for every successive prefix repeats earlier games and takes $O(N^2)$ time.

## Alternatives and edge cases

- **Two explicit score totals:** Accumulating `first_score` and `second_score` is also $O(N)$ and may mirror the story more literally, but the signed difference is sufficient state.
- **Prefix recomputation:** Re-simulating every prefix eventually produces the correct full-array difference, but repeats earlier games and requires $O(N^2)$ time.
- **Odd sixth game:** Both swap rules apply. Two toggles cancel; combining the conditions with logical OR would incorrectly perform only one swap.
- **Rule timing:** All applicable swaps happen before points are awarded, so scoring before a toggle assigns the game to the wrong player.
- **Zero-based index:** The sixth-game rule first applies at index `5`, not index `6`.
- **Negative result:** The running difference and final answer may be negative even though every point value is positive.
- **Single game:** An odd first value goes to the second player, while an even first value remains with the initially active first player.
