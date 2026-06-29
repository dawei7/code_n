# Magic Rankings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MGCRNKP |
| Difficulty Rating | 1540 |
| Difficulty Band | Dynamic programming |
| Path | Data Structures and Algorithms |
| Lesson | Different types of dynamic programming problems |
| Official Link | [MGCRNKP](https://www.codechef.com/learn/course/dynamic-programming/LIDPDSA10/problems/MGCRNKP) |

---

## Problem Statement

Everybody loves magic, especially magicians who compete for glory on the Byteland Magic Tournament. Magician Cyael is one such magician.

Cyael has been having some issues with her last performances and today she’ll have to perform for an audience of some judges, who will change her tournament ranking, possibly increasing it. As she is a great magician she managed to gather a description of the fixed judges’ disposition on the room (which is represented as an $N \times N$ square matrix), such that she knows in advance the fixed points each judge will provide.

She also knows that the room is divided into several parallel corridors, such that we will denote the $j^{th}$ cell on corridor $i$, as $[i][j]$. Note that some judges can award Cyael, zero points or negative points, as they are never pleased with her performance. There is just one judge at each cell of the matrix, except the cells $[1][1]$ and $[N][N]$.
To complete her evaluation, she must start on the top leftmost corner of the room (cell $[1][1]$), and finish on the bottom right corner (cell $[N][N]$), moving either to the cell directly in front of her on the same corridor (that is, moving from cell $[r][c]$ to cell $[r][c+1]$, where $c+1$ $\leq$ $N$) or to the cell in the next corridor directly in front of where she is (that is, moving from cell $[r][c]$ to cell $[r+1][c]$, where $r+1$ $\leq$ $N$). She will keep doing this until she reaches the end point of the room, i.e. last cell $[N][N]$ on the last corridor. Cyael will be judged at all visited cells with a judge.

Cyael wants to maximize her average score at end of her performance. More specifically, if she passes $K$ judges, each being on cell $[i_{1}][j_{1}]$, cell $[i_{2}][j_{2}]$, $\ldots$, cell $[i_{K}][j_{K}]$ respectively, then she wants to maximize $\frac{(S[i_{1}][j_{1}] + S[i_{2}][j_{2}] + \ldots + S[i_{K}][j_{K}])}{K}$, where $S[i][j]$ denotes the points that the judge will give her on the cell $[i][j]$.
Help her determine the best path she has to follow in order to maximize her average points.

---

## Input Format

- The first line contains a single integer $T$ denoting the number of test cases. The description for $T$ test cases follows.
- For each test case, the first line contains a single integer $N$.
- Each of the next $N$ lines contains $N$ space-separated integers. The j-th integer $S[i][j]$ in i-th line denotes the points awarded by the judge at cell $[i][j]$.
- Note that the cells $[1][1]$ and $[N][N]$ have no judges, so $S[1][1]$ and $S[N][N]$ will be 0.

---

## Output Format

- For each test case, if the maximum possible average points Cyael can obtain is negative, output a single line containing "Bad Judges" (quotes for clarity).
- Otherwise, output the maximum possible average points.
- The answer will be considered correct if it has an absolute error no more than  $10^{-6}$.

---

## Constraints

- 1 $\leq$ $T$ $\leq 20$
- 2 $\leq$ $N$ $\leq 100$
- -2500 $\leq$ $S[i][j]$ $\leq 2500$
- $S[1][1]$ = $S[N][N] = 0$

---

## Examples

**Example 1**

**Input**

```text
2
2
0 -4
8 0
2
0 -45
-3  0
```

**Output**

```text
8.000000
Bad Judges
```

**Explanation**

**Test case $1$:** An optimal path for Cyael would be $(1,1)\rightarrow (2,1)\rightarrow (2,2)$. This way Cyael faces $1$ judge and gets a total score of $8$. Thus, the average score is $\frac{8}{1} = 8$.

**Test case $2$:** No matter what path Cyael chooses, the final score would be less than $0$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
0 -4
8 0
```

**Output for this case**

```text
8.000000
```



#### Test case 2

**Input for this case**

```text
2
0 -45
-3  0
```

**Output for this case**

```text
Bad Judges
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Magic Rankings](https://www.codechef.com/learn/course/dynamic-programming/LIDPDSA10/problems/MGCRNKP)

### [](#problem-statement-1)Problem Statement:

Everybody loves magic, especially magicians who compete for glory in the Byteland Magic Tournament. Magician Cyael faces challenges in her performances and must perform for judges whose fixed scores she knows in advance, represented in an `N×N` square matrix. The task is to calculate the maximum score Cyael can achieve based on the judges’ scores.

### [](#approach-2)Approach:

The key idea of this solution is to use dynamic programming to find the maximum score Cyael can achieve while traversing the matrix from the top-left to the bottom-right corner. We maintain a `DP` array where each cell `DP[i][j]` represents the maximum score obtainable at that position by considering the maximum scores from the top and left cells, effectively allowing us to find the best path through the judges’ scores. If the final score is negative, it indicates “Bad Judges”; otherwise, we calculate the average score based on the total movements made.

### [](#time-complexity-3)Time Complexity:

- **O(n^2)** for filling the `DP` array as we iterate through each cell in the n×n matrix.

### [](#space-complexity-4)Space Complexity:

- **O(n^2)** for the `DP` array used to store the maximum scores.

</details>
