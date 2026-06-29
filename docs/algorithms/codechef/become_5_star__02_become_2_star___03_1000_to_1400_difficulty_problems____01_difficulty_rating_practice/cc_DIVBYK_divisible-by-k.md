# Divisible by K

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DIVBYK |
| Difficulty Rating | 1329 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [DIVBYK](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/DIVBYK) |

---

## Problem Statement

You are given an array $A$ consisting of $N$ positive integers and a positive integer $K$.

Find whether there exists a *subset* $S$ of the elements of $A$ such that the **product** of all elements of $S$ is divisible by $K$.

Note that a *subset* is obtained by deleting some or no elements without changing the order of the remaining elements.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $K$ — the number of elements of $A$ and the above mentioned integer $K$.
    - The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$ representing the array $A$.

---

## Output Format

For each test case, print on a new line the answer: `YES` if there exists a subset $S$ and `NO` otherwise.

Each character of the output may be printed in either uppercase or lowercase, i.e, the strings `Yes`, `YES, `yes`, `yEs` will all be treated as identical.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq A_i, K \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
3
2 2
7 8
5 3
1 1 2 1 1
3 6
7 2 3
```

**Output**

```text
YES
NO
YES
```

**Explanation**

**Test case $1$:** Consider the subset $S = [8]$. The product of all the elements is $8$ which is divisible by $K = 2$.

**Test case $2$:** There exists no subset of $A$ such that the product of all elements of the subset is divisible by $K$.

**Test case $3$:** Consider the subset $S = [2, 3]$. The product of all the elements is $6$ which is divisible by $K = 6$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2 2
7 8
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
5 3
1 1 2 1 1
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
3 6
7 2 3
```

**Output for this case**

```text
YES
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/DIVBYK)

[Contest: Division 1](https://www.codechef.com/DEC221A/problems/DIVBYK)

[Contest: Division 2](https://www.codechef.com/DEC221B/problems/DIVBYK)

[Contest: Division 3](https://www.codechef.com/DEC221C/problems/DIVBYK)

[Contest: Division 4](https://www.codechef.com/DEC221D/problems/DIVBYK)

***Author:*** [satyam_343](https://www.codechef.com/users/satyam_343)

***Testers:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093), [tejas10p](https://www.codechef.com/users/tejas10p)

***Editorialist:*** [IceKnight1093](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1329

#
[](#prerequisites-3)PREREQUISITES:

[Basic modular arithmetic](https://codeforces.com/blog/entry/97623)

#
[](#problem-4)PROBLEM:

Given an array A, find a subset whose product is divisible by K or report that none exist.

#
[](#explanation-5)EXPLANATION:

Suppose that we had a subset S whose product was divisible by K.

Then, notice that if we add more elements to the subset, its product will still be divisible by K.

So, it’s enough to check whether the product of all the elements is divisible by K.

However, the product of all elements is too large to compute (at least in C/C++).

Instead, notice that we only care about whether the product is divisible by K or not, not what the actual product is.

So, we can just compute A_1\cdot A_2 \cdot \ldots \cdot A_N \pmod K and check whether this is zero or not.

Computing this can be done with a loop as follows:

- Initialize a variable prod = 1.

- For each i from 1 to N, do the following:

- Multiply prod with A_i modulo K, i.e, set prod \to (prod \cdot A_i) \pmod K

- The final value of prod is what we want. Check whether it’s zero or not, and we’re done.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(1) per testcase.

#
[](#code-7)CODE:

Code (Python)
``for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    prod = 1
    for x in a:
        prod *= x
        prod %= k
    print('Yes' if prod == 0 else 'No')
``

</details>
