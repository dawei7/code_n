# Odd Pairs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ODDPAIRS |
| Difficulty Rating | 1044 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [ODDPAIRS](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/ODDPAIRS) |

---

## Problem Statement

Given an integer $N$, determine the number of pairs $(A, B)$ such that:

- $1 \leq A, B \leq N$;
- $A + B$ is **odd**.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single integer $N$.

---

## Output Format

For each test case, output the number of required pairs.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
5
1
2
3
100
199
```

**Output**

```text
0
2
4
5000
19800
```

**Explanation**

**Test case $1$:** There are no pairs satisfying the given conditions.

**Test case $2$:** The pairs satisfying both conditions are: $(1, 2)$ and $(2, 1)$.

**Test case $3$:** The pairs satisfying both conditions are: $(1, 2), (2, 1), (2, 3),$ and $(3, 2)$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
0
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
3
```

**Output for this case**

```text
4
```



#### Test case 4

**Input for this case**

```text
100
```

**Output for this case**

```text
5000
```



#### Test case 5

**Input for this case**

```text
199
```

**Output for this case**

```text
19800
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/ODDPAIRS)

[Contest: Division 1](https://www.codechef.com/START53A/problems/ODDPAIRS)

[Contest: Division 2](https://www.codechef.com/START53B/problems/ODDPAIRS)

[Contest: Division 3](https://www.codechef.com/START53C/problems/ODDPAIRS)

[Contest: Division 4](https://www.codechef.com/START53D/problems/ODDPAIRS)

***Author:*** [ Abhinav Gupta](https://www.codechef.com/users/abhi_inav)

***Testers:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093), [Tejas Pandey](https://www.codechef.com/users/tejas10p)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1044

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given N, count the number of pairs (A, B) such that 1 \leq A, B \leq N and A+B is odd.

#
[](#explanation-5)EXPLANATION:

For A+B to be odd, one of A must be odd and the other must be even. In fact, this is the only restriction.

So, to count the total number of pairs:

- Let the number of even numbers from 1 to N be E, and the number of odd numbers from 1 to N be O.

- If A is odd and B is even, we have O\cdot E choices for them (O for A and E for B)

- If A is even and B is odd, we have E\cdot O choices for them.

- So, the total number of choices is 2\cdot E \cdot O.

All that remains is to find E and O quickly. This is quite easy:

-
O = \left\lceil \frac{N}{2}\right\rceil, which can be implemented in most languages as `(N+1)/2`, using integer division.

-
E = \left\lfloor \frac{N}{2}\right\rfloor, which can be implemented in most languages as simply `N/2` using integer division

Note that N \leq 10^9, so the answer can exceed the range of 32-bit integers. Make sure to use a 64-bit integer datatype.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    odds, evens = (n+1)//2, n//2
    print(2*odds*evens)
``

</details>
