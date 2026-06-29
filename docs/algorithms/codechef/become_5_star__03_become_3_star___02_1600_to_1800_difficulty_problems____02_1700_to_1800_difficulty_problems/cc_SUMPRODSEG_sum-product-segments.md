# Sum Product Segments

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUMPRODSEG |
| Difficulty Rating | 1713 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [SUMPRODSEG](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/SUMPRODSEG) |

---

## Problem Statement

A *segment* is a range of **non-negative** integers $L, L + 1, L + 2, \ldots, R$, denoted $[L, R]$ where $L \leq R$.

Chef has a set $S$ consisting of **all** segments $[L, R]$ such that either $L + R = X$ or $L\cdot R = Y$.

For example, if $X = 5$ and $Y = 6$, then Chef's set is $S = \{[0, 5], [1, 4], [1, 6], [2, 3]\}$.

Given the integers $X$ and $Y$, can you help Chef find two non-intersecting segments from his set $S$? If it is not possible to find two such non-intersecting segments, print $-1$. If there are multiple possible answers, you may output **any** of them.

**Note:** Two segments are said to be non-intersecting if they have no number in common. For example,
- $[1, 4]$ and $[10, 42]$ are non-intersecting
- $[1, 4]$ and $[3, 10]$ are intersecting since they have $3$ and $4$ in common.
- $[1, 4]$ and $[4, 6]$ are intersecting since they have $4$ in common.

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line containing two space separated integers $X$ and $Y$.

---

## Output Format

- If there are non-intersecting segments, then output two lines:
    - In the first line, output two space-separated integers $L_1, R_1$ denoting the first segment.
    - In the second line, output two space-separated integers $L_2, R_2$ denoting the second segment.
- If there are no such segments, print $-1$ on a single line.

---

## Constraints

- $1 \leq T \leq 10$
- $1 \leq X, Y \leq 10^{12}$

---

## Examples

**Example 1**

**Input**

```text
3
4 24
1 1
3 30
```

**Output**

```text
1 3
4 6
-1
5 6
0 3
```

**Explanation**

**Test case $1$:** $1+3 = 4$ and $4 \cdot 6 = 24$, so $[1, 3]$ and $[4, 6]$ are both valid segments. Clearly, they also don't intersect.

**Test case $2$:** When $X = Y = 1$, we have $S = \{[0, 1], [1, 1]\}$. The only two segments intersect with each other, so there is no answer.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest Division 1](https://www.codechef.com/START50A/problems/SUMPRODSEG)

[Contest Division 2](https://www.codechef.com/START50B/problems/SUMPRODSEG)

[Contest Division 3](https://www.codechef.com/START50C/problems/SUMPRODSEG)

[Contest Division 4](https://www.codechef.com/START50D/problems/SUMPRODSEG)

Setter: [Tejas Pandey](https://www.codechef.com/users/tejas_adm)

Tester: [Nishank Suresh](https://www.codechef.com/users/iceknight1093), [Utkarsh Gupta](https://www.codechef.com/users/utkarsh_adm)

Editorialist: [Pratiyush Mishra](https://www.codechef.com/users/foxy7)

#
[](#difficulty-2)DIFFICULTY:

1713

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

A *segment* is a range of **non-negative** integers L, L + 1, L + 2, \ldots, R, denoted [L, R] where L \leq R.

Chef has a set S consisting of **all** segments [L, R] such that either L + R = X or L\cdot R = Y.

For example, if X = 5 and Y = 6, then Chef’s set is S = \{[0, 5], [1, 4], [1, 6], [2, 3]\}.

Given the integers X and Y, can you help Chef find two non-intersecting segments from his set S? If it is not possible to find two such non-intersecting segments, print -1. If there are multiple possible answers, you may output **any** of them.

**Note:** Two segments are said to be non-intersecting if they have no number in common. For example, [1, 4] and [10, 42] are non-intersecting, while [1, 4] and [4, 6] are not since they have 4 in common.

#
[](#explanation-5)EXPLANATION:

**Observation 1**: The smallest interval [L,R] such that L+R = X would be:

[\frac{X}{2},\frac{X}{2}], \;if\;X\;is\;even.

[\frac{X}{2},\frac{X}{2} + 1], \;if\;X\;is\;odd.

Any other interval would overlap the above one.

So we can choose one of the intervals as above and then loop through all possible intervals such that L \times R = Y and for each interval we check if the two intersect each other or not.

#
[](#time-complexity-6)TIME COMPLEXITY:

O(\sqrt{N}), for each test case.

#
[](#solution-7)SOLUTION:

[Editorialist’s Solution](http://p.ip.fi/UAZU)

[Setter’s Solution](http://p.ip.fi/r0mr)

[Tester1’s Solution](http://p.ip.fi/O2fM)

[Tester2’s Solution](http://p.ip.fi/wexn)

</details>
