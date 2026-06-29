# Count Beautiful Pairs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HSH05 |
| Difficulty Rating | 932 |
| Difficulty Band | Hashing |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to Hashing |
| Official Link | [HSH05](https://www.codechef.com/learn/course/hashing/HASH01/problems/HSH05) |

---

## Problem Statement

You have an array $A$ of $N$ integers. \
A pair of indices $(i, j)$ is called Beautiful if $A_i = A_j^2$ and $1 \leq i \lt j \leq N$.

Count the number of Beautiful Pairs in the given array.

### Task
Try to solve this problem in $N$ time complexity with Hash array.

---

## Input Format

- The first line of the input contains a single integer $N$, denoting the length of array $A$.
- The second line of the input contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — denoting the array $A$.

---

## Output Format

- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^4$

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

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Count Beautiful Pairs in Hashing](https://www.codechef.com/learn/course/hashing/HASH01/problems/HSH05)

### [](#problem-statement-1)Problem Statement:

You have an array A of N integers. A pair of indices`(i,j)` is called Beautiful if A_i = A_j^2 and 1≤i<j≤N.

Count the number of Beautiful Pairs in the given array. Your task is to do it in `O(N)` time complexity using **Hash array**.

### [](#approach-2)Approach:

**1. Hash Array Initialization**:

- Initialize a hash array `Hash` of size 10,001 (to cover all possible values of A[i] from 1 to 10,001) to count occurrences of each number.

**2. Counting Beautiful Pairs**:

- Iterate through each element of the array:

- For each element A[i], calculate its square A[i] * A[i].

- Check if this square is less than the maximum size of the hash array (to *prevent overflow*).

- If it is present, add the count of occurrences of A[i]^2 from the hash array to the result.

- Update the hash array with the current element A[i].

### [](#complexity-3)Complexity:

- **Time Complexity:**  `O(N)`  Iterate through the whole array to compute the hash.

- **Space Complexity:** `O(M)`, `M` is the size of the hash array declared. Here we have used the hash size of `10^4`. So space complexity will be `O(M)-> O(10^4)`.

</details>
