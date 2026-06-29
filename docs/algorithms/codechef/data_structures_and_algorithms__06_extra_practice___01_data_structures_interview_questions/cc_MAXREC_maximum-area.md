# Maximum Area

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXREC |
| Difficulty Rating | 1800 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Stacks |
| Official Link | [MAXREC](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_10/problems/MAXREC) |

---

## Problem Statement

Bob has a rectangle garden of size $N*M$  in the form of a grid.
Bob was thinking of getting the grass in his garden cut, but due to some reason ,grass hasn’t grown in some regions , anyhow he thinks of hiring a gardener Dumbu. Dumbu does the job free of cost but has some conditions:-
- Cuts only $1$ rectangle
- Rectangle has to be wholly filled with grass.
Bob wants the maximum amount of grass to be cut. Help Bob find the maximum area of grass the Dumbu can cut.

---

## Input Format

- First line will contain 2 numbers N , M separated by a space.
- Next N lines contain M integers 0 or 1 separated by a space in each line.

---

## Output Format

Maximum Area that Dumbu can cut.

---

## Constraints

- $1 \leq N,M \leq 2000$
- grid[i][j] is either 0 signifying no grass or 1 sigifying grass.

---

## Examples

**Example 1**

**Input**

```text
2 2
1 0 
0 1
```

**Output**

```text
1
```

**Explanation**

Maximum are that Dumbu can cut is the square at (1,1) (0-based indexing)

**Example 2**

**Input**

```text
4 5
1 0 0 0 0 
1 1 1 1 1 
1 0 0 1 1 
1 0 0 1 1
```

**Output**

```text
6
```

**Explanation**

Maximum are that dumbu can cut is the rectangle from (1,3) to (3,4) hence the area being 6.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we will discuss how to solve the problem of finding the maximum area rectangle containing only 1’s in a binary grid. We will explore two effective approaches. Each approach is explained in detail along with its implementation in both C++ and Python. Understanding these methods will build important problem-solving techniques and strengthen your grasp of dynamic programming and stack-based algorithms.

---

## Approach 1: Histogram Based Method Using Largest Rectangle in Histogram

**Concept:**

This method transforms each row of the grid into a “histogram” that represents consecutive 1’s in that column. For each row, you maintain an array of heights that count how many 1’s occur consecutively up to the current row. Then, using a well-known “Largest Rectangle in Histogram” algorithm implemented with a stack, you can compute the maximum rectangular area for that histogram.

**How It Works:**

- For every row $i$, update an array $heights$ where for every column $j$:
  - If $matrix[i][j] = 1$, then $heights[j]$ is incremented.
  - Otherwise, reset $heights[j]$ to 0.
- Process the $heights$ array using a stack to quickly determine the largest rectangle area that can be formed in a histogram.
- The overall maximum area found over all rows is the answer.

**Time Complexity:**

The overall time complexity is $O(N \times M)$, where $N$ is the number of rows and $M$ is the number of columns.

**C++ Code:**

```cpp
#include
#include
#include
#include
using namespace std;

int largestRectangleArea(vector& heights) {
    int n = heights.size();
    stack s;
    int maxArea = 0;
    for (int i = 0; i <= n; i++) {
        int h = (i == n ? 0 : heights[i]);
        while (!s.empty() && h < heights[s.top()]) {
            int height = heights[s.top()];
            s.pop();
            int width = s.empty() ? i : i - s.top() - 1;
            maxArea = max(maxArea, height * width);
        }
        s.push(i);
    }
    return maxArea;
}

int maximalRectangle(vector>& matrix) {
    if (matrix.empty() || matrix[0].empty()) return 0;
    int m = matrix.size(), n = matrix[0].size();
    vector heights(n, 0);
    int maxArea = 0;
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            heights[j] = (matrix[i][j] == 1 ? heights[j] + 1 : 0);
        }
        maxArea = max(maxArea, largestRectangleArea(heights));
    }
    return maxArea;
}

int main(){
    int N, M;
    cin >> N >> M;
    vector> garden(N, vector(M));
    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j++){
            cin >> garden[i][j];
        }
    }
    cout << maximalRectangle(garden) << endl;
    return 0;
}
```

**Python Code:**

```python
def largestRectangleArea(heights):
    stack = []
    max_area = 0
    n = len(heights)
    for i in range(n + 1):
        curr_height = 0 if i == n else heights[i]
        while stack and curr_height < heights[stack[-1]]:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)
    return max_area

def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    max_area = 0
    for row in matrix:
        for j in range(n):
            heights[j] = heights[j] + 1 if row[j] == 1 else 0
        max_area = max(max_area, largestRectangleArea(heights))
    return max_area

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        exit(0)
    N = int(data[0])
    M = int(data[1])
    garden = []
    index = 2
    for i in range(N):
        row = [int(x) for x in data[index:index+M]]
        index += M
        garden.append(row)
    print(maximalRectangle(garden))
```

---

## Approach 2: Dynamic Programming with Left and Right Boundaries

**Concept:**

This method leverages dynamic programming by maintaining three arrays for each row:
- **height:** the number of consecutive 1’s ending at the current row,
- **left:** the leftmost boundary where the rectangle of 1’s can extend, and
- **right:** the rightmost boundary (exclusive) where the rectangle of 1’s can extend.

For every row, update these arrays and compute the area for each column as:
$$ \text{area} = height[j] \times (right[j] - left[j]). $$

**How It Works:**

1. **Update Height:**
   For every cell, if $matrix[i][j] == 1$, increase $height[j]$ by 1; otherwise, reset it to 0.
2. **Update Left Boundary:**
   Traverse from left to right. For a cell with a 1, set $left[j]$ to the maximum of its previous value and the current left boundary. If a cell is 0, reset $left[j]$ to 0 and update the current left boundary.
3. **Update Right Boundary:**
   Traverse from right to left. For a cell with a 1, set $right[j]$ to the minimum of its previous value and the current right boundary. If a cell is 0, reset $right[j]$ to the total number of columns and update the current right boundary.
4. **Calculate Maximum Area:**
   With these arrays, compute the area for every column and update the global maximum.

**Time Complexity:**

This approach runs in $O(N \times M)$ and is quite efficient.

**C++ Code:**

```cpp
#include
#include
#include
using namespace std;

int maximalRectangleDP(vector>& matrix) {
    if (matrix.empty() || matrix[0].empty()) return 0;
    int m = matrix.size(), n = matrix[0].size();
    vector height(n, 0), left(n, 0), right(n, n);
    int maxArea = 0;
    for (int i = 0; i < m; i++){
        int current_left = 0, current_right = n;
        // Update heights
        for (int j = 0; j < n; j++){
            if (matrix[i][j] == 1)
                height[j]++;
            else
                height[j] = 0;
        }
        // Update left boundaries
        for (int j = 0; j < n; j++){
            if (matrix[i][j] == 1)
                left[j] = max(left[j], current_left);
            else {
                left[j] = 0;
                current_left = j + 1;
            }
        }
        // Update right boundaries
        for (int j = n - 1; j >= 0; j--){
            if (matrix[i][j] == 1)
                right[j] = min(right[j], current_right);
            else {
                right[j] = n;
                current_right = j;
            }
        }
        // Calculate the area using height, left, and right arrays
        for (int j = 0; j < n; j++){
            maxArea = max(maxArea, height[j] * (right[j] - left[j]));
        }
    }
    return maxArea;
}

int main(){
    int N, M;
    cin >> N >> M;
    vector> garden(N, vector(M));
    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j++){
            cin >> garden[i][j];
        }
    }
    cout << maximalRectangleDP(garden) << endl;
    return 0;
}
```

**Python Code:**

```python
def maximalRectangleDP(matrix):
    if not matrix or not matrix[0]:
        return 0
    m, n = len(matrix), len(matrix[0])
    height = [0] * n
    left = [0] * n
    right = [n] * n
    max_area = 0
    for i in range(m):
        current_left, current_right = 0, n
        # Update heights
        for j in range(n):
            if matrix[i][j] == 1:
                height[j] += 1
            else:
                height[j] = 0
        # Update left boundaries
        for j in range(n):
            if matrix[i][j] == 1:
                left[j] = max(left[j], current_left)
            else:
                left[j] = 0
                current_left = j + 1
        # Update right boundaries
        for j in range(n - 1, -1, -1):
            if matrix[i][j] == 1:
                right[j] = min(right[j], current_right)
            else:
                right[j] = n
                current_right = j
        # Compute area for each column
        for j in range(n):
            max_area = max(max_area, height[j] * (right[j] - left[j]))
    return max_area

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        exit(0)
    N = int(data[0])
    M = int(data[1])
    garden = []
    index = 2
    for i in range(N):
        row = [int(x) for x in data[index:index+M]]
        index += M
        garden.append(row)
    print(maximalRectangleDP(garden))
```

---

Each of these two approaches provides a different perspective on solving the maximum rectangle problem. The first method transforms the grid into histograms and leverages a stack-based technique, while the second method uses dynamic programming with left and right boundary arrays to efficiently compute the rectangle area. Practice these approaches to build a solid foundation for tackling DSA challenges in interviews.

</details>
