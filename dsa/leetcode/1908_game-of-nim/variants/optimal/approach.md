## General
**Classify positions by their nim-sum**

Let the nim-sum be the bitwise XOR of all pile sizes:

$$
X = \texttt{piles[0]} \mathbin{\oplus} \texttt{piles[1]} \mathbin{\oplus} \cdots \mathbin{\oplus} \texttt{piles[N - 1]}.
$$

A position with $X = 0$ is losing under optimal play. Changing one pile from $a$ stones to a smaller value $b$ changes the total XOR to `0 ^ a ^ b`, which cannot remain zero because $a \ne b$. Thus every legal move from a zero-nim-sum position hands the opponent a nonzero position.

**Find the winning response when the XOR is nonzero**

Suppose $X \ne 0$, and consider the highest bit set in $X$. At least one pile size $a$ also has that bit set. For such a pile, `b = a ^ X` is strictly smaller than $a`, so removing `a - b` stones is legal. Replacing $a$ with $b$ makes the new total XOR equal to `X ^ a ^ b = 0`.

Therefore a player at a nonzero position can always move to a zero position, while a player at a zero position cannot keep the XOR zero. Repeating this response eventually leaves the opponent at the all-zero terminal position. Alice wins exactly when the initial nim-sum is nonzero.

## Complexity detail
The algorithm XORs each of the $N$ pile sizes once, taking $O(N)$ time. The accumulated nim-sum is the only state beyond the loop variable, so the auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Recursive minimax with memoization:** Exploring all smaller values for every pile can solve the tiny stated domain, but its state space grows exponentially with the number and sizes of piles and misses the requested linear-time structure.
- **Two-dimensional win/lose table:** Dynamic programming can classify bounded configurations, but storing configurations is unnecessary once the nim-sum theorem is established.
- **One pile:** Its positive size has a nonzero XOR, so Alice removes the entire pile and wins immediately.
- **Equal pairs:** Two equal piles XOR to zero; more generally, every pile size occurring an even number of times cancels out.
- **Different-looking losing positions:** A zero nim-sum does not require equal piles; `[1,2,3]` is losing because `1 ^ 2 ^ 3` is zero.
