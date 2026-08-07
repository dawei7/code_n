## Description

You are given a **0-indexed** integer array `players`, where $\text{players}[i]$ represents the **ability** of the $$i^{\text{th}}$$player. You are also given a **0-indexed** integer array `trainers`, where$\text{trainers}[j]$represents the **training capacity **of the$$j^{\text{th}}$$ trainer.

The $$i^{\text{th}}$$player can **match** with the$$j^{\text{th}}$$trainer if the player's ability is **less than or equal to** the trainer's training capacity. Additionally, the$$i^{\text{th}}$$player can be matched with at most one trainer, and the$$j^{\text{th}}$$ trainer can be matched with at most one player.

Return *the **maximum** number of matchings between *`players`* and *`trainers`* that satisfy these conditions.*
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

- **Input:** $players = [4,7,9], trainers = [8,2,5,8]$
- **Output:** `2`
- **Explanation:**
One of the ways we can form two matchings is as follows:
- players[0] can be matched with trainers[0] since 4 <= 8.
- players[1] can be matched with trainers[3] since 7 <= 8.
It can be proven that 2 is the maximum number of matchings that can be formed.
#### Example 2

- **Input:** $players = [1,1,1], trainers = [10]$
- **Output:** `1`
- **Explanation:**
The trainer can be matched with any of the 3 players.
Each player can only be matched with one trainer, so the maximum answer is 1.
### Constraints

- $1 \le \text{players.length}, \text{trainers.length} \le 10^{5}$

- $1 \le \text{players}[i], \text{trainers}[j] \le 10^{9}$

**Note:** This question is the same as <a href="https://leetcode.com/problems/assign-cookies/description/" target="_blank"> 445: Assign Cookies.</a>