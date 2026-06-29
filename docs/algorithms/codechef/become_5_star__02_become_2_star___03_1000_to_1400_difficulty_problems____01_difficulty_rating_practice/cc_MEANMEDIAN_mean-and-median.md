# Mean and Median

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MEANMEDIAN |
| Difficulty Rating | 1371 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [MEANMEDIAN](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/MEANMEDIAN) |

---

## Problem Statement

Chef has two numbers $X$ and $Y$. Chef wants to find three integers $A, B,$ and $C$ such that:
- $-1000 \le A, B, C \le 1000$
- $mean([A, B, C]) = X$
- $median([A, B, C]) = Y$

Can you help Chef find such three integers?

As a reminder, $mean([P, Q, R]) = \frac{P + Q + R}{3}$ and $median([P, Q, R])$ is the element at the $2^{nd}$ (middle) position after we sort $[P, Q, R]$ in non-decreasing order.

---

## Input Format

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains two space-separated integers $X$ and $Y$ — the required mean and median of the three integers.

---

## Output Format

For each test case, output three integers $A, B, C$ which satisfy the given conditions.

It is guaranteed that an answer always exists under the given constraints.

If multiple answers exist, output any.

---

## Constraints

- $1 \leq T \leq 10^5$
- $-100 \le X, Y \le 100$

---

## Examples

**Example 1**

**Input**

```text
3
5 5
67 100
4 5
```

**Output**

```text
5 5 5
0 100 101
0 5 7
```

**Explanation**

**Test Case 1:** $mean([5, 5, 5]) = \frac{5 + 5 + 5}{3} = 5$, $median([5, 5, 5]) = 5$.

**Test Case 2:** $mean([0, 100, 101]) = \frac{0 + 100 + 101}{3} = \frac{201}{3} = 67$, $median([0, 100, 101]) = 100$.

**Test Case 3:** $mean([0, 5, 7]) = \frac{0 + 5 + 7}{3} = 4$, $median([0, 5, 7]) = 5$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 5
```

**Output for this case**

```text
5 5 5
```



#### Test case 2

**Input for this case**

```text
67 100
```

**Output for this case**

```text
0 100 101
```



#### Test case 3

**Input for this case**

```text
4 5
```

**Output for this case**

```text
0 5 7
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/MEANMEDIAN)

[Contest: Division 1](https://www.codechef.com/START55A/problems/MEANMEDIAN)

[Contest: Division 2](https://www.codechef.com/START55B/problems/MEANMEDIAN)

[Contest: Division 3](https://www.codechef.com/START55C/problems/MEANMEDIAN)

[Contest: Division 4](https://www.codechef.com/START55D/problems/MEANMEDIAN)

***Author:*** [Jeevan Jyot Singh](https://www.codechef.com/users/JeevanJyot)

***Testers:*** [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_25dec), [Hriday](https://www.codechef.com/users/the_hyp0cr1t3)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1371

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

You are given two integers X and Y. Find three integers A, B, C in the range [-1000, 1000] whose mean is X and median is Y.

#
[](#explanation-5)EXPLANATION:

The median is Y, so one of the three numbers should definitely be Y.

The mean is X, which means that \frac{A+B+C}{3} = X, or in other words, A+B+C = 3X.

After noticing this, several constructions are possible.

One solution is to print the three numbers Y, Y, 3X - 2Y. Their sum is clearly 3X, and since there are two occurrences of Y, one of them is guaranteed to be the middle element regardless of the value of 3X-2Y, hence the median is Y.

#
[](#time-complexity-6)TIME COMPLEXITY

\mathcal{O}(1) per test case.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    x, y = map(int, input().split())
    print(y, y, 3*x - 2*y)
``

</details>
