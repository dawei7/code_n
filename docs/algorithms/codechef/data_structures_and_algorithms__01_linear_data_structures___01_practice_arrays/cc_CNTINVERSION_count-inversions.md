# Count Inversions

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | CNTINVERSION |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [CNTINVERSION](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/CNTINVERSION) |

---

## Problem Statement

Chef has an array $arr$ consisting of integers and wants to know **how far the array is from being sorted**. $N$ is the size of the array.

Two elements $arr[i]$ and $arr[j]$ form **an inversion** if:

- $arr[i] > arr[j]$
- $i < j$

An inversion indicates that the array is not sorted.

Your task is to count **the total number of inversions** in the array.

## Function Declaration

### Function Name

$countInversion$ – This function counts the total number of inversions in an array.

### Parameters

* $arr$ : An array of integers.
* $n$ : An integer representing the size of the array.

### Return Value

* Returns a single integer — the **total number of inversions** in the array.

## Constraints

* $1 \leq N \leq 10^5$
* $−10^4 \leq arr[i] \leq 10^4$
* The answer can be large, so use a data type capable of storing large values.

---

## Input Format

* The first line of input contains a single integer $N$ — the size of the array.
* The second line contains $N$ space-separated integers representing the array $arr$.

---

## Output Format

Output a single integer — the **total number of inversions** in the array.

---

## Constraints

- $1 \leq N \leq 10^{5} $
- $ -10^{4} \leq \text{arr}[i] \leq 10^{4} $

---

## Examples

**Example 1**

**Input**

```text
5
3 1 4 2 5
```

**Output**

```text
3
```

**Explanation**

The inversions are:
- (3, 1) -> indices (0, 1)
- (3, 2) -> indices (0, 3)
- (4, 2) -> indices (2, 3) \
Total inversions = 3.

**Example 2**

**Input**

```text
4
10 20 30 40
```

**Output**

```text
0
```

**Explanation**

The array is already sorted in ascending order. There are no inversions.

**Example 3**

**Input**

```text
6
8 6 7 5 3 1
```

**Output**

```text
14
```

**Explanation**

The inversions are:
- (8, 6), (8, 7), (8, 5), (8, 3), (8, 1) -> 5 inversions
- (6, 5), (6, 3), (6, 1) -> 3 inversions
- (7, 5), (7, 3), (7, 1) -> 3 inversions
- (5, 3), (5, 1) -> 2 inversions
- (3, 1) -> 1 inversion

Total inversions = 5 + 3 + 3 + 2 + 1 = 14.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

Chef has an array `nums` of length `N`.\
Two elements `nums[i]` and `nums[j]` form an **inversion** if:

- `nums[i] > nums[j]`
- `i < j`

The inversion count tells us how far the array is from being sorted.

We need to calculate the total number of inversions in the array.

---

## Key Observations

If the array is already sorted in ascending order, the inversion count is `0`.

If the array is sorted in descending order, the inversion count is **maximum** = `N * (N-1) / 2`.

A **brute force approach** would check all pairs `(i, j)` with `i < j`, but this takes `O(N²)` time, which is too slow for `N = 10^5`.

We need a faster approach → `Merge Sort` can be adapted to count inversions efficiently in `O(N log N)`.

---

## Approach (Merge Sort Based)

We modify the merge sort algorithm:

- **Divide the array** into two halves recursively.
- **Count inversions** in the left half and right half.
- **Count cross inversions** while merging the two sorted halves.

---

## Complexity Analysis

- **Time Complexity**:

Each merge step takes `O(N)` and there are `O(log N)` levels in merge sort.
So total = **O(N log N)**.

- **Space Complexity**:

We use temporary arrays for merging.
So space = **O(N)**.

</details>
