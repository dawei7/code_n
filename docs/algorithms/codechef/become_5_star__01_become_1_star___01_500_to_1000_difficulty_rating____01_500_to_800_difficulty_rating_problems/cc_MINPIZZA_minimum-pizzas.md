# Minimum Pizzas

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MINPIZZA |
| Difficulty Rating | 546 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [MINPIZZA](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/MINPIZZA) |

---

## Problem Statement

Each pizza consists of $4$ slices. There are $N$ friends and each friend needs exactly $X$ slices.

Find the **minimum** number of pizzas they should order to satisfy their appetite.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two integers $N$ and $X$, the number of friends and the number of slices each friend wants respectively.

---

## Output Format

For each test case, output the **minimum** number of pizzas required.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N, X \leq 10$

---

## Examples

**Example 1**

**Input**

```text
4
1 5
2 6
4 3
3 5
```

**Output**

```text
2
3
3
4
```

**Explanation**

**Test case $1$:** There is only $1$ friend who requires $5$ slices. If he orders $1$ pizza, he will get only $4$ slices. Thus, at least $2$ pizzas should be ordered to have required number of slices.

**Test case $2$:** There are $2$ friends who require $6$ slices each. Thus, total $12$ slices are required. To get $12$ slices, they should order $3$ pizzas.

**Test case $3$:** There are $4$ friends who require $3$ slices each. Thus, total $12$ slices are required. To get $12$ slices, they should order $3$ pizzas.

**Test case $4$:** There are $3$ friends who require $5$ slices each. Thus, total $15$ slices are required. To get $15$ slices, they should order at least $4$ pizzas.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1 5
```

**Output for this case**

```text
2
```



#### Test case 2

**Input for this case**

```text
2 6
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
4 3
```

**Output for this case**

```text
3
```



#### Test case 4

**Input for this case**

```text
3 5
```

**Output for this case**

```text
4
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MINPIZZA)

[Contest: Division 1](https://www.codechef.com/OCT221A/problems/MINPIZZA)

[Contest: Division 2](https://www.codechef.com/OCT221B/problems/MINPIZZA)

[Contest: Division 3](https://www.codechef.com/OCT221C/problems/MINPIZZA)

[Contest: Division 4](https://www.codechef.com/OCT221D/problems/MINPIZZA)

***Author:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec)

***Tester:*** [Harris Leung](https://www.codechef.com/users/gamegame)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

TBD

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

N friends each want to eat X slices of pizza. Each pizza has 4 slices. How many pizzas are needed?

#
[](#explanation-5)EXPLANATION:

The total number of slices that need to be eaten is N\cdot X.

Buying K pizzas gives us 4K slices. We would like 4K \geq N\cdot X.

The smallest K for which this is true is K = \left\lceil \frac{N\cdot X}{4}\right\rceil, that is, the ceiling of \frac{N\cdot X}{4}.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n, x = map(int, input().split())
    print((n*x + 3)//4)
``

</details>
