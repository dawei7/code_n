# XOR with Subset

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | XORSUB |
| Difficulty Rating | 1879 |
| Difficulty Band | Jump from 2* to 3* |
| Path | Become 5 star |
| Lesson | Bit Manipulation |
| Official Link | [XORSUB](https://www.codechef.com/practice/course/2to3stars/LP2TO305/problems/XORSUB) |

---

## Problem Statement

You have an array of integers **A1, A2, ..., AN**. The function **F(P)**, where **P** is a [subset](http://en.wikipedia.org/wiki/Subset) of **A**, is defined as the [XOR](http://en.wikipedia.org/wiki/Exclusive_or) (represented by the symbol **⊕**) of all the integers present in the subset. If **P** is empty, then **F(P)**=0.

Given an integer **K**, what is the maximum value of **K** **⊕** **F(P)**, over all possible subsets **P** of **A**?

### Input

The first line contains **T**, the number of test cases. Each test case consists of **N** and **K** in one line, followed by the array **A** in the next line.

### Output

For each test case, print the required answer in one line.

### Constraints

- **1** ≤ **T** ≤ **10**

- **1** ≤ **K**, **Ai** ≤ **1000**

- Subtask 1 (30 points):**1** ≤ **N** ≤ **20**

- Subtask 2 (70 points):**1** ≤ **N** ≤ **1000**

---

## Examples

**Example 1**

**Input**

```text
1
3 4
1 2 3
```

**Output**

```text
7
```

**Explanation**

Considering all subsets:

F({}) = 0 ? 4 **?** 0 = 4

F({1}) = 1 ? 4 **?** 1 = 5

F({1,2}) = 3 ? 4 **?** 3 = 7

F({1,3}) = 2 ? 4 **?** 2 = 6

F({1,2,3}) = 0 ? 4 **?** 0 = 4

F({2}) = 2 ? 4 **?** 2 = 6

F({2,3}) = 1 ? 4 **?** 1 = 5

F({3}) = 3 ? 4 **?** 3 = 7

Therefore, the answer is 7.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/problems/XORSUB)

[Contest](http://www.codechef.com/DEC14/problems/XORSUB)

**Author:** [Lalit Kundu](http://www.codechef.com/users/darkshadows)

**Tester 1:** [Minako Kojima](http://www.codechef.com/users/xiaodao)

**Tester 2:** [Shiplu Hawlader](http://www.codechef.com/users/shiplu)

**Editorialist:** [Pawel Kacprzak](http://www.codechef.com/users/pkacprzak)

### DIFFICULTY:

SIMPLE

### PREREQUISITES:

DP, bits

### PROBLEM:

You are given an array A of N integers and an integer K. Your task is to return the maximum possible value of F§ xor K, where P is a subset of A and F§ is defined as a xor of all values in P. If P is empty, then F§ = 0.

### QUICK EXPLANATION:

Since each element of A has a value of at most 1000, we can use dynamic programming dp[i][j] := 1 if and only if there exists a subset P of A[1…i] such that F§ = j. In order to get the result, we return max 1 <= j <= 1023 { dp[n][j] * (j ^ k) }

### EXPLANATION:

Let dp[i][j] := 1 if and only if there exists a subset P of A[1…i] such that F§ = j, otherwise 0

The first observation is that F§ can be at most 1023 since any input number is at most 1000.

Initially we set all dp[i][j] := 0.

Next, we set dp[0][0] := 1, since a xor of the empty set is 0.

We iterate over all elements of A from left to right. For each A[i], we iterate over all possible values of the xor function i.e. a range from 0 to 1023 inclusive and update these values as follows:

``for i = 1 to N:
    for j = 0 to 1023:
        dp[i][j] = dp[i - 1][j] | dp[i - 1][j ^ a[i]]
``

The reason for this is that if there exists a subset P of A[1…i - 1] such that F§ = j then there exists also a subset of A[1…i] such that F§ = j or if there exists a subset P of A[1…i - 1] such that F§ = j ^ a[i], then F§ ^ a[i] = j, so there exists a subset P’ of A[1…i] such that F(P’) = j

At the end we have dp[n][j] for all 0 <= j <= 1023, and we can return a maximum value of dp[n][j] * (j ^ k) for all j.

Time Complexity:

The time complexity per one testcase is O(N * 1023);

### AUTHOR’S AND TESTER’S SOLUTIONS:

To be uploaded soon.

### RELATED PROBLEMS:

To be uploaded soon.

</details>
