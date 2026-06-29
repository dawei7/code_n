# Air Quality Index

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | AIRINDEX |
| Difficulty Rating | 347 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [AIRINDEX](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/AIRINDEX) |

---

## Problem Statement

In the light of `G-20` summit, government has decided to keep the average air quality index (AQI) **strictly below** $100$.
On some random day, Chef measures the AQI and found the value to be $X$.

Find whether the government was able to keep the AQI within limits.

---

## Input Format

- The input consists of an integer $X$ — the AQI Chef measured.

---

## Output Format

Output `YES`, if the government was able to keep the AQI within limits and `NO` otherwise.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

---

## Constraints

- $1 \leq X \leq 150$

---

## Examples

**Example 1**

**Input**

```text
50
```

**Output**

```text
YES
```

**Explanation**

The AQI is strictly less than $100$. Thus, the government was able to keep the AQI within limits.

**Example 2**

**Input**

```text
100
```

**Output**

```text
NO
```

**Explanation**

The AQI is equal to $100$. Thus, the government was not able to keep the AQI within limits.

**Example 3**

**Input**

```text
99
```

**Output**

```text
YES
```

**Explanation**

The AQI is strictly less than $100$. Thus, the government was able to keep the AQI within limits.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/AIRINDEX)

[Contest: Division 1](https://www.codechef.com/START100A/problems/AIRINDEX)

[Contest: Division 2](https://www.codechef.com/START100B/problems/AIRINDEX)

[Contest: Division 3](https://www.codechef.com/START100C/problems/AIRINDEX)

[Contest: Division 4](https://www.codechef.com/START100D/problems/AIRINDEX)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Tester:*** [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

347

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Given the air quality index X, check whether it’s strictly less than 100.

# [](#explanation-5)EXPLANATION:

Simply do as the statement says: use an `if` condition to check whether X \lt 100 or not, and print `Yes` or `No` appropriately.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``x = int(input())
print('Yes' if x < 100 else 'No')
``

</details>
