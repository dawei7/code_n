
---
### Approach #1: Simulation [Accepted]

**Intuition**

We can simulate the position of the robot after each command.

**Algorithm**

Initially, the robot is at $(x, y) = (0, 0)$. If the move is `'U'`, the robot goes to $(x, y - 1)$; if the move is `'R'`, the robot goes to $(x, y) = (x + 1, y)$, and so on.

```python
class Solution(object):
    def judgeCircle(self, moves):
        x = y = 0
        for move in moves:
            if move == 'U': y -= 1
            elif move == 'D': y += 1
            elif move == 'L': x -= 1
            elif move == 'R': x += 1

        return x == y == 0
```

**Complexity Analysis**

* Time Complexity: $O(N)$, where $N$ is the length of `moves`. We iterate through the string.

* Space Complexity: $O(1)$. In Java, our character array is $O(N)$.