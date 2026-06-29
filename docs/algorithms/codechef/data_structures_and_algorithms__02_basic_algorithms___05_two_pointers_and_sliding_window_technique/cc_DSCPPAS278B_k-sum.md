# K Sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSCPPAS278B |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Sliding Window |
| Official Link | [DSCPPAS278B](https://www.codechef.com/practice/course/two-pointers/SLIDINGWINDO/problems/DSCPPAS278B) |

---

## Problem Statement

Given an array arr of positive integers and an integer $k$, write a program that returns the maximum possible sum of $k$ elements taken from either the start of the array, the end of the array, or a combination of both.

---

## Input Format

- The first line contains two positive integers $n$ and $k$ representing the size of $arr$ and number of elements whose sum is to be taken.
- Next line contains $n$ elements of the array.

---

## Output Format

Print the maximum sum that can be achieved by taking $k$ elements.

---

## Constraints

- $1 \leq n \leq 10^5$
- $1 \leq k \leq n$
- $1 \leq arr[i] \leq 10^6$

---

## Examples

**Example 1**

**Input**

```text
5 3
4 2 1 5 1
```

**Output**

```text
10
```

**Explanation**

Take one element from the start of the array and take 2 elements from the end of the array. the sum will be 4+1+5=10.

**Example 2**

**Input**

```text
3 3
1 2 3
```

**Output**

```text
6
```

**Explanation**

Take all three elements from the array, the sum will be 1+2+3=6.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### [](#problem-statement-1)Problem Statement:

You are given an array `arr` of positive integers and an integer `k`. The task is to find the maximum possible sum of `k` elements that can be taken from either the start of the array, the end of the array, or a combination of both.

### [](#approach-2)Approach:

The core idea of the solution is to utilize a **two-pointer technique** to explore all possible combinations of selecting `k` elements from both ends of the array. By carefully shifting elements from the start of the array to the end, we can efficiently determine the maximum sum that can be obtained.

### [](#detailed-approach-3)Detailed Approach:

-

**Initial Sum Calculation**:

- Start by calculating the sum of the first `k` elements from the beginning of the array. This initial sum represents the scenario where all `k` elements are selected from the start.

- This sum is stored as the `current_sum` and is also set as the initial `max_sum`.

For example, if `arr = [1, 2, 3, 4, 5]` and `k = 3`, the initial sum would be `1 + 2 + 3 = 6`.

-

**Two-Pointer Technique**:

- After calculating the initial sum, we consider other possible combinations by gradually replacing elements from the start of the array with elements from the end.

- We maintain two pointers:

- One pointer (`i`) moves backward from the `k-1` index of the array, indicating the elements being subtracted from the `current_sum`.

- The other pointer simultaneously moves forward from the last element of the array, adding these elements to the `current_sum`.

- In each iteration, we update the `current_sum` by subtracting the `i-th` element from the start and adding the `i-th` element from the end.

- After each update, we compare the `current_sum` with `max_sum` and update `max_sum` if `current_sum` is greater.

Continuing from our example, the iterations would be:

- First, subtract `3` and add `5`: `current_sum = 6 - 3 + 5 = 8`.

- Next, subtract `2` and add `4`: `current_sum = 8 - 2 + 4 = 10`.

In this case, the maximum sum of `10` is obtained by taking `2` from the start and `4, 5` from the end.

-

**Result**:

- After iterating through all possible combinations, the `max_sum` will contain the maximum possible sum of `k` elements.

### [](#complexity-4)Complexity:

- **Time Complexity**: The solution runs in `O(k)`, since it involves a fixed number of operations (`k` iterations) regardless of the size of the array.

- **Space Complexity**: The space complexity is `O(1)` as the solution only uses a few extra variables for calculations.

</details>
