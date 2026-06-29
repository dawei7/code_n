# Subarray with k distinct number

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | KSUBARRAYS |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Sliding Window |
| Official Link | [KSUBARRAYS](https://www.codechef.com/practice/course/two-pointers/SLIDINGWINDO/problems/KSUBARRAYS) |

---

## Problem Statement

You are given an integer array $arr$ and an integer $k$. Your task is to find the number of contiguous subarrays in $arr$ that contain **exactly k distinct integers**.

A subarray is defined as a continuous and non-empty sequence of elements within the array.

---

## Function Declaration

### Function Name
$subarraysWithKDistinct$ – This function computes the number of contiguous subarrays that contain exactly **k distinct integers**.

### Parameters

* $arr$ : A list/array of integers of length $n$, representing the input sequence.
* $k$ : An integer representing the required number of distinct elements.

### Return Value

Returns an integer: The total number of contiguous subarrays that contain exactly **k distinct integers**. If there are no such **good arrays** then return $0$ value.

---

### Constraints:
* $1 \leq T \leq 100$
* $1 \leq n \leq 2 \cdot 10^4$
* $1 \leq k \leq n$
* $1 \leq nums[i] \leq n$ for each $1 \leq i \leq n$
* The sum of $n$ over all test cases won't exceed $2 \cdot 10^5$

**The input and output formats provided below are only for testing with custom inputs. You only need to return the value. Printing is handled automatically**

---

## Input Format

* The first line contains an integer $T$, the number of test cases.
* For each test case:

  * The first line contains two integers: $n$ (the size of the array) and $k$.
  * The second line contains $n$ integers representing the array elements.

---

## Output Format

For each test case, output a single integer — the number of good subarrays.

---

## Constraints

* $1 \leq T \leq 100$
* $1 \leq n \leq 2 \cdot 10^4$
* $1 \leq k \leq n$
* $1 \leq nums[i] \leq n$ for each $1 \leq i \leq n$
* The sum of $n$ over all test cases won't exceed $2 \cdot 10^5$

---

## Examples

**Example 1**

**Input**

```text
2
5 2
4 5 4 5 1
4 3
1 2 2 3
```

**Output**

```text
7
1
```

**Explanation**

* **Test case 1:** Array `[4, 5, 4, 5, 1]`
  Good subarrays with exactly 2 distinct integers are:
  `[4,5]`, `[5,4]`, `[4,5]`, `[5,1]`, `[4,5,4]`, `[5,4,5]`, `[4,5,4,5]` -> **7 subarrays**

* **Test case 2:** Array `[1, 2, 2, 3]`
  Good subarrays with exactly 3 distinct integers are:
  `[1,2,2,3]` -> **1 subarrays**

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 2
4 5 4 5 1
```

**Output for this case**

```text
7
```



#### Test case 2

**Input for this case**

```text
4 3
1 2 2 3
```

**Output for this case**

```text
1
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem

Given an array of integers and an integer `k`, find the number of contiguous subarrays that contain exactly `k` distinct integers.

---

## Approach

1. **Understanding the problem**

   * A subarray is a contiguous portion of the array.
   * A "good subarray" contains exactly `k` distinct integers.
   * The brute-force approach would be to generate all subarrays and count distinct elements, but this is too slow for large arrays.

2. **Observation**

   * Counting subarrays with **exactly k distinct integers** can be expressed as:
      $\text{exactlyK} = \text{atMostK}(k) - \text{atMostK}(k-1)$
   * Here, `atMostK(x)` counts the number of subarrays with **at most x distinct integers**.

3. **Sliding Window Technique**

   * Use two pointers (`left` and `right`) to maintain a sliding window.
   * Maintain a frequency map (or array) of numbers inside the window.
   * Expand the window to the right. If adding a new number exceeds the allowed distinct count, shrink the window from the left until the count is valid.
   * At each step, add the number of subarrays ending at the current right pointer to the result.

4. **Efficiency**

   * Both `atMostK(k)` and `atMostK(k-1)` can be computed in **O(n)** using the sliding window.
   * This makes the overall approach **O(n)** per test case.
   * Memory usage depends on the number of distinct elements in the array. A frequency array or map is used.

---

## Steps

1. Define a helper function `atMostK(nums, k)` to count subarrays with at most `k` distinct integers.
2. Compute the answer as:
   $\text{answer} = \text{atMostK}(k) - \text{atMostK}(k-1)$
3. Handle multiple test cases by reading input arrays and `k` values.
4. Return or print the answer for each test case.

---

## Key Points

* Using **atMostK subtraction** avoids enumerating all subarrays.
* The sliding window approach ensures that each element is processed at most twice (once when added, once when removed), resulting in linear time complexity.
* This technique works efficiently even for large arrays and large numbers of test cases.

---

## Example

Array: `[1, 2, 1, 2, 3]`, `k = 2`

1. Count subarrays with at most 2 distinct: `[1]`, `[1,2]`, `[2]`, `[2,1]`, `[1,2]`, `[2,3]`, `[1,2,1]`, `[2,1,2]`, `[1,2,1,2]` → 12 subarrays.
2. Count subarrays with at most 1 distinct: `[1]`, `[2]`, `[1]`, `[2]`, `[3]` → 5 subarrays.
3. Subarrays with exactly 2 distinct: `12 - 5 = 7` → `[1,2]`, `[2,1]`, `[1,2]`, `[2,3]`, `[1,2,1]`, `[2,1,2]`, `[1,2,1,2]`.

---

This approach generalizes to any array size and value constraints efficiently.

</details>
