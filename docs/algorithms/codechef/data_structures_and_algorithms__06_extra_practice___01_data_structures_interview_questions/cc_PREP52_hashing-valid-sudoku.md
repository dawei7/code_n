# Hashing - Valid Sudoku

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PREP52 |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Hashing |
| Official Link | [PREP52](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_13/problems/PREP52) |

---

## Problem Statement

You are given a $9\times 9$ [Sudoku](https://en.wikipedia.org/wiki/Sudoku) represented by a square matrix $A$. Some cells are filled with digits $(1$ to $9)$ and some cells are empty, denoted by $0$.

Find whether the given sudoku is a *valid sudoku*.

A *valid sudoku* is the one with following rules:
- Each row must contain the digits $(1$ to $9)$ without repetition.
- Each column must contain the digits $(1$ to $9)$ without repetition.
- Each of the nine $3\times 3$ sub-boxes that compose the grid must contain the digits $(1$ to $9)$ without repetition.

*Note:*
- A Sudoku board (partially filled) could be valid but not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of nine lines of input.
    - The next $9$ lines describe the rows of sudoku. The $i^{th}$ of these $9$ lines contains $9$ integers. Some cells are filled with digits $(1$ to $9)$ and some cells are empty, denoted by $0$.

---

## Output Format

For each test case, output $1$ if the given Sudoku is a *valid sudoku*, or output $0$ otherwise.

---

## Constraints

- $1 \leq T \leq 10^5$
- $0 \leq A_{(i, j)} \leq 9$

---

## Examples

**Example 1**

**Input**

```text
3
9 0 0 0 2 0 7 5 0
6 0 0 0 5 0 0 4 0
0 2 0 4 0 0 0 1 0
2 0 8 0 0 0 0 0 0
0 7 0 5 0 9 0 6 0
0 0 0 0 0 0 4 0 1
0 1 0 0 0 5 0 8 0
0 9 0 0 7 0 0 0 4
0 8 2 0 4 0 0 0 6
1 5 9 0 0 6 0 3 2
2 7 4 0 0 0 0 0 0
3 8 6 2 0 0 0 0 5
4 9 2 5 0 1 0 8 0
6 3 7 0 4 0 0 0 0
5 1 0 8 2 0 0 0 0
8 2 1 0 0 0 0 0 0
7 6 0 1 0 0 4 2 0
9 4 3 0 7 0 0 6 1
8 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

**Output**

```text
1
1
0
```

**Explanation**

**Test case $1$:** The given Sudoku board is within the given rules.

**Test case $2$:** The given Sudoku board is within the given rules.

**Test case $3$:** There are two $8$s in the top-left $3\times 3$ sub-box. Hence, it is an invalid Sudoku.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
9 0 0 0 2 0 7 5 0
6 0 0 0 5 0 0 4 0
0 2 0 4 0 0 0 1 0
2 0 8 0 0 0 0 0 0
0 7 0 5 0 9 0 6 0
0 0 0 0 0 0 4 0 1
0 1 0 0 0 5 0 8 0
0 9 0 0 7 0 0 0 4
0 8 2 0 4 0 0 0 6
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
1 5 9 0 0 6 0 3 2
2 7 4 0 0 0 0 0 0
3 8 6 2 0 0 0 0 5
4 9 2 5 0 1 0 8 0
6 3 7 0 4 0 0 0 0
5 1 0 8 2 0 0 0 0
8 2 1 0 0 0 0 0 0
7 6 0 1 0 0 4 2 0
9 4 3 0 7 0 0 6 1
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
8 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

In this lesson, we will explore how to validate a partially filled Sudoku board. A board is considered valid if every row, every column, and every $3 \times 3$ sub-box does not contain duplicate digits (ignoring zeros). We will discuss three different approaches to solve this problem, with examples in both C++ and Python.

---

### Approach 1: Iterative Row, Column, and Sub-Box Checks

**Idea:**

We can break the validation into three distinct steps:
1. **Row Check:** For each row, iterate through all cells and ensure no digit from $1$ to $9$ appears more than once.
2. **Column Check:** For each column, ensure the same property holds.
3. **Sub-Box Check:** The board is divided into nine $3 \times 3$ sub-boxes. For each sub-box, check that no digit repeats.

For each of these steps, we can use a boolean array (or a set in languages like Python) to keep track of the digits we have already seen. If we encounter a digit that has already been seen, the board is invalid.

**Time Complexity:** Since we always process a fixed $9 \times 9$ grid, the complexity is constant, i.e. $O(1)$ per test case.

**C++ Implementation:**

```cpp
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while(T--){
        int sudoku[9][9];
        for (int i = 0; i < 9; i++){
            for (int j = 0; j < 9; j++){
                cin >> sudoku[i][j];
            }
        }
        bool valid = true;

        // Check rows
        for (int i = 0; i < 9 && valid; i++){
            bool seen[10] = {false};
            for (int j = 0; j < 9; j++){
                int num = sudoku[i][j];
                if (num != 0){
                    if (seen[num]){
                        valid = false;
                        break;
                    }
                    seen[num] = true;
                }
            }
        }

        // Check columns
        for (int j = 0; j < 9 && valid; j++){
            bool seen[10] = {false};
            for (int i = 0; i < 9; i++){
                int num = sudoku[i][j];
                if (num != 0){
                    if (seen[num]){
                        valid = false;
                        break;
                    }
                    seen[num] = true;
                }
            }
        }

        // Check 3x3 sub-boxes
        for (int block = 0; block < 9 && valid; block++){
            bool seen[10] = {false};
            int startRow = (block / 3) * 3;
            int startCol = (block % 3) * 3;
            for (int i = startRow; i < startRow + 3; i++){
                for (int j = startCol; j < startCol + 3; j++){
                    int num = sudoku[i][j];
                    if (num != 0){
                        if (seen[num]){
                            valid = false;
                            break;
                        }
                        seen[num] = true;
                    }
                }
                if (!valid)
                    break;
            }
        }

        cout << (valid ? 1 : 0) << "\n";
    }
    return 0;
}
```

**Python Implementation:**

```python
def is_valid_sudoku(sudoku):
    # Check rows
    for row in sudoku:
        seen = set()
        for num in row:
            if num != 0:
                if num in seen:
                    return False
                seen.add(num)

    # Check columns
    for j in range(9):
        seen = set()
        for i in range(9):
            num = sudoku[i][j]
            if num != 0:
                if num in seen:
                    return False
                seen.add(num)

    # Check 3x3 sub-boxes
    for block in range(9):
        seen = set()
        startRow = (block // 3) * 3
        startCol = (block % 3) * 3
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                num = sudoku[i][j]
                if num != 0:
                    if num in seen:
                        return False
                    seen.add(num)
    return True

import sys
input_data = sys.stdin.read().strip().split()
if input_data:
    T = int(input_data[0])
    index = 1
    results = []
    for _ in range(T):
        sudoku = []
        for i in range(9):
            row = list(map(int, input_data[index:index+9]))
            index += 9
            sudoku.append(row)
        results.append(1 if is_valid_sudoku(sudoku) else 0)
    print("\n".join(map(str, results)))
```

---

### Approach 2: Unified Single Pass Validation with Hash Sets

**Idea:**

Instead of performing three separate loops for rows, columns, and sub-boxes, you can iterate over the board once. For every non-zero cell at position $(i, j)$, determine its corresponding $3 \times 3$ sub-box using:

$$ box\_index = \left(\lfloor \frac{i}{3} \rfloor \times 3 \right) + \lfloor \frac{j}{3} \rfloor. $$

Maintain three lists (or arrays) of sets:
- One for rows,
- One for columns,
- One for boxes.

When processing each cell, check if the digit already exists in the corresponding row, column, or box. If it does, the Sudoku is invalid; otherwise, add the digit to the corresponding set.

**C++ Implementation:**

```cpp
#include
#include
#include
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while(T--){
        int sudoku[9][9];
        for (int i = 0; i < 9; i++){
            for (int j = 0; j < 9; j++){
                cin >> sudoku[i][j];
            }
        }

        bool isValid = true;
        vector> rows(9), cols(9), boxes(9);

        for (int i = 0; i < 9 && isValid; i++){
            for (int j = 0; j < 9 && isValid; j++){
                int num = sudoku[i][j];
                if (num != 0) {
                    int boxIndex = (i / 3) * 3 + (j / 3);
                    if (rows[i].count(num) || cols[j].count(num) || boxes[boxIndex].count(num)) {
                        isValid = false;
                        break;
                    }
                    rows[i].insert(num);
                    cols[j].insert(num);
                    boxes[boxIndex].insert(num);
                }
            }
        }
        cout << (isValid ? 1 : 0) << "\n";
    }

    return 0;
}
```

**Python Implementation:**

```python
def is_valid_sudoku(sudoku):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]

    for i in range(9):
        for j in range(9):
            num = sudoku[i][j]
            if num:
                box_index = (i // 3) * 3 + (j // 3)
                if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                    return False
                rows[i].add(num)
                cols[j].add(num)
                boxes[box_index].add(num)
    return True

import sys
input_data = sys.stdin.read().strip().split()
if input_data:
    T = int(input_data[0])
    index = 1
    results = []
    for _ in range(T):
        sudoku = []
        for i in range(9):
            row = list(map(int, input_data[index:index+9]))
            index += 9
            sudoku.append(row)
        results.append(1 if is_valid_sudoku(sudoku) else 0)
    print("\n".join(map(str, results)))
```

---

### Approach 3: Bitmasking for Effective Validation

**Idea:**

You can optimize space and performance using bit manipulation. Represent each row, column, and box using a 9-bit integer. For any non-zero digit $d$, the corresponding bit is given by $bit = 1 \ll d$. For each cell, check if the corresponding bit is already set in the row, column, or box. If it is, then the board is invalid. Otherwise, update the corresponding masks using bitwise OR.

**Advantages:**
- This method uses constant space with simple integer arrays.
- Bit-level operations are generally very fast.

**C++ Implementation:**

```cpp
#include
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while(T--){
        int sudoku[9][9];
        for (int i = 0; i < 9; i++){
            for (int j = 0; j < 9; j++){
                cin >> sudoku[i][j];
            }
        }

        bool isValid = true;
        int rows[9] = {0}, cols[9] = {0}, boxes[9] = {0};

        for (int i = 0; i < 9 && isValid; i++){
            for (int j = 0; j < 9 && isValid; j++){
                int num = sudoku[i][j];
                if (num != 0){
                    int bit = 1 << num;  // Create bitmask for num
                    int boxIndex = (i / 3) * 3 + (j / 3);
                    if ((rows[i] & bit) || (cols[j] & bit) || (boxes[boxIndex] & bit)){
                        isValid = false;
                        break;
                    }
                    rows[i] |= bit;
                    cols[j] |= bit;
                    boxes[boxIndex] |= bit;
                }
            }
        }
        cout << (isValid ? 1 : 0) << "\n";
    }

    return 0;
}
```

**Python Implementation:**

```python
def is_valid_sudoku(sudoku):
    rows = [0] * 9
    cols = [0] * 9
    boxes = [0] * 9

    for i in range(9):
        for j in range(9):
            num = sudoku[i][j]
            if num:
                bit = 1 << num  # Bitmask for the current number
                box_index = (i // 3) * 3 + (j // 3)
                if (rows[i] & bit) or (cols[j] & bit) or (boxes[box_index] & bit):
                    return False
                rows[i] |= bit
                cols[j] |= bit
                boxes[box_index] |= bit
    return True

import sys
input_data = sys.stdin.read().strip().split()
if input_data:
    T = int(input_data[0])
    index = 1
    results = []
    for _ in range(T):
        sudoku = []
        for i in range(9):
            row = list(map(int, input_data[index:index+9]))
            index += 9
            sudoku.append(row)
        results.append(1 if is_valid_sudoku(sudoku) else 0)
    print("\n".join(map(str, results)))
```

---

### Conclusion

Each of the approaches described above successfully validates a Sudoku board while checking the necessary constraints:
- **Approach 1** leverages separate iterative checks for rows, columns, and sub-boxes.
- **Approach 2** efficiently combines the checks into one pass using hash sets.
- **Approach 3** utilizes bit manipulation to perform constant-time checks and updates.

Understanding these methods enriches your problem-solving toolkit and offers flexibility depending on the constraints and performance requirements of your task. Choose an approach based on your familiarity and any specific scenario where one method might outperform the others.

Happy coding!

</details>
