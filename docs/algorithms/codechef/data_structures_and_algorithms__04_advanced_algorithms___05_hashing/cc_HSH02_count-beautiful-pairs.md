# Count Beautiful Pairs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HSH02 |
| Difficulty Rating | 932 |
| Difficulty Band | Hashing |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to Hashing |
| Official Link | [HSH02](https://www.codechef.com/learn/course/hashing/HASH01/problems/HSH02) |

---

## Problem Statement

You have an array $A$ of $N$ integers. \
A pair of indices $(i, j)$ is called Beautiful if $A_i = A_j^2$ and $1 \leq i \lt j \leq N$.

Count the number of Beautiful Pairs in the given array.

### Task
Try to solve this problem in $N^2$ time complexity.

---

## Input Format

- The first line of the input contains a single integer $N$, denoting the length of array $A$.
- The second line of the input contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — denoting the array $A$.

---

## Output Format

Output the number of Beautiful Pairs in the given array $A$.

---

## Constraints

- $2 \leq N \leq 10^3$
- $1 \leq A_i \leq 10^4$

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

**Example 2**

**Input**

```text
3
1 2 2
```

**Output**

```text
0
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Count Beautiful Pairs in Hashing](https://www.codechef.com/learn/course/hashing/HASH01/problems/HSH02)

### [](#problem-statement-1)Problem Statement:

You have an array A of N integers. A pair of indices `(i,j)` is called Beautiful if

A_i = A_j^2, 1≤i<j≤N. Count the number of **Beautiful Pairs** in the given array.

### [](#approach-2)Approach:

- It uses a nested loop structure to examine each unique pair of elements in the array.

- For each pair `(i,j)`, it checks whether the condition `A[i] = A[j]^2` holds.

- Each time the condition is satisfied, a counter is incremented to keep track of the number of Beautiful Pairs found.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(N^2)` We are using two nested loops.

- **Space Complexity:** `O(1)` No extra space is used.

</details>
