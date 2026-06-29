# Maximum Sum of K Elements

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SLDW0102 |
| Difficulty Rating | 932 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Sliding Window |
| Official Link | [SLDW0102](https://www.codechef.com/practice/course/two-pointers/SLIDINGWINDO/problems/SLDW0102) |

---

## Problem Statement

You are given an array $A$ containing $N$ elements and an integer $K$. You have to find the subarray with the maximum sum among all the K-sized sub-arrays and output this maximum sum.

This is a perfect example of a question that can be efficiently solved using the sliding window approach.
Normally, we would calculate the sum of all K-sized sub-arrays which would have the time complexity of $O(N)$.
But, using the Sliding Window approach we can assume the K-sized subarray to be a window. Now we just need to calculate the sum of the first window as the sum of the next window can be derived from the previous sum by subtracting the first element and adding the next element.

For example, let's take an array $A = [1, 2, 3, 4, 5, 6, 7]$ and $K = 3$.

- Let's calculate the sum of the first window of three elements. $1+2+3 = 6$
- Now the next window will have element ${2, 3, 4}$.
- Compared to the previous window the first element $(1)$ is removed and the next element $(4)$ is added.
- So, we can calculate the next window's sum by subtracting $1$ and adding $4$ to the sum of the previous window.
- Thus, the sum of the next window will be $6-1+4 = 9$

Solve the above question using the Sliding Window approach

---

## Input Format

- The first line of the input contains a single integer $N$ and $K$, denoting the length of the array $A$ and the length of the sub-array.
- The second line of the input contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — denoting the array $A$.

---

## Output Format

- Output the maximum sum.

---

## Constraints

- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- $2 \leq K \leq N$

---

## Examples

**Example 1**

**Input**

```text
10 3
9 8 2 4 1 9 9 5 1 8
```

**Output**

```text
23
```

**Explanation**

The subarray {9, 9, 5} has the maximum sum.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Statement - [Maximum Sum of K Elements](https://www.codechef.com/practice/course/two-pointers/SLIDINGWINDO/problems/SLDW0102)

### [](#problem-statement-1)Problem Statement

You are given an array A containing N elements and an integer K. You have to find the subarray with the maximum sum among all the K-sized sub-arrays and output this maximum sum.

This is a perfect example of a question that can be efficiently solved using the sliding window approach.

Normally, we would calculate the sum of all K-sized sub-arrays which would have the time complexity of O(N).

But, using the Sliding Window approach we can assume the K-sized subarray to be a window. Now we just need to calculate the sum of the first window as the sum of the next window can be derived from the previous sum by subtracting the first element and adding the next element.

### [](#approach-2)Approach

The code idea involves using a **sliding window** to efficiently calculate the maximum sum of **K-sized** subarrays. After reading N and K, we initialize the sum with the first K elements and set it as the maximum sum. As we slide the window by updating the sum (subtracting the leftmost element and adding the next element), we continually check and update the maximum sum. This approach ensures we only traverse the array once, making it optimal for this problem.

### [](#time-complexity-3)Time Complexity

The time complexity of the solution is O(N).

### [](#space-complexity-4)Space Complexity

The space complexity of the solution is O(1).

</details>
