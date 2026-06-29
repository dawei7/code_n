# Maximal crosses

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXCROSS |
| Difficulty Rating | 1570 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [MAXCROSS](https://www.codechef.com/practice/course/2to3stars/LP2TO306/problems/MAXCROSS) |

---

## Problem Statement

On the matrix A sized n×n, some cells were marked by crosses (X). For each cell (i,j) (with i – the row index, j – the column index), we define B(i,j) as the maximal number of continuous crosses “going across” the cell (i,j) in the same horizontal, vertical or diagonal; B(i,j)=0 if A(i,j) is empty ( '.' ).
[ Empty cells are marked by '.'] .

Clarification:

Continuous crosses going across cell (i,j) in horizontal direction = x1 + x2 - 1

where x1 = highest possible x such that

          j + x - 1<= n and A(i, j ... j + x - 1) are all 'X'

and x2 = highest possible x such that

          j - x + 1 > 0  and A(i, j - x + 1...j) are all 'X'

Similarily we can extend the definition for vertical and diagonal directions.

### Task

Given matrix A as input, calculate matrix B.

### Input

-  The first line contains the integer n.

-  Then follow n lines , each containing n characters. The j-th character of the i-th line represents the cell (i,j) of the matrix A, with A(i,j)='X' if it contains a cross, or A(i,j)='.' if it is empty.

### Output

Output n lines, each contains n integers, the j-th integer of the i-th line shows the value of B(i,j).
***(Each integer on a same line must be separated by exactly one space character)***

### Limitations
0

---

## Examples

**Example 1**

**Input**

```text
10
..X....XX.
XX.X..XX.X
.....XX..X
.XXX..X.X.
.....X..XX
....X....X
X.X....XX.
.X...X.X.X
X.X..X....
..XXXXX.XX
```

**Output**

```text
0 0 2 0 0 0 0 3 3 0
2 2 0 2 0 0 3 3 0 2
0 0 0 0 0 3 3 0 0 2
0 3 3 3 0 0 3 0 2 0
0 0 0 0 0 3 0 0 2 2
0 0 0 0 3 0 0 0 0 3
4 0 3 0 0 0 0 2 3 0
0 4 0 0 0 3 0 3 0 2
3 0 4 0 0 3 0 0 0 0
0 0 5 5 5 5 5 0 2 2
```

**Explanation**

**Cell $(0,0)$:** The cell is empty, thus $B(0,0) = 0$.

**Cell $(0,2)$:** The maximum number of continuous crosses are present diagonally to the bottom left and bottom right. The maximum number of crosses is $2$.

**Cell $(0,8)$:** The maximum number of continuous crosses are present diagonally to the bottom left. The maximum number of crosses is $3$.

**Cell $(9,2)$:** The maximum number of continuous crosses is present to the right. The maximum number of crosses is $5$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
..X....XX.
```

**Output for this case**

```text
0 0 2 0 0 0 0 3 3 0
```



#### Test case 2

**Input for this case**

```text
XX.X..XX.X
```

**Output for this case**

```text
2 2 0 2 0 0 3 3 0 2
```



#### Test case 3

**Input for this case**

```text
.....XX..X
```

**Output for this case**

```text
0 0 0 0 0 3 3 0 0 2
```



#### Test case 4

**Input for this case**

```text
.XXX..X.X.
```

**Output for this case**

```text
0 3 3 3 0 0 3 0 2 0
```



#### Test case 5

**Input for this case**

```text
.....X..XX
```

**Output for this case**

```text
0 0 0 0 0 3 0 0 2 2
```



#### Test case 6

**Input for this case**

```text
....X....X
```

**Output for this case**

```text
0 0 0 0 3 0 0 0 0 3
```



#### Test case 7

**Input for this case**

```text
X.X....XX.
```

**Output for this case**

```text
4 0 3 0 0 0 0 2 3 0
```



#### Test case 8

**Input for this case**

```text
.X...X.X.X
```

**Output for this case**

```text
0 4 0 0 0 3 0 3 0 2
```



#### Test case 9

**Input for this case**

```text
X.X..X....
```

**Output for this case**

```text
3 0 4 0 0 3 0 0 0 0
```



#### Test case 10

**Input for this case**

```text
..XXXXX.XX
```

**Output for this case**

```text
0 0 5 5 5 5 5 0 2 2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINKS

[Practice](http://www.codechef.com/problems/MAXCROSS/)

[Contest](http://www.codechef.com/JULY10/problems/MAXCROSS/)

### DIFFICULTY

EASY

### EXPLANATION

[

4786143715_cf8f98d352_b.jpg734×843
](http://farm5.static.flickr.com/4101/4786143715_cf8f98d352_b.jpg)

</details>
