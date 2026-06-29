# Powered Parameters

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | POWPM |
| Difficulty Rating | 1673 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1600 to 1700 difficulty problems |
| Official Link | [POWPM](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1700/problems/POWPM) |

---

## Problem Statement

You are given an array $A$ containing $N$ integers.
Count the number of **ordered pairs** $(i, j)$ such that:
- $1 \leq i, j \leq N$, and
- $A_i^j \leq A_j$
That is, $A_i$ raised to the power $j$ doesn't exceed $A_j$.

Note that we're counting ordered pairs, meaning the pair $(1, 2)$ is *different* from the pair $(2, 1)$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ — the number of elements in the array.
    - The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

---

## Output Format

For each test case, output on a new line the number of ordered pairs $(i, j)$ that satisfy the given condition.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2\cdot 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
3
2 3 4
4
2 7 2 3
5
1000 100 1 10 1
```

**Output**

```text
1
4
14
```

**Explanation**

**Test case $1$:** The only valid pair is $(1, 1)$, since $A_i^j = 2^1 \leq 2 = A_j$.
$(1, 3)$ is an invalid pair for example, since $A_i^j = 2^3 = 8 \gt 4 = A_j$. The same can be verified for all the other pairs.

**Test case $2$:** The valid pairs are $(1, 1), (1, 2), (3, 1), (3, 2)$.

**Test case $3$:** The valid pairs are:
$(1, 1),$
$(2, 1),$
$(3, 1), (3, 2), (3, 3), (3, 4), (3, 5),$
$(4, 1), (4, 2),$
$(5, 1), (5, 2), (5, 3), (5, 4), (5, 5).$

**Separated test cases**

#### Test case 1

**Input for this case**

```text
3
2 3 4
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4
2 7 2 3
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
5
1000 100 1 10 1
```

**Output for this case**

```text
14
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# [](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/POWPM)

[Contest: Division 1](https://www.codechef.com/START133A/problems/POWPM)

[Contest: Division 2](https://www.codechef.com/START133B/problems/POWPM)

[Contest: Division 3](https://www.codechef.com/START133C/problems/POWPM)

[Contest: Division 4](https://www.codechef.com/START133D/problems/POWPM)

***Author:*** [munch_01](https://www.codechef.com/users/munch_01)

***Tester:*** [apoorv_me](https://www.codechef.com/users/apoorv_me)

***Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

# [](#difficulty-2)DIFFICULTY:

TBD

# [](#prerequisites-3)PREREQUISITES:

None

# [](#problem-4)PROBLEM:

You’re given an array A. Find the number of pairs of indices (i, j) such that A_i^j \leq A_j.

# [](#explanation-5)EXPLANATION:

Powers of positive integers generally grow pretty fast: in particular, if x \geq 2, then x^{30} \gt 10^9.

This means that any pair (i, j) such that A_i \geq 2 and j \geq 30 is automatically invalid!

In other words, every valid pair should have either A_i = 1, or j \lt 30.

Looking at these two cases:

- If A_i = 1, then it doesn’t matter what j is: A_i^j = 1^j = 1 will always be \leq A_j.

So, in this case we can simply add N to the answer, since every j is valid.

- If A_i \gt 1, then our observation tells us that it’s enough to check for only j \lt 30, which can be done using a brute force.

We check at most 30\cdot N pairs of indices this way, which is fast enough.

Note that depending on your implementation, you will have to deal with overflow issues appropriately.

A simple way of doing this is to store the current power in a `64`-bit variable, and break out once it exceeds 10^9 - this way you will never encounter overflow since at any point you only multiply something \leq 10^9 with something else \leq 10^9.

# [](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N\log 10^9) per testcase.

# [](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if a[i] == 1: ans += n
        else:
            pw = 1
            for j in range(n):
                pw *= a[i]
                if pw > 10**9: break
                ans += pw <= a[j]
    print(ans)
``

</details>
