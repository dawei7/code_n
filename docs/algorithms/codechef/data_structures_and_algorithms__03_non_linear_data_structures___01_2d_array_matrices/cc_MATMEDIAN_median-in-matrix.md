# Median in Matrix

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATMEDIAN |
| Difficulty Band | 2D Array / Matrices |
| Path | Data Structures and Algorithms |
| Lesson | Practice |
| Official Link | [MATMEDIAN](https://www.codechef.com/practice/course/matrices/MATRICES/problems/MATMEDIAN) |

---

## Problem Statement

Given a `N x M` row-wise sorted matrix, find the median of the matrix. (*Note:* `N*M` is always odd)

For eg., in the following matrix:

![matmedian](https://i.ibb.co/JHZXwzj/Screenshot-2024-03-15-at-12-25-28-PM.png)

If we place all elements in the sorter order: 2 3 4 4 4 5 6 6 7

Then the median of the matrix is: `4`

**Follow up:** Can you solve it in better time than **O(NMlog(NM))** and without taking extra space ?

---

## Input Format

- The first line of input will contain two space separated integers $N$ and $M$, denoting the no. of rows and columns in the input matrix.
- Next $N$ lines contains $M$ space separated integers, the elements of the matrix.

---

## Output Format

- Output on a single line, the median of the matrix.

---

## Constraints

- $1 \leq N, M \leq 100$
- The elements of the matrix are non-negative and won't exceed $1000$.
- The elements in each row are sorted in non-decreasing order.
- `N*M` is always odd

---

## Examples

**Example 1**

**Input**

```text
3 3
3 4 5
2 4 6
4 6 7
```

**Output**

```text
4
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Matrix, Binary Search.

**Problem:** Given a `N x M` row-wise sorted matrix, find the median of the matrix. (*Note:* `N*M` is always odd)

**Solution Approach:**

The naive solution is to store all elements of the matrix in an array, sort it and return the middle element. That will take O(N*Mlog(N*M)) time and O(N*M) space. However since the matrix is row-wise sorted, we can use binary search to find the median value of the matrix.

We can perform binary search on the possible range of values that the median can take. We initialize a low value as the minimum possible value in the matrix and a high value as the maximum possible value. We then iterate through the search space, finding the middle value. For each middle value, we count the number of elements in the matrix that are smaller than or equal to the middle value using binary search in each row. If the count of such elements is less than or equal to half of the total number of elements in the matrix, we update the low value to move towards higher values. Otherwise, we update the high value to move towards lower values. We continue this process until we find the median value. This approach efficiently identifies the median value by narrowing down the search space using binary search.

**Time Complexity**:  O(log(maxValue - minValue) * N * log(M)). The first log factor is due to BS on possible range of median, and in each iteration  of  while loop, we’re again iterating through each row taking log(M) time to count smaller elements.

**Space Complexity**:  O(1) as no extra space required except few variables.

</details>
