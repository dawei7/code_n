# Magic Rankings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MGCRNK |
| Difficulty Rating | 1540 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [MGCRNK](https://www.codechef.com/practice/course/2to3stars/LP2TO306/problems/MGCRNK) |

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

# PROBLEM LINKS

[Practice](http://www.codechef.com/problems/MGCRNK)

[Contest](http://www.codechef.com/DEC12/problems/MGCRNK)

## DIFFICULTY

SIMPLE

## PREREQUISITES

Dynamic Programming

## PROBLEM

There is an N × N matrix. The cells in this matrix are numbered [1][1] through [N][N]. Each cell [i][j] contains an integer S[i][j]. A path is defined as a sequence of cells that starts on the top left cell (cell [1][1]), moving only rightwards or downwards, and ends on the bottom right cell (cell [N][N]). Cyael wants to find a path with the maximum average value of all integers on the path, excluding the first and the last cells. Help her.

## QUICK EXPLANATION

The number of cells on any path is constant, i.e., 2N-3. Therefore, we can just find a path with the maximum total values of all integers on the path, and then divide the maximum total values by the number of cells.

This becomes a classical dynamic programming problem. Let dp[i][j] be the maximum total values of any path from [1][1] to [i][j]. The recurrence is dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + S[i][j], with dp[i][j] = -infinity for i < 1 or j < 1. The base case is dp[1][1] = S[1][1].

The answer to this problem is the maximum average value = dp[N][N] / (2N-3).

## EXPLANATION

First, let’s count how many cells Cyael will pass in any path. It turns out that this number is always constant, i.e., 2N-1. An easy way to see this is as follows. In any path, Cyael must move rightwards exactly (N-1) times and downwards exactly (N-1) times to get to cell [N][N]. Therefore, the number of cells is 1 + (N-1) + (N-1) = 2N-1. Excluding the first and the last cells, the number of cells is 2N-3.

Since the number of cells on any path is constant, we can simplify the problem into finding a path with the maximum total values instead of the average. In the end, we can divide the answer with 2N-3 to get the average value.

The simpler problem can be solved using dynamic programming. The state consists of two values: the current row and the current column. Let dp[i][j] be the maximum total values of any path from [1][1] to [i][j]. There are (at most) two possibilities:

- The path with the maximum total value goes from cell [1][1] to cell [i-1][j], and then downwards to cell [i][j]. The maximum total value is dp[i-1][j] + S[i][j]. This can happen when i > 1.

- The path with the maximum total value goes from cell [1][1] to cell [i][j-1], and then rightwards to cell [i][j]. The maximum total value is dp[i][j-1] + S[i][j]. This can happen when j > 1.

The base case is when we are on the first cell of the path. dp[1][1] = S[1][1].

As we want to maximize the total value, we get the recurrence dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + S[i][j]. Note that in this recurrence, dp[i-1][j] and dp[i][j-1] may refer to non-existing cells. We can fix this by improving the recurrence into:

dp[i][j] =

- S[1][1], if i = 1 and j = 1

- dp[i-1][j] + S[i][j]; if j = 1

- dp[i][j-1] + S[i][j]; if i = 1

- max(dp[i-1][j], dp[i][j-1]) + S[i][j]; otherwise.

Another easy way is to assign dp[i][j] = -infinity if i < 1 or j < 1. Because we don’t have infinity in any programming language, we can assign dp[i][j] to a value that is smaller than any value in the DP table. The minimum value is -2500 × (2N-3), so we can assign safely to for example -1,000,000,000.

The time and space complexity of this problem is O(N2).

Here is a pseudocode of this solution:

`
read(N)

for i = 1; i ? N; i++:
    dp[0][i] = dp[i][0] = -1000000000

for i = 1; i ? N; i++:
    for j = 1; j ? N; j++:
        read(S[i][j])
        if 1 = 1 and j = 1:
    	    dp[i][j] = S[i][j]
    	else
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + S[i][j]

print(dp[N][N] / (2N-3))
`

## SETTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/December/Setter/MGCRNK.cpp).

## TESTER’S SOLUTION

Can be found [here](http://www.codechef.com/download/Solutions/2012/December/Tester/MGCRNK.c).

</details>
