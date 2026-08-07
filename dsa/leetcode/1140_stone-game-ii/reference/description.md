## Description

Alice and Bob continue their games with piles of stones. There are a number of piles **arranged in a row**, and each pile has a positive integer number of stones $\text{piles}[i]$. The objective of the game is to end with the most stones.

Alice and Bob take turns, with Alice starting first.

On each player's turn, that player can take **all the stones** in the **first** `X` remaining piles, where $1 \le X \le 2M$. Then, we set $M = max(M, X)$. Initially, M = 1.

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** piles = [2,7,9,4,4]

**Output:** 10

**Explanation:**

- If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get $2 + 4 + 4 = 10$ stones in total.

- If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get $2 + 7 = 9$ stones in total.

So we return 10 since it's larger.

</div>
#### Example 2

<div class="example-block">
**Input:** piles = [1,2,3,4,5,100]

**Output:** 104

</div>
### Constraints

- $1 \le \text{piles.length} \le 100$

- $1 \le \text{piles}[i] \le 10^{4}$