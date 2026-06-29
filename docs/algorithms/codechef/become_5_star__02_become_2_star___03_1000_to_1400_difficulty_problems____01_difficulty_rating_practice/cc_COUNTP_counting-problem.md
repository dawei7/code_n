# Counting Problem

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COUNTP |
| Difficulty Rating | 1065 |
| Difficulty Band | 1000 to 1400 difficulty problems |
| Path | Become 5 star |
| Lesson | 1000 to 1200 difficulty problems |
| Official Link | [COUNTP](https://www.codechef.com/practice/course/1-star-difficulty-problems/DIFF1200/problems/COUNTP) |

---

## Problem Statement

You are given an array $A = [A_1, A_2, \ldots, A_N]$.

Is it possible to partition $A$ into two non-empty [subsequences](https://en.wikipedia.org/wiki/Subsequence) $S_1$ and $S_2$ such that $sum(S_1) \times sum(S_2)$ is **odd**?

Here, $sum(S_1)$ denotes the sum of elements in $S_1$, and $sum(S_2)$ is defined similarly.

**Note:** $S_1$ and $S_2$ must *partition* $A$, that is:
- $S_1$ and $S_2$ must be non-empty
- Every element of $A$ must be in either $S_1$ or $S_2$
- $S_1$ and $S_2$ must be disjoint (in terms of which indices their subsequences represent)

---

## Input Format

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of 2 lines of input.
    - The first line of each test case contains a single integer $N$, the size of the array.
    - The next line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$: the elements of the array.

---

## Output Format

For each test case, print on a new line the answer: `YES` if the array can be partitioned into two subsequences satisfying the condition, and `NO` otherwise.

Each character of the output may be printed in either uppercase or lowercase, i.e, `YES`, `yes`, `YEs`, and `yEs` will all be treated as equivalent.

---

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ across all test cases won't exceed $10^6$.

---

## Examples

**Example 1**

**Input**

```text
4
4
1 1 2 2
6
1 2 4 6 8 10
2
3 5
3
1 3 5
```

**Output**

```text
YES
NO
YES
NO
```

**Explanation**

**Test case $1$:** We have $A = [\underline{1}, 1, \underline{2}, 2]$. Let $S_1$ be the underlined elements and $S_2$ be the other ones. $sum(S_1) \times sum(S_2) = 3\times 3 = 9$.

**Test case $2$:** It can be proved that no partition of $A$ into $S_1, S_2$ satisfies the condition.

**Test case $4$:** Choose $S_1 = \{3\}, S_2 = \{5\}$.

**Test case $4$:** It can be proved that no partition of $A$ into $S_1, S_2$ satisfies the condition.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 1 2 2
```

**Output for this case**

```text
YES
```



#### Test case 2

**Input for this case**

```text
6
1 2 4 6 8 10
```

**Output for this case**

```text
NO
```



#### Test case 3

**Input for this case**

```text
2
3 5
```

**Output for this case**

```text
YES
```



#### Test case 4

**Input for this case**

```text
3
1 3 5
```

**Output for this case**

```text
NO
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Practice](https://www.codechef.com/problems/COUNTP)

[Contest: Division 1](https://www.codechef.com/START67A/problems/COUNTP)

[Contest: Division 2](https://www.codechef.com/START67B/problems/COUNTP)

[Contest: Division 3](https://www.codechef.com/START67C/problems/COUNTP)

[Contest: Division 4](https://www.codechef.com/START67D/problems/COUNTP)

***Author:*** [Kunj Rakesh Patel](https://www.codechef.com/users/kunjrp_1402)

***Testers:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093), [Tejas Pandey](https://www.codechef.com/users/tejas10p)

***Editorialist:*** [Nishank Suresh](https://www.codechef.com/users/IceKnight1093)

#
[](#difficulty-2)DIFFICULTY:

1065

#
[](#prerequisites-3)PREREQUISITES:

None

#
[](#problem-4)PROBLEM:

Given an array A of length N, it is possible to partition it into two non-empty subsequences such that the product of their sums is odd?

#
[](#explanation-5)EXPLANATION:

Suppose we were able to split A into two subsequences S_1 and S_2 satisfying the given condition.

Then, note that we want sum(S_1)\times sum(S_2) to be odd, which is only possible when sum(S_1) and sum(S_2) are both odd.

Further, S_1 and S_2 partition A, and so sum(S_1) + sum(S_2) = sum(A).

Since sum(S_1) and sum(S_2) must both be odd, sum(A) must be even.

So, if sum(A) is odd the answer is immediately “No”.

From now on, let’s consider sum(A) to be even.

If A contains only even numbers, then any subsequence also has even sum so splitting into two subsequences with odd sum is impossible.

On the other hand, if A contains an odd number, say x, then we can simply choose S_1 = \{x\} and S_2 to be all the other elements.

S_1 obviously has odd sum, and since sum(A) is even, S_2 also has odd sum and we’re done.

So, the answer is “Yes” if and only if sum(A) is even *and* A contains at least one odd number.

#
[](#time-complexity-6)TIME COMPLEXITY:

\mathcal{O}(N) per testcase.

#
[](#code-7)CODE:

Editorialist's code (Python)
``for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print('Yes' if sum(a)%2 == 0 and sum(x for x in a if x%2 == 1) else 'No')
``

</details>
