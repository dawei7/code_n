# Bytelandian Robots

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | F2 |
| Difficulty Rating | 1844 |
| Difficulty Band | Rise from 3* to 4* |
| Path | Become 5 star |
| Lesson | Dynamic Programming |
| Official Link | [F2](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/F2) |

---

## Problem Statement

The Bytelandian Robotic Deparment has just succesfully made a robot that can be programmed to   move. Our robot can perform two type of movements: moving one step to the left or one step to the   right.

Our robot moves according to the instruction from its control sequence. A control sequence of the   robot is a string consisting of only two type of characters: '+' and '-' symbols, in which '+' means   a rightward step and '-' means a leftward step. For example, '+--' is a control sequence that instruct the robot to go one step to the right   followed by two steps to the left.

Our robot also has a master control sequence (MCQ), which is a string of N characters '+' and   '-'. **Any valid control sequence of the robot must be a subsequence of the MCQ**. Recall that a   subsequence is a sequence obtained by removing some characters of the initial sequence. An empty   sequence is also a subsequence of the MCQ.

Our robot is currently placed on a runway of length L, in which the leftmost point has coordinate 0   and the rightmost point has coordinate L. Intially our robot stands at the point at coordinate A. It   needs to move to the point at coordinate B. Of course, it cannot go outside the runway.

How many different control sequences are there that make the robot go from A to B?

### Input

The first line contains t, the number of test cases (about 50). Then t test cases follow. Each   test case has the following form:

- The first line contains four integers N, L, A, B (1 ≤ N ≤ 500, 1 ≤ L ≤   109, 0 ≤ A, B ≤ L).

-  The second line contains the MCQ which is a string of exactly N characters. The MCQ contains only   symbols '+' and '-'.

### Output

For each test case, print a single number that is the number of different control sequences that   could make the robot to go from A to B. Since the result may be a very large number, you only need   to print the remainder of the result when dividing by 7051954.

---

## Examples

**Example 1**

**Input**

```text
5
6 6 0 0
+-+-+-
6 6 3 3
+-+-+-
6 1 0 0 
+-+-+-
6 6 1 4
+-+-+-
6 6 2 6
+-+-+-
```

**Output**

```text
5 
9
4
1
0
```

**Explanation**

Case 1: the different control sequences are +-, +-+-, ++--, +-+-+- and the empty sequence.

Case 2: same as case 1 together with 4 additional sequences: -+, -+-+, -++-, +--+. These additional   sequences no longer make the robot go outside the runway as in case 1.

Case 3: same as case 1 but without the sequence ++-- since it will make the robot go outside the   runway

Case 4: there is only one possible control sequence: +++

Case 5: there is no way for the robot to go to coordinate 6

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 6 0 0
+-+-+-
```

**Output for this case**

```text
5
```



#### Test case 2

**Input for this case**

```text
6 6 3 3
+-+-+-
```

**Output for this case**

```text
9
```



#### Test case 3

**Input for this case**

```text
6 1 0 0
+-+-+-
```

**Output for this case**

```text
4
```



#### Test case 4

**Input for this case**

```text
6 6 1 4
+-+-+-
```

**Output for this case**

```text
1
```



#### Test case 5

**Input for this case**

```text
6 6 2 6
+-+-+-
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Bytelandian Robots](https://www.codechef.com/practice/course/3to4stars/LP3TO406/problems/F2)

### [](#problem-statement-1)Problem Statement

The Bytelandian Robotic Deparment has just succesfully made a robot that can be programmed to   move. Our robot can perform two type of movements: moving one step to the left or one step to the   right.

Our robot moves according to the instruction from its control sequence. A control sequence of the   robot is a string consisting of only two type of characters: '+' and '-' symbols, in which '+' means   a rightward step and '-' means a leftward step. For example, '+--' is a control sequence that instruct the robot to go one step to the right   followed by two steps to the left.

Our robot also has a master control sequence (MCQ), which is a string of N characters '+' and   '-'. **Any valid control sequence of the robot must be a subsequence of the MCQ**. Recall that a   subsequence is a sequence obtained by removing some characters of the initial sequence. An empty   sequence is also a subsequence of the MCQ.

Our robot is currently placed on a runway of length L, in which the leftmost point has coordinate 0   and the rightmost point has coordinate L. Intially our robot stands at the point at coordinate A. It   needs to move to the point at coordinate B. Of course, it cannot go outside the runway.

How many different control sequences are there that make the robot go from A to B?

### [](#approach-2)Approach

The solution uses dynamic programming with preprocessing. Precompute the `next_plus` and `next_minus` arrays to track the next occurrences of `+` and `-` for each position, along with `plus_cnt` and `minus_cnt` arrays to store cumulative counts. This allows us to determine the possible range of reachable positions, **farthest_left** and **farthest_right**.

The `dp` table is defined where `dp[x][i]` indicates the number of valid sequences that move the robot from position `x` to **B** starting at command index `i`. Iterate through the MCQ from the end to the beginning, updating the table based on whether the robot moves left or right. The result is stored at `dp[A][0]`, representing valid sequences starting from **A**.

### [](#time-complexity-3)Time Complexity

The time complexity is **O(N × R)**, where **N** is the length of the MCQ and **R** is the range of reachable positions.

### [](#space-complexity-4)Space Complexity

The space complexity is **O(N × R)**, due to the `dp` table storing states for all positions and command indices.

</details>
