# Height of Rationals

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HEIGHTRATION |
| Difficulty Rating | 405 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [HEIGHTRATION](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/HEIGHTRATION) |

---

## Problem Statement

In a recent [breakthrough](https://www.quantamagazine.org/mathematicians-prove-30-year-old-andre-oort-conjecture-20220203/) in mathematics, the proof utilized a concept called `Height`.

Consider a fraction $\frac{a}{b}$. Its `Height` is defined as the **maximum** of its numerator and denominator. So, for example, the `Height` of $\frac{3}{19}$ would be $19$, and the `Height` of $\frac{27}{4}$ would be $27$.

Given $a$ and $b$, find the `Height` of $\frac{a}{b}$.

---

## Input Format

The only line of input contains two integers, $a$ and $b$.

---

## Output Format

Output a single integer, which is the `Height` of $\frac{a}{b}$.

---

## Constraints

- $1 \leq a, b \leq 100$
- $a$ and $b$ do not have any common factors.

---

## Examples

**Example 1**

**Input**

```text
3 19
```

**Output**

```text
19
```

**Explanation**

The maximum of $\{3, 19\}$ is $19$. Hence the `Height` of $\frac{3}{19}$ is $19$.

**Example 2**

**Input**

```text
27 4
```

**Output**

```text
27
```

**Explanation**

The maximum of $\{27, 4\}$ is $27$. Hence the `Height` of $\frac{27}{4}$ is $27$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/HEIGHTRATION)

[Contest: Division 1](https://www.codechef.com/LTIME111A/problems/HEIGHTRATION)

[Contest: Division 2](https://www.codechef.com/LTIME111B/problems/HEIGHTRATION)

[Contest: Division 3](https://www.codechef.com/LTIME111C/problems/HEIGHTRATION)

[Contest: Division 4](https://www.codechef.com/LTIME111D/problems/HEIGHTRATION)

***Tester:*** [Harris Leung](https://www.codechef.com/users/gamegame)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

405

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given a fraction of the form \frac{a}{b}, find its height, i.e, the maximum of a and b.

#
[](#explanation-5)EXPLANATION:

Simply implement what is asked for. In most languages, this can be done with the inbuilt function `max`. However, you can also use an `if` condition.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``a, b = map(int, input().split())
print(max(a, b))
``

</details>
