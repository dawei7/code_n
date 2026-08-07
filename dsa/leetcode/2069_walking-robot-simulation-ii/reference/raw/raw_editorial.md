### Approach: Simulation

#### Intuition

From the problem description, we can observe that the robot always moves in a loop along the outermost layer of the grid.

![fig1](images/5911.png)

Therefore, we can preprocess the robot’s movement cycle (positions and directions) and store it in an array. We use a pointer $\textit{idx}$ to represent the robot’s current position and direction.

The preprocessing can be divided into four steps. As shown in the figure above, grids of different colors represent the robot’s direction at those positions. Accordingly, we can use four loops to enumerate the positions for each direction and store them in the preprocessing arrays.

For the three interfaces required by the problem, we can implement them as follows:

* $\texttt{void move(int num)}$: Increase $\textit{idx}$ by $\textit{num}$. Since the robot’s path is cyclic, we take the result modulo the length of the cycle.

* $\texttt{int[] getPos()}$: Return the position from the preprocessed array based on $\textit{idx}$.

* $\texttt{String getDir()}$: Return the direction from the preprocessed array based on $\textit{idx}$.

Note that when the robot returns to the origin, its direction becomes `'South'`, whereas its initial direction at the origin is `'East'`. To handle this, we set the direction of the origin in the preprocessing array to `'South'` and use a boolean variable to track whether the robot has moved:

* If the robot has not moved, we always return `'East'`.

* If the robot has moved, we return the direction from the preprocessing array based on $\textit{idx}$.

#### Implementation


```python
class Robot:

    TO_DIR = {
        0: "East",
        1: "North",
        2: "West",
        3: "South",
    }

    def __init__(self, width: int, height: int):
        self.moved = False
        self.idx = 0
        self.pos = list()
        self.dirs = list()

        pos_, dirs_ = self.pos, self.dirs

        for i in range(width):
            pos_.append((i, 0))
            dirs_.append(0)
        for i in range(1, height):
            pos_.append((width - 1, i))
            dirs_.append(1)
        for i in range(width - 2, -1, -1):
            pos_.append((i, height - 1))
            dirs_.append(2)
        for i in range(height - 2, 0, -1):
            pos_.append((0, i))
            dirs_.append(3)

        dirs_[0] = 3

    def step(self, num: int) -> None:
        self.moved = True
        self.idx = (self.idx + num) % len(self.pos)

    def getPos(self) -> List[int]:
        return list(self.pos[self.idx])

    def getDir(self) -> str:
        if not self.moved:
            return "East"
        return Robot.TO_DIR[self.dirs[self.idx]]
```


#### Complexity Analysis

- Time complexity: The preprocessing takes $O(\textit{width} + \textit{height})$, and each query operation runs in $O(1)$ time.

- Space complexity: $O(\textit{width} + \textit{height})$.
  
  This accounts for storing the preprocessed positions and directions.

---