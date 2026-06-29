# Solve More Problems!

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SOLVEMORE |
| Difficulty Rating | 1993 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1900 to 2000 difficulty problems |
| Official Link | [SOLVEMORE](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/SOLVEMORE) |

---

## Problem Statement

Chef came across a new online judge that has $N$ problems, and decided that he wants to solve them.

Chef takes $A_i$ consecutive minutes to solve the $i$-th problem, and will take a break of $B_i$ minutes immediately after solving it.
That is, Chef will solve a problem, then take a break. Solve another problem, then take another break, and so on.

Chef has $K$ minutes of free time. If he chooses the problems and their order optimally, what is the **maximum** number of problems he can solve in this time?

Note that a problem is considered solved if Chef finishes solving it by the $K$-th minute, even if the break time of the last problem extends past minute $K$. See the sample tests below for an example.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $K$ — the number of problems in the online judge and Chef's free time, respectively.
    - The second line of each test case contains $N$ space-separated integers — the values $A_1, A_2, \ldots, A_N$.
    - The third line of each test case contains $N$ space-separated integers — the values $B_1, B_2, \ldots, B_N$.

---

## Output Format

For each test case, output on a new line the **maximum** number of problems that Chef can solve within $K$ minutes.

---

## Constraints

- $1 \leq T \leq 2\cdot 10^4$
- $1 \leq N \leq 2\cdot 10^5$
- $1 \leq K \leq 10^8$
- $1 \leq A_i \leq 10^8$
- $0 \leq B_i \leq 10^8$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
3 10
3 4 5
2 4 2
3 8
3 4 5
2 4 2
5 20
23 54 124 54 83
2 9 5 2 10
5 20
4 7 12 34 13
30 4 3 0 9
```

**Output**

```text
2
1
0
2
```

**Explanation**

**Test case $1$:** Chef can solve the first problem followed by the second problem.
- $3$ minutes for the first problem
- $2$ minutes of break time after solving it, for a total of $5$ minutes
- $5$ minutes for the third problem, for a total of $10$ minutes
- There's two minutes of break time left which goes beyond $10$ minutes, but that's ok: Chef finished solving $2$ problems within $10$ minutes.

**Test case $2$:** The same times as the first sample, but with $K = 8$. Now, Chef can solve any one problem, but cannot solve a second one no matter what.

**Test case $3$:** Chef can't solve anything within $20$ minutes.

**Test case $4$:** Chef can solve the third problem followed by the first problem.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 10
3 4 5
2 4 2
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
3 8
3 4 5
2 4 2
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
5 20
23 54 124 54 83
2 9 5 2 10
```

**Output for this case**

```text
0
```



#### Test case 4

**Input for this case**

```text
5 20
4 7 12 34 13
30 4 3 0 9
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Problem link](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF2000/problems/SOLVEMORE)

### [](#problem-statement-1)Problem Statement:

Chef came across a new online judge that has N problems, and decided that he wants to solve them.

Chef takes A_i consecutive minutes to solve the i-th problem, and will take a break of B_i minutes immediately after solving it.

That is, Chef will solve a problem, then take a break. Solve another problem, then take another break, and so on.

Chef has K minutes of free time. If he chooses the problems and their order optimally, what is the **maximum** number of problems he can solve in this time?

Note that a problem is considered solved if Chef finishes solving it by the K-th minute, even if the break time of the last problem extends past minute K. See the sample tests below for an example.

### [](#approach-2)Approach:

The code solves the problem by calculating the total time Chef needs to solve and take breaks for each problem. Each problem has two components: solving time A[i] and break time B[i] . The goal is to pick problems such that the total time spent doesn’t exceed Chef’s available free time K.

**Key Points of Approach:**

-

**Sorting the Problems**: The problems are sorted by their total time (solving time + break time) in ascending order, prioritizing problems that take the least time.

-

**Tracking the Total Time**: The algorithm iterates through the sorted problems, keeping a running total of the time. If the total time exceeds K, it adjusts by skipping a problem or part of it to fit within the available time.

-

**Final Result**: The algorithm calculates the maximum number of problems Chef can solve within K minutes.

This approach ensures Chef solves as many problems as possible within the available time.

### [](#time-complexity-3)Time Complexity

The time complexity is O(NlogN), where N is the number of problems, due to sorting the problems.

### [](#space-complexity-4)Space Complexity:

The space complexity is O(N), where N is the number of problems, due to storing the problems and their times.

</details>
