# MIN To MAX

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | OPMIN |
| Difficulty Rating | 838 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [OPMIN](https://www.codechef.com/practice/course/arrays/ARRAYS/problems/OPMIN) |

---

## Problem Statement

You are given an array $A$ of size $N$.

Let $M$ be the **minimum** value present in the array initially.
In one operation, you can choose an element $A_i$ $(1\le i \le N)$ and an integer $X$ $(1\le X \le 100)$, and set $A_i = X$.

Determine the **minimum** number of operations required to make $M$ the **maximum** value in the array $A$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a single integer $N$ - the size of the array.
    - The next line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ - the elements of the array.

---

## Output Format

For each test case, output on a new line, the **minimum** number of operations required to make $M$ the **maximum** value in the array $A$.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq A_i \leq 100$

---

## Examples

**Example 1**

**Input**

```text
3
2
1 2
4
2 2 3 4
1
1
```

**Output**

```text
1
2
0
```

**Explanation**

**Test case $1$:** The minimum value in the array, $M$, is initially $1$. We can use one operation as following:
- Choose $A_2$ and set it as $X = 1$. Thus, the final array becomes $[1, 1]$.

Since all elements of the final array are $1$, the maximum value of the array is now $1$. It can be shown that this is the minimum number of operations required to do so.

**Test case $2$:** The minimum value in the array, $M$, is initially $2$. We can use two operations as following:
- Choose $A_4$ and set it as $X = 2$. Thus, the array becomes $[2, 2, 3, 2]$.
- Choose $A_3$ and set it as $X = 2$. Thus, the array becomes $[2, 2, 2, 2]$.

Since all elements of the final array are $2$, the maximum value of the array is now $2$.

**Test case $3$:** The minimum value in the array, $M$, is initially $1$. It is also the maximum value of the array. Hence, no operations are required.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
1 2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4
2 2 3 4
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
1
1
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/OPMIN)

[Contest: Division 1](https://www.codechef.com/START82A/problems/OPMIN)

[Contest: Division 2](https://www.codechef.com/START82B/problems/OPMIN)

[Contest: Division 3](https://www.codechef.com/START82C/problems/OPMIN)

[Contest: Division 4](https://www.codechef.com/START82D/problems/OPMIN)

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

You have an array A of N integers between 1 and 100. Let M be its minimum.

In one move, you can change A_i to any integer you like between 1 and 100.

What’s the minimum number of moves needed to make M the maximum element?

#
[](#explanation-5)EXPLANATION:

For M to be the maximum, the array can’t contain any elements larger than M.

So, every element larger than M requires at least one move, since it must be reduced to M (or something less than M).

Since M is the minimum element of the original array, the number of such elements is exactly N - x, where x is the number of times M appears in A.

So, use a loop to find x: the number of times M occurs in A.

Then, the answer is N - x.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(n - a.count(min(a)))
``

</details>
