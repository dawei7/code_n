# Subarray Sum equals k

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | HASHP03 |
| Difficulty Rating | 1696 |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [HASHP03](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/HASHP03) |

---

## Problem Statement

Given an array of integers $nums$ and an integer $k$, return the total number of subarrays whose sum equals to $k$.

Note: A **subarray** is a contiguous non-empty sequence of elements within an array.

---

### **Function Declaration**

#### Function Name
$subarraySum$ – This function computes the total number of continuous subarrays whose sum is exactly equal to $k$.

### **Parameters**

* $nums$ : An array of integers of length $n$, representing the input array.
* $n$ : An integer representing the size of the array.
* $k$ : An integer representing the target sum.

### **Return Value**

Returns a single integer — the total number of continuous subarrays whose sum equals $k$.
If no such subarray exists, the function returns $0$.

### Constraints
- $1 \le N \le 2*10^4$
- $ -1000 \le nums[i] \le 1000$
- $ -10^7 \le k \le 10^7$

---

## Input Format

- The first line contains n the length of an array.
- The second line contains an array of length n
- The third line contains an integer representing the target sum.

---

## Output Format

- Output the total number of subarrays whose sum equals to $k$.

---

## Constraints

- $1 \le N \le 2*10^4$
- $ -1000 \le nums[i] \le 1000$
- $ -10^7 \le k \le 10^7$

---

## Examples

**Example 1**

**Input**

```text
3
1 1 1
2
```

**Output**

```text
2
```

**Explanation**

There are two subarrays whose sum equals 2:
- [1, 1] (starting at index 0, ending at index 1)
- [1, 1] (starting at index 1, ending at index 2)

**Example 2**

**Input**

```text
3
1 2 3
3
```

**Output**

```text
2
```

**Explanation**

There are two subarrays whose sum equals 3:
- [1, 2] (starting at index 0, ending at index 1)
- [3] (starting at index 2, ending at index 2)

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

Problem Link - [Subarray Sum equals k in Hashing](https://www.codechef.com/learn/course/hashing/HASH04/problems/HASHP03)

### [](#problem-statement-1)Problem Statement:

Given an array `nums` of integers and an integer `k`, you need to find the total number of continuous subarrays whose sum equals `k`.

### [](#approach-1-brute-force-2)Approach 1: Brute Force

In this approach, we consider every possible subarray of the given array nums, compute the sum of elements for each subarray, and check if the sum is equal to k. If it matches, we increment the count of valid subarrays.

### [](#complexity-3)Complexity:

- **Time Complexity:** `O(N^3)` Finding all subarrays takes `O(N^2)` Summing the elements of each subarray takes `O(N)`.

- **Space Complexity:** `O(1)` No additional space used.

### [](#approach-2-cumulative-sum-and-hash-map-4)Approach 2: Cumulative sum and Hash Map

The problem is solved using a **Prefix Sum** and **Hash Map** (or unordered_map in C++). The idea is to use the prefix sum technique to track subarray sums efficiently.

### [](#detailed-explanation-5)Detailed Explanation

**1. Prefix Sum:**

- The **prefix sum** up to an index `i` is the sum of all elements from the start of the array to `i`. It helps quickly calculate subarray sums.

**2. Key Insight**:

- If the sum of a subarray from index `i` to `j` is `k`, then:

sum[0…j]−sum[0…(i−1)]=k

- This means if the current prefix sum minus `k` exists in our map, there’s a subarray summing to `k` between those indices.

**3. Using a Map**:

- Use an unordered map to store prefix sums and their frequencies.

- For each new prefix sum, check if `sum - k` exists in the map. If so, it means a subarray with sum `k` ends at the current index.

### [](#complexity-6)Complexity:

- **Time Complexity:** `O(N)` We traverse the array once and use the hash map for constant-time lookups and updates.

- **Space Complexity:** `O(N)` The hash map stores prefix sums. In the worst case, all prefix sums could be unique, so the hash map could contain `N` entries.

</details>
