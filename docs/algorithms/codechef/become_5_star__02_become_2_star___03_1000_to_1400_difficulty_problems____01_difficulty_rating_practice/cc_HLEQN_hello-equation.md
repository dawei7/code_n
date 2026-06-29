# Hello Equation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HLEQN |
| Difficulty Rating | 1315 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [HLEQN](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/HLEQN) |

---

## Problem Statement

You are given a positive integer $X$. Your task is to tell whether there exist two **positive** integers $a$ and $b$ $(a \gt 0, b \gt 0)$ such that
$$
2\cdot a + 2\cdot b + a\cdot b = X
$$

If there exist positive integers $a$ and $b$ satisfying the above condition print `YES`, otherwise print `NO`.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of single line containing a positive integer $X$.

---

## Output Format

For each test case, output on a new line `YES` or `NO`.

You may print each character of the string in either uppercase or lowercase (for example, the strings `yes`, `YES`, `Yes`, and `yeS` will all be treated as identical).

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
4
2
5
6
12
```

**Output**

```text
NO
YES
NO
YES
```

**Explanation**

**Test case $1$:** There do not exist any positive integers $a$ and $b$ such that $2\cdot a + 2\cdot b + a\cdot b = 2$.

**Test case $2$:** Let $a=1$ and $b=1$, then $2\cdot a+2\cdot b+a\cdot b=5$.

**Test case $3$:** There do not exist any positive integers $a$ and $b$ such that $2\cdot a + 2\cdot b + a\cdot b = 6$.

**Test case $4$:** Let $a=2$ and $b=2$, then $2\cdot a+2\cdot b+a\cdot b=12$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
```

**Output for this case**

```text
NO
```



#### Test case 2

**Input for this case**

```text
5
```

**Output for this case**

```text
YES
```



#### Test case 3

**Input for this case**

```text
6
```

**Output for this case**

```text
NO
```



#### Test case 4

**Input for this case**

```text
12
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

[Practice](https://www.codechef.com/problems/HLEQN)

[Contest: Division 1](https://www.codechef.com/AUG221A/problems/HLEQN)

[Contest: Division 2](https://www.codechef.com/AUG221B/problems/HLEQN)

[Contest: Division 3](https://www.codechef.com/AUG221C/problems/HLEQN)

[Contest: Division 4](https://www.codechef.com/AUG221D/problems/HLEQN)

***Author:*** [Abhinav Sharma](https://www.codechef.com/users/inov_360)

***Testers:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093), [Nishant Shah](https://www.codechef.com/users/nishant403)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1315

#
[](#prerequisites-3)PREREQUISITES:

Basic math

#
[](#problem-4)PROBLEM:

Given X, find if there exist any positive integer solutions to 2\cdot a + 2\cdot b + a\cdot b = X.

#
[](#explanation-5)EXPLANATION:

Suppose we fix the value of a. Can we find out whether a valid b exists?

Yes we can

Rearrange the equation to bring b to one side, and we obtain

b = \frac{X - 2\cdot a}{a + 2}

We want b to be a positive integer, and so all that needs to be done is to check two conditions:

- X - 2\cdot a \gt 0

-
a + 2 divides X - 2\cdot a

both of which are easy to check.

With this in mind, we can iterate over all possible values of a, and check if a valid value of b exists or not.

However, there can be upto 10^9 possible values for a, and iterating over them all is too slow so we need to speed up a little.

Note that, since a\gt 0 and b\gt 0, we must have a\cdot b \leq X. In particular, this means that at least one of a and b must be no larger than \sqrt X. In particular, \min(a, b) \leq \sqrt X.

Also note that the equation is symmetric in a and b, i.e, if we swap a and b, the value of 2\cdot a + 2\cdot b + a\cdot b doesn’t change.

So, without loss of generality, we can always say that a \leq b. This, combined with our earlier observation that \min(a, b) \leq \sqrt X now gives us only \mathcal{O}(\sqrt X) different values of a that need to be checked, which is fast enough to solve the problem.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(\sqrt X) per test case.

#
[](#code-7)CODE:

Editorialist's Code (Python)
``for _ in range(int(input())):
    x = int(input())
    ans = 'no'
    # b = (x - 2*a)/(a+2)
    for a in range(1, x+10):
        if a*a > x:
            break
        if 2*a >= x:
            break
        if (x - 2*a)%(a + 2) != 0:
            continue
        ans = 'yes'
        break
    print(ans)
``

</details>
