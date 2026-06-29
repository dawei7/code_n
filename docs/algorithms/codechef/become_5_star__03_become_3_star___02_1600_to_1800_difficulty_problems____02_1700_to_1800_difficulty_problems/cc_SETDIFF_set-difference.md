# Set Difference 

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SETDIFF |
| Difficulty Rating | 1729 |
| Difficulty Band | 1600 to 1800 difficulty problems |
| Path | Become 5 star |
| Lesson | 1700 to 1800 difficulty problems |
| Official Link | [SETDIFF](https://www.codechef.com/practice/course/3-star-difficulty-problems/DIFF1800/problems/SETDIFF) |

---

## Problem Statement

Churu is working as a data scientist in Coderpur. He works on a lot of data on the daily basis. One day, he found an interesting problem, which was very easy to solve for small data but was getting more complex with increasing number of data points. So, Churu needs your help in solving this problem.

 Given a set **S** of **N** non-negative integers (Some integers might occur more than once in the set), find out the value of **SETDIFF(S)**.

Where **max(s)** represents the maximum value in set **s** whereas **min(s)** represents the minimum value in the set **s**.
As value of ** SETDIFF(S)** can be very large, print it modulo ** (109 + 7) **.

There might be repeated values in the set. For set **S** = **{1,2,2}**, consider that first 2 is not same as the second 2 and there will be two different subsets **{1,2}**. See last sample case for the more clarifications.

### Input

- First line of input contains an integer **T** denoting number of test cases.

- For each test case, first line will contain an integer **N** denoting number of elements in set **S**.

-  Next line contains **N** space separated integers denoting the set **S**.

### Output
For each test case, print a single integer representing the answer of that test case.

### Note

Two subsets will be called different if there exists an index **i** such that **S[i]** occurs in one of the subset and not in another.

### Constraints

**Subtask #1: 20 points**

- **1 ≤ T  ≤ 5, 1 ≤ N  ≤ 1000,  0 ≤ value in set ≤ 109**

**Subtask #2: 25 points**

- **1 ≤ T  ≤ 5, 1 ≤ N  ≤ 105,  0 ≤ value in set ≤ 1000**

**Subtask #3: 55 points**

- **1 ≤ T  ≤ 5, 1 ≤ N  ≤ 105,  0 ≤ value in set ≤ 109**

---

## Examples

**Example 1**

**Input**

```text
4
2
1 2
3
1 2 3
4
1 2 3 4
3
1 2 2
```

**Output**

```text
1
6 
23
3
```

**Explanation**

For first case answer will be 2-1 = 1.

For the second case:

Subset = {1}, max(s)-min(s) = 0.
Subset = {2}, max(s)-min(s) = 0.
Subset = {3}, max(s)-min(s) = 0.
Subset = {1,2}, max(s)-min(s) = 1.
Subset = {2,3}, max(s)-min(s) = 1.
Subset = {1,3}, max(s)-min(s) = 2.
Subset = {1,2,3}, max(s)-min(s) = 2.
So the output will be 1+1+2+2 = 6.

In the last case, there are three subsets, {1,2}, {1,2} and {1,2,2} having max(s) - min(s) = 1 for each.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
1 2
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
3
1 2 3
```

**Output for this case**

```text
6
```



#### Test case 3

**Input for this case**

```text
4
1 2 3 4
```

**Output for this case**

```text
23
```



#### Test case 4

**Input for this case**

```text
3
1 2 2
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### PROBLEM LINK:

[Practice](http://www.codechef.com/MAY15/problems/SETDIFF)

[Contest](http://www.codechef.com/MAY15/problems/SETDIFF)

**Author:** [Amit Kumar Pandey](http://www.codechef.com/users/amitpandeykgp)

**Tester:** [Kevin Atienza](http://www.codechef.com/users/kevinsogo)

**Editorialist:** [Ajay K. Verma](http://www.codechef.com/users/djdolls)

**Russian Translator:** [Sergey Kulik](http://www.codechef.com/users/xcwgf666)

**Mandarian Translator:** [Gedi Zheng](http://www.codechef.com/users/stzgd)

### DIFFICULTY:

Easy

### PREREQUISITES:

Basic maths

### PROBLEM:

Given a multiset consisting of N numbers, find the sum of difference between maximum and minimum element of each subset.

### QUICK EXPLANATION:

Compute the sum of maximum element of each set, and the sum of minimum element of each set separately, and then subtract the latter from the former to get the answer. The sum of maximum (minimum) element of each subset can be computed easily by iterating through the elements of the multiset in sorted order (see explanation below).

### EXPLANATION:

We are given a multiset S consisting of N numbers, and we need to compute the sum of difference between maximum and minimum element of each subset of S, i.e.,

T = \sum (max(s) - min(s)), where sum goes over all subsets s of S.

Equivalently,

T = (\sum max(s)) - (\sum min(s))

In other words, we can compute the sum of maximum element of each subset, and the sum of minimum element of each subset separately, and then compute their difference.

### Sum of Minimum Elements of All Subsets:

Let us say that the elements of S in non-decreasing order are \{a_1, a_2, \cdots, a_N\}. Now, we can partition the subsets of S into following categories:

-
**subsets containing element a_1:**

These subsets can be obtained by taking any subset of \{a_2, a_3, \cdots, a_N\}, and then adding a_1 into it. Number of such subsets will be 2^{N - 1}, and they all have a_1 as their minimum element.

-
**subsets not containing element a_1, but containing a_2:**

These subsets can be obtained by taking any subset of \{a_3, a_4, \cdots, a_N\}, and then adding a_2 into it. Number of such subsets will be 2^{N - 2}, and they all have a_2 as their minimum element.

\cdots

i) **subsets not containing elements a_1, a_2, \cdots a_{i - 1}, but containing a_i:**

These subsets can be obtained by taking any subset of \{a_{i + 1}, a_{i + 2}, \cdots, a_N\}, and then adding a_i into it. Number of such subsets will be 2^{N - i}, and they all have a_i as their minimum element.

\cdots

It can be seen that the above iteration is complete, i.e., it considers each subset exactly once. Hence, the sum of minimum element of all subsets will be:

P = a_1  2^{N - 1} + a_2  2^{N - 2} + \cdots + a_i  2^{N - i} + \cdots + a_N  2^0

P = a_N + 2  (a_{N - 1} + 2  (a_{N - 2} + 2  (\cdots 2  (a_2 + 2  a_1) \cdots))))

This sum can be computed easily in linear time.

In a similar way we can compute the sum Q of maximum element of all subsets of S. The only difference is that we need to iterate the elements of S in non-increasing order. Finally, the answer of our problem will be (Q - P). The following snippet shows how to compute P and Q

`
// sort the array in increasing order.
sort(S.begin(), S.end());

P = 0;
Q = 0;

for (int i = 0; i < N; ++i) {
  P = (2 * P + A[i]) % mod;
  Q = (2 * Q + A[N - 1 - i]) % mod;
}

return (Q + mod - P) % mod;

`

#### Time Complexity:

O (N \log N)

### AUTHOR’S AND TESTER’S SOLUTIONS:

Author’s solution will be put up soon.

Tester’s solution will be put up soon.

</details>
