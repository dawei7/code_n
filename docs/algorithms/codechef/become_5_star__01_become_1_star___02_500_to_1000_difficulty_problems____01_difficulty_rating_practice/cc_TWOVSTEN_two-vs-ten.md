# Two vs Ten

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TWOVSTEN |
| Difficulty Rating | 936 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [TWOVSTEN](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/TWOVSTEN) |

---

## Problem Statement

Chef Two and Chef Ten are playing a game with a number $X$. In one turn, they can multiply $X$ by $2$. The goal of the game is to make $X$ divisible by $10$.

Help the Chefs find the smallest number of turns necessary to win the game (it may be possible to win in zero turns) or determine that it is impossible.

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer denoting the initial value of $X$.

### Output
For each test case, print a single line containing one integer — the minimum required number of turns or $-1$ if there is no way to win the game.

### Constraints
- $1 \le T \le 1000$
- $0 \le X \le 10^9$

### Subtasks
**Subtask #1 (100 points):** original constraints

---

## Examples

**Example 1**

**Input**

```text
3
10
25
1
```

**Output**

```text
0
1
-1
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
25
```

**Output for this case**

```text
1
```



#### Test case 3

**Input for this case**

```text
1
```

**Output for this case**

```text
-1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](https://www.codechef.com/problems/TWOVSTEN)

[Contest](https://www.codechef.com/LTIME59B/problems/TWOVSTEN)

**Author:** [Denis Anishchenko](https://www.codechef.com/users/altruist_)

**Tester:** [Hasan Jaddouh](https://www.codechef.com/users/kingofnumbers)

**Editorialist:** [Sarv Shakti Singh](https://www.codechef.com/users/mr_knownothing)

**Difficulty:** cakewalk

**Prerequisites:** Basic math

**Problem:** Given a number `X`, the operation allowed is multiplication by 2, find the minimum number of times the operation has to be performed to make `X` divisible by 10.

**Explanation:** The approach is quite simple and can be classified in 3 cases :

-

If the number is already divisible by 10, then the answer is 0.

-

If the number is divisible by 5, then the answer is 1. It can be proved,

Consider `N = K * 5`, then if we apply the operation once, it becomes, `N = K * 5 * 2` which in turn simpllifies to `N = K * 10`, thus giving the desired result.

-

If the number doesn’t fall in previous 2 cases, then it is impossible to achieve the desired result, as for a number to be divisible by `10`, it has to be divisble by `5` and `2`.

[Author’s code](https://ideone.com/OingHj)

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution can be found [here](http://www.codechef.com/download/Solutions/LTIME59/setter/TWOVSTEN.cpp).

Tester’s solution can be found [here](http://www.codechef.com/download/Solutions/LTIME59/tester/TWOVSTEN.cpp).

</details>
