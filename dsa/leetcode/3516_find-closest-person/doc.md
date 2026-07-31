# Find Closest Person

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3516 |
| Difficulty | Easy |
| Topics | Math |
| Official Link | [LeetCode](https://leetcode.com/problems/find-closest-person/) |

## Problem Description
### Goal
Three people occupy integer positions on a number line. Person 1 starts at `x`, Person 2 starts at `y`, and Person 3 remains stationary at `z`.

Person 1 and Person 2 begin moving toward Person 3 at the same speed. Return `1` if Person 1 reaches `z` first, return `2` if Person 2 reaches `z` first, or return `0` if their arrival times are equal. A person who already starts at `z` has distance zero.

### Function Contract
**Inputs**

- `x`: Person 1's position, where $1 \le x \le 100$.
- `y`: Person 2's position, where $1 \le y \le 100$.
- `z`: The stationary Person 3's position, where $1 \le z \le 100$.

**Return value**

Return `1`, `2`, or `0` according to whether Person 1 arrives first, Person 2 arrives first, or both arrive simultaneously.

### Examples
**Example 1**

- Input: `x = 2, y = 7, z = 4`
- Output: `1`
- Explanation: The two travel distances are `2` and `3`, so Person 1 arrives first.

**Example 2**

- Input: `x = 2, y = 5, z = 6`
- Output: `2`
- Explanation: Person 2 is one unit away, while Person 1 is four units away.

**Example 3**

- Input: `x = 1, y = 5, z = 3`
- Output: `0`
- Explanation: Both moving people are two units from Person 3.
