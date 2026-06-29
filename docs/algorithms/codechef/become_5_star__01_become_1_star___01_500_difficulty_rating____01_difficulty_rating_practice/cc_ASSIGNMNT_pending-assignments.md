# Pending Assignments

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ASSIGNMNT |
| Difficulty Rating | 468 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [ASSIGNMNT](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/ASSIGNMNT) |

---

## Problem Statement

Chef has finally decided to complete all of his pending assignments.

There are $X$ assignments where each assignment takes $Y$ **minutes** to complete.
Find whether Chef would be able to complete all the assignments in $Z$ **days**.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists three space-separated integers $X, Y,$ and $Z$ — the number of assignments, time taken in minutes to complete each assignment, and the number of days in which Chef wants to complete the assignments.

---

## Output Format

For each test case, output on a new line, `YES`, if Chef would be able to complete all the assignments in $Z$ **days**. Otherwise, print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq X, Y \leq 100$
- $1 \leq Z \leq 10$

---

## Examples

**Example 1**

**Input**

```text
3
5 5 5
50 80 2
20 72 1
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Test case $1$:** Chef needs a total of $5\cdot 5 = 25$ minutes to complete all the assignments. Thus, he would be able to complete the assignments in $5$ days.

**Test case $2$:** Chef needs a total of $50\cdot 80 = 4000$ minutes to complete all the assignments. However, in $2$ days, he only has $2\cdot 24\cdot 60 = 2880$ minutes.
Thus, he would not be able to complete the assignments in $2$ days.

**Test case $3$:** Chef needs a total of $20\cdot 72 = 1440$ minutes to complete all the assignments. In $1$ days, he has $24\cdot 60 = 1440$ minutes.
Thus, he would be able to complete the assignments in $1$ day.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 5 5
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
50 80 2
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
20 72 1
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ASSIGNMNT)

[Contest: Division 1](https://www.codechef.com/START107A/problems/ASSIGNMNT)

[Contest: Division 2](https://www.codechef.com/START107B/problems/ASSIGNMNT)

[Contest: Division 3](https://www.codechef.com/START107C/problems/ASSIGNMNT)

[Contest: Division 4](https://www.codechef.com/START107D/problems/ASSIGNMNT)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Tester:*** [yash_daga](https://www.codechef.com/users/yash_daga)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

468

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

Can X assignments, each requiring Y minutes, be completed within Z days?

# [](#explanation-5)EXPLANATION:

We have X assignments that need Y minutes each.

In total, we’d need X\cdot Y *minutes* to finish them all.

In Z *days*, there are 24\cdot 60\cdot Z *minutes* (24 hours in a day, 60 minutes in an hour).

So, the answer is `Yes` if X\cdot Y \leq 1440\cdot Z and `No` otherwise.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

# [](#code-7)CODE

Editorialist's code (Python)
``for _ in range(int(input())):
    x, y, z = map(int, input().split())
    print('Yes' if x*y <= 24*60*z else 'No')
``

</details>
