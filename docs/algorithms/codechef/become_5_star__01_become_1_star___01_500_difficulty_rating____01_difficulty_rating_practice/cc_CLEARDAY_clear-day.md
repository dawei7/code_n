# Clear Day

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CLEARDAY |
| Difficulty Rating | 233 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [CLEARDAY](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/CLEARDAY) |

---

## Problem Statement

Chef classifies a day to be either `rainy`, `cloudy`, or `clear`.

In a particular **week**, Chef finds $X$ days to be `rainy` and $Y$ days to be `cloudy`.
Find the number of `clear` days in the week.

---

## Input Format

- The first and only line of input will contain two space-separated integers $X$ and $Y$, denoting the number of rainy and cloudy days in the week.

---

## Output Format

Output the number of clear days in the week.

---

## Constraints

- $0 \leq X, Y \leq 7$
- $0 \leq X+Y \leq 7$

---

## Examples

**Example 1**

**Input**

```text
2 3
```

**Output**

```text
2
```

**Explanation**

There are $7$ days in a week. If there are $2$ rainy days and $3$ cloudy days, then the remaining $7-2-3=2$ days are clear.

**Example 2**

**Input**

```text
3 4
```

**Output**

```text
0
```

**Explanation**

If there are $3$ rainy days and $4$ cloudy days, then the remaining $7-3-4=0$ days are clear.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/CLEARDAY)

[Contest: Division 1](https://www.codechef.com/START107A/problems/CLEARDAY)

[Contest: Division 2](https://www.codechef.com/START107B/problems/CLEARDAY)

[Contest: Division 3](https://www.codechef.com/START107C/problems/CLEARDAY)

[Contest: Division 4](https://www.codechef.com/START107D/problems/CLEARDAY)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Tester:*** [yash_daga](https://www.codechef.com/users/yash_daga)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

233

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

A certain week has X rainy days and Y cloudy days.

How many days were clear?

# [](#explanation-5)EXPLANATION:

Out of 7 days in the week, X were rainy and Y were cloudy.

The remaining days are clear: and there are 7-X-Y of them.

# [](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per testcase.

# [](#code-7)CODE

Editorialist's code (Python)
``x, y = map(int, input().split())
print(7-x-y)
``

</details>
