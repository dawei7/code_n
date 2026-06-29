# Valid Matrix Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSCPPAS263 |
| Difficulty Band | 2D Array / Matrices |
| Path | Data Structures and Algorithms |
| Lesson | Practice |
| Official Link | [DSCPPAS263](https://www.codechef.com/practice/course/matrices/MATRICES/problems/DSCPPAS263) |

---

## Problem Statement

You are given an integer $n$ and $m$, representing the dimensions of an $n×m$ matrix. You need to construct an $n×m$ matrix such that the following properties are satisfied:

- Each element in the matrix is 1.
- The sum of the elements of the matrix is even.

If it is not possible then print $-1$.

---

## Input Format

- The first line contains one integer $n$ and $m$, the size of the matrix.

---

## Output Format

- Print a 2d matrix with given properties or $-1$.

---

## Constraints

- $ 1 \leq n, m \leq 100 $

---

## Examples

**Example 1**

**Input**

```text
2 2
```

**Output**

```text
1 1
1 1
```

**Explanation**

The sum of elements of the matrix is 4 which is even.

**Example 2**

**Input**

```text
1 1
```

**Output**

```text
-1
```

**Explanation**

No such matrix is possible.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#### [](#problem-statement-1)Problem Statement:

You are given two integers, `n` and `m`, representing the dimensions of an `n × m` matrix. The task is to construct an `n × m` matrix such that:

- Each element in the matrix is `1`.

- The sum of the elements of the matrix is even.

If it’s not possible to satisfy these conditions, you should output `-1`.

#### [](#solution-explanation-2)Solution Explanation:

The problem can be broken down into the following steps:

-

**Understanding the Matrix Composition:**

- The matrix is of dimensions `n × m`.

- Each element in the matrix is `1`.

- The sum of the elements in the matrix will be `n * m` since every element is `1`.

-

**Check for Evenness:**

- For the sum of all elements in the matrix to be even, the product of `n` and `m` must be even. This is because the sum of all `1`s (which equals `n * m`) needs to be even.

- Therefore, if `n * m` is even, it’s possible to create the matrix where the sum of all elements is even. If `n * m` is odd, it’s impossible to make the sum even with all elements being `1`, and hence the output should be `-1`.

-

**Constructing the Matrix:**

- If `n * m` is even, construct the matrix by filling all positions with `1`.

- The matrix can then be printed row by row.

#### [](#edge-cases-3)Edge Cases:

- If either `n` or `m` is `1`, the sum of the matrix elements will be `n * m`. If `n * m` is odd (e.g., when both `n` and `m` are odd), output `-1`.

- The smallest possible input (e.g., `n = 1`, `m = 1`) should be handled correctly.

#### [](#time-complexity-4)Time Complexity:

The time complexity of this solution is `O(n * m)` because it involves iterating through each element of the `n × m` matrix once to print it.

#### [](#space-complexity-5)Space Complexity:

The space complexity is `O(1)` in terms of additional space, as the solution does not use any extra space that scales with input size.

</details>
