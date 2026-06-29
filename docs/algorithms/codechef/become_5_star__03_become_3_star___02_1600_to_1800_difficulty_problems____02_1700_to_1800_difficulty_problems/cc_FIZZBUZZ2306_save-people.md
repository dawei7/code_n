# Save People

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FIZZBUZZ2306 |
| Difficulty Rating | 1750 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [FIZZBUZZ2306](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/FIZZBUZZ2306) |

---

## Problem Statement

Chef has a $2$-D grid with $N$ rows and $M$ columns. The cell at the intersection of the $i$-th row and $j$-th column is denoted cell $(i, j)$.
Initially, *only* cell $(x, y)$ of the grid is infected.

Chef can select **exactly one** non-infected cell and *vaccinate* it.
Then, the infection and the vaccine spread across the grid, as follows:
- First, any cell that is neither vaccinated nor infected, but is adjacent (horizontally or vertically) to an infected cell, becomes infected itself.
- Next, any cell that is neither vaccinated nor infected, but is adjacent (horizontally or vertically) to a vaccinated cell, becomes vaccinated itself.

This process repeats till every cell in the grid is either infected or vaccinated.
For example, on a $6\times 6$ grid with $(x, y) = (2, 2)$ and the vaccine placed at $(5, 4)$ initially, the spread would look like:

Find the **maximum** possible number of vaccinated cells Chef can obtain, if he chooses the initial position of the vaccine optimally.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the dimensions of the grid.
    - The second line of each test case contains two space-separated integers $x$ and $y$ — the coordinates of the infected cell.

---

## Output Format

For each test case, output on a new line the maximum number of vaccinated cells attainable.

---

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N, M \leq 10^5$
- $1 \leq x \leq N$
- $1 \leq y \leq M$

---

## Examples

**Example 1**

**Input**

```text
2
3 3
1 2
3 2
1 1
```

**Output**

```text
6
4
```

**Explanation**

**Test case $1$:** It's optimal to vaccinate cell $(2, 2)$.
The spread of infection and vaccine is visualized below.
![](https://cdn.codechef.com/download/Contest+images/START106/image_4.gif)

$6$ cells are vaccinated, and this is the best we can do.

**Test case $2$:** It's optimal to vaccinate cell $(2, 1)$.
The spread of infection and vaccine is visualized below.
![](https://cdn.codechef.com/download/Contest+images/START106/image_3.gif)

$4$ cells are vaccinated, which is the best we can do.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 3
1 2
```

**Output for this case**

```text
6
```



#### Test case 2

**Input for this case**

```text
3 2
1 1
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/FIZZBUZZ2306)

[Contest: Division 1](https://www.codechef.com/START106A/problems/FIZZBUZZ2306)

[Contest: Division 2](https://www.codechef.com/START106B/problems/FIZZBUZZ2306)

[Contest: Division 3](https://www.codechef.com/START106C/problems/FIZZBUZZ2306)

[Contest: Division 4](https://www.codechef.com/START106D/problems/FIZZBUZZ2306)

***Authors:*** [naisheel](https://www.codechef.com/users/naisheel), [jalp1428](https://www.codechef.com/users/jalp1428), [vasu_2344](https://www.codechef.com/users/vasu_2344)

***Tester:*** [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

1750

# [](#prerequisites-3)PREREQUISITES:

Observation

# [](#problem-4)PROBLEM:

There’s an N\times M grid with a single cell (x, y) initially infected.

You can choose some other cell (x', y') to vaccinate, then both the infection and vaccine spread across the grid horizontally and vertically in stages, with the infection spreading first.

If the vaccination cell is chosen optimally, what’s the maximum number of cells that can be vaccinated?

# [](#explanation-5)EXPLANATION:

Trying out a couple of cases on paper, you might notice that it always seems optimal to choose to place the vaccine right next to the infection.

Intuitively this seems reasonable too, since we curtail the infection as much as possible.

Indeed, this is optimal. Let’s prove it!

Proof

Suppose the vaccine is placed at cell (x', y'). Without loss of generality, let x'\geq x and y'\geq y.

Notice that the infection and vaccine both spread out in a ‘diamond’ shape with the sources as the center.

Consider the first instant of time when the two diamonds touch reach other at their borders.

Since the vaccine spreads only after the infection, note that the vaccine’s diamond cannot include *both* (x', y) and (x, y') — at most one of them can be included in it.

So suppose (x', y) isn’t included in the vaccine’s diamond.

Then, no cell in a column \leq y can ever be vaccinated, so the absolute best we can do is vaccinate all the cells in columns \gt y.

Note that we could’ve achieved this by placing the vaccine at (x, y+1) as well, which is adjacent to the initial infection cell.

Similarly, if (x ,y') isn’t included, no cell at row \leq x can be vaccinated ever; and the best we can do in this case is to vaccinate all rows \gt x, doable by placing the vaccine at (x+1, y).

So, placing the vaccine adjacent to the infection is always optimal.

Now that we know this, there are at most four choices to check: (x\pm 1, y) and (x, y\pm 1).

For each one, computing the number of vaccinated cells isn’t too hard:

- (x+1, y) will vaccinate every row \gt x and nothing \leq x, for a total of (N-x)\cdot M cells.

- (x-1, y) will vaccinate every row \lt x and nothing \geq x, for a total of (x-1)\cdot M cells.

- (x, y+1) will vaccinate every column \gt y and nothing \leq y, for a total of (M-y)\cdot N cells.

- (x, y-1) will vaccinate every column \lt y and nothing \geq y, for a total of (y-1)\cdot N cells.

The final answer is the maximum of these four numbers.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n, m = map(int, input().split())
    x, y = map(int, input().split())

    ans = n*max(m-y, y-1)
    ans = max(ans, m*max(n-x, x-1))
    print(ans)
``

</details>
