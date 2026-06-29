# Weights

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | WGHTS |
| Difficulty Rating | 697 |
| Difficulty Band | 500 to 1000 difficulty problems |
| Path | Become 5 star |
| Lesson | 500 to 800 difficulty rating problems |
| Official Link | [WGHTS](https://www.codechef.com/practice/course/logical-problems/DIFF800/problems/WGHTS) |

---

## Problem Statement

Chef is playing with weights. He has an object weighing $W$ units. He also has three weights each of $X, Y,$ and $Z$ units respectively. Help him determine whether he can measure the **exact** weight of the object with one or more of these weights.

If it is possible to measure the weight of object with one or more of these weights, print `YES`, otherwise print `NO`.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of single line containing a four positive integers $W, X, Y,$ and $Z$.

---

## Output Format

For each test case, output on a new line `YES` if it is possible to measure the weight of object with one or more of these weights, otherwise print `NO`.

You may print each character of the string in either uppercase or lowercase (for example, the strings `yes`, `YES`, `Yes`, and `yeS` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq W, X, Y, Z \leq 10^5$

---

## Examples

**Example 1**

**Input**

```text
4
5 2 1 6
7 9 7 2
20 8 10 12
20 10 11 12
```

**Output**

```text
NO
YES
YES
NO
```

**Explanation**

**Test Case $1$:** It is not possible to measure $5$ units using any combination of given weights.

**Test Case $2$:** Chef can use the second weight of $7$ units to measure the object exactly.

**Test Case $3$:** Chef can use combination of first and third weights to measure $8+12=20$ units.

**Test Case $4$:** Chef cannot measure $20$ units of weight using any combination of given weights.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 2 1 6
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
7 9 7 2
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
20 8 10 12
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
20 10 11 12
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

[Practice](https://www.codechef.com/problems/WGHTS)

[Contest: Division 1](https://www.codechef.com/START53A/problems/WGHTS)

[Contest: Division 2](https://www.codechef.com/START53B/problems/WGHTS)

[Contest: Division 3](https://www.codechef.com/START53C/problems/WGHTS)

[Contest: Division 4](https://www.codechef.com/START53D/problems/WGHTS)

***Author:*** [ Abhinav Sharma](https://www.codechef.com/users/inov_360)

***Testers:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093), [Tejas Pandey](https://www.codechef.com/users/tejas10p)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

697

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Chef has 3 weights, weighing x, y, and z. Can he measure a weight of exactly W using these?

#
[](#explanation-5)EXPLANATION:

There are seven possible positive weights that Chef can measure, namely, \{x, y, z, x+y, x+z, y+z, x+y+z\}. The answer is “Yes” if W equals one of these seven, and “No” otherwise.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    w, a, b, c = map(int, input().split())
    s = {a, b, c, a+b, a+c, b+c, a+b+c}
    print('yes' if w in s else 'no')
``

</details>
