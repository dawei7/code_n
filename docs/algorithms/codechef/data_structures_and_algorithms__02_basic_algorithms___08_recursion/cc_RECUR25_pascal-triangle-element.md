# Pascal Triangle Element

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | RECUR25 |
| Difficulty Band | Recursion |
| Path | Data Structures and Algorithms |
| Lesson | Fundamentals of Recursion |
| Official Link | [RECUR25](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/RECUR25) |

---

## Problem Statement

Given an integer $N$, representing the row number, and an integer $M$, representing the column number, find the value at the intersection of the $N$th row and $M$th column of Pascal's Triangle.

Pascal's Triangle is defined as follows:

The $0$th row is 1.
Each element in subsequent rows is the sum of the two elements directly above it in the previous row:

## Function Declaration

### Function Name

$getPascalElement$ – This function returns the element at the given row and column of Pascal’s Triangle.

### Parameters

* $N$ : An integer representing the row number in Pascal’s Triangle (0-based indexing).
* $M$ : An integer representing the column number in Pascal’s Triangle (0-based indexing).

### Return Value

* Returns an integer representing the value at row **N** and column **M** of Pascal’s Triangle.

## Constraints
- $0 \leq N \leq 20$
- $0 \leq M \leq N$

---

## Input Format

* The input consists of a single line containing two space-separated integers:

  * **`N`** – the row number
  * **`M`** – the column number

---

## Output Format

* Print a single integer — the element at the **Mᵗʰ column** of the **Nᵗʰ row** in Pascal’s Triangle.

---

## Examples

**Example 1**

**Input**

```text
4 2
```

**Output**

```text
6
```

**Explanation**

The 4th row of Pascal’s Triangle is [1, 4, 6, 4, 1].
The element at the 2nd column (0-based index) in the 4th row is 6.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Pascal Triangle Element in Recursion](https://www.codechef.com/learn/course/recursion/LRECUR03/problems/RECUR25)

### [](#problem-statement-1)Problem Statement:

Given an integer N, representing the row number, and an integer M, representing the column number, find the value at the intersection of the Nth row and Mth column of Pascal’s Triangle.

### [](#approach-2)Approach:

The logic is based on the fact that each element in Pascal’s Triangle is the sum of the two elements directly above it.

-

**Base Case**: If M=0 or M=N, the answer is `1`. This corresponds to the edges of Pascal’s Triangle, where the first and last elements of each row are always `1`. An additional check ensures that the column value M is within a valid range. If M>N, it’s an invalid input.

-

**Recursive Case**: For other positions, the value at the Nth row and Mth column is the sum of the values from the previous row:

Pascal’s value at (N, M) = Pascal’s value at (N−1, M−1) + Pascal’s value at (N−1, M).

### [](#complexity-3)Complexity:

-

**Time Complexity:** Since this recursive solution has overlapping subproblems, its time complexity is exponential, specifically `O(2^N)` because each recursive call contains two more recursive calls, leading to a binary tree-like recursion.

-

**Space Complexity:** `O(N)` because of the recursion stack, where `N` is the depth of the recursion (equal to the row number).

</details>
