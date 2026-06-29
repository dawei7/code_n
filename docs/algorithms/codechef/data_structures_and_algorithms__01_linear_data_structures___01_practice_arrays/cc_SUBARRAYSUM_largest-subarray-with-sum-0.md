# Largest Subarray with Sum 0

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SUBARRAYSUM |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [SUBARRAYSUM](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/SUBARRAYSUM) |

---

## Problem Statement

Chef has an array of integers $arr$ which may contain both positive and negative values.\
He is curious to know the length of the **longest contiguous subarray** whose sum is equal to $0$.

Your task is to help Chef find this length.\
If no such subarray exists, output $0$.

## Function Declaration

### Function Name

$largestSubarrayWithSumZero$ – This function finds the length of the longest contiguous subarray with sum equal to zero.

### Parameters

* $arr$ : An array of integers (can contain positive and negative values).

### Return Value

* Returns a single integer — the **maximum length** of a contiguous subarray whose sum is $0$.
* Returns $0$ if no such subarray exists.

## Constraints

* $1 \leq n \leq 10^6$
* $−10^3 \leq arr[i] \leq 10^3$
* Array elements can be positive, negative, or zero

---

## Input Format

* The first line of each test case contains a single integer $n$ — the number of elements in the array.
* The next line contains $n$ space-separated integers $arr[i]$ — the elements of the array.

---

## Output Format

* For each test case, print a single integer — the length of the longest subarray whose sum is `0`.

---

## Constraints

- $1 \le n \le 10^6 $
- $-10^3 \le arr[i] \le 10^3 $

---

## Examples

**Example 1**

**Input**

```text
7
4 -3 1 -2 2 6 -6
```

**Output**

```text
4
```

**Explanation**

The longest subarray with sum `0` is `[-2, 2, 6, -6]` (indexes 1 to 4) with length **4**.

**Example 2**

**Input**

```text
5
1 2 -3 3 -3
```

**Output**

```text
5
```

**Explanation**

The longest subarray with sum `0` is `[1, 2, -3, 3, -3]` with length **5**.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

You are given an array `arr` of length `n` that may contain both positive and negative numbers.\
You need to find the **length of the longest contiguous subarray** whose sum is exactly **0**.\
If no such subarray exists, return **0**.

---

## Key Observations

1. **Brute force approach**

Check every subarray `(i..j)` and compute sum.

This takes `O(N²)` for subarray checks and `O(N³)` if sum recomputed each time -> **too slow for n = 10⁶**.

2. **Prefix Sum idea**

- Define prefix sum:
`prefixSum[i] = arr[0] + arr[1] + ... + arr[i]`.

- A subarray `(l..r)` has sum = 0 if:\
`prefixSum[r] == prefixSum[l-1]` (or if `prefixSum[r] == 0` from start).

- So we only need to detect when the same prefix sum occurs **more than once**.

3. **Hashing technique**

- Store the **first occurrence index** of each prefix sum in a hashmap.

If we see the same prefix sum again at index `i`, then the subarray between these two indices has sum = 0.

Keep track of the **maximum length**.

---

## Approach

1. Initialize:
- `prefixSum = 0`
- `maxLen = 0`
- HashMap `map` to store first index of each prefix sum.

2. Traverse array:
- Add current element to `prefixSum`.
- If `prefixSum == 0`, then the subarray `(0..i)` has sum = 0 → update `maxLen = i+1`.
- If `prefixSum` has been seen before at index `j`, then subarray `(j+1 .. i)` has sum 0 → update length = `i - j`.

Otherwise, store current index as first occurrence of this prefix sum.

3. Return `maxLen`.

---

## Complexity Analysis

- **Time Complexity**: `O(N)` → single pass over array, each lookup in hashmap is `O(1)` average.

- **Space Complexity**: `O(N)` → hashmap stores prefix sums.

</details>
