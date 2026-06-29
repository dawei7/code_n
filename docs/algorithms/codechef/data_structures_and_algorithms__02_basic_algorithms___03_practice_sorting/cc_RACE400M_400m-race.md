# 400M Race

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RACE400M |
| Difficulty Rating | 548 |
| Difficulty Band | Practice Sorting |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [RACE400M](https://www.codechef.com/practice/course/sorting/SORTING/problems/RACE400M) |

---

## Problem Statement

Alice, Bob, and Charlie participated in a $400$-metre race.
The time taken by Alice, Bob, and Charlie to complete the race was $X, Y,$ and $Z$ seconds respectively. Note that $X, Y,$ and $Z$ are **distinct**.

Determine the person having the highest average speed in the race.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains three space-separated integers $X, Y,$ and $Z$ — the time taken by Alice, Bob, and Charlie to complete the race.

---

## Output Format

For each test case, output on a new line:
- `ALICE`, if Alice had the highest average speed.
- `BOB`, if Bob had the highest average speed.
- `CHARLIE`, if Charlie had the highest average speed.

Note that you may print each character in uppercase or lowercase. For example, the strings `BOB`, `bob`, `Bob`, and `BoB` are all considered identical.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq X, Y, Z \leq 100$
- $X, Y,$ and $Z$ are distinct.

---

## Examples

**Example 1**

**Input**

```text
3
1 2 8
4 100 1
7 3 5
```

**Output**

```text
ALICE
CHARLIE
BOB
```

**Explanation**

**Test case $1$:** The time taken by the three participants to complete a $400$ metre race was $1, 2, $ and $8$ respectively. Thus, their respective speeds were $\frac{400}{1} = 400, \frac{400}{2} = 200,$ and $\frac{400}{8} = 50$ metres per second respectively.

Thus, Alice has the maximum speed.

**Test case $2$:** The time taken by the three participants to complete a $400$ metre race was $4, 100, $ and $1$ respectively. Thus, their respective speeds were $\frac{400}{4} = 100, \frac{400}{100} = 4,$ and $\frac{400}{1} = 400$ metres per second respectively.

Thus, Charlie has the maximum speed.

**Test case $3$:** Since Bob takes the minimum time to complete the race, he has the maximum average speed.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 2 8
```

**Output for this case**

```text
ALICE
```



#### Test case 2

**Input for this case**

```text
4 100 1
```

**Output for this case**

```text
CHARLIE
```



#### Test case 3

**Input for this case**

```text
7 3 5
```

**Output for this case**

```text
BOB
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/RACE400M)

[Contest: Division 1](https://www.codechef.com/START76A/problems/RACE400M)

[Contest: Division 2](https://www.codechef.com/START76B/problems/RACE400M)

[Contest: Division 3](https://www.codechef.com/START76C/problems/RACE400M)

[Contest: Division 4](https://www.codechef.com/START76D/problems/RACE400M)

***Author:*** [notsoloud](https://www.codechef.com/users/notsoloud)

***Testers:*** [iceknight1093](https://www.codechef.com/users/iceknight1093), [yash_daga](https://www.codechef.com/users/yash_daga)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given the times taken by Alice, Bob, and Charlie to run a 400\ M race, (A, B, C respectively), who had the highest average speed?

#
[](#explanation-5)EXPLANATION:

Using the formula \text{distance} = \text{speed} \times \text{time}, we can see that the highest average speed corresponds to the lowest time taken.

So, find who out of Alice/Bob/Charlie took the lowest time; that person also has the highest average speed.

This can be implemented with a couple of `if` conditions.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    x, y, z = map(int, input().split())
    if x == min(x, y, z): print('Alice')
    if y == min(x, y, z): print('Bob')
    if z == min(x, y, z): print('Charlie')
``

</details>
