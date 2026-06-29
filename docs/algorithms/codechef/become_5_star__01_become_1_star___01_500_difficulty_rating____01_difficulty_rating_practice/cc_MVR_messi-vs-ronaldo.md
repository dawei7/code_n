# Messi vs Ronaldo

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MVR |
| Difficulty Rating | 316 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [MVR](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/MVR) |

---

## Problem Statement

In Chefland, a football player gets $2$ points for each goal and $1$ point for each assist.

Messi has $A$ goals and $B$ assists this season, whereas Ronaldo has $X$ goals and $Y$ assists.
Find out the player with more points this season.

---

## Input Format

- The first and only line of input will contains four space-separated integers $A$, $B$, $X$ and $Y$, the number of goals and assists that Messi has and the number of goals and assists that Ronaldo has, respectively.

---

## Output Format

Print a single line containing:
- `Messi`, if Messi has more points than Ronaldo.
- `Ronaldo`, if Ronaldo has more points than Messi.
- `Equal`, if both have equal points.

You can print each character in uppercase or lowercase. For example, the strings `Messi`, `MESSI`, `messi`, and `MeSSi` are considered identical.

---

## Constraints

- $0 \leq A,B,X,Y \leq 100$

---

## Examples

**Example 1**

**Input**

```text
40 30 50 10
```

**Output**

```text
Equal
```

**Explanation**

- Messi has $40$ goals and $30$ assists. Thus, his total points are $40\cdot 2+30 = 110$.
- Ronaldo has $50$ goals and $10$ assists. Thus, his total points are $50\cdot 2+10 = 110$.

Both have $110$ points.

**Example 2**

**Input**

```text
91 22 60 30
```

**Output**

```text
Messi
```

**Explanation**

- Messi has $91$ goals and $22$ assists. Thus, his total points are $91\cdot 2+22 = 204$.
- Ronaldo has $60$ goals and $30$ assists. Thus, his total points are $60\cdot 2+30 = 150$.

Messi has $204$ points, whereas Ronaldo has $150$.

**Example 3**

**Input**

```text
60 30 80 20
```

**Output**

```text
Ronaldo
```

**Explanation**

- Messi has $60$ goals and $30$ assists. Thus, his total points are $60\cdot 2+30 = 150$.
- Ronaldo has $80$ goals and $20$ assists. Thus, his total points are $80\cdot 2+20 = 180$.

Messi has $150$ points, whereas Ronaldo has $180$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MVR)

[Contest: Division 1](https://www.codechef.com/START98A/problems/MVR)

[Contest: Division 2](https://www.codechef.com/START98B/problems/MVR)

[Contest: Division 3](https://www.codechef.com/START98C/problems/MVR)

[Contest: Division 4](https://www.codechef.com/START98D/problems/MVR)

***Author:*** [pols_agyi_pols](https://www.codechef.com/users/pols_agyi_pols)

***Tester & Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

316

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Messi has A goals and B assists; while Ronaldo has X goals and Y assists.

A goal is worth two points, and an assist is worth one point.

Who has more points?

# [](#explanation-5)EXPLANATION:

Messi has 2A + B points in total, while Ronaldo has 2X + Y points.

Compute these two numbers, then use an `if` condition to compare them and output the appropriate answer.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``a, b, x, y = map(int, input().split())
messi = 2*a + b
ronaldo = 2*x + y
print('Messi' if messi > ronaldo else ('Ronaldo' if messi < ronaldo else 'Equal'))
``

</details>
