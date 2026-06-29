# Chef Odd

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CHEFODD |
| Difficulty Rating | 1486 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [CHEFODD](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/CHEFODD) |

---

## Problem Statement

You want to partition the set $S = \{1, 2, \ldots, N\}$ into $K$ sets $S_1, S_2, \ldots, S_K$, such that $|S_i| \ge 2$, and the sum of elements in each $S_i$ is odd.

Is it possible to do so?

**Note 1:** Partitioning the set $S = \{1, 2, \ldots, N\}$ into $K$ sets $S_1, S_2, \ldots, S_K$ means that every element of $S$ should be in exactly one of the sets $S_1, S_2, \ldots, S_K$, and $S_i \subseteq S$, for all $1 \leq i \leq K$.

**Note 2:** $|A|$ denotes the number of elements in the set $A$.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line and only line of each test case contains two space-separated integers, $N$ and $K$.

---

## Output Format

For each test case, output `YES` if you can partition the set satisfying the requirements. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

---

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 10^{18}$
- $1 \leq K \leq 10^{18}$

---

## Examples

**Example 1**

**Input**

```text
2
5 2
14 5
```

**Output**

```text
NO
YES
```

**Explanation**

**Test case $1$**: There is no way you can partition $\{1, 2, 3, 4, 5\}$ into $2$ subsets such that each has an odd sum and each subset contains at least $2$ integers.

**Test case $2$**: One of the ways to partition is $\{1, 4, 6, 12\}, \{2, 5\}, \{3, 14\}, \{7, 10, 11, 13\}, \{9, 8\}$. The sum of elements in each subset is $23, 7, 17, 41, 17$, each of which is odd and each subset contains at least $2$ integers.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 2
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
14 5
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

[Practice](https://www.codechef.com/problems/CHEFODD)

[Contest: Division 1](https://www.codechef.com/START91A/problems/CHEFODD)

[Contest: Division 2](https://www.codechef.com/START91B/problems/CHEFODD)

[Contest: Division 3](https://www.codechef.com/START91C/problems/CHEFODD)

[Contest: Division 4](https://www.codechef.com/START91D/problems/CHEFODD)

***Author:*** [souradeep1999](https://www.codechef.com/users/souradeep1999)

***Tester and Editorialist:*** [iceknight1093](https://www.codechef.com/users/iceknight1093)

#
[](#difficulty-2)DIFFICULTY:

1486

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given N and K, determine whether it’s possible to partition the integers \{1, 2, \ldots, N\} into exactly K groups such that:

- Each group contains \geq 2 integers.

- The sum of each group is odd.

#
[](#explanation-5)EXPLANATION:

First off, note that we want to form K groups with \geq 2 integers each.

This means we need at least 2K integers in the first place; so if N \lt 2K the answer is immediately `No`.

Now let’s analyze when N \geq 2K.

We have x = \left\lceil \frac{N}{2} \right\rceil odd integers and y = \left\lfloor \frac{N}{2} \right\rfloor even integers to work with.

Note that we’ll have x = y if N is even, and x = y+1 if N is odd.

Also, N \geq 2K means x, y \geq K.

The sum of each group must be odd, which means each group should contain an odd number of odd integers. The even integers don’t affect the parity of the sum, so they can be distributed however we like.

Since x, y \geq K, let’s first put one odd and one even integer into each group.

Now, each group has odd sum and \geq 2 elements; we just need to figure out whether the other elements can be distributed properly while maintaining this property.

We’re left with x-K odd integers, which need to be distributed among the K groups.

To keep the sum of each group odd, note that even group must receive an even number of these x-K integers.

In particular, this means x-K itself must be even; and it’s not hard to see that this condition is also sufficient (if x-K is even, give all x-K odd integers to the first group and we’re done).

So, when N \geq 2K, the answer is `Yes` if x-K is even and `No` otherwise.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n, k = map(int, input().split())
    if n < 2*k: print('No')
    else: print('Yes' if ((n+1)//2 - k)%2 == 0 else 'No')
``

</details>
