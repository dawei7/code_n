# Double Rent

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DOUBLERENT |
| Difficulty Rating | 234 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [DOUBLERENT](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DOUBLERENT) |

---

## Problem Statement

Chefina decided to move into Chef's apartment.
Chef was initially paying a rent of $X$ rupees. Since Chefina is moving in, the owner decided to **double** the rent.

Find the final rent Chef needs to pay.

---

## Input Format

The input consists of a single integer $X$, denoting the rent Chef was initially paying.

---

## Output Format

Output on a new line, the final rent Chef needs to pay.

---

## Constraints

- $1 \leq X \leq 10$

---

## Examples

**Example 1**

**Input**

```text
2
```

**Output**

```text
4
```

**Explanation**

Chef was initially paying $2$ rupees. After Chefina moves in, he needs to pay $2\cdot 2 = 4$ rupees.

**Example 2**

**Input**

```text
3
```

**Output**

```text
6
```

**Explanation**

Chef was initially paying $3$ rupees. After Chefina moves in, he needs to pay $2\cdot 3 = 6$ rupees.

**Example 3**

**Input**

```text
10
```

**Output**

```text
20
```

**Explanation**

Chef was initially paying $10$ rupees. After Chefina moves in, he needs to pay $2\cdot 10 = 20$ rupees.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DOUBLERENT)

[Contest: Division 1](https://www.codechef.com/START104A/problems/DOUBLERENT)

[Contest: Division 2](https://www.codechef.com/START104B/problems/DOUBLERENT)

[Contest: Division 3](https://www.codechef.com/START104C/problems/DOUBLERENT)

[Contest: Division 4](https://www.codechef.com/START104D/problems/DOUBLERENT)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Tester:*** [apoorv_me](https://www.codechef.com/users/apoorv_me)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

234

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Chef’s rent is X. The owner decided to double it. What’s the new rent?

# [](#explanation-5)EXPLANATION:

The new rent is twice of X, i.e, 2X.

So, just output `2*x`.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``x = int(input())
print(2*x)
``

</details>
