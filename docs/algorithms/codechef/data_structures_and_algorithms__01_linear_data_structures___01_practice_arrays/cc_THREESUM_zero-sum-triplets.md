# Zero Sum Triplets

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | THREESUM |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [THREESUM](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/THREESUM) |

---

## Problem Statement

Chef is arranging dishes on a table.\
You are given an array of dishes with $N$ dishes. Each dish has a number (positive, negative, or zero).

Chef wants to know:\
**Can we pick any 3 different dishes indices such that their total is exactly 0?**

Your task is to find all such unique triplets.
- A valid triplet contains 3 different numbers (on different indices) from the array.
- The same triplet should not repeat.
- Print each triplet in non-decreasing order.
- If no triplet exists return empty array that will be treated as print -1.

## Function Declaration

### Function Name
$findZeroSumTriplets$ – This function finds all unique triplets in the array whose sum is exactly zero.

### Parameters

* $nums$ : A reference to an integer array containing $N$ elements, where each element can be positive, negative, or zero.

### Return Value

* Returns a 2D array containing all **unique triplets** whose sum is `0`.
* Each triplet is sorted in **non-decreasing order**.
* If no such triplet exists, return an **empty array** (this will be treated as printing `-1`).

## Constraints

- $3 \leq N \leq 3000$
- $-100000 \leq nums[i] \leq 100000$

---

## Input Format

* The first line contains a single integer $N$ — the number of elements in the array.
* The second line contains $N$ space-separated integers representing the array elements.

---

## Output Format

* Print all valid triplets, one triplet per line.
* Each triplet should contain three space-separated integers.
* If no triplet exists, print `-1`.

---

## Constraints

3 <= N <= 3000\
-100000 <= value <= 100000

---

## Examples

**Example 1**

**Input**

```text
5
2 -2 0 1 -1
```

**Output**

```text
-2 0 2
-1 0 1
```

**Explanation**

Triplet `(-2, 0, 2)` -> sum = 0\
Triplet `(-1, 0, 1)` -> sum = 0\
These are the only unique triplets.

**Example 2**

**Input**

```text
4
5 -3 -2 1
```

**Output**

```text
-3 -2 5
```

**Explanation**

Triplet `(-3, -2, 5)` -> sum = 0\
No other triplet exists.

**Example 3**

**Input**

```text
4
1 2 3 4
```

**Output**

```text
-1
```

**Explanation**

No three numbers add up to 0, so output is `-1`.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

We are given an array of integers `A` of length `N`.\
We must find all unique triplets `(A[i], A[j], A[k])` such that:
- i < j < k
- A[i] + A[j] + A[k] = 0

If no such triplet exists, print `-1`.

The triplets must be unique and sorted in **non-decreasing order**.

---

## Key Observations

1. A **naïve solution** would check every triplet using three nested loops → `O(N³)`, which is too slow for `N = 3000` (`≈ 2.7 × 10¹⁰` operations).

2. We need a **better approach**:
- Sort the array.
- Fix one element `nums[i]`.
- Use two pointers (`left` and `right`) to find two other elements that sum to `-nums[i]`.

This reduces the problem from `O(N³)` to `O(N²)`.

---

## Step-by-Step Approach

1.**Sort** the array. This helps:
- Avoid duplicates easily.
- Use the two-pointer technique.

2. Loop over each index `i` (`0 ≤ i < N-2`):
- Skip duplicates (if `nums[i] == nums[i-1`]).
- Set two pointers:
   - `left = i + 1`
   - `right = N - 1`
- While `left < right`:
   - Compute `sum = nums[i] + nums[left] + nums[right]``.
   - If `sum == 0` → store triplet, move both pointers while skipping duplicates.
   - If `sum < 0` → increase `left` (need bigger number).
   - If `sum > 0` → decrease `right` (need smaller number).

3. Collect unique triplets.

---

## Complexity Analysis

- **Time Complexity**: `O(N²)` → sorting takes `O(N log N)` + two-pointer search for each element takes `O(N²)`.

- **Space Complexity**: `O(1)` (ignoring result storage) → we only use pointers/variables.

</details>
