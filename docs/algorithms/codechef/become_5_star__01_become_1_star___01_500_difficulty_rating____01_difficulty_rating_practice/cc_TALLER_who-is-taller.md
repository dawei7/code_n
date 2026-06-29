# Who is taller!

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | TALLER |
| Difficulty Rating | 281 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [TALLER](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/TALLER) |

---

## Problem Statement

Alice and Bob were having an argument about which of them is taller than the other. Charlie got irritated by the argument, and decided to settle the matter once and for all.

Charlie measured the heights of Alice and Bob, and got to know that Alice's height is $X$ centimeters and Bob's height is $Y$ centimeters. Help Charlie decide who is taller.

It is guaranteed that $X \neq Y$.

---

## Input Format

- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two integers $X$ and $Y$, as described in the problem statement.

---

## Output Format

For each test case, output on a new line $\texttt{A}$ if Alice is taller than Bob, else output $\texttt{B}$.
The output is case insensitive, i.e, both $\texttt{A}$ and $\texttt{a}$ will be accepted as correct answers when Alice is taller.

---

## Constraints

- $1 \leq T \leq 1000$
- $100 \leq X, Y \leq 200$
- $X \neq Y$

---

## Examples

**Example 1**

**Input**

```text
2
150 160
160 150
```

**Output**

```text
B
A
```

**Explanation**

**Test case $1$**: In this case, $150 < 160$ so Bob is taller than Alice.

**Test case $2$**: In this case, $160 > 150$ so Alice is taller than Bob.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
150 160
```

**Output for this case**

```text
B
```



#### Test case 2

**Input for this case**

```text
160 150
```

**Output for this case**

```text
A
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START36A/problems/TALLER)

[Contest Division 2](https://www.codechef.com/START36B/problems/TALLER)

[Contest Division 3](https://www.codechef.com/START36C/problems/TALLER)

[Contest Division 4](https://www.codechef.com/START36D/problems/TALLER)

Setter: [Lavish Gupta](https://www.codechef.com/users/lavish_adm)

Testers: [Felipe Mota](https://www.codechef.com/users/fmota), [Aryan](https://www.codechef.com/users/aryanc403)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

281

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Alice and Bob were having an argument about which of them is taller than the other. Charlie got irritated by the argument, and decided to settle the matter once and for all.

Charlie measured the heights of Alice and Bob, and got to know that Alice’s height is X centimeters and Bob’s height is Y centimeters. Help Charlie decide who is taller.

It is guaranteed that X \neq Y.

#
[](#explanation-5)EXPLANATION:

For each test case, we just have to find out which of the height value is greater .If Alice's height is greater, then print A else if Bobs's height is greater print B.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(1) for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](https://p.ip.fi/MaPr)

[Tester 1’s Solution](https://p.ip.fi/f1u_)

[Tester 2’s Solution](https://p.ip.fi/O7yd)

</details>
