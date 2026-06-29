# A Balanced Contest

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PERFCONT |
| Difficulty Rating | 1184 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [PERFCONT](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/PERFCONT) |

---

## Problem Statement

Chef wants to organize a contest. Predicting difficulty levels of the problems can be a daunting task. Chef wants his contests to be balanced in terms of difficulty levels of the problems.

Assume a contest had total **P** participants. A problem that was solved by at least half of the participants (i.e. **P / 2** (integer division)) is said to be cakewalk difficulty. A problem solved by at max **P / 10** (integer division) participants is categorized to be a hard difficulty.

Chef wants the contest to be balanced. According to him, a balanced contest must have exactly 1 cakewalk and exactly 2 hard problems. You are given the description of **N** problems and the number of participants solving those problems. Can you tell whether the contest was balanced or not?

### Input

The first line of the input contains an integer **T** denoting the number of test cases.

The first line of each test case contains two space separated integers, **N, P** denoting the number of problems, number of participants respectively.

The second line contains **N** space separated integers, **i**-th of which denotes number of participants solving the **i**-th problem.

### Output

For each test case, output "yes" or "no" (without quotes) denoting whether the contest is balanced or not.

### Constraints

- 1 ≤ **T, N** ≤ 500

- 1 ≤ **P** ≤ 108

- 1 ≤ Number of participants solving a problem ≤ **P**

### Subtasks

- **Subtask #1** (40 points): **P** is a multiple of 10

- **Subtask #2** (60 points): Original constraints

---

## Examples

**Example 1**

**Input**

```text
6
3 100
10 1 100
3 100
11 1 100
3 100
10 1 10
3 100
10 1 50
4 100
50 50 50 50
4 100
1 1 1 1
```

**Output**

```text
yes
no
no
yes
no
no
```

**Explanation**

**Example case 1.**: The problems are of hard, hard and cakewalk difficulty. There is 1 cakewalk and 2 hard problems, so the contest is balanced.

**Example case 2.**: The second problem is hard and the third is cakewalk. There is 1 cakewalk and 1 hard problem, so the contest is not balanced.

**Example case 3.**: All the three problems are hard. So the contest is not balanced.

**Example case 4.**: The problems are of hard, hard, cakewalk difficulty. The contest is balanced.

**Example case 5.**: All the problems are cakewalk. The contest is not balanced.

**Example case 6.**: All the problems are hard. The contest is not balanced.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 100
10 1 100
```

**Output for this case**

```text
yes
```



#### Test case 2

**Input for this case**

```text
3 100
11 1 100
```

**Output for this case**

```text
no
```



#### Test case 3

**Input for this case**

```text
3 100
10 1 10
```

**Output for this case**

```text
no
```



#### Test case 4

**Input for this case**

```text
3 100
10 1 50
```

**Output for this case**

```text
yes
```



#### Test case 5

**Input for this case**

```text
4 100
50 50 50 50
```

**Output for this case**

```text
no
```



#### Test case 6

**Input for this case**

```text
4 100
1 1 1 1
```

**Output for this case**

```text
no
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK

[Practice](https://www.codechef.com/problems/PERFCONT)

[Contest](https://www.codechef.com/OCT17/problems/PERFCONT)

**Author:** [Praveen Dhinwa](https://www.codechef.com/users/admin2)

**Tester:** [Alexey Zayakin](https://www.codechef.com/users/alex_2008)

**Editorialist:** [Jakub Safin](https://www.codechef.com/users/xellos0)

### DIFFICULTY

CAKEWALK

### PREREQUISITIES

none

### PROBLEM

For a contest with P participants and N problems, you’re given the number of participants who solved each problem. Determine if exactly one problem was solved by at least \frac{P}{2} participants and exactly two problems were solved by at most \frac{P}{10} participants.

### QUICK EXPLANATION

Count how many problems satisfy each inequality.

### EXPLANATION

As a cakewalk problem, this is very easy: read N,P, compute \left\lfloor P/2 \right\rfloor and \left\lfloor P/10 \right\rfloor (the result of integer division is obtained when dividing an integer by another integer in most languages, where P/2 and P/10 gives what we need; Python 3 for instance needs P//2 and P//10), then read the numbers of participants solving each problem to count the number of cakewalk problems c and of hard problems h.

For a problem solved by x participants, check if x \ge \left\lfloor P/2 \right\rfloor or x \le \left\lfloor P/10 \right\rfloor. If x \ge \left\lfloor P/2 \right\rfloor is true, the problem has cakewalk difficulty and you should increase c by 1. If x \le \left\lfloor P/10 \right\rfloor is true, the problem has hard difficulty and you should increase h by 1.

Afterwards, you should check if c=1 and h=2.

Note that it’s possible for a problem to be both cakewalk and hard if P=1 and in that case, all problems will be cakewalk, so if we have exactly 2 hard problems, then we have at least 2 cakewalk problems, so it’s not a balanced contest (and contests with 1 participant are stupid anyway). For P \ge 2, it can’t happen since \left\lfloor P/2 \right\rfloor > P/2-1 and \left\lfloor P/10 \right\rfloor \le P/10, so we get \left\lfloor P/2 \right\rfloor > \left\lfloor P/10 \right\rfloor.

The time complexity is obviously O(N), since we’re doing just a linear number of comparisons and some arithmetic. The memory complexity is O(1) – we’re only storing a small constant number of variables.

### AUTHOR’S AND TESTER’S SOLUTIONS

Setter’s solution: Will be uploaded soon.

[Tester’s solution](http://www.codechef.com/download/Solutions/OCT17/Tester/PERFCONT.cpp)

[Editorialist’s solution](https://ideone.com/2i88hg)

</details>
