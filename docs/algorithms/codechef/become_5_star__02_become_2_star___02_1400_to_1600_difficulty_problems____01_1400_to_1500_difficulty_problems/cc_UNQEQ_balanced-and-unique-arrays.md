# Balanced and Unique Arrays

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | UNQEQ |
| Difficulty Rating | 1431 |
| Difficulty Band | 1400 to 1600 difficulty problems |
| Path | Become 5 star |
| Lesson | 1400 to 1500 difficulty problems |
| Official Link | [UNQEQ](https://www.codechef.com/practice/course/2-star-difficulty-problems/DIFF1500/problems/UNQEQ) |

---

## Problem Statement

For a positive, $\textbf{even}$ integer $N$, we call a pair of arrays $A$ and $B$ to be **interesting** if they satisfy the following conditions :

- $|A| = |B| = N/2$ i.e. the length of array $A$ is equal to the length of array $B$.

- Each integer from $1$ to $N$ occurs exactly once in exactly one of the arrays.

- The $i^{th}$ prefix sum of $A$ is not equal to $i^{th}$ prefix sum of $B$ for all $1 \leq i \leq N/2-1$. \
Formally, $\displaystyle \sum_{j = 1}^{i} A_j$ != $ \displaystyle \sum_{j = 1}^{i} B_j$ for all $1 \leq i \leq N/2 - 1$

- Sum of all elements in $A$ is equal to sum of all elements in $B$ i.e. $\displaystyle \sum_{j = 1}^{N/2} A_j = \sum_{j = 1}^{N/2} B_j$

You are given a positive, even integer $N$. If there exists an **interesting** pair of arrays, then print "YES" followed by an interesting pair for this given $N$. If there exists multiple **interesting** pairs of arrays for given $N$, you can print any. Print "NO" in a single line if no such pair exists.

---

## Input Format

- First line of input will contain $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, the integer $N$.

---

## Output Format

For each test case, if there exists an **interesting** pair of arrays, say $(A, B)$, then in the first line print "YES", in the second line print array $A$ separated by spaces, and in third line print array $B$ separated by spaces. Print "NO" in a single line if no such pair exists. If there are multiple answers, print any of them.

---

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $N$ is guaranteed to be even.
- Sum of $N$ over all test cases doesn't exceed $10^6$

---

## Examples

**Example 1**

**Input**

```text
2
2
4
```

**Output**

```text
NO
YES
1 4
2 3
```

**Explanation**

**Test case 2:** Consider $A = [1, 4]$ and $B = [2, 3]$. Every integer from $1$ to $4$ occurs exactly once in exactly one of the arrays. Also, $1$st prefix sum of $A$ is not equal to $1$st prefix sum of $B$ ($1 \neq 2$). And sum of the elements is equal to $5$ for both arrays. So, $(A, B)$ is an interesting pair.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest - Division 3](https://www.codechef.com/LTIME100C/problems/UNQEQ)

[Contest - Division 2](https://www.codechef.com/LTIME100B/problems/UNQEQ)

[Contest - Division 1](https://www.codechef.com/LTIME100A/problems/UNQEQ)

#
[](#difficulty-2)DIFFICULTY:

SIMPLE

#
[](#problem-3)PROBLEM:

Arrays A and B form an **interesting** pair if

- sizes of both arrays are equal,

- each number 1,2,\dots,N occurs in exactly one of the arrays,

- sum of elements in A is equal to the sum of elements in B, and

- sum of first i elements of A is unequal to the sum of first i elements of B, for all 1\le i< \frac N 2.

Determine if any **interesting** pair exists.

#
[](#explanation-4)EXPLANATION:

**Claim:** No **interesting** pair exists when N is not divisible by 4.

Proof

We prove by contradiction.

Let A and B form an  **interesting** pair for some N not divisible by 4. The combined sum of their elements is

1+2+\dots+N = \frac{N*(N+1)}{2}

Now, since the sum of elements of A is equal to the sum of elements of B, the sum of elements of each array is equal to

\frac{N*(N+1)}{2}\div2=\frac{N*(N+1)}{4}

It is easy to deduce that the above equation is non-integral when N\equiv 0 \pmod 2 and N\not\equiv 0 \pmod 4. But since the elements of the arrays are integral, their sum is also supposed to be integral.

A contradiction and we are done.

Let’s only consider the case where N is divisible by 4. I claim that an **interesting** pair always exists.

Hint 1

Experimenting helps a lot. Try formulating a solution for N=8. Do you observe any pattern?

Hint 2

A solution has been given below, for N=8.

A = [1,3,6,8] \\
B = [2,4,5,7]

Can you generalise the above solution for all valid N?

Generalised solution

Consider the following sequences for A and B (each array has been divided into two equal length parts for clarity):

A = [1,3,\dots,N/2-1]+[N/2+2,\dots,N-2,N]\\
B = [2,4,\dots,N/2]+[N/2+1,\dots,N-3,N-1]

I claim they form an **independent** pair, so they should satisfy the 3 constraints given in the problem (or shall I call it question? )

Proving |A|=|B| and \sum A = \sum B in the above sequences is trivial (and left to the reader as an exercise). All we are left to show is that the sum of first i elements of A is unequal to the sum of first i elements of B, for all 1\le i< \frac N 2.

Proof of criteria 3

From the alternating pattern of elements in A and B, it is easy to see that, for all 1\le i \le \frac N 4

\sum_x^iA_x+i=\sum_x^i B_x

and that for all \frac N 4 < i \le \frac N 2

\sum_x^i A_x + (\frac N 2-i) = \sum_x^iB_x

Now, for all 1\le i < \frac N 2, the extra term on the LHS is non-zero, which implies that the sum of first i elements of A is unequal to the sum of first i elements of B.

Thus proved.

#
[](#time-complexity-5)TIME COMPLEXITY:

Since we iterate from 1 to N once to create the output, the total time complexity is

O(N)

per test case.

#
[](#solutions-6)SOLUTIONS:

Editorialist’s solution can be found [here](https://www.codechef.com/viewsolution/51617956).

***Experimental:** For evaluation purposes, please rate the editorial (1 being poor and 5 excellent)*

- 1

- 2

- 3

- 4

- 5

0
voters

</details>
