# Missing Sums

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MISSSUMS |
| Difficulty Rating | 1374 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1200 to 1400 difficulty problems |
| Official Link | [MISSSUMS](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1400/problems/MISSSUMS) |

---

## Problem Statement

Given a positive integer $N$, construct an array $A$ containing $N$ $\textbf{distinct}$ elements such that the sum of any two elements in the array (not necessarily different) is not present in the array.

That is, there have to be $\textbf{no}$ such $i, j, k$ such that
- $1 \le i, j, k \le N$
- $A_i + A_j = A_k$.

The elements of the array $A$ should be in the range $[1, 10^5]$. It is guaranteed that such an array always exists under given constraints.

---

## Input Format

- First line of the input contains $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single positive integer $N$, the size of the array $A$.

---

## Output Format

For each test case, print $N$ space-separated integers in a single line, describing the contents of the array $A$.

---

## Constraints

- $1 \leq T \leq 50$
- $1 \leq N \leq 1000$

---

## Examples

**Example 1**

**Input**

```text
3
1
2
3
```

**Output**

```text
1
1 5
1 4 9
```

**Explanation**

**Test case 1:**
The only possible sum of pair of integers from $A$ is $1 + 1 = 2$ and it is not present in the array $A$.

**Test case 2:**
The only possible sums of pair of integers from $A$ are
- $1 + 1 = 2$
- $1 + 5 = 6$
- $5 + 5 = 10$

And none of these is present in the array $A$.

**Test case 3:**
The only possible sums of pair of integers from $A$ are
- $1 + 1 = 2$
- $1 + 4 = 5$
- $1 + 9 = 10$
- $4 + 4 = 8$
- $4 + 9 = 13$
- $9 + 9 = 18$

And none of these is present in the array $A$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
1
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
2
```

**Output for this case**

```text
1 5
```



#### Test case 3

**Input for this case**

```text
3
```

**Output for this case**

```text
1 4 9
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest - Division 3](https://www.codechef.com/COOK135C/problems/MISSSUMS)

[Contest - Division 2](https://www.codechef.com/COOK135B/problems/MISSSUMS)

[Contest - Division 1](https://www.codechef.com/COOK135A/problems/MISSSUMS)

#
[](#difficulty-2)DIFFICULTY:

SIMPLE

#
[](#problem-3)PROBLEM:

Given a positive integer N. Output *any* array A of length N, such that

-
A_i+A_j\ne A_k for all 1\le i,j,k\le N

-
1\le A_i\le 10^5 for all valid i.

#
[](#explanation-4)EXPLANATION:

The array [10^5-1,10^5-2,\dots,10^5-N] is a valid solution, **for the given constraints** on N.

Proof

It is trivial to show that the requirement 1\le A_i\le 10^5 holds for all valid i. All we are left to do is prove A_i+A_j\ne A_k for all valid i,j,k.

A_i+A_j=(10^5-i)+(10^5-j)=2\cdot10^5-i-j\\
\implies 2\cdot 10^5-i-j>2\cdot 10^5-2\cdot N> 10^5\\
\therefore A_i+A_j > 10^5 > A_k

Thus, we have shown the correctness of our solution.

#
[](#time-complexity-5)TIME COMPLEXITY:

O(N)

per test case.

#
[](#solutions-6)SOLUTIONS:

Editorialist’s solution can be found [here](https://www.codechef.com/viewsolution/54153291)

***Experimental:** For evaluation purposes, please rate the editorial (1 being poor and 5 excellent)*

- 1

- 2

- 3

- 4

- 5

0
voters

</details>
