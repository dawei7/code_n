# Reach Home

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | REACH_HOME |
| Difficulty Rating | 395 |
| Difficulty Band | 500 difficulty rating |
| Path | Become 5 star |
| Lesson | Less than 500 difficulty rating |
| Official Link | [REACH_HOME](https://www.codechef.com/practice/course/basic-programming-concepts/DIFF500/problems/REACH_HOME) |

---

## Problem Statement

Chef is hungry and wants to reach home.

Chef can travel up to $5$ kilometres on $1$ litre of fuel on his motorcycle.
Currently, his motorcycle is filled with $X$ litres of fuel and his home is $Y$ kilometres away.

Determine whether Chef can reach his home on his motorcycle or not.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains two space-separated integers $X$ and $Y$ — the amount of fuel in Chef’s motorcycle and the distance to Chef’s home in kilometres.

---

## Output Format

For each test case, output `YES`, if Chef can reach home on his motorcycle. Otherwise output `NO`.

You can output each character of the answer in uppercase or lowercase. For example, the strings `yEs`, `yes`, `Yes`, and YES are considered the same.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X, Y \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
4
2 10
3 17
4 2
6 45
```

**Output**

```text
YES
NO
YES
NO
```

**Explanation**

**Test case $1$:** With $2$ litres of fuel, Chef can go up to $10$ kilometres. Since his home is $10$ kilometres away, he can reach his home on his motorcycle.

**Test case $2$:** With $3$ litres of fuel, Chef can go up to $15$ kilometres. Since his home is $17$ kilometres away, he cannot reach his home on his motorcycle.

**Test case $3$:** With $4$ litres of fuel, Chef can go up to $20$ kilometres. Since his home is $2$ kilometres away, he can reach his home on his motorcycle.

**Test case $4$:** With $6$ litres of fuel, Chef can go up to $30$ kilometres. Since his home is $45$ kilometres away, he cannot reach his home on his motorcycle.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 10
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
3 17
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
4 2
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
6 45
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/REACH_HOME)

[Contest: Division 1](https://www.codechef.com/START82A/problems/REACH_HOME)

[Contest: Division 2](https://www.codechef.com/START82B/problems/REACH_HOME)

[Contest: Division 3](https://www.codechef.com/START82C/problems/REACH_HOME)

[Contest: Division 4](https://www.codechef.com/START82D/problems/REACH_HOME)

***Authors:*** [shubham_grg](https://www.codechef.com/users/shubham_grg)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [tabr](https://www.codechef.com/users/tabr)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has X liters of fuel, each of which allows him to travel 5 km.

Chef’s house is Y km away. Will he be able to reach it?

#
[](#explanation-5)EXPLANATION:

The maximum distance Chef can travel is 5X kilometers, by using all his fuel.

So, the answer is “Yes” if 5X \leq Y and “No” otherwise.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    x, y = map(int, input().split())
    print('Yes' if y < 5*x else 'No')
``

</details>
