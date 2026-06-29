# Finding the Subarray with Minimum Sum of Size K

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SLDW0105 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Sliding Window |
| Official Link | [SLDW0105](https://www.codechef.com/practice/course/two-pointers/SLIDINGWINDO/problems/SLDW0105) |

---

## Problem Statement

You are given an array of integers and you need to find a subarray of size $K$ that has the minimum sum in all the subarray of size $K$.

---

## Input Format

- The first line contains two integers $N$ and $K$, representing the size of the array and the size of the subarray, respectively.
- The second line contains $N$ space-separated integers representing the elements of the array.

---

## Output Format

Output a single integer representing the minimum sum of a subarray of size $K$.

---

## Constraints

- $ 1 \leq N \leq 10^5 $
- $ 1 \leq K \leq N $
- $ 0 \leq |A[i]| \leq 10^9 $

---

## Examples

**Example 1**

**Input**

```text
10 3
1 2 3 4 5 6 7 8 9 10
```

**Output**

```text
6
```

**Explanation**

The subarray with the minimum sum of size 3 is [1, 2, 3], and the sum is 6.

**Example 2**

**Input**

```text
5 2
4 3 2 1 5
```

**Output**

```text
3
```

**Explanation**

The subarray with the minimum sum of size 2 is [1, 2], and the sum is 3.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Statement - [Finding the Subarray with Minimum Sum of Size K](https://www.codechef.com/practice/course/two-pointers/SLIDINGWINDO/problems/SLDW0105)

### [](#problem-statement-1)Problem Statement

You are given an array of integers, and you need to find a subarray of size **K** that has the minimum sum among all the subarrays of size **K**.

### [](#approach-2)Approach

The code idea is to use a sliding window technique to efficiently calculate the sum of each subarray of size **K**. Initially, we compute the sum of the first **K** elements of the array. This sum is stored as the minimum sum found so far. We then slide the window one element at a time; for each step, we add the next element in the array and subtract the element that is no longer in the window (the leftmost element). This allows us to update the sum in constant time, making the process efficient. Throughout this sliding process, we continuously check and update the minimum sum whenever we calculate a new sum. Finally, we return the **minimum sum** found.

### [](#time-complexity-3)Time Complexity

O(N), where **N** is the length of the array.

### [](#space-complexity-4)Space Complexity

O(1), as we are using a constant amount of space.

</details>
