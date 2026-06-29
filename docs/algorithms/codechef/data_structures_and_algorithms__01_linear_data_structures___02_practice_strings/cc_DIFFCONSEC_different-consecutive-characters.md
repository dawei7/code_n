# Different Consecutive Characters 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DIFFCONSEC |
| Difficulty Rating | 879 |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [DIFFCONSEC](https://www.codechef.com/practice/course/strings/STRINGS/problems/DIFFCONSEC) |

---

## Problem Statement

Chef has a binary string $S$ of length $N$. Chef can perform the following operation on $S$:
- Insert any character ($0$ or $1$) at any position in $S$.

Find the minimum number of operations Chef needs to perform so that no two consecutive characters are same in $S$.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the length of the binary string $S$.
- The second line of each test case contains a binary string $S$ of length $N$ containing $0$s and $1$s only.

---

## Output Format

For each test case, output on a new line the minimum number of operations Chef needs to perform so that no two consecutive characters are same in $S$.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \le N \le 1000$

---

## Examples

**Example 1**

**Input**

```text
3
2
11
4
0101
5
00100
```

**Output**

```text
1
0
2
```

**Explanation**

**Test case 1:** We can perform the following operations: $11 \rightarrow 1\underline{0}1$.

**Test case 2:** We do not need to perform any operations.

**Test case 3:** We can perform the following operations: $00100 \rightarrow 0\underline{1}0100 \rightarrow 01010\underline{1}0$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
11
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4
0101
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
5
00100
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DIFFCONSEC)

[Contest: Division 1](https://www.codechef.com/START61A/problems/DIFFCONSEC)

[Contest: Division 2](https://www.codechef.com/START61B/problems/DIFFCONSEC)

[Contest: Division 3](https://www.codechef.com/START61C/problems/DIFFCONSEC)

[Contest: Division 4](https://www.codechef.com/START61D/problems/DIFFCONSEC)

***Author:*** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

***Testers:*** [Tejas Pandey](https://www.codechef.com/users/tejas10p), [Hriday](https://www.codechef.com/users/the_hyp0cr1t3)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given a binary string S, in one move you can insert either 0 or 1 at any position. Find the minimum number of moves so that the resulting string has no adjacent equal characters.

#
[](#explanation-5)EXPLANATION:

Note that a single move allows us to ‘break apart’ exactly one pair of equal adjacent characters, by inserting either 1 between 00 or 0 between 11.

Further, this move doesn’t create any new equal adjacencies.

So, the answer is simply the number of pairs that are already adjacent and equal, i.e, positions i \ (1 \leq i \lt N) such that S_i = S_{i+1}, which can be computed with a simple `for` loop.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    s = input()
    print(sum(1 if s[i] == s[i+1] else 0 for i in range(n-1)))
``

</details>
