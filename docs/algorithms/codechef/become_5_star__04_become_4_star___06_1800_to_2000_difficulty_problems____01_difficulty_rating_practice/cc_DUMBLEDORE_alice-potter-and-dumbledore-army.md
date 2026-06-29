# Alice Potter And Dumbledore Army

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DUMBLEDORE |
| Difficulty Rating | 1885 |
| Difficulty Band | 1800 to 2000 difficulty problems |
| Path | Become 5 star |
| Lesson | 1800 to 1900 difficulty problems |
| Official Link | [DUMBLEDORE](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/DUMBLEDORE) |

---

## Problem Statement

Dumbledore's Army consists of $N$ members. Alice Potter is planning to hold $M$ Dumbledore's Army sessions, where the members will perform training tasks to improve their skills in Defense Against the Dark Arts.

Initially, each member of the Army has no tasks. Before the $i$-th training session, Alice gives the $P_i$-th participant a task that he can complete in $T_i$ seconds. And each subsequent session Alice will add more and more difficult tasks, i.e. $T_i \le T_{i+1}$.

Let's assume that by the $i$-th session, the $j$-th participant has accumulated $C_j$ tasks. Alice knows that sometimes there is not enough time to complete all the tasks in a single session, so instead of forcing them to complete all $C_1+C_2+\ldots+C_N$ tasks, she can allow them to complete only a certain number $k$ of them. In this case, each participant can choose a subset of their tasks (in total, they have to choose $k$ tasks) and perform only those tasks. Each participant performs his tasks sequentially and spends time equal to the sum of the times of his tasks. However, different participants can perform tasks in parallel, so the total time of the session is equal to the maximum of the times of each participant. We denote the minimum possible value of this time by $ans_{i, k}$.

In order to optimally train participants, for each session $i$ Alice needs to know the value of $ans_{i, 1} + ans_{i, 2} + \ldots + ans_{i, i}$. Help Alice — calculate these sums for her.

---

## Input Format

- The first line contains two integers $N$ and $M$ — the number of members of Dumbledore's Army and the number of classes.

- The $i$-th of the next $M$ lines contains two integers $P_i$ and $T_i$ — the participant who will receive the next task and the amount of time it will take to complete it.

---

## Output Format

Print $M$ integers. The $i$-th of them should be equal to $ans_{i, 1} + ans_{i, 2} + \ldots + ans_{i, i}$.

---

## Constraints

- $1 \le N, M \le 10^6$
- $1 \le P_i \le N$, $1 \le T_i \le 10^6$
- $T_1 \le T_2 \le \ldots \le T_M$

---

## Examples

**Example 1**

**Input**

```text
5 12
5 1
3 2
5 2
1 2
4 3
4 3
4 3
5 3
1 5
3 5
1 8
2 10
```

**Output**

```text
1
3
6
8
11
17
26
32
39
46
61
71
```

**Explanation**

Consider the third session in the example. The fifth participant has tasks with $T=1$ and $T=2$, and the third participant has a single task with $T=2$. It takes $1$ unit of time to complete one task (only the fifth participant will complete the task with $T=1$), $2$ unit of time to complete two tasks, and $3$ unit of time to complete all three tasks. Therefore, the third number in the answer is $1+2+3=6$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Alice Potter And Dumbledore Army](https://www.codechef.com/practice/course/4-star-difficulty-problems/DIFF1900/problems/DUMBLEDORE)

### [](#problem-statement-1)Problem Statement

Dumbledore’s Army consists of N members. Alice Potter is planning to hold M Dumbledore’s Army sessions, where the members will perform training tasks to improve their skills in Defense Against the Dark Arts.

Initially, each member of the Army has no tasks. Before the i-th training session, Alice gives the P_i-th participant a task that he can complete in T_i seconds. And each subsequent session Alice will add more and more difficult tasks, i.e. T_i \le T_{i+1}.

Let’s assume that by the i-th session, the j-th participant has accumulated C_j tasks. Alice knows that sometimes there is not enough time to complete all the tasks in a single session, so instead of forcing them to complete all C_1+C_2+\ldots+C_N tasks, she can allow them to complete only a certain number k of them. In this case, each participant can choose a subset of their tasks (in total, they have to choose k tasks) and perform only those tasks. Each participant performs his tasks sequentially and spends time equal to the sum of the times of his tasks. However, different participants can perform tasks in parallel, so the total time of the session is equal to the maximum of the times of each participant. We denote the minimum possible value of this time by ans_{i, k}.

In order to optimally train participants, for each session i Alice needs to know the value of ans_{i, 1} + ans_{i, 2} + \ldots + ans_{i, i}. Help Alice — calculate these sums for her.

### [](#approach-2)Approach

To solve this problem, we maintain a running total of tasks for each participant in an array, `sum`. This array keeps track of the cumulative time required by each participant based on their tasks. With each new session, Alice assigns tasks to a participant, increasing their accumulated time by the task duration for that session.

The approach is to maintain a `sum` array where each index represents a participant’s accumulated task time. For each session, we read the participant index p and the task time t. We then update the cumulative task time for participant p by adding t to `sum[p]`. After updating, we calculate the total cumulative time of all participants by summing up all values in `sum`. This total represents the minimum training time required for that session under Alice’s conditions.

### [](#time-complexity-3)Time Complexity

The solution processes each session in fixed steps, so the time complexity is O(M).

### [](#space-complexity-4)Space Complexity

An array of size N is used for participants’ task times, giving a space complexity of O(N).

</details>
