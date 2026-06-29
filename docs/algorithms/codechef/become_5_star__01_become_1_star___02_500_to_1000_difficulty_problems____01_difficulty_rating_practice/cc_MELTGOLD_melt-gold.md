# Melt Gold

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MELTGOLD |
| Difficulty Rating | 835 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 800 to 1000 difficulty rating problems |
| Official Link | [MELTGOLD](https://www.codechef.com/practice/course/logical-problems/DIFF1000/problems/MELTGOLD) |

---

## Problem Statement

Chef has an ore with melting point of $X$ degrees.
 Chef’s kiln has a initial temperature of $Y$ degrees. The temperature of the kiln increases by $i$ degrees after the $i^{th}$ minute.

Find the **minimum** time in minutes after which the ore starts melting.

Note:
- We are only concerned about the temperature at the end of each minute and not during a minute.
- The ore starts melting if the temperature of the kiln becomes greater than or equal to the melting point.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $X$ and $Y$ — the melting point of the ore and the initial temperature of kiln.

---

## Output Format

For each test case, output on a new line, the **minimum** time in minutes after which the ore starts melting.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq Y \lt X \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
3
3 2
5 3
10 5
```

**Output**

```text
1
2
3
```

**Explanation**

**Test case $1$:** The initial temperature of the kiln is $2$ and the melting point of ore is $3$.
After first minute, the temperature of kiln increases by $1$.
Thus, after $1$ minute the temperature of kiln becomes $2+1=3$, which is equal to the melting point. Thus, the ore starts melting.

**Test case $2$:** The initial temperature of the kiln is $3$ and the melting point of ore is $5$.
After first minute, the temperature of kiln increases by $1$, and becomes $4$.
After second minute, the temperature of kiln increases by $2$, and becomes $6$.

Thus, after $2$ minutes the temperature of kiln becomes $6$, which is greater than the melting point. Thus, the ore starts melting.

**Test case $3$:** The initial temperature of the kiln is $5$ and the melting point of ore is $10$.
After first minute, the temperature of kiln increases by $1$, and becomes $6$.
After second minute, the temperature of kiln increases by $2$, and becomes $8$.
After third minute, the temperature of kiln increases by $3$, and becomes $11$.

Thus, after $3$ minutes the temperature of kiln becomes $11$, which is greater than the melting point. Thus, the ore starts melting.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3 2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
5 3
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
10 5
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MELTGOLD)

[Contest: Division 1](https://www.codechef.com/START84A/problems/MELTGOLD)

[Contest: Division 2](https://www.codechef.com/START84B/problems/MELTGOLD)

[Contest: Division 3](https://www.codechef.com/START84C/problems/MELTGOLD)

[Contest: Division 4](https://www.codechef.com/START84D/problems/MELTGOLD)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Tester:*** [abhidot](https://www.codechef.com/users/abhidot)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

835

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef’s kiln is at Y degrees, and he has an ore that melts at X degrees.

In the i-th second, the kiln’s temperature increases by i degrees.

Find the time needed for the ore’s melting temperature to be reached.

#
[](#explanation-5)EXPLANATION:

It’s enough to directly simulate the process!

That is, start with the temperature at Y, and in the i-th step, increase it by i.

Stop once you reach \geq X.

This is fast enough because the temperature grows quickly: after i seconds, the temperature is exactly Y + \frac{i\cdot (i+1)}{2}, so it will take about 2\sqrt{X-Y} seconds for us to reach X, which is pretty small.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(\sqrt{X-Y}) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    x, y = map(int, input().split())
    ans = 0
    while y < x:
        y += ans + 1
        ans += 1
    print(ans)
``

</details>
