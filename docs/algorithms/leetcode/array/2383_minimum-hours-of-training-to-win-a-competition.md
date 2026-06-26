# Minimum Hours of Training to Win a Competition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2383 |
| Difficulty | Easy |
| Topics | Array, Greedy |
| Official Link | [minimum-hours-of-training-to-win-a-competition](https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/) |

## Problem Description & Examples
### Goal
Calculate the minimum number of training hours required to defeat a series of opponents. You start with an initial energy and experience level. To defeat an opponent, your current energy must strictly exceed their energy requirement, and your current experience must strictly exceed their experience requirement. After each victory, your energy decreases by the opponent's energy, and your experience increases by the opponent's experience. You can train to increase your initial energy or experience by 1 hour per unit.

### Function Contract
**Inputs**

- `initialEnergy` (int): Your starting energy level.
- `initialExperience` (int): Your starting experience level.
- `energy` (List[int]): A list of energy requirements for each opponent.
- `experience` (List[int]): A list of experience requirements for each opponent.

**Return value**

- `int`: The total number of training hours needed to ensure all opponents are defeated.

### Examples
**Example 1**

- Input: `initialEnergy = 5, initialExperience = 3, energy = [1, 4, 3, 2], experience = [2, 6, 3, 1]`
- Output: `8`

**Example 2**

- Input: `initialEnergy = 2, initialExperience = 4, energy = [1], experience = [3]`
- Output: `0`

**Example 3**

- Input: `initialEnergy = 1, initialExperience = 1, energy = [1, 1, 1, 1], experience = [1, 1, 1, 1]`
- Output: `5`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Greedy approach**. Since the order of opponents is fixed, we iterate through the list once. At each step, we check if our current stats meet the requirements. If they do not, we calculate the difference, add that difference to our total training hours, and update our current stats to the minimum threshold required to win.

---

## Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of opponents, as we perform a single pass through the input arrays.
- **Space Complexity**: `O(1)`, as we only use a few variables to track current stats and total training hours.
