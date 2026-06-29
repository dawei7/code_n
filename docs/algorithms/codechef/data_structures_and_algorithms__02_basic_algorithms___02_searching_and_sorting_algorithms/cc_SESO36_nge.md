# NGE

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SESO36 |
| Difficulty Band | Searching and Sorting Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [SESO36](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH5/problems/SESO36) |

---

## Problem Statement

Given an array of integers, find the next greater element for each element in the array. The next greater element for an element x in the array is the first greater element on the right side of x in the array. If no such element exists, output -1 for that element.

---

## Input Format

- The first line contains an integer n, representing the number of elements in the array.
- The second line contains n integers, representing the elements of the array.

---

## Output Format

- Output n integers, each representing the next greater element for the corresponding element in the array.

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
4
4 5 2 10
```

**Output**

```text
5 10 10 -1
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Problem Link](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH5/problems/SESO36)

#### [](#problem-statement-1)Problem Statement

Given an array of integers, the task is to find the next greater element for each element in the array. The next greater element for an element `x` in the array is the first element on the right side of `x` that is greater than `x`. If no such element exists, we output `-1` for that element.

#### [](#approach-2)Approach

The approach to finding the next greater element for each element in an array involves using a nested loop where the outer loop iterates through each element, and the inner loop searches for the first greater element to the right of the current element. We initialize a result array with `-1` and, for each element in the outer loop, we traverse the subsequent elements in the inner loop to find the first element greater than the current one. If found, we store this greater element in the result array and break out of the inner loop. This process is repeated for all elements, resulting in a time complexity of O(n^2).

#### [](#complexity-analysis-3)Complexity Analysis

-

**Time Complexity**: The time complexity of this solution is O(n^2), where `n` is the number of elements in the array. This is because, for each element, we potentially compare it with every other element to its right.

-

**Space Complexity**: The space complexity is O(n), which is used to store the next greater elements in the `nge` vector. The solution also requires constant extra space for other variables.

</details>
