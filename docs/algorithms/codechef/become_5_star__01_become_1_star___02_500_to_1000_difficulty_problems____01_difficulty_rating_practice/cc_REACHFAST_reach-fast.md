# Reach fast

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | REACHFAST |
| Difficulty Rating | 777 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [REACHFAST](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/REACHFAST) |

---

## Problem Statement

Chef is standing at coordinate $A$ while Chefina is standing at coordinate $B$.

In one step, Chef can increase or decrease his coordinate by **at most** $K$.

Determine the **minimum** number of steps required by Chef to reach Chefina.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of three integers $A, B,$ and $K$, the initial coordinate of Chef, the initial coordinate of Chefina and the maximum number of coordinates Chef can move in one step.

---

## Output Format

For each test case, output the minimum number of steps required by Chef to reach Chefina.

---

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq A, B \leq 100$
- $1 \leq K \leq 100$

---

## Examples

**Example 1**

**Input**

```text
4
10 20 3
36 36 5
50 4 100
30 4 2
```

**Output**

```text
4
0
1
13
```

**Explanation**

**Test case $1$:** In the first three steps, Chef increases his coordinate by $K = 3$. In the fourth step, Chef increases his coordinate by $1$ which is less than equal to $K$. It can be shown that this is the minimum number of steps required by Chef.

**Test case $2$:** Chef is already at the same coordinate as Chefina. Thus, he needs $0$ steps.

**Test case $3$:** Chef can use $1$ step to decrease his coordinate by $46$ which is less than $K = 100$ and reach Chefina.

**Test case $4$:** Chef can use $13$ steps to decrease his coordinate by $K = 2$ and reach the coordinate $30-13\cdot 2 = 4$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
10 20 3
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
36 36 5
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
50 4 100
```

**Output for this case**

```text
1
```



#### Test case 4

**Input for this case**

```text
30 4 2
```

**Output for this case**

```text
13
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/REACHFAST)

[Contest: Division 1](https://www.codechef.com/DEC221A/problems/REACHFAST)

[Contest: Division 2](https://www.codechef.com/DEC221B/problems/REACHFAST)

[Contest: Division 3](https://www.codechef.com/DEC221C/problems/REACHFAST)

[Contest: Division 4](https://www.codechef.com/DEC221D/problems/REACHFAST)

***Author:*** [utkarsh_25dec](https://www.codechef.com/users/utkarsh_25dec)

***Testers:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093), [tejas10p](https://www.codechef.com/users/tejas10p)

***Editorialist:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

777

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef wants to move from point A to point B, each time moving a distance of at most K. How many steps are needed?

#
[](#explanation-5)EXPLANATION:

Suppose Chef takes n steps. Then, notice that Chef can move a distance of anywhere between 0 and n\cdot K.

Now, let d = |A - B| be the distance between A and B.

Notice that we want the smallest possible n such that n\cdot K \geq d, since this is the smallest number of steps needed to move a distance of d.

Finding this n can be done by brute-force, or you can use the formula

n = \left\lceil \frac{d}{K} \right\rceil

where \left\lceil \ \right\rceil denotes the ceiling function.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    x, y, k = map(int, input().split())
    print((abs(y-x) + k - 1)//k)
``

</details>
