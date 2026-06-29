# Infernos

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | INFERNO |
| Difficulty Rating | 1162 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [INFERNO](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/INFERNO) |

---

## Problem Statement

Ved started playing a new mobile game called Fighting Clans. An army of $N$ enemies is approaching his base. The $i^{th}$ enemy has $H_i$ health points. An enemy gets killed if his health points become $0$.
Ved defends his base using a weapon named `Inferno`. He can set the `Inferno` to one of the following two modes:
- Single-Target Mode: In one second, the `Inferno` can target **exactly one** living enemy and cause damage of at most $X$ health points.
- Multi-Target Mode: In one second, the `Inferno` can target **all** living enemies and cause damage of $1$ health point to each of them.

Find the **minimum** time required to kill all the enemies.

**Note:** Ved is **not allowed** to change the mode of the weapon once it is set initially.

---

## Input Format

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $N$ and $X$ - the number of enemies and the damage caused by the single-target mode of `Inferno` in one second respectively.
- The second line of each test case contains $N$ space-separated integers $H_1, H_2, \dots, H_N$ where $H_i$ denotes the initial health points of $i^{th}$ enemy.

---

## Output Format

For each test case, output in a single line, the **minimum** time required to kill all the enemies.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 200$
- $1 \le X \le 100$
- $1 \le A_i \le 100$

---

## Examples

**Example 1**

**Input**

```text
4
5 4
2 2 4 1 1
3 5
5 4 5
4 4
4 4 4 4
3 10
7 8 9
```

**Output**

```text
4
3
4
3
```

**Explanation**

**Test case 1:** In single-target mode, all enemies can be killed in $1$ second each. Thus, in single-target mode, the total time required is $5$ seconds.
In multi-target mode:
- After one second, the health points of the enemies are: $[1, 1, 3, 0, 0]$. Enemies $4$ and $5$ are dead after one second.
- After two seconds, the health points of the enemies are: $[0, 0, 2, 0, 0]$.
- After three seconds, the health points of the enemies are: $[0, 0, 1, 0, 0]$.
- After four seconds, the health points of the enemies are: $[0, 0, 0, 0, 0]$.

Thus, $4$ seconds are required to kill enemies using multi-target mode. The minimum time required to kill all the enemies is $4$ seconds.

**Test case 2:** In single-target mode, all enemies can be killed in $1$ second each. Thus, in single-target mode, the total time required is $3$ seconds.
In multi-target mode:
- After one second, the health points of the enemies are: $[4, 3, 4]$.
- After two seconds, the health points of the enemies are: $[3, 2, 3]$.
- After three seconds, the health points of the enemies are: $[2, 1, 2]$.
- After four seconds, the health points of the enemies are: $[1, 0, 1]$.
- After five seconds, the health points of the enemies are: $[0, 0, 0]$.

Thus, $5$ seconds are required to kill enemies using multi-target mode. The minimum time required to kill all the enemies is $3$ seconds.

**Test case 3:** Here, single-target mode will take $4$ seconds and multi-target mode will also take $4$ seconds. Therefore, the minimum time required is $4$ seconds.

**Test case 4:** Here, single-target mode will take $3$ seconds, while multi-target mode will take $9$ seconds. Therefore, the minimum time required is $3$ seconds.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 4
2 2 4 1 1
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
3 5
5 4 5
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
4 4
4 4 4 4
```

**Output for this case**

```text
4
```



#### Test case 4

**Input for this case**

```text
3 10
7 8 9
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

[Contest Division 1](https://www.codechef.com/START37A/problems/INFERNO)

[Contest Division 2](https://www.codechef.com/START37B/problems/INFERNO)

[Contest Division 3](https://www.codechef.com/START37C/problems/INFERNO)

[Contest Division 4](https://www.codechef.com/START37D/problems/INFERNO)

Setter: [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

Tester: [Jakub Safin](https://www.codechef.com/users/xellos0), [Satyam](https://www.codechef.com/users/satyam_343)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

1162

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Ved started playing a new mobile game called Fighting Clans. An army of N enemies is approaching his base. The i^{th} enemy has H_i health points. An enemy gets killed if his health points become 0.

Ved defends his base using a weapon named `Inferno`. He can set the `Inferno` to one of the following two modes:

- Single-Target Mode: In one second, the `Inferno` can target **exactly one** living enemy and cause damage of at most X health points.

- Multi-Target Mode: In one second, the `Inferno` can target **all** living enemies and cause damage of 1 health point to each of them.

Find the **minimum** time required to kill all the enemies.

**Note:** Ved is **not allowed** to change the mode of the weapon once it is set initially.

#
[](#explanation-5)EXPLANATION:

Let us calculate answer for both modes:

- Single Target Mode: Here we would loop through each enemy and calculate the time required to kill him. Let us assume a function f(i) that tells the time taken to kill the i_{th} enemy then,

f(i) = \lceil \frac{H_i}{X}  \rceil

single\_mode\_answer = \sum_{i=1}^{i=n} f(i)

- Multi Target Mode: Here the answer would be the maximum H_i among all the enemies since each second it is reducing the health of all enemies by 1. Thus,

multi\_mode\_answer = max(H_i), 1 \leq i \leq n

Once we calculate these two, our final answer would be:

answer = min(single\_mode\_answer,  multi\_mode\_answer)

#
[](#time-complexity-6)TIME COMPLEXITY:

O(N), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/-S7x)

[Setter’s Solution](http://p.ip.fi/YsoJ)

[Tester1’s Solution](http://p.ip.fi/l1RC)

[Tester2’s Solution](http://p.ip.fi/07GQ)

</details>
