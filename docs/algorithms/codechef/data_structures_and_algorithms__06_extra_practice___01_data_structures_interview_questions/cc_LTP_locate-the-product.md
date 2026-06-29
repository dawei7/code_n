# Locate The Product

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LTP |
| Difficulty Band | Data Structures Interview Questions |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [LTP](https://www.codechef.com/practice/course/interview-dsa/DSAPREP_03/problems/LTP) |

---

## Problem Statement

Chef has $N$ toys and each of his toys has its beauty - with the $i$-th toy having $a_i$ units of beauty. Chef is also obsessed with number $X$, so he wants to combine the beauty of 4 different of his toys to be exactly $X$. The beauty of combined toys is their product. Chef is doing his homework and doesn't have time to play with his toys, so he asks you to help him find 4 different toys whose combined beauty is exactly $X$. If there are multiple answers print the lexicographically minimal solution.

---

## Input Format

- First line will contain $T$, number of testcases. Then the testcases follow.
- First line of each testcase contains two integers $N$ and $X$.
- Second line of each testcase contains $N$ integers representing the beauty of each toys: $a_i$.

---

## Output Format

For each testcase, if the solution exists - output four pair-wise different space-separated integers $i,j,k,l$ such that combined beauty of $a_i, a_j, a_k, a_l$ is exactly $X$. If there are multiple answers output the lexicographically smallest solution.

If the solution doesn't exist - output $-1$.

---

## Constraints

- $1 \leq T \leq 100$
- $4 \leq N \leq 1000$
- The sum of $N$ over all test cases does not exceed $2000$
- $0 \leq X \leq 10^{18}$
- $0 \leq a_i \leq 10^9$

---

## Examples

**Example 1**

**Input**

```text
2
6 24
3 2 2 8 9 2
6 24
6 9 4 24 1 3
```

**Output**

```text
1 2 3 6
-1
```

**Explanation**

For the first test case we can pick numbers: $3, 2, 2, 2$ and their product is $24$ as requested. Their indices are obviously $1, 2, 3, 6$.

In the second test case we cannot pick four different indices so the product of the elements with those indices is $24$.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 24
3 2 2 8 9 2
```

**Output for this case**

```text
1 2 3 6
```



#### Test case 2

**Input for this case**

```text
6 24
6 9 4 24 1 3
```

**Output for this case**

```text
-1
```


