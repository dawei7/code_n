# Array - Matrix operations

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP02 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [PREP02](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/PREP02) |

---

## Problem Statement

You are given a matrix $A$ of size $N \times N$.

You need to rotate the matrix $A$ by $180$ degrees, either in clockwise or anti-clockwise direction.
Check the samples below for clarity.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a $N + 1$ lines of input.
   - First line of each test case contains the size of the matrix $N$.
   - This is followed by $N$ lines - Each line of input contains $N$ space-separated integers which form the $N \times N$ matrix.

---

## Output Format

For each test case, output $N$ lines, where each line has $N$ space-separated integers, denoting the matrix after rotating it $180$ degrees.

---

## Constraints

- $1 \leq T \leq 5000$
- $1 \leq N \leq 100$
- $1 \leq A_{(i,j)} \leq 10^5$, where $A_{(i, j)}$ denotes the $j^{th}$ element of the $i^{th}$ row.

---

## Examples

**Example 1**

**Input**

```text
4
1
1
2
1 2
3 4
3
1 2 3
4 5 6
7 8 9
4
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
```

**Output**

```text
1
4 3
2 1
9 8 7
6 5 4
3 2 1
16 15 14 13
12 11 10 9
8 7 6 5
4 3 2 1
```

**Explanation**

**Test case $1$:** There is only one element in the matrix, thus the rotated matrix is same.

**Test case $2$**: On rotating by $180$ degrees, the matrix becomes $[[4, 3], [2, 1]]$.

**Test case $3$:** On rotating by $180$ degrees, the matrix becomes $[[9, 8, 7], [6, 5, 4], [3, 2, 1]]$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Rotating a Matrix by 180 Degrees

In this lesson, we will explore different approaches to rotate a given $N \times N$ matrix by $180^\circ$. Rotating a matrix by $180^\circ$ means that each element at position $(i, j)$ in the matrix moves to the position $(N-1-i, N-1-j)$ after rotation.

This problem is essential for DSA interview preparation because it tests your understanding of array manipulations, in-place algorithms, and the use of auxiliary space.

---

## Approach 1: In-Place Swapping

**Idea:**
For each element in the matrix, swap it with its $180^\circ$ counterpart. In a matrix with indices from $0$ to $N-1$, the element at $(i, j)$ swaps with the element at $(N-1-i, N-1-j)$.
If $N$ is odd, after swapping the top and bottom halves, the middle row remains; we then swap the elements in the middle row to achieve the correct order.

### C++ Implementation (Approach 1)
```cpp
#include
#include
using namespace std;

void rotateMatrix(vector>& matrix) {
    int n = matrix.size();
    // Swap elements in the top half with their corresponding bottom half elements
    for (int i = 0; i < n / 2; i++) {
        for (int j = 0; j < n; j++) {
            swap(matrix[i][j], matrix[n - 1 - i][n - 1 - j]);
        }
    }
    // If the matrix has an odd size, swap the elements in the middle row
    if (n % 2 == 1) {
        int mid = n / 2;
        for (int j = 0; j < n / 2; j++) {
            swap(matrix[mid][j], matrix[mid][n - 1 - j]);
        }
    }
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        vector> matrix(n, vector(n));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> matrix[i][j];
            }
        }

        rotateMatrix(matrix);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << matrix[i][j] << " ";
            }
            cout << endl;
        }
    }

    return 0;
}
```

### Python Implementation (Approach 1)
```python
def rotate_matrix(matrix):
    n = len(matrix)
    # Swap elements in the top half with their corresponding rotated positions
    for i in range(n // 2):
        for j in range(n):
            matrix[i][j], matrix[n - 1 - i][n - 1 - j] = matrix[n - 1 - i][n - 1 - j], matrix[i][j]
    # If the matrix has an odd size, swap the middle row's symmetric elements
    if n % 2 == 1:
        mid = n // 2
        for j in range(n // 2):
            matrix[mid][j], matrix[mid][n - 1 - j] = matrix[mid][n - 1 - j], matrix[mid][j]

# Example usage:
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = [list(map(int, input().split())) for _ in range(n)]
        rotate_matrix(matrix)
        for row in matrix:
            print(" ".join(map(str, row)))
```

---

## Approach 2: Reverse Rows and Columns

**Idea:**
Rotating a matrix by $180^\circ$ is equivalent to reversing the order of the rows of the matrix and then reversing each row individually. This method is simple and leverages high-level operations such as list or array reversal.

### C++ Implementation (Approach 2)
```cpp
#include
#include
#include
using namespace std;

void rotateMatrix(vector>& matrix) {
    int n = matrix.size();
    // Reverse the rows of the matrix
    reverse(matrix.begin(), matrix.end());
    // Reverse each row individually
    for (int i = 0; i < n; i++) {
        reverse(matrix[i].begin(), matrix[i].end());
    }
}

int main() {
    int t;
    cin >> t;

    while(t--) {
        int n;
        cin >> n;
        vector> matrix(n, vector(n));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> matrix[i][j];
            }
        }

        rotateMatrix(matrix);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << matrix[i][j] << " ";
            }
            cout << endl;
        }
    }

    return 0;
}
```

### Python Implementation (Approach 2)
```python
def rotate_matrix(matrix):
    # Reverse the matrix (reverse the order of rows)
    matrix.reverse()
    # Reverse each individual row to complete the rotation
    for row in matrix:
        row.reverse()

# Example usage:
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = [list(map(int, input().split())) for _ in range(n)]
        rotate_matrix(matrix)
        for row in matrix:
            print(" ".join(map(str, row)))
```

---

## Approach 3: Using Extra Space

**Idea:**
Instead of modifying the matrix in place, we create a new matrix of the same size and copy elements from the original matrix into their correct rotated positions. The element in position $(i, j)$ of the original matrix is placed at position $(N-1-i, N-1-j)$ in the new matrix.

### C++ Implementation (Approach 3)
```cpp
#include
#include
using namespace std;

vector> rotateMatrix(const vector>& matrix) {
    int n = matrix.size();
    vector> rotated(n, vector(n, 0));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            rotated[i][j] = matrix[n - 1 - i][n - 1 - j];
        }
    }
    return rotated;
}

int main() {
    int t;
    cin >> t;

    while(t--) {
        int n;
        cin >> n;
        vector> matrix(n, vector(n));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> matrix[i][j];
            }
        }

        vector> rotated = rotateMatrix(matrix);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << rotated[i][j] << " ";
            }
            cout << endl;
        }
    }

    return 0;
}
```

### Python Implementation (Approach 3)
```python
def rotate_matrix(matrix):
    n = len(matrix)
    # Create a new matrix initialized with zeros
    rotated = [[0] * n for _ in range(n)]
    # Place each element in its rotated position
    for i in range(n):
        for j in range(n):
            rotated[i][j] = matrix[n - 1 - i][n - 1 - j]
    return rotated

# Example usage:
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = [list(map(int, input().split())) for _ in range(n)]
        rotated = rotate_matrix(matrix)
        for row in rotated:
            print(" ".join(map(str, row)))
```

---

## Summary

- **Approach 1 (In-Place Swapping):** Efficiently rotates the matrix by directly swapping elements with their $180^\circ$ counterparts without using extra space.
- **Approach 2 (Reversing Rows and Columns):** Utilizes simple reversal operations to achieve the rotation, making the solution easy to understand and implement.
- **Approach 3 (Using Extra Space):** Creates a new matrix and assigns each element to its rotated position, which is intuitive but uses additional memory.

Understanding these approaches enhances your problem-solving toolkit and prepares you for handling similar matrix manipulation challenges in technical interviews.

</details>
