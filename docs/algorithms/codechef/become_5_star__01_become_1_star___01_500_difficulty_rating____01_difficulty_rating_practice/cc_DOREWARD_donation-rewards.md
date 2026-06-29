# Donation Rewards

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DOREWARD |
| Difficulty Rating | 395 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [DOREWARD](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/DOREWARD) |

---

## Problem Statement

On the occasion of World Blood Donor Day, Chef has organized an event to reward regular blood donars in Chefland.

- If the donor has made less than or equal to $3$ donations, they receive a `BRONZE` donor badge.
- If the donor has made more than $3$ but less than equal to $6$ donations, they receive a `SILVER` donor badge.
- If the donor has made more than $6$ donations, they receive a `GOLD` donor badge.

Given that a person has made $X$ donations, find the badge they receive.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case contains an integer $X$, denoting the number of blood donations the person has made.

---

## Output Format

For each test case, output on a new line:
- `BRONZE`, if the person has made less than or equal to $3$ donations;
- `SILVER`, if the person has made more than $3$ but less than equal to $6$ donations;
- `GOLD`, if the person has made more than $6$ donations.

Each character can be printed in uppercase or lowercase. For example, `GOLD`, `gold`, `Gold`, and `gOlD` are considered identical.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 10$

---

## Examples

**Example 1**

**Input**

```text
4
1
3
5
7
```

**Output**

```text
BRONZE
BRONZE
SILVER
GOLD
```

**Explanation**

**Test case $1$:** The person has made less than equal to $3$ donations. Thus they receive bronze badge.

**Test case $2$:** The person has made less than equal to $3$ donations. Thus they receive bronze badge.

**Test case $3$:** The person has made more than $3$ but less than equal to $6$ donations. Thus they receive silver badge.

**Test case $4$:** The person has made more than $6$ donations. Thus they receive gold badge.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
BRONZE
```



#### Test case 2

**Input for this case**

```text
3
```

**Output for this case**

```text
BRONZE
```



#### Test case 3

**Input for this case**

```text
5
```

**Output for this case**

```text
SILVER
```



#### Test case 4

**Input for this case**

```text
7
```

**Output for this case**

```text
GOLD
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DOREWARD)

[Contest: Division 1](https://www.codechef.com/START95A/problems/DOREWARD)

[Contest: Division 2](https://www.codechef.com/START95B/problems/DOREWARD)

[Contest: Division 3](https://www.codechef.com/START95C/problems/DOREWARD)

[Contest: Division 4](https://www.codechef.com/START95D/problems/DOREWARD)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Tester:*** [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

395

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Given the number of times a person has donated blood, X, decide whether they receive a Bronze, Silver, or Gold medal.

# [](#explanation-5)EXPLANATION:

It’s enough to directly implement the conditions provided in the statement, using `if` conditions.

That is,

- If X \leq 3, print `Bronze`.

- If 4 \leq X \leq 6, print `Silver`.

- If 7 \leq X, print `Gold`.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``testcases = int(input())
for t in range(testcases):
    x = int(input())
    if x <= 3: print('Bronze')
    elif x <= 6: print('Silver')
    else: print('Gold')
``

</details>
