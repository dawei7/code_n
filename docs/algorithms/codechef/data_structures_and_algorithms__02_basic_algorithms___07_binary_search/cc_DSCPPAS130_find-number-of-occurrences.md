# Find Number of Occurrences

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSCPPAS130 |
| Difficulty Band | Binary Search |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to binary search |
| Official Link | [DSCPPAS130](https://www.codechef.com/learn/course/binary-search/BSVARIATIONS/problems/DSCPPAS130) |

---

## Problem Statement

You are given a sorted array containing $N$ integers and a number $target$. Complete the given function to find the number of occurrences of target in the given array.

***Note: You need to solve this problem in O(log(n)) complexity.***

---

## Input Format

- The first line contains an integer `n` (1 <= n <= 10^5), the size of the array.
- The second line contains `n` space-separated integers representing the sorted array elements.
- The third line contains an integer `target` for which the occurrences need to be found.

---

## Output Format

- Return the number of occurrences of the target value in the array.

---

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq M \leq N\cdot(N-1)/2$
- $1 \leq u_i, v_i \leq N$
- $u_i \neq v_i$ for each $1 \leq i \leq M$.
- The sum of $N$ over all test cases won't exceed $100$.

---

## Examples

**Example 1**

**Input**

```text
8
1 2 3 5 5 5 7 8
5
```

**Output**

```text
3
```

**Explanation**

- In this case, the target is 5, and the array is {1, 2, 3, 5, 5, 5, 7, 8}. The number of occurrences of 5 is 3.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Find Number of Occurrences in Binary Search](https://www.codechef.com/learn/course/binary-search/BSVARIATIONS/problems/DSCPPAS130)

### [](#problem-statement-1)Problem Statement:

You are given a sorted array containing N integers and a number target. Complete the given function to find the **number of occurrences** of target in the given array.

**Note**: You need to solve this problem in `O(log n)` complexity.

### [](#approach-2)Approach:

To find the number of occurrences of a target in a sorted array in `O(log n)` time, we can make use of binary search. We’ll break this task into two parts:

- **Find the first occurrence** of the target using binary search.

- **Find the last occurrence** of the target using binary search.

Once we know both the first and last occurrence indices, the number of occurrences of the target is simply the difference between these indices plus one.

**Steps:**

- **For First Occurrence**:

- Perform a binary search to find the first index where the target appears.

- Keep track of the index and move towards the left half to ensure it is the first occurrence.

- **For Last Occurrence**:

- Similarly, perform a binary search to find the last index where the target appears.

- Move towards the right half to ensure it is the last occurrence.

- **Calculate Occurrences**: Once the first and last occurrence indices are known, the number of occurrences is `last_occurrence - first_occurrence + 1`. If the target is not found, return `0`.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(log n)` Using Binary search

- **Space Complexity:** `O(1)` No extra space needed.

</details>
