# Count Beautiful Pairs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HSH12 |
| Difficulty Rating | 932 |
| Difficulty Band | Hashing |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to Hashing |
| Official Link | [HSH12](https://www.codechef.com/learn/course/hashing/HASH02/problems/HSH12) |

---

## Problem Statement

You have an array $A$ of $N$ integers. \
A pair of indices $(i, j)$ is called Beautiful if $A_i = A_j^2$ and $1 \leq i \lt j \leq N$.

Count the number of Beautiful Pairs in the given array.

### Task
Use the built-in hashing data structure to solve this task.

---

## Input Format

- The first line of the input contains a single integer $N$, denoting the length of array $A$.
- The second line of the input contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — denoting the array $A$.

---

## Output Format

- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$

---

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ across all test cases does not exceed $10^5$

---

## Examples

**Example 1**

**Input**

```text
4
4 4 2 2
```

**Output**

```text
4
```
