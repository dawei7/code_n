# Single-use Attack

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SINGLEUSE |
| Difficulty Rating | 777 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [SINGLEUSE](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/SINGLEUSE) |

---

## Problem Statement

Chef is playing a video game, and is now fighting the final boss.

The boss has $H$ health points. Each attack of Chef reduces the health of the boss by $X$.
Chef also has a special attack that can be used **at most once**, and will decrease the health of the boss by $Y$.

Chef wins when the health of the boss is $\leq 0$.
What is the **minimum** number of attacks needed by Chef to win?

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case will contain three space-separated integers $H, X, Y$ — the parameters described in the statement.

---

## Output Format

For each test case, output on a new line the minimum number of attacks needed by Chef to win.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X \lt Y \leq H \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
100 25 40
100 29 45
46 1 2
78 15 78
```

**Output**

```text
4
3
45
1
```

**Explanation**

**Test case $1$:** Chef can attack the boss $4$ times normally. This results in $25 + 25 + 25 + 25 = 100$ damage, which is enough to defeat the boss.

**Test case $2$:** Chef can attack the boss $2$ times normally, then use the special attack. This results in $29 + 29 + 45 = 103$ damage, which is enough to defeat the boss.

**Test case $3$:** Chef can proceed as follows:
- First, use the special attack. This leaves the boss with $46 - 2 = 44$ health.
- Then, use $44$ normal attacks to defeat the boss, since each one does $1$ damage.

This takes a total of $44 + 1 = 45$ attacks.

**Test case $4$:** Chef can use the special attack to immediately bring the health of the boss to zero, hence only needing one attack.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
100 25 40
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
100 29 45
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
46 1 2
```

**Output for this case**

```text
45
```



#### Test case 4

**Input for this case**

```text
78 15 78
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SINGLEUSE)

[Contest: Division 1](https://www.codechef.com/START80A/problems/SINGLEUSE)

[Contest: Division 2](https://www.codechef.com/START80B/problems/SINGLEUSE)

[Contest: Division 3](https://www.codechef.com/START80C/problems/SINGLEUSE)

[Contest: Division 4](https://www.codechef.com/START80D/problems/SINGLEUSE)

***Author:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

***Testers:*** [wuhudsm](https://www.codechef.com/users/wuhudsm), [satyam_343](https://www.codechef.com/users/satyam_343)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef is fighting a boss with H health, and does X damage per attack.

At most once, Chef can use a special move and do Y damage.

What’s the minimum number of attacks Chef needs to defeat the boss?

#
[](#explanation-5)EXPLANATION:

Since X \lt Y, it’s always optimal to use the special attack.

After using the special attack, the boss’ remaining health is H-Y.

This needs to be depleted using normal attacks, and since they do X damage each, the number of them needed is \left\lceil \frac{H-Y}{X}\right\rceil.

Here, \lceil \ \rceil denotes the [ceiling function](https://en.wikipedia.org/wiki/Floor_and_ceiling_functions).

Including the first special attack, the answer is

1 + \left\lceil \frac{H-Y}{X}\right\rceil

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
	h, x, y = map(int, input().split())
	print(1 + (h-y+x-1)//x)
``

</details>
