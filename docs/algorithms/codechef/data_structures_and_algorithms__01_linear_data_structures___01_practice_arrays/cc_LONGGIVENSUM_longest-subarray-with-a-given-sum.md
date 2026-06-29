# Longest subarray with a given sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LONGGIVENSUM |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [LONGGIVENSUM](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/LONGGIVENSUM) |

---

## Problem Statement

You are given an array of integers $nums$ with length $n$ and an integer $k$. Your task is to determine the length of the longest continuous sub-array whose elements sum up exactly to $k$. If there is no such sub-array, return $0$.

## **Function Declaration**

### **Function Name**

$longestSubarraySum$ – This function computes the length of the longest continuous sub-array whose sum is exactly equal to $k$.

### **Parameters**

* $arr$ : A vector of integers of length $n$, representing the array.
* $k$ : An integer representing the required target sum.

### **Return Value**

* Returns a single integer —
  the **maximum length** of any continuous sub-array whose sum equals $k$.
  If no such sub-array exists, the function returns $0$.

`The input and output formats given below are only if you want to test using custom inputs.`

---

## **Constraints**

* $1 \leq T \leq 10^5$
* $1 \leq n \leq 10^5$
* $-10^5 \leq arr[i] \leq 10^5$
* $-10^9 \leq k \leq 10^9$

---

## Input Format

* The first line of input will contain a single integer **$T$**, denoting the number of test cases.
* Each test case consists of multiple lines of input.

  * The first line of each test case contains two space-separated integers **$n$** and **$k$** — the length of the array and the required sum respectively.
  * The next line contains **$n$** space-separated integers, representing the array **`nums`**.

---

## Output Format

For each test case, output on a new line a single integer —
the **length of the longest continuous subarray whose sum is exactly $k$**.
If no such subarray exists, output **0**.

---

## Constraints

- $1 \leq n \leq 10^{5}$
- $-10^{5} \leq \text{nums}[i] \leq 10^{5}$
- $-10^{9} \leq k \leq 10^{9}$

---

## Examples

**Example 1**

**Input**

```text
3
6 15
10 5 2 7 1 9
3 6
-3 2 1
5 5
1 2 3 2 1
```

**Output**

```text
4
0
2
```

**Explanation**

* In the first test case the sub-array `[5, 2, 7, 1]` has a total sum of 15 and is the longest one with this sum. It starts at index 1 and ends at index 4, so its length is 4.
* In the second test case there is no continuous sub-array in the array that adds up to 6. Hence, the result is 0.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 15
10 5 2 7 1 9
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
3 6
-3 2 1
```

**Output for this case**

```text
0
```



#### Test case 3

**Input for this case**

```text
5 5
1 2 3 2 1
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

### Problem Restatement

We are given an array of integers and a target sum `k`.
The task is to find the **length of the longest contiguous subarray** whose sum is exactly equal to `k`.

---

### Key Observations

1. **Brute Force Approach**

   * One naive way is to check all possible subarrays, compute their sums, and check if they equal `k`.
   * This would take **O(n²)** time for sum computation (or **O(n³)** if recomputed each time).
   * This is inefficient for large arrays.

2. **Prefix Sum Concept**

   * Define a **prefix sum** at index `i` as the sum of all elements from the start up to index `i`.
   * If we want a subarray from index `l` to `r` to have sum `k`, then:

     ```
     prefix[r] - prefix[l-1] = k
     ```

     which rearranges to:

     ```
     prefix[l-1] = prefix[r] - k
     ```
   * So, if we know the prefix sum up to `r`, we just need to check if `prefix[r] - k` appeared before.

3. **Hash Map / Dictionary Usage**

   * We maintain a hash map that stores the **first occurrence of each prefix sum**.
   * At every index `i`, compute `prefix[i]`:

     * If `prefix[i] == k`, then the subarray `[0...i]` is valid.
     * If `prefix[i] - k` exists in the map at some earlier index `j`, then the subarray `[j+1...i]` has sum `k`.
     * Update the maximum length accordingly.
   * Important: we store the **first index** where each prefix sum occurs, because that gives the longest subarray.

---

### Algorithm

1. Initialize:

   * `prefixSum = 0`
   * `maxLen = 0`
   * A hash map `prefixIndex` to store prefix sums.
2. Iterate through the array:

   * Update `prefixSum` by adding the current element.
   * If `prefixSum == k`, update `maxLen` as the whole subarray length so far.
   * If `(prefixSum - k)` is in the map, calculate subarray length from that index and update `maxLen`.
   * If `prefixSum` is not already in the map, store it with the current index.
3. Return `maxLen`.

---

### Complexity

* **Time Complexity**: `O(n log n)` (one pass through the array).
* **Space Complexity**: `O(n)` (to store prefix sums in the map).

---

### Example Walkthrough

Input:

```
6 15
10 5 2 7 1 9
```

Step-by-step:

* prefix = 10 → not equal to 15, store {10:0}
* prefix = 15 → equals `k`, update maxLen = 2 (subarray \[0..1])
* prefix = 17 → check (17-15=2), not found
* prefix = 24 → check (24-15=9), not found
* prefix = 25 → check (25-15=10), found at index 0 → subarray length = 4 (from 1..4) → maxLen = 4
* prefix = 34 → check (34-15=19), not found

Answer: **4**

---

### Edge Cases

1. **No subarray exists** → Output should be `0`.
   Example: `n=3, k=8, arr=[1,2,3]`.
2. **Negative numbers** → The algorithm still works, since prefix sum handles both positives and negatives.
   Example: `n=3, k=-3, arr=[-2,-1,4]`.
3. **Entire array matches** → The longest subarray could be the whole array.
   Example: `n=5, k=15, arr=[1,2,3,4,5]`.

</details>
