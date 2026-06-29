# Count Beautiful Pairs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HSH09 |
| Difficulty Rating | 932 |
| Difficulty Band | Hashing |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to Hashing |
| Official Link | [HSH09](https://www.codechef.com/learn/course/hashing/HASH02/problems/HSH09) |

---

## Problem Statement

You have an array $A$ of $N$ integers. \
A pair of indices $(i, j)$ is called Beautiful if $A_i = A_j^2$ and $1 \leq i \lt j \leq N$.

Count the number of Beautiful Pairs in the given array.

### Task
Use the Hash Function given in the IDE to index the Hash array.

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

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Count Beautiful Pairs in Hashing](https://www.codechef.com/learn/course/hashing/HASH02/problems/HSH09)

### [](#problem-statement-1)Problem Statement:

You have an array A of N integers. A pair of indices `(i,j)` is called Beautiful if A_i = A_j^2 and 1≤i<j≤N. Count the number of Beautiful Pairs in the given array.

**Note:** You have to use the hash function given in the `IDE`

### [](#approach-2)Approach:

**1. Hash Function**:

- A hash function f(x)=x mod M is used to map values to a hash array of size M. Here, M=999983 is a large prime number to minimize collisions in the hash array.

**2. Counting Beautiful Pairs**:

- Loop through each element of the array:

- For each element `A[i]`, check if its square `A[i]^2` is less than `MX` (which is 10^9).

- If true, look up how many times `A[i]^2` has been seen before (i.e., check Hash[f(a_i^2)] to see how many occurrences exist).

- Increase the count, as it represents the number of pairs that can be formed with the current element.

- Update the hash array with the current element `A[i]` by incrementing Hash[f(a[i])]

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(N)` due to a single loop through the array.

- **Space Complexity:** `O(M)` Size of hash array

</details>
