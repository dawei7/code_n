# Far Away

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | FARAWAY |
| Difficulty Rating | 1090 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [FARAWAY](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/FARAWAY) |

---

## Problem Statement

Chef has an array $A$ of size $N$ and an integer $M$, such that $1 \leq A_i \leq M$ for every $1 \leq i \leq N$.

The *distance* of an array $B$ from array $A$ is defined as:
$$
d(A, B) = \sum_{i=1}^N |A_i - B_i|
$$

Chef wants an array $B$ of size $N$, such that $1 \le B_i \le M$ and the value $d(A, B)$ is as large as possible, i.e, the distance of $B$ from $A$ is **maximum**.

Find the **maximum** distance for any valid array $B$.

Note: $|X|$ denotes the absolute value of an integer $X$. For example, $|-4| = 4$ and $|7| = 7$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the length of array $A$ and the limit on the elements of $A$ and $B$.
    - The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

---

## Output Format

For each test case, output on a new line the **maximum** distance of an array from $A$.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2\cdot 10^5$
- $1 \leq M \leq 10^9$
- $1 \leq A_i \leq M$
- The sum of $N$ over all test cases won't exceed $3\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
4
2 6
3 5
4 1
1 1 1 1
5 7
2 3 4 5 6
7 24
23 7 6 16 12 4 24
```

**Output**

```text
7
0
21
127
```

**Explanation**

**Test case $1$:** The array having maximum distance from $A$ is $B = [6, 1]$. Thus the distance is $|3-6| + |5-1| = 3+4=7$.

**Test case $2$:** The only array possible is $B = [1,1,1,1]$. The distance of this array from $A$ is $0$.

**Test case $3$:** One of the possible arrays having maximum distance from $A$ is $B = [7,7,1,1,1]$. Thus the distance is $|2-7| + |3-7| + |4-1| + |5-1| + |6-1| = 5+4+3+4+5=21$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 6
3 5
```

**Output for this case**

```text
7
```



#### Test case 2

**Input for this case**

```text
4 1
1 1 1 1
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
5 7
2 3 4 5 6
```

**Output for this case**

```text
21
```



#### Test case 4

**Input for this case**

```text
7 24
23 7 6 16 12 4 24
```

**Output for this case**

```text
127
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/FARAWAY)

[Contest: Division 1](https://www.codechef.com/START56A/problems/FARAWAY)

[Contest: Division 2](https://www.codechef.com/START56B/problems/FARAWAY)

[Contest: Division 3](https://www.codechef.com/START56C/problems/FARAWAY)

[Contest: Division 4](https://www.codechef.com/START56D/problems/FARAWAY)

***Author:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

***Testers:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec), [Jatin Garg](https://www.codechef.com/users/rivalq)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1056

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given an array A whose elements lie between 1 and M, define the *distance* of an array B (also with elements from 1 to M) to be \sum_{i=1}^N |A_i - B_i|. Compute the maximum possible distance of an array from A.

#
[](#explanation-5)EXPLANATION:

It is of course optimal to choose either B_i = 1 or B_i = M for each index i.

Note that this choice can be made independently for every index, so the solution is to simply take the best option for each one.

That is, the answer is

\sum_{i=1}^N \max(|A_i - 1|, |A_i - M|)

Note that the answer might not fit inside a 32-bit integer, so make sure to use an appropriate data type.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(N) per test case.

#
[](#code-7)CODE:

Setter's code (Python)
``for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    print(sum([max(x-1, m-x) for x in a]))
``

</details>
