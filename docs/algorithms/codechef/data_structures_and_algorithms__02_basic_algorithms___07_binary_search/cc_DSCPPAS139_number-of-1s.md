# Number of 1s

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSCPPAS139 |
| Difficulty Band | Binary Search |
| Path | Data Structures and Algorithms |
| Lesson | Introduction to binary search |
| Official Link | [DSCPPAS139](https://www.codechef.com/learn/course/binary-search/BSVARIATIONS/problems/DSCPPAS139) |

---

## Problem Statement

You are given a sorted binary array containing 0's and 1's. Your task is to efficiently determine the total number of 1's in the array.

**Note:**
- Your implementation should have a time complexity of O(log n), where 'n' is the length of the binary array.

---

## Input Format

- First line contains `n`, representing the size of `binaryArray`.
- Second line contains `n` elements of `binaryArray`, where each element is either 0 or 1.

---

## Output Format

- Print an integer representing the total number of 1's in the given binary array.

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
7
0 0 1 1 1 1 1
```

**Output**

```text
5
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Number of 1s in Binary Search](https://www.codechef.com/learn/course/binary-search/BSVARIATIONS/problems/DSCPPAS139)

### [](#problem-statement-1)Problem Statement:

You are given a sorted binary array containing 0’s and 1’s. Your task is to efficiently determine the total number of 1’s in the array.

**Note:** Your implementation should have a time complexity of O(log n), where ‘n’ is the length of the binary array.

### [](#approach-2)Approach:

To solve this problem efficiently in `O(log⁡ n)` time complexity, we can use **binary search** to find the first occurrence of `1` in the sorted binary array. Once we find the index of the first `1`, we can easily compute the total number of `1`s by subtracting the index from the array length.

**Steps**

- Set two pointers: `low` and `high` to the start and end of the array.

- Use binary search to find the first occurrence of `1`:

- If the middle element is `0`, move the `low` pointer to `mid + 1`.

- If the middle element is `1`, move the `high` pointer to `mid - 1` and store the current index as the potential first `1`.

- Once the first `1` is found, compute the total number of `1`s as `n - index of first 1`.

- If the array contains no `1`s, return `0`.

### [](#complexity-3)Complexity:

- **Time Complexity**: `O(log n)` Binary search uses O(log n) time complexity to search for any element in the array of size n.

- **Space Complexity**: `O(1)` No extra Space is used .

</details>
