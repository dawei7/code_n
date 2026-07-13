# Determine the Winner of a Bowling Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2660 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [determine-the-winner-of-a-bowling-game](https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/).

### Goal
Given two lists of integers, `player1` and `player2`, representing the scores of each roll for two players in a simplified bowling game, determine the winner. The scoring rule is as follows: for any roll `i`, if either of the two preceding rolls (`i-1` or `i-2`) had a score of 10, then the current roll `rolls[i]` counts as double its value. Otherwise, it counts as its face value. Calculate the total score for both players based on this rule. Return `1` if player 1 has a higher total score, `2` if player 2 has a higher total score, or `0` if their total scores are equal.

### Function Contract
**Inputs**

- `player1`: A list of integers representing the scores of player 1's rolls. Each integer `rolls[i]` is between 0 and 10, inclusive. The length of `player1` is `n`.
- `player2`: A list of integers representing the scores of player 2's rolls. Each integer `rolls[i]` is between 0 and 10, inclusive. The length of `player2` is `n`.
The lengths of `player1` and `player2` are guaranteed to be equal.

**Return value**

An integer:
- `1` if player 1's total score is greater than player 2's.
- `2` if player 2's total score is greater than player 1's.
- `0` if both players have the same total score.

### Examples
**Example 1**

- Input: `player1 = [4, 10, 7, 9]`, `player2 = [6, 5, 2, 3]`
- Output: `1`
- Explanation:
  - Player 1's score:
    - Roll 0 (4): 4 (no previous rolls)
    - Roll 1 (10): 10 (previous roll 4 != 10)
    - Roll 2 (7): 7 * 2 = 14 (previous roll 10 == 10)
    - Roll 3 (9): 9 * 2 = 18 (roll 1 (10) == 10)
    - Total: 4 + 10 + 14 + 18 = 46
  - Player 2's score:
    - Roll 0 (6): 6
    - Roll 1 (5): 5
    - Roll 2 (2): 2
    - Roll 3 (3): 3
    - Total: 6 + 5 + 2 + 3 = 16
  - Since 46 > 16, player 1 wins.

**Example 2**

- Input: `player1 = [3, 5, 7, 6]`, `player2 = [8, 10, 10, 2]`
- Output: `2`
- Explanation:
  - Player 1's score:
    - Roll 0 (3): 3
    - Roll 1 (5): 5
    - Roll 2 (7): 7
    - Roll 3 (6): 6
    - Total: 3 + 5 + 7 + 6 = 21
  - Player 2's score:
    - Roll 0 (8): 8
    - Roll 1 (10): 10
    - Roll 2 (10): 10 * 2 = 20 (previous roll 10 == 10)
    - Roll 3 (2): 2 * 2 = 4 (previous roll 10 == 10)
    - Total: 8 + 10 + 20 + 4 = 42
  - Since 21 < 42, player 2 wins.

**Example 3**

- Input: `player1 = [2, 3, 10]`, `player2 = [3, 2, 10]`
- Output: `0`
- Explanation:
  - Player 1's score:
    - Roll 0 (2): 2
    - Roll 1 (3): 3
    - Roll 2 (10): 10
    - Total: 2 + 3 + 10 = 15
  - Player 2's score:
    - Roll 0 (3): 3
    - Roll 1 (2): 2
    - Roll 2 (10): 10
    - Total: 3 + 2 + 10 = 15
  - Since 15 == 15, it's a tie.

---

## Solution
### Approach
- **Simulation / Iteration**: The core of the solution involves simulating the scoring process for each player by iterating through their sequence of rolls. For each roll, we apply the given conditional doubling rule based on the scores of the two preceding rolls.
- **Array Traversal**: We traverse the input arrays (lists of rolls) linearly to calculate the total score for each player.

### Complexity Analysis
Let `n` be the number of rolls for each player (i.e., the length of `player1` and `player2`).

- **Time Complexity**: `O(n)`
  The `calculate_score` helper function iterates through the `n` rolls of a player exactly once. Inside the loop, all operations (array access, comparisons, arithmetic) are constant time. Since this function is called twice (once for each player), the total time complexity is `O(n) + O(n)`, which simplifies to `O(n)`.

- **Space Complexity**: `O(1)`
  The solution uses a few constant-size variables to store scores, loop indices, and multipliers. No data structures are created that scale with the input size `n`. Therefore, the space complexity is constant.

### Reference Implementations
<details>
<summary>python</summary>

```python
def calculate_score(rolls: list[int]) -> int:
    """
    Calculates the total score for a player based on the given bowling rules.
    A roll is doubled if either of the two preceding rolls scored 10.
    """
    total_score = 0
    for i in range(len(rolls)):
        current_roll_value = rolls[i]
        multiplier = 1

        # Check if the immediately preceding roll (i-1) was a 10
        if i > 0 and rolls[i-1] == 10:
            multiplier = 2
        # Else, check if the roll two positions ago (i-2) was a 10
        elif i > 1 and rolls[i-2] == 10:
            multiplier = 2

        total_score += current_roll_value * multiplier
    return total_score

def solve(player1: list[int], player2: list[int]) -> int:
    """
    Determines the winner of a bowling game between two players.

    Args:
        player1: A list of integers representing player 1's roll scores.
        player2: A list of integers representing player 2's roll scores.

    Returns:
        1 if player 1 wins, 2 if player 2 wins, or 0 for a tie.
    """
    score1 = calculate_score(player1)
    score2 = calculate_score(player2)

    if score1 > score2:
        return 1
    elif score2 > score1:
        return 2
    else:
        return 0
```
</details>
