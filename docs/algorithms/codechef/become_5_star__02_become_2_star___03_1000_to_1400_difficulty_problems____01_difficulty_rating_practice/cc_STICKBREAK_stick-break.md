# Stick Break

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | STICKBREAK |
| Difficulty Rating | 1123 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [STICKBREAK](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/STICKBREAK) |

---

## Problem Statement

Chef has a stick of length $L$. Chef wants to break the stick into $K$ parts such that each part has a non-zero length.

Let the lengths of the $K$ parts be $A_1, A_2, \ldots, A_K$ (Note that $A_1 + A_2 + \ldots + A_K = L$ and $A_i$ is a **positive integer** for all $i$). Chef wants to minimize the value of $\displaystyle \sum_{i = 1}^{K - 1}|A_{i + 1} - A_i|$. Can you help Chef? (Here $|x|$ denotes the absolute value of $x$)

Under the given constraints it will always be possible to break the stick into $K$ parts of non-zero lengths.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space-separated integers $L$ and $K$ — the initial length of the stick and the number of parts Chef wants to break the stick into.

---

## Output Format

For each test case, output the minimum value of $\displaystyle \sum_{i = 1}^{K - 1}|A_{i + 1} - A_i|$.

---

## Constraints

- $1 \leq T \leq 10^4$
- $2 \le K \le L \le 10^9$

---

## Examples

**Example 1**

**Input**

```text
2
4 3
2 2
```

**Output**

```text
1
0
```

**Explanation**

**Test Case 1:** It is optimal to break the stick of length $4$ into $3$ parts in the following manner: $[2, 1, 1]$. The value of $\displaystyle \sum_{i = 1}^{K - 1}|A_{i + 1} - A_i| = |1 - 2| + |1 - 1| = 1$.

**Test Case 2:** It is optimal to break the stick of length $2$ into $2$ parts in the following manner: $[1, 1]$. The value of $\displaystyle \sum_{i = 1}^{K - 1}|A_{i + 1} - A_i| = |1 - 1| = 0$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 3
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2 2
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

[Practice](https://www.codechef.com/problems/STICKBREAK)

[Contest: Division 1](https://www.codechef.com/LTIME112A/problems/STICKBREAK)

[Contest: Division 2](https://www.codechef.com/LTIME112B/problems/STICKBREAK)

[Contest: Division 3](https://www.codechef.com/LTIME112C/problems/STICKBREAK)

[Contest: Division 4](https://www.codechef.com/LTIME112D/problems/STICKBREAK)

***Author:*** [Jeevan Jyot Singh](https://www.codechef.com/users/jeevanjyot)

***Tester:*** [Hriday](https://www.codechef.com/users/the_hyp0cr1t3)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1123

#
[](#prerequisites-3)PREREQUISITES:

Basic math

#
[](#problem-4)PROBLEM:

Given a stick of length L, you want to break it into exactly K positive integer-sized parts A_1, A_2, \ldots, A_K

What is the minimum possible value of \sum_{i=1}^{K-1} |A_i - A_{i+1}|?

#
[](#explanation-5)EXPLANATION:

The answer is 0 if K divides L and 1 otherwise.

Proof

If K divides L, obviously we can make K parts of size \frac{L}{K} and the given expression evaluates to zero.

Otherwise, it’s always possible to obtain a difference of 1. Here’s a construction:

Let x = \left\lfloor \frac{L}{K}\right\rfloor and y = \left\lceil \frac{L}{K}\right\rceil.

Also, let r denote the remainder when L is divided by K. Since K doesn’t divide L, 0 \lt r \lt K.

Now, set A_1 = A_2 = \ldots = A_r = y, and everything else equal to x.

It’s easy to see that the sum of all A_i is L. Further, almost every pair of adjacent terms are equal: only A_r and A_{r+1} are not equal, and they differ by |x-y| = 1, as required.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n, k = map(int, input().split())
    print(1 if n%k > 0 else 0)
``

</details>
