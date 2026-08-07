[TOC]

## Solution

---

### Approach 1: Spiral Backtracking

**Concepts to use**

Let's use two programming concepts.

> The first one is called _constrained programming_. 

That basically means to put restrictions after each robot moves. The robot moves, and the cell is marked as `visited`. That propagates _constraints_ and helps to reduce the number of combinations to consider.

![bla](images/489_constraints.png)

> The second one called _backtracking_. 

Let's imagine that after several moves the robot is surrounded by the visited cells. But several steps before there was a cell that proposed an alternative path. That path wasn't used and hence the room is not yet cleaned up. What to do? _To backtrack_. That means to come back to that cell and to explore the alternative path. 

![bla](images/489_backtrack.png)

**Intuition**

This solution is based on the same idea as the solving algorithm called [right-hand rule](https://en.wikipedia.org/wiki/Maze_solving_algorithm#Wall_follower). Go forward, cleaning and marking all the cells on the way as visited. At the obstacle _turn right_, again go forward, _etc_. Always _turn right_ at the obstacles and then go forward. Consider already visited cells as virtual obstacles.

> What to do if, after the right turn, there is an obstacle just in front?

_Turn right_ again.

> How to explore the alternative paths from the cell? 

Go back to that cell and then _turn right_ from your last explored direction.

> When to stop?

Stop when you explored all possible paths, _i.e._  all `4` directions (up, right, down, and left) for each visited cell.

**Algorithm**

Time to write down the algorithm for the backtrack function `backtrack(cell = (0, 0), direction = 0)`.

- Mark the cell as visited and clean it up.

- Explore `4` directions: `up`, `right`, `down`, and `left` (the order is important since the idea is always to turn right) : 

    - Check the next cell in the chosen direction :
    
        - If it's not visited yet and there are no obstacles :
            
            - Move forward.
            
            - Explore next cells `backtrack(new_cell, new_direction)`.
            
            - Backtrack, _i.e._ go back to the previous cell.
            
        - Turn right because now there is an obstacle (or a virtual obstacle) just in front.


**Implementation**

![bla](images/489_implementation.png)


```python
class Solution:       
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
            
        def backtrack(cell = (0, 0), d = 0):
            visited.add(cell)
            robot.clean()
            # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
            for i in range(4):
                new_d = (d + i) % 4
                new_cell = (cell[0] + directions[new_d][0], \
                            cell[1] + directions[new_d][1])
                
                if not new_cell in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()
                # turn the robot following chosen direction : clockwise
                robot.turnRight()
    
        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backtrack()
```


**Complexity Analysis**

* Time complexity : $$O(N - M)$$, where $$N$$ is a number of cells in the room and $$M$$ is a number of obstacles.

  - We visit each non-obstacle cell once and only once.
  - At each visit, we will check 4 directions around the cell. Therefore, the total number of operations would be $$4 \cdot (N-M)$$.

* Space complexity : $$O(N - M)$$, where $$N$$ is a number of cells in the room and $$M$$ is a number of obstacles.

  - We employed a hashtable to keep track of whether a non-obstacle cell is visited or not.