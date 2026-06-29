# Remove One Element

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | REMONE |
| Difficulty Rating | 1700 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Sorting |
| Official Link | [REMONE](https://www.codechef.com/practice/course/2to3stars/LP2TO302/problems/REMONE) |

---

## Problem Statement

Alice has an array $A$ consisting of $N$ **distinct** integers. Bob takes exactly $N - 1$ elements from this array and adds a positive integer $X$ (i.e. $X \gt 0$) to each of these numbers and then shuffles them to form a new array $B$ of length $N - 1$.

You are given both arrays $A$ and $B$. You have to identify the value of $X$ chosen by Bob. If there are multiple possible values of $X$, print the **smallest** of them. It is guaranteed that for the given input, there exists at least one possible value of $X$.

**Note:** Since the input is large, prefer using fast input methods.

---

## Input Format

- The first line of input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- Each test case contains $3$ lines of input.
- The first line contains an integer $N$ - the length of array $A$.
- The second line contains $N$ space-separated integers $A_1, A_2, \dots, A_N$, denoting the array $A$.
- The third line contains $N - 1$ space-separated integers $B_1, B_2, \dots, B_{N-1}$, denoting the array $B$.

---

## Output Format

For each test case, output the value of $X$ chosen by Bob. In case there are multiple possible values of $X$, print the smallest of them.

---

## Constraints

- $1 \leq T \leq 7$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- $1 \leq B_i \leq 2 \cdot 10^9$
- $A_1, A_2, \dots, A_N$ are pairwise distinct.
- $B_1, B_2, \dots, B_{N-1}$ are pairwise distinct.
- Sum of $N$ over all test cases does not exceed $5 \cdot 10^5$.

---

## Examples

**Example 1**

**Input**

```text
3
4
1 4 3 8
15 8 11
2
4 8
10
2
2 4
3
```

**Output**

```text
7
2
1
```

**Explanation**

**Test case $1$:** Bob takes the elements $\{1, 4, 8\}$ and adds $7$ to them to obtain a new sequence $\{8, 11, 15\}$. There is no other value of $X$ that can be added to the elements of $A$ to get $B$.

**Test case $3$:** There is only one option with Bob to consider, i.e. to take element $\{2\}$ and add $1$ to it to get array $B$. If he takes element $\{4\}$, he will have to add $-1$ which is not allowed.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4
1 4 3 8
15 8 11
```

**Output for this case**

```text
7
```



#### Test case 2

**Input for this case**

```text
2
4 8
10
```

**Output for this case**

```text
2
```



#### Test case 3

**Input for this case**

```text
2
2 4
3
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#
[](#problem-link-1)PROBLEM LINK:

[Contest - Division 3](https://www.codechef.com/START10C/problems/REMONE)

[Contest - Division 2](https://www.codechef.com/START10B/problems/REMONE)

[Contest - Division 1](https://www.codechef.com/START10A/problems/REMONE)

#
[](#difficulty-2)DIFFICULTY:

SIMPLE

#
[](#prerequisites-3)PREREQUISITES:

[Greedy](https://www.geeksforgeeks.org/greedy-algorithms/)

#
[](#problem-4)PROBLEM:

You are given an array A of N distinct integers. You are also given an array B of N-1 distinct integers. Determine the smallest possible **positive integer** X such that B_i-X exists in A, for all valid i.

It is guaranteed that X exists.

#
[](#explanation-5)EXPLANATION:

Sort A and B. Then A_1 is the smallest element of A, and A_N the largest. Similarly with B too.

**Claim:** X is either B_1-A_1 or B_1-A_2.

Proof

Since array B was generated using N-1 elements of A, exactly one element of A was left out. Therefore, at least one of \{A_1,A_2\} was selected to generate array B.

Say A_1 was selected. Since X was added to each selected term to create array B,  A_1+X is still the smallest term, corresponding to the smallest term in B. Thus A_1+X=B_1 implies X=B_1-A_1.

A similar argument can be made for when *only* A_2 is selected.

All that remains now is to set X to each of the two possible values and validate if B_i-X exists in A, for all i. This can be done efficiently using hash tables.

If both values are possible, select the **smallest positive** value of the two.

#
[](#time-complexity-6)TIME COMPLEXITY:

Sorting A and B takes O(N\log N) each. Checking if B_i-X exists in array A, for all i, takes O(N) using hash tables.

The total time complexity per test case is thus:

O(2*(N\log N)+N+N) \approx O(N\log N)

#
[](#solutions-7)SOLUTIONS:

Editorialist’s solution can be found [here](https://www.codechef.com/viewsolution/50400003)

***Experimental:** For evaluation purposes, please rate the editorial (1 being poor and 5 excellent)*

- 1

- 2

- 3

- 4

- 5

0
voters

</details>
