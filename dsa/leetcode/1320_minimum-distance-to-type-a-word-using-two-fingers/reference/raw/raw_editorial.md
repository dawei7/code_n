### Approach 1: Dynamic Programming

#### Intuition

We define `dp[i][l][r]` as the minimum movement distance required to reach a state where, after typing the `i`-th character of the string `word`, the left hand is at position `l` and the right hand is at position `r`. Here, the position refers to the index of the character, for example, `A` corresponds to `0`, `B` corresponds to `1`, and so on. This representation maps characters to integers instead of using 2D keyboard coordinates, which simplifies state transitions.

Now, how do we perform the state transitions?

We first observe an important property: for any state `dp[i][l][r]`, either `word[i] == l` or `word[i] == r`. In other words, after typing the `i`-th character, at least one of the hands must be at the position of `word[i]`.

We consider the transitions based on these two cases:

* When `word[i] == l`, the left hand is at the position of `word[i]`. We consider where the `i - 1`-th character was typed:

  * If the left hand was at `word[i - 1]`, then it moves from `word[i - 1]` to `word[i]`:

    

#### Implementation


```python
class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)
        BIG = 2**30
        dp = [[[BIG] * 26 for x in range(26)] for y in range(n)]
        for i in range(26):
            dp[0][i][ord(word[0]) - 65] = 0
            dp[0][ord(word[0]) - 65][i] = 0

        def getDistance(p, q):
            x1, y1 = p // 6, p % 6
            x2, y2 = q // 6, q % 6
            return abs(x1 - x2) + abs(y1 - y2)

        for i in range(1, n):
            cur, prev = ord(word[i]) - 65, ord(word[i - 1]) - 65
            d = getDistance(prev, cur)
            for j in range(26):
                dp[i][cur][j] = min(dp[i][cur][j], dp[i - 1][prev][j] + d)
                dp[i][j][cur] = min(dp[i][j][cur], dp[i - 1][j][prev] + d)
                if prev == j:
                    for k in range(26):
                        d0 = getDistance(k, cur)
                        dp[i][cur][j] = min(dp[i][cur][j], dp[i - 1][k][j] + d0)
                        dp[i][j][cur] = min(dp[i][j][cur], dp[i - 1][j][k] + d0)

        ans = min(min(dp[n - 1][x]) for x in range(26))
        return ans
```


#### Complexity Analysis

Let $N$ be the length of the string `word`, and $|\Sigma| = 26$.

* Time complexity: $O(|\Sigma|N)$

  For each index `i`, we iterate over all possible positions. Each transition takes constant time or iterates over $|\Sigma|$, leading to an overall complexity of $O(|\Sigma|N)$.

* Space complexity: $O(|\Sigma|^2 N)$

---

### Approach 2: Dynamic Programming + Space Optimization

#### Intuition

From Approach 1, recall the key property: for any state `dp[i][l][r]`, either `word[i] == l` or `word[i] == r`. This means that for each `i`, we only need to store $2|\Sigma|$ states instead of $|\Sigma|^2$.

We can redefine the state as `dp[i][op][rest]`, where:

* `op = 0` means the left hand is at `word[i]`
* `op = 1` means the right hand is at `word[i]`
* `rest` represents the position of the other hand

We can simplify this further by observing symmetry. Swapping the roles of the left and right hands does not change the total movement cost. Therefore, `dp[i][op = 0][rest]` and `dp[i][op = 1][rest]` are always equal.

This allows us to reduce the state to `dp[i][rest]`, which represents the minimum movement cost when one hand is at `word[i]` and the other is at position `rest`. We no longer need to distinguish between left and right hands.

#### Implementation


```python
class Solution:
    def minimumDistance(self, word: str) -> int:
        n = len(word)
        BIG = 2**30
        dp = [[0] * 26] + [[BIG] * 26 for _ in range(n - 1)]

        def getDistance(p, q):
            x1, y1 = p // 6, p % 6
            x2, y2 = q // 6, q % 6
            return abs(x1 - x2) + abs(y1 - y2)

        for i in range(1, n):
            cur, prev = ord(word[i]) - 65, ord(word[i - 1]) - 65
            d = getDistance(prev, cur)
            for j in range(26):
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + d)
                if prev == j:
                    for k in range(26):
                        d0 = getDistance(k, cur)
                        dp[i][j] = min(dp[i][j], dp[i - 1][k] + d0)

        ans = min(dp[n - 1])
        return ans
```


#### Complexity Analysis

- Time complexity: $O(|\Sigma|N)$.

- Space complexity: $O(|\Sigma|N)$.

---