### 1. Description

You are the manager of a basketball team. For the upcoming tournament, you want to choose the team with the highest overall score. The score of the team is the **sum** of scores of all the players in the team.

However, the basketball team is not allowed to have **conflicts**. A **conflict** exists if a younger player has a **strictly higher** score than an older player. A conflict does **not** occur between players of the same age.

Given two lists, `scores` and `ages`, where each $\text{scores}[i]$ and $\text{ages}[i]$ represents the score and age of the $$i^{\text{th}}$$ player, respectively, return *the highest overall score of all possible basketball teams*.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $scores = [1,3,5,10,15], ages = [1,2,3,4,5]$
- **Output:** `34`
- **Explanation:** You can choose all the players.
#### Example 2

- **Input:** $scores = [4,5,6,5], ages = [2,1,2,1]$
- **Output:** `16`
- **Explanation:** It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.
#### Example 3

- **Input:** $scores = [1,2,3,5], ages = [8,9,10,1]$
- **Output:** `6`
- **Explanation:** It is best to choose the first 3 players.

### 4. Constraints

- $1 \le \text{scores.length}, \text{ages.length} \le 1000$

- $\text{scores.length} = \text{ages.length}$

- $1 \le \text{scores}[i] \le 10^{6}$

- $1 \le \text{ages}[i] \le 1000$