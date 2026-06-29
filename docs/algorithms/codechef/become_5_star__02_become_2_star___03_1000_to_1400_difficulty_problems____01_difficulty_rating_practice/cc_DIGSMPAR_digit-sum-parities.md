# Digit Sum Parities

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DIGSMPAR |
| Difficulty Rating | 1077 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [DIGSMPAR](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/DIGSMPAR) |

---

## Problem Statement

For a positive integer $M$, MoEngage defines $\texttt{digitSum(M)}$ as the sum of digits of the number $M$ (when written in decimal).

For example, $\texttt{digitSum(1023)} = 1 + 0 + 2 + 3 = 6$.

Given a positive integer $N$, find the **smallest** integer $X$ **strictly greater** than $N$ such that:
- $\texttt{digitSum(N)}$ and $\texttt{digitSum(X)}$ have different [parity](https://en.wikipedia.org/wiki/Parity_(mathematics)), i.e. one of them is odd and the other is even.

---

## Input Format

- The first line contains an integer $T$, the number of test cases. The description of the $T$ test cases follow.
- Each test case consists of a single line of input with a single integer, the number $N$.

---

## Output Format

- For each test case, print in a single line, an integer, the answer to the problem.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \lt 10^{9}$

---

## Examples

**Example 1**

**Input**

```text
3
123
19
509
```

**Output**

```text
124
21
511
```

**Explanation**

**Test Case $1$:** $\texttt{digitSum}(123) = 1 + 2 + 3 = 6$ is **even** and $\texttt{digitSum}(124) = 1 + 2 + 4 = 7$ is **odd**, so the answer is $124$.

**Test Case $2$:** $\texttt{digitSum}(19) = 1 + 9 = 10$ is **even**, $\texttt{digitSum}(20) = 2 + 0 = 2$ is also **even**, whereas $\texttt{digitSum}(21) = 2 + 1 = 3$ is **odd**. Hence, the answer is $21$.

**Test Case $3$:** $\texttt{digitSum}(509) = 5 + 0 + 9 = 14$ is **even**, $\texttt{digitSum}(510) = 5 + 1 + 0 = 6$ is also **even**, whereas $\texttt{digitSum}(511) = 5 + 1 + 1 = 7$ is **odd**. Hence, the answer is $511$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
123
```

**Output for this case**

```text
124
```



#### Test case 2

**Input for this case**

```text
19
```

**Output for this case**

```text
21
```



#### Test case 3

**Input for this case**

```text
509
```

**Output for this case**

```text
511
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/COOK140A/problems/DIGSMPAR)

[Contest Division 2](https://www.codechef.com/COOK140B/problems/DIGSMPAR)

[Contest Division 3](https://www.codechef.com/COOK140C/problems/DIGSMPAR)

[Contest Division 4](https://www.codechef.com/COOK140D/problems/DIGSMPAR)

Setter: [Srikkanth R](https://www.codechef.com/users/srikkanth_adm)

Tester: [Harris Leung](https://www.codechef.com/users/gamegame)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7), [Jakub Safin](https://www.codechef.com/users/xellos)

#
[](#difficulty-2)DIFFICULTY:

Cakewalk

#
[](#prerequisites-3)PREREQUISITES:

Basic Arithmetic

#
[](#problem-4)PROBLEM:

For a positive integer M, let ????????????????????????????????(????) be the sum of digits of the number M (when written in decimal).

For example, ????????????????????????????????(????????????????)=1+0+2+3=6.

Given a positive integer N, find the smallest integer X greater than N such that

????????????????????????????????(????) and ????????????????????????????????(????) have different parity, i.e. one of them is odd and the other is even

#
[](#explanation-5)EXPLANATION:

Let I be the given integer, S be the digit sum, x be the last digit.

**Case 1:** S+1 has different parity as S

**Ans:** (I+1)

**Case 2:** S+1 has same parity as S

\implies x = 9

\implies x+1 = 10

\therefore x for S+1 will be 0 and previous digits would be affected

\implies x+1 = 1

\therefore x for S+2 will be 1 and previous digits won’t be affected

\implies S+2 will have different parity than S+1 and hence, S

**Ans:** (I+2)

#
[](#time-complexity-6)TIME COMPLEXITY:

The above computation can be done in constant time. Hence, the solution has a time complexity of O(1).

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](https://pastebin.com/3y8gWvTr)

[Setter’s Solution](http://p.ip.fi/RdSO)

[Tester’s Solution](http://p.ip.fi/pPWC)

</details>
