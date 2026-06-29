# Cricket World Cup Qualifier

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CWC23QUALIF |
| Difficulty Rating | 203 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [CWC23QUALIF](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CWC23QUALIF) |

---

## Problem Statement

The cricket World Cup has started in Chefland. There are many teams participating in the group stage matches. Any team that scores $12$ or more points in the group stage matches qualifies for the next stage.

You know the score that a particular team has scored in the group stage matches. Determine if the team has qualified for the next stage or not.

---

## Input Format

The first and only line of input consists of an integer $X$ denoting the total points scored by the given team in the group stage matches.

---

## Output Format

Output `Yes`, if the team has qualified for the next stage, and `No` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).

---

## Constraints

- $1 \leq X \leq 20$

---

## Examples

**Example 1**

**Input**

```text
3
```

**Output**

```text
No
```

**Explanation**

The team has not scored $\ge 12$ points. Hence it does not qualify.

**Example 2**

**Input**

```text
17
```

**Output**

```text
Yes
```

**Explanation**

The team has scored $\ge 12$ points. Hence it does qualify.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CWC23QUALIF)

[Contest: Division 1](https://www.codechef.com/START109A/problems/CWC23QUALIF)

[Contest: Division 2](https://www.codechef.com/START109B/problems/CWC23QUALIF)

[Contest: Division 3](https://www.codechef.com/START109C/problems/CWC23QUALIF)

[Contest: Division 4](https://www.codechef.com/START109D/problems/CWC23QUALIF)

***Tester:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

A team that scores 12 or more points in the group stage qualifies for the next stage.

A certain team has X points. Will they qualify?

# [](#explanation-5)EXPLANATION:

As the statement says, the answer is `Yes` if X \geq 12 and `No` otherwise.

Check this using an `if` condition.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``x = int(input())
print('Yes' if x >= 12 else 'No')
``

</details>
