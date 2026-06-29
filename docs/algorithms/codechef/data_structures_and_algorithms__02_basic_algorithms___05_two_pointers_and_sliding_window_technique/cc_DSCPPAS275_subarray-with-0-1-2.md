# Subarray with 0, 1, 2

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | DSCPPAS275 |
| Difficulty Band | Two Pointers and Sliding Window Technique |
| Path | Data Structures and Algorithms |
| Lesson | Sliding Window |
| Official Link | [DSCPPAS275](https://www.codechef.com/practice/course/two-pointers/SLIDINGWINDO/problems/DSCPPAS275) |

---

## Problem Statement

You are given an array $arr$ consisting of only the integers $0$, $1$, and $2$. Your task is to find the number of contiguous subarrays that contain at least one occurrence of each integer (0, 1, and 2).

---

## Input Format

- The first line contains one integer $n$, the size of the array.                                                                                                               - Next line contains $n$ integers $arr[0],arr[1]...arr[n]$, representing the elements of the array.

---

## Output Format

- Print the count of all subarrays that contains at least one occurrence of each integer $(0, 1,
 2)$.

---

## Constraints

- $1 \leq n \leq 10^5$
- $0 \leq arr[i] \leq 2$

---

## Examples

**Example 1**

**Input**

```text
4
0 1 2 0
```

**Output**

```text
3
```

**Explanation**

The subarrays are:
[0, 1, 2], [0, 1, 2, 0], [1, 2, 0]
Each subarray contains at least one 0, 1, 2.

**Example 2**

**Input**

```text
4
1 2 1 2
```

**Output**

```text
0
```

**Explanation**

There is no subarray such that each contains all three elements. so the answer is 0.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

#### [](#problem-statement-1)Problem Statement:

Given an array `arr` consisting of only the integers `0`, `1`, and `2`, the task is to find the number of contiguous subarrays that contain at least one occurrence of each integer (0, 1, and 2).

#### [](#approach-2)Approach:

To solve this problem, we can use the sliding window (two-pointer) technique in combination with a hashmap (or unordered_map) to efficiently count the number of valid subarrays that include at least one `0`, `1`, and `2`. The key idea is to maintain a window that expands to include more elements and contracts when it has included at least one of each of the required numbers.

### [](#time-complexity-3)Time Complexity:

-

**Time Complexity:** The algorithm runs in `O(N)` time, where `N` is the length of the array. This is because each element is processed at most twice—once by the `j` pointer and once by the `i` pointer.

-

**Space Complexity:** The space complexity is `O(1)` in terms of the number of distinct elements (since `countMap` only stores counts for `0`, `1`, and `2`).

</details>
