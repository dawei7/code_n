# Count Reverse Pairs

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | REVERSEPAIRS |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [REVERSEPAIRS](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/REVERSEPAIRS) |

---

## Problem Statement

You are given an integer array $nums$. Your task is to **count the number of reverse pairs** in the array.

A **reverse pair** is defined as a pair of indices $(i, j)$ such that:

* `0 <= i < j < nums.length`, and
* `nums[i] > 2 * nums[j]`.

## Function Declaration

### Function Name
$reversePairs$ – This function counts the number of reverse pairs in the given array.

### Parameters

* $nums$ : An integer array of length $N$ containing positive, negative, or zero values.

### Return Value

* Returns an integer representing the **total number of reverse pairs** in the array.

## Constraints

- $1 \leq T \leq 100$
- $1 \le N \le 5 \times 10^4$
- $-2^{31} \le nums[i] \le 2^{31} - 1$
- Time-efficient solutions are expected due to large input size.

---

## Input Format

* The first line contains a single integer $T$ — the number of test cases.
* For each test case:
  * The first line contains a single integer $N$ — the size of the array.
  * The second line contains $N$ space-separated integers representing the array elements.

---

## Output Format

* For each test case, output a single integer — the number of reverse pairs in the array.

---

## Constraints

* 1 <= nums.length <= 5 * 10^4
* -2^31 <= nums[i] <= 2^31 - 1

---

## Examples

**Example 1**

**Input**

```text
2
5
5 1 2 1 4
5
6 1 7 3 1
```

**Output**

```text
3
5
```

**Explanation**

#### For the first test case the pairs are:
* (0, 1): `nums[0] = 5`, `nums[1] = 1`, and `5 > 2 * 1`
* (0, 2): `nums[0] = 5`, `nums[2] = 2`, and `5 > 2 * 2`
* (0, 3): `nums[0] = 5`, `nums[3] = 1`, and `5 > 2 * 1`

#### For the second test case the pairs are:
* (0, 1): `nums[0] = 6`, `nums[1] = 1`, and `6 > 2 * 1`
* (0, 4): `nums[0] = 6`, `nums[4] = 1`, and `6 > 2 * 1`
* (2, 3): `nums[2] = 7`, `nums[3] = 3`, and `7 > 2 * 3`
* (2, 4): `nums[2] = 7`, `nums[4] = 1`, and `7 > 2 * 1`
* (3, 4): `nums[3] = 3`, `nums[4] = 1`, and `3 > 2 * 1`

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5
5 1 2 1 4
```

**Output for this case**

```text
3
```



#### Test case 2

**Input for this case**

```text
5
6 1 7 3 1
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

You are given an array of integers. The task is to find the number of **reverse pairs** in the array.

A **reverse pair** is a pair of indices `(i, j)` such that:

* `0 <= i < j < n`
* `nums[i] > 2 * nums[j]`

You are to count all such pairs in the array.

---

## Examples

**Example 1:**

```
Input: [1, 3, 2, 3, 1]
Output: 3
Explanation: The reverse pairs are (1,2), (1,4), and (3,4).
```

**Example 2:**

```
Input: [2, 4, 3, 5, 1]
Output: 5
Explanation: Reverse pairs are (0,4), (1,4), (2,4), (3,4), and (1,2)
```

---

## Constraints

* `1 <= nums.length <= 5 * 10^4`
* `-2^31 <= nums[i] <= 2^31 - 1`

---

## Brute Force Approach

1. Use two nested loops:

   * Outer loop `i` from `0` to `n-2`
   * Inner loop `j` from `i+1` to `n-1`
2. Check if `nums[i] > 2 * nums[j]`.
3. Increment count if the condition holds.

**Time Complexity:** `O(n^2)`
**Space Complexity:** `O(1)`

✅ Works for small arrays but **too slow** for large arrays (up to `5 * 10^4` elements).

---

## Optimized Approach: Merge Sort Technique

The problem can be efficiently solved using a **modified merge sort**.

### Key Idea

* During merge sort, when merging two sorted halves:

  * For each element in the left half, count how many elements in the right half satisfy the condition `nums[i] > 2 * nums[j]`.
* Since both halves are sorted, you can use a pointer to efficiently count the number of valid `j`s for each `i`.
* After counting, perform the standard merge to maintain sorted order for further recursion.

---

### Steps

1. **Divide:** Recursively split the array into two halves.
2. **Conquer:** Count reverse pairs in the left and right halves recursively.
3. **Combine:**

   * Count cross reverse pairs (pairs where `i` is in left half and `j` is in right half).
   * Merge the two halves into a sorted array.

---

### Example Walkthrough

Array: `[1, 3, 2, 3, 1]`

1. Split into `[1, 3, 2]` and `[3, 1]`
2. Further split and recursively sort/count:

   * `[1,3]` → `[1]` and `[3]` → count = 0 → merge → `[1,3]`
   * `[2]` → count = 0
   * Merge `[1,3]` and `[2]`:

     * Count pairs where left > 2\*right: `(1,2)` → `3 > 2*2`? No → 0
     * Merge → `[1,2,3]`
3. Right half `[3,1]`:

   * Split → `[3]` and `[1]`
   * Count cross pairs: `(3,1)` → `3 > 2*1` → Yes → count = 1
   * Merge → `[1,3]`
4. Merge `[1,2,3]` and `[1,3]`:

   * Count cross pairs: `(3,1)` → `3>2*1` → Yes, `(2,1)` → `2>2*1`? No
   * Total count = 3
   * Merge → `[1,1,2,3,3]`

**Answer:** 3

---

### Complexity Analysis

* **Time Complexity:** `O(n log n)`

  * Each merge step takes `O(n)` to count and merge.
  * There are `log n` levels of recursion.

* **Space Complexity:** `O(n)`

  * Temporary array for merging.

---

### Why This Works

* Sorting each half ensures that the right half is sorted for each element in the left half.
* This allows counting the number of valid `j`s efficiently using a **two-pointer approach** instead of iterating every element.
* The merging ensures the array remains sorted for subsequent counting in upper recursion levels.

---

### Summary

1. Brute force is simple but too slow (`O(n^2)`).
2. Merge sort provides an efficient `O(n log n)` solution by counting reverse pairs during merge.
3. Works for large arrays and handles negative numbers and large integer values.

---

This approach is **standard for problems involving counting pairs with inequalities** while maintaining efficiency using divide-and-conquer.

</details>
