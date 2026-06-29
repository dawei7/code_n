# October Marathon

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | OCTATHON |
| Difficulty Rating | 319 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [OCTATHON](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/OCTATHON) |

---

## Problem Statement

Chef organised a $30$ kilometres marathon in Chefland.
The participants receive medals on completing the marathon as following:
- If the total time taken is less than $3$ hours, they receive a `GOLD` medal.
- If the total time taken is greater than equal to $3$ hours but less than $6$ hours, they receive a `SILVER` medal.
- If the total time taken is greater than equal to $6$ hours, they receive a `BRONZE` medal.

Chefina participated in the marathon and completed it in $X$ hours. Which medal would she receive?

---

## Input Format

- The input consists of a single integer $X$ — the number of hours Chefina took to complete the marathon.

---

## Output Format

Output the medal Chefina would recieve.

Note that you may print each character in uppercase or lowercase. For example, the strings `GOLD`, `gold`, `Gold`, and `gOlD` are considered the same.

---

## Constraints

- $1\le X \le 10$.

---

## Examples

**Example 1**

**Input**

```text
2
```

**Output**

```text
GOLD
```

**Explanation**

Chefina completed the marathon in less than $3$ hours. Thus, she gets a `GOLD` medal.

**Example 2**

**Input**

```text
5
```

**Output**

```text
SILVER
```

**Explanation**

Chefina took more than $3$ but less than $6$ hours. Thus, she gets a `SILVER` medal.

**Example 3**

**Input**

```text
6
```

**Output**

```text
BRONZE
```

**Explanation**

Chefina took $6$ hours to complete the marathon. Thus, she gets a `BRONZE` medal.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/OCTATHON)

[Contest: Division 1](https://www.codechef.com/START103A/problems/OCTATHON)

[Contest: Division 2](https://www.codechef.com/START103B/problems/OCTATHON)

[Contest: Division 3](https://www.codechef.com/START103C/problems/OCTATHON)

[Contest: Division 4](https://www.codechef.com/START103D/problems/OCTATHON)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Tester:*** [raysh07](https://www.codechef.com/users/raysh07)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Chef runs a marathon and finishes in X hours. Find which medal he gets.

# [](#explanation-5)EXPLANATION:

Simply implement what the statement says, using `if` conditions.

- If X \lt 3, the answer is `Gold`.

- If 3 \leq X \lt 6, the answer is `Silver`.

- Otherwise, the answer is `Bronze`.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``x = int(input())
if x < 3: print('Gold')
elif x < 6: print('Silver')
else: print('Bronze')
``

</details>
