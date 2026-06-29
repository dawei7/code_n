# Kitchen Timings

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KITCHENTIME |
| Difficulty Rating | 273 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [KITCHENTIME](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/KITCHENTIME) |

---

## Problem Statement

The working hours of Chef’s kitchen are from $X$ pm to $Y$ pm $(1 \le X \lt Y \le 12)$.

Find the number of hours Chef works.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $X$ and $Y$ — the starting and ending time of working hours respectively.

---

## Output Format

For each test case, output on a new line, the number of hours Chef works.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \lt Y \leq 12$

---

## Examples

**Example 1**

**Input**

```text
4
1 2
3 7
9 11
2 10
```

**Output**

```text
1
4
2
8
```

**Explanation**

**Test case $1$:** Chef starts working at $1$ pm and works till $2$ pm. Thus, he works for $1$ hour.

**Test case $2$:** Chef starts working at $3$ pm and works till $7$ pm. Thus, he works for $4$ hours.

**Test case $3$:** Chef starts working at $9$ pm and works till $11$ pm. Thus, he works for $2$ hours.

**Test case $4$:** Chef starts working at $2$ pm and works till $10$ pm. Thus, he works for $8$ hours.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3 7
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
9 11
```

**Output for this case**

```text
2
```



#### Test case 4

**Input for this case**

```text
2 10
```

**Output for this case**

```text
8
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/KITCHENTIME)

[Contest: Division 1](https://www.codechef.com/START70A/problems/KITCHENTIME)

[Contest: Division 2](https://www.codechef.com/START70B/problems/KITCHENTIME)

[Contest: Division 3](https://www.codechef.com/START70C/problems/KITCHENTIME)

[Contest: Division 4](https://www.codechef.com/START70D/problems/KITCHENTIME)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Testers:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093), [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

273

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef works from X pm to Y pm. How many hours does he work?

#
[](#explanation-5)EXPLANATION:

The number of hours between X pm and Y pm is Y - X. Thus, the answer is Y - X.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
	x, y = map(int, input().split())
	print(y - x)
``

</details>
