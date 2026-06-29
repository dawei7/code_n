# Search In Matrix

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MATSEARCH |
| Difficulty Band | 2D Array / Matrices |
| Path | Data Structures and Algorithms |
| Lesson | Practice |
| Official Link | [MATSEARCH](https://www.codechef.com/practice/course/matrices/MATRICES/problems/MATSEARCH) |

---

## Problem Statement

You are given an `N x M` integer matrix with the following properties:

- Each row of the matrix is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer `X`, determine whether it exists in the matrix.

Write a solution with a time complexity of **O(log(NM))**.

---

## Input Format

- The first line of input will contain three space separated integers $N$, $M$ and $X$, denoting the no. of rows and columns in the input matrix along with the integer which needs to be searched in matrix.
- Next $N$ lines contains $M$ space separated integers, the elements of the matrix.

---

## Output Format

- Output on a single line `YES` if `X` exists in the the given matrix, else `NO`.

---

## Constraints

- $0 \leq N, M \leq 100$
- $0 \leq X \leq 100000$
- The elements of the matrix are non-negative and won't exceed $100000$.
- Each row of the matrix is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

---

## Examples

**Example 1**

**Input**

```text
3 4 7
1 2 3 4
5 6 7 8
9 10 11 12
```

**Output**

```text
YES
```

**Example 2**

**Input**

```text
3 4 7
1 2 3 4
5 6 6 8
9 10 11 12
```

**Output**

```text
NO
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

**Prerequisites:** Matrix, Binary Search.

**Problem:** You are given an `N x M` integer matrix with the following properties:

- Each row of the matrix is sorted in non-decreasing order.

- The first integer of each row is greater than the last integer of the previous row.

Given an integer `X`, determine whether it exists in the matrix.

**Solution Approach:**

The core idea of the solution is to perform a binary search on the entire matrix treating it as a flattened array.

We define a start index pointing to the first element of the matrix and an end index pointing to the last element of the matrix. Within each iteration of the binary search, we calculate the middle element of the matrix. We compare the middle element with the target value. If they match, we return true. Otherwise, if the target is less than the middle element, we update the end index to mid - 1, indicating that we should search in the lower half of the matrix. Conversely, if the target is greater than the middle element, we update the start index to mid + 1, indicating that we should search in the upper half of the matrix. We continue this process until the start index exceeds the end index, indicating that the target is not present in the matrix, in which case we return false. This approach leverages the sorted nature of the matrix rows to efficiently search for the target value.

In binary search, by dividing the index `mid` by the number of columns `numCols` , we obtain the row index, as `mid` represents the index within the flattened matrix. Similarly, taking the remainder of `mid` divided by `numCols` gives us the column index.

**Time Complexity**: O(log(N * M)), where N is the number of rows and M is the number of columns in the matrix. This complexity arises from the binary search algorithm applied to the flattened matrix, which has N * M elements.

**Space Complexity**:  O(1) because it only uses a constant amount of additional space for storing variables regardless of the size of the input matrix.

</details>
