# Minimum Hours of Training to Win a Competition

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2383 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-hours-of-training-to-win-a-competition](https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/).

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

## Solution
### Approach
The problem is solved using a **Greedy approach**. Since the order of opponents is fixed, we iterate through the list once. At each step, we check if our current stats meet the requirements. If they do not, we calculate the difference, add that difference to our total training hours, and update our current stats to the minimum threshold required to win.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the number of opponents, as we perform a single pass through the input arrays.
- **Space Complexity**: `O(1)`, as we only use a few variables to track current stats and total training hours.

### Reference Implementations
<details>
<summary>python</summary>

```python
from typing import List

def solve(initial_energy: int, initial_experience: int, energy: List[int], experience: List[int]) -> int:
    total_training_hours = 0
    current_energy = initial_energy
    current_experience = initial_experience

    for e_req, x_req in zip(energy, experience):
        # Check energy requirement
        if current_energy <= e_req:
            needed = e_req - current_energy + 1
            total_training_hours += needed
            current_energy += needed

        # Check experience requirement
        if current_experience <= x_req:
            needed = x_req - current_experience + 1
            total_training_hours += needed
            current_experience += needed

        # Update stats after winning
        current_energy -= e_req
        current_experience += x_req

    return total_training_hours
```
</details>
