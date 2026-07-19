# Find the Winner of an Array Game

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1535 |
| Difficulty | Medium |
| Topics | Array, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-winner-of-an-array-game/) |

## Problem Description
### Goal

An array of distinct integers defines a repeated game between its first two values. In each round, the larger value wins and remains at index 0, while the smaller value moves to the end of the array.

The game stops as soon as one value has won `k` consecutive rounds. Return that winning value. A winner is guaranteed, even when `k` is much larger than the array length.

### Function Contract
**Inputs**

- `arr`: An array of $n$ distinct integers, where $2 \leq n \leq 10^5$ and each value lies from 1 through $10^6$.
- `k`: The required consecutive-win count, where $1 \leq k \leq 10^9$.

**Return value**

Return the first value to win `k` consecutive rounds under the described front-versus-next game.

### Examples
**Example 1**

- Input: `arr = [2, 1, 3, 5, 4, 6, 7], k = 2`
- Output: `5`
- Explanation: Values 2, 3, and 5 successively become champion; 5 then defeats 4 for its second consecutive win.

**Example 2**

- Input: `arr = [3, 2, 1], k = 10`
- Output: `3`
- Explanation: The maximum begins at the front and can keep winning indefinitely.

**Example 3**

- Input: `arr = [1, 9, 8, 2, 3, 7, 6, 4, 5], k = 7`
- Output: `9`
- Explanation: Once 9 reaches the front, no later value can defeat it.
