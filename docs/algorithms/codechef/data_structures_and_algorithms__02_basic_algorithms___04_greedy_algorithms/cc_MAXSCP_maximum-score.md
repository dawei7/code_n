# Maximum Score

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MAXSCP |
| Difficulty Rating | 1561 |
| Difficulty Band | Greedy Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Additional Applications of Greedy Algorithms |
| Official Link | [MAXSCP](https://www.codechef.com/learn/course/greedy-algorithms/LIGRDSA05/problems/MAXSCP) |

---

## Problem Statement

You are given **N** integer sequences **A1, A2, ..., AN**. Each of these sequences contains **N** elements. You should pick **N** elements, one from each sequence; let's denote the element picked from sequence **Ai** by **Ei**. For each **i** (2 ≤ **i** ≤ **N**), **Ei** should be strictly greater than **Ei-1**.

Compute the maximum possible value of **E1 + E2 + ... + EN**. If it's impossible to pick the elements **E1, E2, ..., EN**, print -1 instead.

### Input

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first line of each test case contains a single integer **N**.

- **N** lines follow. For each valid **i**, the **i**-th of these lines contains **N** space-separated integers **Ai1, Ai2, ..., AiN** denoting the elements of the sequence **Ai**.

### Output

For each test case, print a single line containing one integer — the maximum sum of picked elements.

### Constraints

- 1 ≤ **T** ≤ 10

- 1 ≤ **N** ≤ 700

- 1 ≤ sum of **N** in all test-cases ≤ 3700

- 1 ≤ **Aij** ≤ 109 for each valid **i**, **j**

---

## Examples

**Example 1**

**Input**

```text
1
3
1 2 3
4 5 6
7 8 9
```

**Output**

```text
18
```

**Explanation**

**Example case 1:** To maximise the score, pick 3 from the first row, 6 from the second row and 9 from the third row. The resulting sum is **E1+E2+E3** = 3+6+9 = 18.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Maximum Score in Greedy Algorithms](https://www.codechef.com/learn/course/greedy-algorithms/LIGRDSA05/problems/MAXSCP)

### [](#problem-statement-1)Problem Statement:

We are tasked with selecting one element from each row of an N x N matrix, where the elements picked must strictly increase as we move from the first row to the last row. The goal is to maximize the sum of the selected elements. If it’s not possible to select such elements, the output should be -1.

### [](#approach-2)Approach:

**1. Sort Each Row:** Start by sorting each row of the matrix. This ensures that when we pick elements from the rows, we can efficiently choose the maximum possible element from the current row that satisfies the strictly increasing condition.

**2. Pick Maximum Element with Constraints:**

- We initialize by selecting the maximum element from the last row.

- Then, for each row before the last (moving backward), we select the largest element that is smaller than the previously chosen element from the next row (to maintain the strictly increasing condition).

- If at any row, it’s impossible to find such an element, we mark the solution as invalid and print `-1`.

**3. Continue or Break:** If a valid selection of elements is found (i.e., elements strictly increase as we move up), we compute the sum and print it. Otherwise, print `-1`.

### [](#complexity-3)Complexity:

- **Time Complexity:**  Sorting each row takes `O(N log N)`. Finding the maximum element in the row smaller than the previously chosen element takes `O(N)`. So, the overall time complexity is `O(N^2 log N)`.

- **Space Complexity:** `O(1)`

</details>
