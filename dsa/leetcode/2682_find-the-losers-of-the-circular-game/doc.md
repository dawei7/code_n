# Find the Losers of the Circular Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2682 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [find-the-losers-of-the-circular-game](https://leetcode.com/problems/find-the-losers-of-the-circular-game/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/find-the-losers-of-the-circular-game/).

### Goal
Simulate a circular game involving `n` friends, numbered 1 to `n`. The game starts with friend 1 holding a ball. In each subsequent round `i` (starting from round 1), the friend currently holding the ball passes it `i * k` positions clockwise. A friend who receives the ball is no longer considered a "loser". The game concludes when a friend receives the ball who has already received it at least once before. The objective is to identify all friends who never received the ball throughout the game and return their IDs in ascending order.

### Function Contract
**Inputs**

- `n`: An integer representing the total number of friends participating in the game. Friends are numbered from 1 to `n`. (`1 <= n <= 1000`)
- `k`: An integer representing the multiplier for the number of steps the ball is passed in each round. (`1 <= k <= 1000`)

**Return value**

A list of integers, sorted in ascending order, representing the IDs of the friends who never received the ball during the game. If all friends receive the ball, an empty list should be returned.

### Examples
**Example 1**

- Input: `n = 5, k = 2`
- Output: `[4, 5]`
- Explanation:
    - Initially, friend 1 has the ball. `Received: {1}`.
    - Round 1: Friend 1 passes `1 * 2 = 2` steps. Ball goes to friend `(1 + 2 - 1) % 5 + 1 = 3`. `Received: {1, 3}`.
    - Round 2: Friend 3 passes `2 * 2 = 4` steps. Ball goes to friend `(3 + 4 - 1) % 5 + 1 = 2`. `Received: {1, 3, 2}`.
    - Round 3: Friend 2 passes `3 * 2 = 6` steps. Ball goes to friend `(2 + 6 - 1) % 5 + 1 = 3`. Friend 3 already received the ball. Game ends.
    - Friends 4 and 5 never received the ball.

**Example 2**

- Input: `n = 4, k = 4`
- Output: `[2, 3, 4]`
- Explanation:
    - Initially, friend 1 has the ball. `Received: {1}`.
    - Round 1: Friend 1 passes `1 * 4 = 4` steps. Ball goes to friend `(1 + 4 - 1) % 4 + 1 = 1`. Friend 1 already received the ball. Game ends.
    - Friends 2, 3, and 4 never received the ball.

**Example 3**

- Input: `n = 2, k = 3`
- Output: `[]`
- Explanation:
    - Initially, friend 1 has the ball. `Received: {1}`.
    - Round 1: Friend 1 passes `1 * 3 = 3` steps. Ball goes to friend `(1 + 3 - 1) % 2 + 1 = 2`. `Received: {1, 2}`.
    - Round 2: Friend 2 passes `2 * 3 = 6` steps. Ball goes to friend `(2 + 6 - 1) % 2 + 1 = 1`. Friend 1 already received the ball. Game ends.
    - All friends (1 and 2) received the ball.

---

## Solution
### Approach
The problem is best solved using a **simulation** approach. We explicitly model the game round by round, tracking which friends have received the ball and the current state (who has the ball, what round it is). A hash set (or boolean array) is used to efficiently check and record which friends have received the ball. The simulation continues until the termination condition (a friend receiving the ball for the second time) is met.

### Complexity Analysis
- **Time Complexity**: `O(n)`
    The simulation proceeds round by round. In each round, a new friend receives the ball, or a friend who has already received it gets it again, ending the game. Since there are `n` friends, at most `n` unique friends can receive the ball before the game terminates. Each step of the simulation (set lookup, set insertion, modulo arithmetic) takes constant time. Therefore, the loop runs at most `n+1` times (at most `n` times for unique recipients, plus one more for the repeat recipient). After the loop, we iterate through `n` friends to identify the losers. Thus, the total time complexity is proportional to `n`.

- **Space Complexity**: `O(n)`
    We use a hash set (or a boolean array) to store the IDs of friends who have received the ball. In the worst case, all `n` friends receive the ball at least once before the game ends. This requires storing `n` friend IDs. Therefore, the space complexity is `O(n)`.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(n: int, k: int) -> list[int]:
    # Use a set to efficiently track friends who have received the ball.
    # Friends are 1-indexed, so we store their IDs directly.
    received_ball = set()

    # The game starts with friend 1 holding the ball.
    current_friend = 1
    # The round number starts from 1.
    round_num = 1

    # Simulate the game until a friend receives the ball who has already received it.
    while current_friend not in received_ball:
        # Mark the current friend as having received the ball.
        received_ball.add(current_friend)

        # Calculate the number of steps for this round.
        steps = round_num * k

        # Calculate the next friend to receive the ball.
        # We adjust to 0-indexed for modulo arithmetic (current_friend - 1),
        # then convert back to 1-indexed (+ 1).
        current_friend = (current_friend - 1 + steps) % n + 1

        # Increment the round number for the next iteration.
        round_num += 1

    # After the game ends, identify the friends who never received the ball.
    losers = []
    for i in range(1, n + 1):
        if i not in received_ball:
            losers.append(i)

    # The problem requires the output to be sorted in ascending order,
    # which is naturally achieved by iterating from 1 to n.
    return losers
```
</details>
