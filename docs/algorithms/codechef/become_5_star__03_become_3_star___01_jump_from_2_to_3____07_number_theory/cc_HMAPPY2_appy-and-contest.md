# Appy and Contest

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HMAPPY2 |
| Difficulty Rating | 1358 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Number Theory |
| Official Link | [HMAPPY2](https://www.codechef.com/practice/course/2to3stars/LP2TO307/problems/HMAPPY2) |

---

## Problem Statement

Appy and Chef are participating in a contest. There are $N$ problems in this contest; each problem has a unique problem code between $1$ and $N$ inclusive. Appy and Chef decided to split the problems to solve between them ― Appy should solve the problems whose problem codes are divisible by $A$ but not divisible by $B$, and Chef should solve the problems whose problem codes are divisible by $B$ but not divisible by $A$ (they decided to not solve the problems whose codes are divisible by both $A$ and $B$).

To win, it is necessary to solve at least $K$ problems. You have to tell Appy whether they are going to win or lose.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains four space-separated integers $N$, $A$, $B$ and $K$.

### Output
For each test case, print a single line containing the string `"Win"` if they can solve at least $K$ problems or `"Lose"` otherwise (without quotes).

### Constraints
- $1 \le T \le 15$
- $1 \le K \le N \le 10^{18}$
- $1 \le A, B \le 10^9$

### Subtasks
**Subtask #1 (15 points):**
- $1 \le T \le 15$
- $1 \le K \le N \le 10^6$
- $1 \le A, B \le 10^3$

**Subtask #2 (85 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
1
6 2 3 3
```

**Output**

```text
Win
```

**Explanation**

**Example case 1:** Appy is solving the problems with codes $2$ and $4$, Chef is solving the problem with code $3$. Nobody is solving problem $6$, since $6$ is divisible by both $2$ and $3$. Therefore, they can solve $3$ problems and win.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/HMAPPY2)

[Contest: Division 1](https://www.codechef.com/FEB19A/problems/HMAPPY2)

[Contest: Division 2](https://www.codechef.com/FEB19B/problems/HMAPPY2)

**Setter:** [Himanshu Mishra](https://www.codechef.com/users/hmrockstar)

**Tester:** [Alexey Zayakin](https://www.codechef.com/users/alex_2oo8) and [Yash Chandnani](https://www.codechef.com/users/yash_chandnani)

**Editorialist:** [Taranpreet Singh](https://www.codechef.com/users/taran_1407)

### DIFFICULTY:

Cakewalk.

### PREREQUISITES:

Greatest Common Factor and Least Common Multiple.

### PROBLEM:

Given four numbers N, A, B and K. There are N problems labelled from 1 to N. Appy solves each problem whose label is divisible by A but not B, while Chef solves all problems whose label is divisible by B but not by A. Check if Appy and Chef together solve at least K problems or not.

### QUICK EXPLANATION

- Number of problems solved by Appy is N/A - N/lcm(A, B).

- Number of problems solved by Chef is N/B - N/lcm(A,B).

- Total number of problems solved become N/A+N/B-2*N/lcm(A,B). We can simply check if it is at least K or not.

### EXPLANATION

Number of multiples of x in range [1, N] is given by \lfloor N/x \rfloor.

Appy solves all problems whose label is divisible by A, which are N/A problems. But this also includes problems whose labels are divisible by both A and B. We know, all such problems are the multiples of lcm(A, B). So, we can just subtract it from N/A to get N/A - N/lcm(A, B) which is the number of problems solved by Appy.

Chef solves all problems whose label is divisible by B, which are N/B problems. But this also includes problems whose labels are divisible by both A and B. We know, all such problems are the multiples of lcm(A, B). So, we can just subtract it from N/B to get N/B - N/lcm(A, B) which is the number of problems solved by Chef.

The total number of problems solved by Chef and Appy is N/A+N/B-2*N/lcm(A, B). We can simply use an if statement to check if this exceeds K or not.

As an exercise, solve the problem, where problems are not labeled from 1 to N, but from L to R which is given in the problem.

Finding LCM of two numbers is just the product of two numbers divided by its Greatest Common Factor, which can be easily found using Euclid’s GCD method.

### Time Complexity

Time complexity is O(1) per test case.

### AUTHOR’S AND TESTER’S SOLUTIONS:

[Setter’s solution](https://www.codechef.com/download/Solutions/FEB19/setter/HMAPPY2.cpp)

[Tester’s solution](https://www.codechef.com/download/Solutions/FEB19/tester/HMAPPY2.cpp)

[Editorialist’s solution](https://www.codechef.com/download/Solutions/FEB19/editorialist/HMAPPY2.java)

Feel free to Share your approach, If it differs. Suggestions are always welcomed.

</details>
