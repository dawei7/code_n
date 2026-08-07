[TOC]

## Solution

---

### Overview

The problem statement asks us to _return all elements of the `matrix` in spiral order_, which means we will start from the top left corner and move towards right, then down, then left, and then up. Let's break this into further details:
1. We can achieve moving in different directions by modifying row and column indices. Specifically, we have:

```plain
Given that we are at (row, col), where row is the row index, and col is the column index.

move right: (row, col + 1)
move downwards: (row + 1, col)
move left: (row, col - 1)
move upwards: (row - 1, col)
```
2. When shall we change our direction? We need to turn when we either _reach the matrix boundaries_, or we _reach the cells in the array that we have visited before_. Matrix boundaries are fixed and provided already, but how could we know if we have visited a particular cell or not?
In fact, we have two different strategies and they will be introduced in the following approaches. Generally speaking, they are as follows:
   - Approach 1. We can move the boundaries towards the center of the matrix after we have traversed a row or a column. Then when we meet a boundary, we know it's time to change the direction and update the boundary.
   - Approach 2. While traversing the matrix, we can record each location that we have visited. Then when we meet a matrix boundary or a previously visited cell, we know it's time to change the direction.

> This is a good time to stop and see if you can come up with the implementations yourselves!

</br>

---

### Approach 1: Set Up Boundaries

**Intuition**

Our goal is to update boundaries as follows: when we finish traversing a row or column, we want to set up a boundary on it so that next time we get there, we know we need to change the direction. Here is a demo for the first round of updating the top, right, bottom, and left boundaries.



![Slide 1](images/slideshow_54_spiral_matrix_54-001.png)

![Slide 2](images/slideshow_54_spiral_matrix_54-002.png)

![Slide 3](images/slideshow_54_spiral_matrix_54-003.png)

![Slide 4](images/slideshow_54_spiral_matrix_54-004.png)

![Slide 5](images/slideshow_54_spiral_matrix_54-005.png)

![Slide 6](images/slideshow_54_spiral_matrix_54-006.png)

![Slide 7](images/slideshow_54_spiral_matrix_54-007.png)

![Slide 8](images/slideshow_54_spiral_matrix_54-008.png)

![Slide 9](images/slideshow_54_spiral_matrix_54-009.png)




</br>


**Algorithm**

1. Initialize the top, right, bottom, and left boundaries as `up`, `right`, `down`, and `left`.
2. Initialize the output array `result`.
3. Traverse the elements in spiral order and add each element to `result`:
    - Traverse from `left` boundary to `right` boundary.
    - Traverse from `up` boundary to `down` boundary.
    - Before we traverse from right to left, we need to make sure that we are not on a row that has already been traversed. If we are not, then we can traverse from `right` to `left`.
    - Similarly, before we traverse from top to bottom, we need to make sure that we are not on a column that has already been traversed. Then we can traverse from `down` to `up`.
    - Remember to move the boundaries by updating `left`, `right`, `up`, and `down` accordingly.
4. Return `result`.


```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows, columns = len(matrix), len(matrix[0])
        up = left = 0
        right = columns - 1
        down = rows - 1

        while len(result) < rows * columns:
            # Traverse from left to right.
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            # Traverse downwards.
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            # Make sure we are now on a different row.
            if up != down:
                # Traverse from right to left.
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            # Make sure we are now on a different column.
            if left != right:
                # Traverse upwards.
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return result
```


**Complexity Analysis**

Let $$M$$ be the number of rows and $$N$$ be the number of columns.

* Time complexity: $$O(M \cdot N)$$. This is because we visit each element once.

* Space complexity: $$O(1)$$. This is because we don't use other data structures. Remember that we don't include the output array in the space complexity.


<br/>

---

### Approach 2: Mark Visited Elements

**Intuition**

If we mark the cells that we have visited, then when we run into a visited cell, we know we need to turn.

> How do we know which direction we need to turn to? Well, we are always following this loop: right, down, left, up, right again, and so on. Therefore, when we run into a cell that we have visited, we can simply turn to the next direction in the aforementioned loop.

Note that elements in the matrix are constrained to `-100 <= matrix[row][col] <= 100`, therefore we can select a number that is out of this range to mark it. In this article, `101` is selected for marking purposes.

> Modifying the original data may not be a good choice sometimes. Therefore, we can also prepare another boolean matrix to store the cells we visited. However, the implementation of this approach is quite similar. You are welcome to explore this implementation as an exercise.

The last puzzle piece is when shall we stop. An interesting observation is that if we reach the visited cell, we need to turn.  However, when we meet another visited cell immediately after changing the direction, it means we reached the last element in the matrix. You'll see that an integer `changeDirection` is used to track the number of times we changed the direction consecutively.

**Algorithm**

- Initializations:
    - Initialize a 2D array `directions ` to represent the four directions that we will move.
    - Initialize `currentDirection` to 0 to signify that we are moving right at the beginning.
    - Initialize `VISITED` to 101 to mark visited cells.
    - Initialize `changeDirection` to 0.
    - Initialize `row` and `col` to 0 since our initial position is `(0, 0)`.
- We follow the current direction until we reach the matrix boundaries or a visited cell.
    - While traversing in the current direction, remember to reset `changeDirection` to 0 at every step.
    - Move to the next cell by updating the row and column indices.
    - Append the element to the result and mark the location as visited.
- Update the direction and `changeDirection`. If `changeDirection` is larger than 1, it means we are continuously changing our directions, and therefore we've visited all of the elements.


```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        VISITED = 101
        rows, columns = len(matrix), len(matrix[0])
        # Four directions that we will move: right, down, left, up.
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Initial direction: moving right.
        current_direction = 0
        # The number of times we change the direction.
        change_direction = 0
        # Current place that we are at is (row, col).
        # row is the row index; col is the column index.
        row = col = 0
        # Store the first element and mark it as visited.
        result = [matrix[0][0]]
        matrix[0][0] = VISITED

        while change_direction < 2:

            while True:
                # Calculate the next place that we will move to.
                next_row = row + directions[current_direction][0]
                next_col = col + directions[current_direction][1]

                # Break if the next step is out of bounds.
                if not (0 <= next_row < rows and 0 <= next_col < columns):
                    break
                # Break if the next step is on a visited cell.
                if matrix[next_row][next_col] == VISITED:
                    break

                # Reset this to 0 since we did not break and change the direction.
                change_direction = 0
                # Update our current position to the next step.
                row, col = next_row, next_col
                result.append(matrix[row][col])
                matrix[row][col] = VISITED

            # Change our direction.
            current_direction = (current_direction + 1) % 4
            # Increment change_direction because we changed our direction.
            change_direction += 1

        return result
```


**Complexity Analysis**

Let $$M$$ be the number of rows and $$N$$ be the number of columns.

* Time complexity: $$O(M \cdot N)$$. This is because we visit each element once.

* Space complexity: $$O(1)$$. This is because we don't use other data structures. Remember that we don't consider the output array or the input matrix when calculating the space complexity. However, if we were prohibited from mutating the input matrix, then this would be an $$O(M \cdot N)$$ space solution.  This is because we would need to use a boolean matrix to track all of the previously seen cells.


<br/>

---