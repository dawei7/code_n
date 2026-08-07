[TOC]

## Solution

---

### Overview

Stone Game is a turn-based game where the goal is to take more stones than the other player. The players can see how many stones are in each pile from the beginning of the game, so the key is to make strategic choices each turn while following the game rules:

1. Alice always goes first. 
2. On the first turn, Alice can take either 1 pile of stones or 2 piles from the front of the row. 
3. On every following turn, the player can take between 1 and double what the previous person took before (always starting from the front of the row). For example:
- If Alice takes 1 pile during the first turn, Bob can take either 1 pile or 2 piles on his turn. 
- If Alice takes 2 piles during the first turn, Bob can take anywhere between 1 to 4 piles.
4. On turn three, Alice could take between 1-8 piles, depending on Bob’s choice. 

With our knowledge of the number of stones in each pile, we need to figure out the largest possible number of stones Alice can take in the game. 

Note: Bob is a mastermind at this game. We can assume he will make every right move to limit Alice’s overall total with his decisions. 

Let’s consider an example where the piles of stones are `[2, 7, 9, 4, 4]`.

Alice starts with $M = 1$, so she can take either one or two piles. After her turn, $M$ is updated to the number of piles she picked.

- Alice’s Strategy:
  1. Alice can take the first pile (2 stones). If she does this, Bob can take up to $2 \times M = 2$ piles on his turn. Let’s say Bob takes the next two piles (7 and 9 stones).
  2. Alice is left with the last two piles (4 and 4 stones). She takes both, giving her a total of `2 + 4 + 4 = 10` stones.

- Alternative Strategy:
  1. Alice could start by taking the first two piles (2 and 7 stones), leaving Bob with the last three piles (since $2 \times M = 2 \times 2 = 4$). Bob can then take all three remaining piles (9, 4, 4 stones).
  2. In this scenario, Alice would only get `2 + 7 = 9` stones.

The problem is essentially a two-player game where both players (Alice and Bob) aim to maximize their gains while minimizing their opponent's gains. This is a classic scenario where the minimax principle is applied. The minimax principle states that:
- Each player makes the optimal move to maximize their own payoff while assuming the opponent is also playing optimally to minimize their payoff.
- Alice aims to maximize her final score, while Bob aims to minimize Alice’s score in each of his turns.

To solve this problem, we must account for each player's optimal strategy.

To learn more about dynamic programming, you can refer to the [Dynamic Programming Explore Card](https://leetcode.com/explore/featured/card/dynamic-programming/).

---

### Approach 1: Dynamic Programming (Memoization)

#### Intuition

This scenario invokes classic game theory concepts, particularly the minimax strategy. This strategy involves making decisions that minimize the possible loss in a worst-case scenario.

Initially, Alice can choose to take between 1 and `2M` piles of stones, where `M` starts at 1. The twist is that after Alice's turn, the value of `M` can increase depending on the number of piles Alice chose. If Alice picks `X` piles, the new value of `M` becomes `max(M, X)` for the next turn, which Bob will then use to make his decision.

Alice's goal is to not only maximize her stones in the current turn but also to minimize Bob's potential gain in his following turn. This is where the minimax strategy is crucial: Alice should aim to make the move that leaves Bob with the least advantageous situation, thus maximizing her total gain in the end.

We can break down the approach into three steps:

1. Recursive Exploration
2. Dynamic Programming with Memoization
3. Minmax and Suffix Sum Optimization

##### Recursive Exploration

In this step, we explore all possible numbers of piles Alice can take. For each possibility, we calculate the minimum number of stones Bob could then take on his turn. The idea is to compute this recursively until the end of the game is reached (i.e., all stones are taken).

##### Dynamic Programming with Memoization

Since many subproblems overlap (i.e., the same game state can be reached through different sequences of moves), we store the results of previously computed states in a `memo` array. This prevents redundant calculations and speeds up the algorithm.

##### Minmax and Suffix Sum Optimization

To efficiently determine how many stones Alice and Bob can take, we precompute the sum of the remaining stones using a suffix sum array. This array allows us to compute the remaining stones after any move, which is crucial for calculating the optimal strategy.

A suffix sum array is a precomputed array that stores the sum of all elements from a given index to the end of the array. For the array `piles`, the suffix sum at index `i`, denoted as `suffixSum[i]`, represents the total number of stones in the piles from index `i` to the last pile.

- To construct the suffix sum array, we start from the end of the `piles` array and move towards the beginning. The last element of the suffix sum array is simply the last element of `piles`, and for every other element, we add the current pile to the suffix sum of the next element.
- If Alice picks `X` piles starting from index `i`, the remaining stones after Alice's move are all the stones from index `i + X` onwards. The sum of these remaining stones is directly given by `suffixSum[i + X]`. The suffix sum array aids in determining the sum of remaining stones.

The principle behind why this algorithm works lies in the minimax strategy and dynamic programming. By recursively exploring every possible move and evaluating all potential moves Alice can make while considering Bob's optimal responses, we ensure that every possible outcome is explored. This comprehensive exploration guarantees that the chosen move is indeed the best possible one, considering the "worst-case scenario enforced" by Bob.

#### Algorithm

- Compute the suffix sum array `suffixSum`:
  - Initialize `suffixSum` with a copy of `piles`.
  - Update each element of `suffixSum` to include the sum of all elements from that index to the end of the array.
- Call `maxStones` to find the maximum number of stones that can be picked:
  - Pass the `suffixSum`, `1` (initial value for `maxTillNow`), `0` (initial `currIndex`), and an empty memoization table `memo`.

- In the `maxStones` function:
  - Check if `currIndex + 2 * maxTillNow` is out of bounds of the array:
    - If so, return `suffixSum[currIndex]` as all remaining stones can be picked.
  - Use memoization to avoid redundant calculations:
    - If `memo[currIndex][maxTillNow]` has a value greater than 0, return it.
  - Initialize `res` to `Integer.MAX_VALUE` to find the minimum number of stones that can be picked by the opponent:
    - Iterate through possible moves (from `1` to `2 * maxTillNow`):
      - Recursively call `maxStones` to calculate the number of stones the opponent can leave us with.
      - Update `res` with the minimum value obtained from these recursive calls.
  - Store the result in `memo[currIndex][maxTillNow]`:
    - Compute the maximum number of stones that can be picked by subtracting `res` from `suffixSum[currIndex]`.
  - Return the computed value from the memoization table.



![Slide 1](images/slideshow_slideshow1_slide1.png)

![Slide 2](images/slideshow_slideshow1_slide2.png)

![Slide 3](images/slideshow_slideshow1_slide3.png)

![Slide 4](images/slideshow_slideshow1_slide4.png)

![Slide 5](images/slideshow_slideshow1_slide5.png)

![Slide 6](images/slideshow_slideshow1_slide6.png)



#### Implementation


```python
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # Initialize the memoization table
        memo = [[0] * len(piles) for _ in range(len(piles))]
        # Initialize the suffixSum array
        suffix_sum = piles[:]

        # Compute the suffix sums
        for i in range(len(suffix_sum) - 2, -1, -1):
            suffix_sum[i] += suffix_sum[i + 1]

        # Call the recursive function to find the maximum stones Alex can collect
        return self.max_stones(suffix_sum, 1, 0, memo)

    def max_stones(
        self,
        suffix_sum: List[int],
        max_till_now: int,
        curr_index: int,
        memo: List[List[int]],
    ) -> int:
        # If the current index plus twice the maxTillNow exceeds the array size, take all remaining stones
        if curr_index + 2 * max_till_now >= len(suffix_sum):
            return suffix_sum[curr_index]

        # Return the memoized result if it exists
        if memo[curr_index][max_till_now] > 0:
            return memo[curr_index][max_till_now]

        # Initialize the result to a very large number (infinity)
        res = float("inf")

        # Iterate through possible moves and calculate the minimum result for the opponent
        for i in range(1, 2 * max_till_now + 1):
            res = min(
                res,
                self.max_stones(
                    suffix_sum,
                    max(i, max_till_now),
                    curr_index + i,
                    memo,
                ),
            )

        # Memoize the result as the current suffix sum minus the opponent's best outcome
        memo[curr_index][max_till_now] = suffix_sum[curr_index] - res
        return memo[curr_index][max_till_now]
```


#### Complexity Analysis

Let $n$ be the size of the array `piles`.

- Time complexity: $O(n^3)$
    
    Calculating the suffix sum for all elements in the array requires $O(n)$ time. The `maxStones` function iterates from `1` to $2 \times \text{maxTillNow}$ in each call. Within each iteration, we update two states of size $n$. Consequently, each iteration involves $O(n^2)$ operations, leading to a total time complexity of $O(n^3)$ for the recursive function.

- Space complexity: $O(n^2)$
    
    We use a memoization matrix of size $n \times n$ to store the states of recursion calls. Apart from this matrix, no additional space is utilized.

---

### Approach 2: Dynamic Programming (Tabulation)

#### Intuition

Instead of solving the problem using recursion (which can lead to deep recursion issues), we use a tabulation approach. We create a table (DP matrix) where each entry represents the optimal number of stones Alice can collect starting from a given pile, considering the current value of $M$.

To address this, we use a DP table, `dp[i][j]`, where $i$ represents the starting index of the piles and $j$ represents the maximum number of piles Alice can pick on her turn ($M$). The value in `dp[i][j]` will store the maximum number of stones Alice can collect starting from index $i$ with the maximum pick limit of $j$.

We need to efficiently compute the total number of stones remaining after Alice’s move. To achieve this, we build a suffix sum array. This array allows us to calculate the total number of stones from any given pile index to the end of the row, streamlining our calculations for each possible move, similar to the recursive approach.

We then fill the DP table by iterating backward from the end of the piles. For each index $i$ and each possible value of $M$, we determine the maximum stones Alice can collect by evaluating every possible move she can make. This involves picking between 1 and $2M$ piles and calculating how many stones Alice would get from the current move and what would be left for Bob.

By working backward, we ensure that when calculating the optimal number of stones Alice can collect for a given index and $M$, we already have the optimal results for all subsequent states. This backward iteration ensures that each decision is made with complete knowledge of future outcomes.

Once the DP table is fully populated, the entry `dp[0][1]` contains the maximum number of stones Alice can collect starting from the first pile with $M$ initially set to 1. This value represents the optimal solution to the problem.

#### Algorithm

- Create a 2D `dp` table to store the maximum stones a player can collect starting from index `i` with `maxTillNow` piles.
  - Initialize `dp` with dimensions `(length + 1) x (length + 1)` and set all values to 0.

- Create a `suffixSum` array to store the cumulative sum of stones from index `i` to the end of the piles.
  - Iterate from the end of the `piles` array to the beginning, calculating and storing the suffix sums.

- Initialize the `dp` array for the base case:
  - For each index `i`, set `dp[i][length]` to the corresponding suffix sum `suffixSum[i]`.

- Fill the `dp` table from the end to the beginning:
  - Iterate backwards from the last index to the start.
  - For each `index`, iterate from `maxTillNow` down to 1.
  - For each possible number of piles `X` (from 1 to `2 * maxTillNow`), update `dp[index][maxTillNow]` with the maximum stones collectible considering taking `X` piles.

- Return the result from `dp[0][1]`, which represents the maximum stones collectible starting from index 0 with the initial maximum allowed piles of 1.

#### Implementation


```python
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        length = len(piles)
        dp = [[0 for _ in range(length + 1)] for _ in range(length + 1)]

        # Store suffix sum for all possible suffix
        suffix_sum = [0 for _ in range(length + 1)]
        for i in range(length - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        # Initialize the dp array.
        for i in range(length + 1):
            dp[i][length] = suffix_sum[i]

        # Start from the last index to store the future state first.
        for index in range(length - 1, -1, -1):
            for max_till_now in range(length - 1, 0, -1):
                for X in range(1, min(2 * max_till_now, length - index) + 1):
                    dp[index][max_till_now] = max(
                        dp[index][max_till_now],
                        suffix_sum[index] - dp[index + X][max(max_till_now, X)],
                    )
        return dp[0][1]
```


#### Complexity Analysis

Let $n$ be the size of the array `piles`.

- Time complexity: $O(n^3)$ 

    Storing the suffix sum of all array elements requires $O(n)$ time. During tabulation, we need to iterate through all possible states for `index`, `maxTillNow`, and `X`, where each variable can take values from $1$ to $n$. As a result, the total number of iterations is $O(n^3)$, leading to a time complexity of $O(n^3)$.

- Space complexity: $O(n^2)$

    We use a `dp` matrix of size $n \times n$ to memoize the states of the recursion calls. Aside from this matrix, no additional significant space is required. Thus, the space complexity is $O(n^2)$.

---