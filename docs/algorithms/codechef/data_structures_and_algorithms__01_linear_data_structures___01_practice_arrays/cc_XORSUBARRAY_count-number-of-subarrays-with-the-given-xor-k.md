# Count number of subarrays with the given xor K

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | XORSUBARRAY |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [XORSUBARRAY](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/XORSUBARRAY) |

---

## Problem Statement

You are given an array of integers $arr$ and a target integer $targetXOR$. Your task is to compute the total number of **contiguous subarrays** whose **XOR of all elements equals $targetXOR$**.

## **Function Declaration**

### **Function Name**

$countSubarraysWithXOR$ – Counts the number of contiguous subarrays whose XOR equals the target value.

### **Parameters**

* $arr$ : A list/array of integers.
* $k$ : An integer representing the target XOR value.

### **Return Value**

* Returns an **integer** — \
  the number of contiguous subarrays whose XOR is exactly equal to $k$.

## Constraints:

* $1 \leq arr.length \leq 10^5$
* $0 \leq arr[i] \leq 10^9$
* $0 \leq targetXOR \leq 10^9$

---

## Input Format

* $T$ → number of test cases
* For each test case:

  * Line 1 → $n$ (array size) and $k$ (target XOR)
  * Line 2 → **n integers** representing the array

---

## Output Format

One number per test case.

---

## Examples

**Example 1**

**Input**

```text
3
5 5
3 8 2 6 3
5 1
1 2 3 4 5
3 0
7 1 3
```

**Output**

```text
1
4
0
```

**Explanation**

* [3] = 3
* [3^8] = 11
* [3^8^2] = 9
* [3^8^2^6] = 15
* [3^8^2^6^3] = 12
* [8] = 8
* [8^2] = 10
* [8^2^6] = 12
* [8^2^6^3] = 15
* [2] = 2
* [2^6] = 4
* [2^6^3] = 7
* [6] = 6
* [6^3] = 5  ? this is the only subarray with XOR = 5
* [3] = 3

**Separated test cases**

#### Test case 1

**Input for this case**

```text
5 5
3 8 2 6 3
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
5 1
1 2 3 4 5
```

**Output for this case**

```text
4
```



#### Test case 3

**Input for this case**

```text
3 0
7 1 3
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

You are given an array of integers and an integer `k`. Your task is to **count the number of subarrays** whose elements’ XOR equals `k`.

A **subarray** is a contiguous portion of the array.

**Example:**

* Input: `[4, 2, 2, 6, 4]`, `k = 6`
* Output: `4`
* Explanation: Subarrays with XOR = 6 are `[4,2]`, `[2,2,6]`, `[6]`, `[4,2,2,6,4]`.

---

## Observations

1. **Brute force approach:**

   * Iterate over all possible subarrays and compute their XOR.
   * Complexity: `O(n^2)` for computing all subarrays.
   * **Not efficient** for large arrays (`n <= 10^5`).

2. **Optimized approach using prefix XOR:**

   * Define `prefixXOR[i]` as the XOR of all elements from index `0` to `i`.
   * XOR of a subarray `[l, r]` can be computed as:

     ```
     subarrayXOR = prefixXOR[r] ^ prefixXOR[l-1]
     ```

     (if `l = 0`, then subarrayXOR = prefixXOR\[r]).

---

## Key Insight

We want `subarrayXOR = k`. Using prefix XOR:

```
prefixXOR[r] ^ prefixXOR[l-1] = k
=> prefixXOR[l-1] = prefixXOR[r] ^ k
```

This means:

* For every index `r`, if there exists a prefix XOR `prefixXOR[l-1]` equal to `prefixXOR[r] ^ k`, then the subarray `[l, r]` has XOR = k.
* Also, if `prefixXOR[r] == k`, then the subarray from `0` to `r` counts.

---

## Algorithm

1. Initialize a **map/dictionary** to store the frequency of prefix XORs seen so far.
2. Initialize `prefixXOR = 0` and `count = 0`.
3. Traverse the array:

   * Update `prefixXOR ^= arr[i]`.
   * If `prefixXOR == k`, increment `count` (subarray from start).
   * If `prefixXOR ^ k` exists in the map, add its frequency to `count`.
   * Increment the frequency of `prefixXOR` in the map.
4. Return `count`.

---

## Complexity Analysis

* **Time Complexity:** `O(n)`

  * We traverse the array once, and all map operations (insert/get) are `O(1)` on average.
* **Space Complexity:** `O(n)`

  * For storing prefix XOR frequencies in a map.

---

## Edge Cases

1. **Single element arrays**

   * Example: `[5]`, `k = 5` → count = 1
   * Example: `[3]`, `k = 5` → count = 0

2. **All elements same**

   * Example: `[2,2,2,2]`, `k = 2` → count = 4
   * XOR of consecutive elements may cancel out, forming subarrays with XOR = 0.

3. **XOR = 0**

   * Subarrays whose XOR cancels out completely.
   * Example: `[1,2,3]`, `k = 0` → `[1,2,3]` has XOR = 0.

4. **Large numbers**

   * Each number can be up to `10^9`.
   * Make sure data types can handle XOR results without overflow.

5. **No subarray equals k**

   * The algorithm correctly returns `0`.

6. **Stress test**

   * Large array size (`n = 10^5`) and random numbers.
   * Optimized approach works efficiently.

---

## Summary

* **Prefix XOR + hashmap** is the key technique.
* Brute force is too slow (`O(n^2)`), optimized approach is `O(n)` time and `O(n)` space.
* Works for all edge cases: single elements, zeros, repeated elements, large numbers.
* This approach is a classic **XOR subarray counting problem** that leverages **bitwise properties of XOR**.

</details>
