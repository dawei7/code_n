# Bone Appetit

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | BNE_APT |
| Difficulty Rating | 280 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [BNE_APT](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/BNE_APT) |

---

## Problem Statement

*Trick or treat, bags of sweets, ghosts are walking down the street*

It's Halloween and Suri Bhai is out to get his treats.
There are two sectors in his neighborhood, "Bones" and "Blood". They have $N$ and $M$ people, respectively.

Each person in "Bones" will hand out $X$ treats, and each person in "Blood" will hand out $Y$ treats.
How many treats does Suri Bhai get from visiting everyone in his neighborhood in total?

---

## Input Format

- The first line of input contains two space-separated integers $N$ and $M$ — the number of people in "Bones" and "Blood", respectively.
- The second line of input contains two space-separated integers $X$ and $Y$ — the number of treats handed out by each person in "Bones" and "Blood", respectively.

---

## Output Format

For each test case output a single integer: the total number of treats Suri Bhai will receive.

---

## Constraints

- $0 \leq N,M \leq 100$
- $0 \leq X,Y \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
4 2
5 6
```

**Output**

```text
32
```

**Explanation**

- "Bones" has $4$ people, each of who will give out $5$ treats, for a total of $4\times 5 = 20$ treats.
- "Blood" has $2$ people, each of who will give out $6$ treats, for a total of $2\times 6 = 12$ treats.
- The total number of treats is $20 + 12 = 32$.

**Example 2**

**Input**

```text
5 0
0 2
```

**Output**

```text
0
```

**Explanation**

- "Bones" has $5$ people, each of who will give out $0$ treats, for a total of $5\times 0 = 0$ treats.
- "Blood" has $0$ people, each of who will give out $2$ treats, for a total of $0\times 2 = 0$ treats.
- The total number of treats is $0 + 0 = 0$.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/BNE_APT)

[Contest: Division 1](https://www.codechef.com/START105A/problems/BNE_APT)

[Contest: Division 2](https://www.codechef.com/START105B/problems/BNE_APT)

[Contest: Division 3](https://www.codechef.com/START105C/problems/BNE_APT)

[Contest: Division 4](https://www.codechef.com/START105D/problems/BNE_APT)

***Author:*** [pranjali_07](https://www.codechef.com/users/pranjali_07)

***Tester:*** [raysh07](https://www.codechef.com/users/raysh07)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

280

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

In a neighborhood, there are two sectors - one with N people and the other with M.

Each person in the first sector hands out X treats, each in the second hands out Y.

What’s the total number of treats a single person can receive by visiting everyone?

# [](#explanation-5)EXPLANATION:

The first sector has N people handing out X treats each, for a total of N\cdot X treats.

The first sector has M people handing out Y treats each, for a total of M\cdot Y treats.

The total number of treats is their sum, that is

N\cdot X + M\cdot Y

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``n, m = map(int, input().split())
x, y = map(int, input().split())
print(n*x + m*y)
``

</details>
