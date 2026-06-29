# Off By One

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | OFFBY1 |
| Difficulty Rating | 271 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [OFFBY1](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/OFFBY1) |

---

## Problem Statement

You just bought a new calculator, but it seems to have a small problem: all its results have an extra $1$ appended to the end.
For example, if you ask it for `3 + 5`, it'll print `81`, and `4 + 12` will result in `161`.

Given $A$ and $B$, can you predict what the calculator will print when you ask it for $A + B$?

---

## Input Format

- The first and only line of input will contain two space-separated integers $A$ and $B$.

---

## Output Format

Print a single integer: the calculator's output when you enter $A+B$ into it.

---

## Constraints

- $1 \leq A, B \leq 50$

---

## Examples

**Example 1**

**Input**

```text
3 5
```

**Output**

```text
81
```

**Explanation**

$3 + 5 = 8$, and the calculator appends a $1$ to print $81$.

**Example 2**

**Input**

```text
4 12
```

**Output**

```text
161
```

**Explanation**

$4+12 = 16$, and the calculator appends a $1$ to print $161$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/OFFBY1)

[Contest: Division 1](https://www.codechef.com/START101A/problems/OFFBY1)

[Contest: Division 2](https://www.codechef.com/START101B/problems/OFFBY1)

[Contest: Division 3](https://www.codechef.com/START101C/problems/OFFBY1)

[Contest: Division 4](https://www.codechef.com/START101D/problems/OFFBY1)

***Author:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

***Tester:*** [apoorv_me](https://www.codechef.com/users/apoorv_me)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

271

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

A calculator appends 1 to the result of every operation.

Given A and B, what does it print when asked for A+B?

# [](#explanation-5)EXPLANATION:

Print A+B followed by a 1.

This can be done in several ways:

- As an integer, the resulting number is 10\cdot (A+B) + 1.

- Otherwise, you can print A+B and then separately print a 1 after it - just make sure there’s no space between the two outputs.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``a, b = map(int, input().split())
print(10*(a+b) + 1)
``

</details>
