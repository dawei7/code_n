# Find an integer

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUMDIV2 |
| Difficulty Rating | 1714 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [SUMDIV2](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/SUMDIV2) |

---

## Problem Statement

Chef has two nephews who love integers $X$ and $Y$. An integer $N$ is *awesome* if the following conditions hold:
- $1 \leq N \leq 10^{18}$
- $(N+Y)$ is divisible by $X$.
- $(N+X)$ is divisible by $Y$.

Find **any** awesome integer $N$. We can prove that under the given constraints, an answer always exists.

Note that you do **not** have to minimize the answer.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input.
    - The first line of each test case contains two space-separated integers $X$ and $Y$ — favourite numbers of Chef's nephews.

---

## Output Format

For each test case, output an awesome integer. If there are several answers, you may print any of them.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq X, Y \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
18 42
1 1
100 200
```

**Output**

```text
192
5
500
```

**Explanation**

**Test Case 1:** In this case, $N = 192$ is an awesome integer because:
- $1 \le 192 \le 10^{18}$
- $192 + 18 = 210$ is divisible by $42$
- $192 + 42 = 234$ is divisible by $18$

**Test Case 2:** We can output any positive integer $N$ such that $(1 \le N \le 10^{18})$ because $N + 1$ is divisible by $1$ for all such $N$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
18 42
```

**Output for this case**

```text
192
```



#### Test case 2

**Input for this case**

```text
1 1
```

**Output for this case**

```text
5
```



#### Test case 3

**Input for this case**

```text
100 200
```

**Output for this case**

```text
500
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/SUMDIV2)

[Contest: Division 1](https://www.codechef.com/START73A/problems/SUMDIV2)

[Contest: Division 2](https://www.codechef.com/START73B/problems/SUMDIV2)

[Contest: Division 3](https://www.codechef.com/START73C/problems/SUMDIV2)

[Contest: Division 4](https://www.codechef.com/START73D/problems/SUMDIV2)

***Author:*** [frtransform](https://www.codechef.com/users/frtransform)

***Testers:*** [mexomerf](https://www.codechef.com/users/mexomerf), [rivalq](https://www.codechef.com/users/rivalq)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given X and Y, find any positive integer N such that Y divides N+X and X divides N+Y.

#
[](#explanation-5)EXPLANATION:

Let’s analyze what a valid N must look like.

-
Y should divide N+X, which means N+X = aY for some *positive* integer a.

-
X should divide N+Y, which means N+Y = bX for some *positive* integer b.

Putting these equations together, we see that N = aY-X = bX - Y, which reduces to

X\cdot(b+1) = Y\cdot(a+1)

Our task is to choose appropriate a and b so that these equations are satisfied.

The simplest way to do this is to make both sides equal to XY, by choosing b = Y-1 and a = X-1.

This gives us N = aY-X = (X-1)Y - X = XY-X-Y.

However, note that we need to find a positive value of N, and the above value isn’t always positive.

In fact, it fails to be positive in exactly three cases: X = 1, Y = 1, or X = Y = 2.

For those three cases, we simply need to choose higher values of a and b.

For example, choose a = 3X-1 and b = 3Y-1 to obtain N = 3XY-X-Y.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    x, y = map(int, input().split())
    ans = x*y - x - y
    if ans <= 0: ans = 5*x*y - x - y
    print(ans)
``

</details>
