# Accumulate Count

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | SESO39 |
| Difficulty Band | Searching and Sorting Algorithms |
| Path | Data Structures and Algorithms |
| Lesson | Sorting |
| Official Link | [SESO39](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH9/problems/SESO39) |

---

## Problem Statement

You are given the length of an array n, followed by the array itself and a number k. The array consists of integers where each integer is between $0$ and $k-1$ (inclusive). Your task is to create an accumulated count array from the given array. The accumulated count array at index $i$ should contain the sum of counts from index $0$ to $i$ of the count array.

---

## Input Format

- **n** (int): The length of the array arr.
- **arr** : A array of n integers where each integer is between 0 and k-1.
- **k** (int): The range of integers in the array, such that each integer in arr is in the range [0, k-1].

---

## Output Format

- A list of integers where the element at index i represents the accumulated count of integers from 0 to i in the arr.

---

## Constraints

- 1 ≤ n ≤ 10^6
- 1 ≤ k ≤ 10^6
- Each integer in arr is in the range [0, k-1].

---

## Examples

**Example 1**

**Input**

```text
6
2 0 2 1 1 0
3
```

**Output**

```text
2 4 6
```

**Example 2**

**Input**

```text
5
1 0 2 1 0
3
```

**Output**

```text
2 4 5
```

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

[Problem Link](https://www.codechef.com/learn/course/searching-sorting/SORTSEARCH9/problems/SESO39)

#### [](#problem-recap-1)Problem Recap:

You are given an integer `n` representing the length of an array, followed by the array itself, and an integer `k`. The array consists of integers where each integer is between `0` and `k−1` (inclusive). Your task is to create an accumulated count array from the given array. The accumulated count array at index `i` should contain the sum of counts from index `0` to `i` of the count array.

#### [](#approach-2)Approach:

The problem can be broken down into three main steps:

-

**Counting Occurrences:**

We first need to determine the frequency of each integer in the given array. This is achieved by using a `count` array of size `k`, where each index corresponds to the integers from `0` to `k-1`. We iterate through the input array and increment the corresponding index in the `count` array for each integer encountered.

-

**Accumulating Counts:**

Once we have the frequency of each integer, we need to create the accumulated count array. The accumulated count at index `i` is simply the sum of the counts from index `0` to `i`. This can be efficiently calculated by iterating through the `count` array and maintaining a running sum.

-

**Output the Result:**

Finally, the accumulated count array is printed as the result.

#### [](#complexity-analysis-3)Complexity Analysis:

- **Time Complexity:** The algorithm runs in `O(n + k)` time, where `n` is the length of the array and `k` is the range of the elements. Counting the occurrences takes `O(n)` time, and calculating the accumulated count takes `O(k)` time.

- **Space Complexity:** The space complexity is `O(k)`, primarily due to the `count` and `accumulated_count` arrays.

</details>
