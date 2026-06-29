# Merging

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SESO27 |
| Difficulty Band | Searching and Sorting Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [SESO27](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH7/problems/SESO27) |

---

## Problem Statement

You are given two sorted arrays of lengths **n** and **m** respectively. Your task is to merge these two arrays into a single array such that the resulting array is also sorted.

Write a function or algorithm that performs this task and prints the resulting sorted array.

---

## Input Format

- The first line contains an integer **n** denoting the length of the first array.
- The second line contains **n** space-separated integers representing the elements of the first array.
- The third line contains an integer **m** denoting the length of the second array.
- The fourth line contains **m** space-separated integers representing the elements of the second array.

---

## Output Format

- Print a single line containing the merged sorted array.

---

## Constraints

- The lengths of the arrays, n and m, are positive integers.
- Elements of the arrays can be any integers.

---

## Examples

**Example 1**

**Input**

```text
3
1 3 5
3
2 4 6
```

**Output**

```text
1 2 3 4 5 6
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Problem Link](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH7/problems/SESO27)

To efficiently merge two sorted arrays, we can use a two-pointer technique. This method leverages the fact that both input arrays are already sorted, allowing us to merge them in linear time.

-

**Initialization**:

- We start by initializing two pointers, `i` and `j`, to zero. These pointers will be used to traverse the first and second arrays, respectively.

- We also initialize an empty list (or array) `mergedArray` to store the result of the merge.

-

**Merging Process**:

- The main idea is to compare the elements pointed to by `i` and `j` in the two arrays. The smaller of the two elements is added to the `mergedArray`, and the corresponding pointer (`i` or `j`) is incremented.

- This process continues until one of the pointers reaches the end of its array, meaning all elements in that array have been processed.

-

**Appending Remaining Elements**:

- After one array is fully traversed, the remaining elements in the other array (if any) are directly appended to the `mergedArray`. This is because the remaining elements are already sorted and larger than all elements in the `mergedArray`.

-

**Output**:

- The resulting `mergedArray` contains all the elements from both input arrays in sorted order. This array is then returned or printed as the output.

#### [](#complexity-analysis-1)Complexity Analysis

-

**Time Complexity**: The time complexity of this approach is O(n + m), where `n` and `m` are the lengths of the two arrays. This is optimal because each element from both arrays is processed exactly once.

-

**Space Complexity**: The space complexity is O(n + m), which is the space required to store the merged array. The space complexity does not include the space used by the input arrays as they are provided.

</details>
