
## Solution
---
### Approach 1: Dynamic Programming

**Intuition**

Let's change the game so that whenever Bob scores points, it deducts from Alice's score instead.

Let `dp(i, j)` be the largest score Alice can achieve where the piles remaining are $\text{piles}[i], piles[i+1], ..., \text{piles}[j]$.  This is natural in games with scoring: we want to know what the value of each position of the game is.

We can formulate a recursion for `dp(i, j)` in terms of `dp(i+1, j)` and `dp(i, j-1)`, and we can use dynamic programming to not repeat work in this recursion.  (This approach can output the correct answer, because the states form a DAG (directed acyclic graph).)

**Algorithm**

When the piles remaining are $\text{piles}[i], piles[i+1], ..., \text{piles}[j]$, the player who's turn it is has at most 2 moves.

The person who's turn it is can be found by comparing `j-i` to `N` modulo 2.

If the player is Alice, then she either takes $\text{piles}[i]$ or $\text{piles}[j]$, increasing her score by that amount.  Afterwards, the total score is either $\text{piles}[i] + dp(i+1, j)$, or $\text{piles}[j] + dp(i, j-1)$; and we want the maximum possible score.

If the player is Bob, then he either takes $\text{piles}[i]$ or $\text{piles}[j]$, decreasing Alice's score by that amount.  Afterwards, the total score is either $-\text{piles}[i] + dp(i+1, j)$, or $-\text{piles}[j] + dp(i, j-1)$; and we want the *minimum* possible score.

```python
from functools import lru_cache

class Solution:
    def stoneGame(self, piles):
        N = len(piles)

        @lru_cache(None)
        def dp(i, j):
            # The value of the game [piles[i], piles[i+1], ..., piles[j]].
            if i > j: return 0
            parity = (j - i - N) % 2
            if parity == 1:  # first player
                return max(piles[i] + dp(i+1,j), piles[j] + dp(i,j-1))
            else:
                return min(-piles[i] + dp(i+1,j), -piles[j] + dp(i,j-1))

        return dp(0, N - 1) > 0
```

**Complexity Analysis**

* Time Complexity:  $O(N^2)$, where $N$ is the number of piles.

* Space Complexity:  $O(N^2)$, the space used storing the intermediate results of each subgame.
<br />
<br />

---
### Approach 2: Mathematical

**Intuition and Algorithm**

Alice clearly always wins the 2 pile game.  With some effort, we can see that she always wins the 4 pile game.

If Alice takes the first pile initially, she can always take the third pile.  If she takes the fourth pile initially, she can always take the second pile.  At least one of $first + third, second + fourth$ is larger, so she can always win.

We can extend this idea to `N` piles.  Say the first, third, fifth, seventh, etc. piles are white, and the second, fourth, sixth, eighth, etc. piles are black.  Alice can always take either all white piles or all black piles, and one of the colors must have a sum number of stones larger than the other color.

Hence, Alice always wins the game.

```python
class Solution:
    def stoneGame(self, piles):
        return True
```

**Complexity Analysis**

* Time and Space Complexity:  $O(1)$.
<br />
<br />