# Count subarrays with given sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | COUNTSUBARAY |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [COUNTSUBARAY](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/COUNTSUBARAY) |

---

## Problem Statement

You are given an integer array $arr$ and a target integer $k$.
Your task is to **find the number of contiguous subarrays** in $arr$ whose sum is exactly equal to $k$.

A **subarray** is defined as a continuous and non-empty sequence of elements within the array.

## **Function Declaration**

### **Function Name**

$subarraySum$ – This function computes the number of contiguous subarrays whose sum equals the target value **k**.

### **Parameters**

* $arr$ : A list/array of integers of length **n**, representing the input sequence.
* $k$ : An integer representing the target sum.

### **Return Value**

* Returns an **integer**:
  The total number of contiguous subarrays whose sum is exactly $k$.

## Constraints:

* $1 \leq \text{T} \leq   100$,
* $1 \leq \text{arr.length} \leq   10^5$,
* $-1000 \leq \text{arr}[i] \leq 1000$,
* $-10^7 \leq \text{k} \leq 10^7$

---

## Input Format

* The first line contains $T$ — the number of test cases.
* For each test case:

  * The first line contains $n$ and $k$.
  * The second line contains **n integers** representing the array.

---

## Output Format

* Output a single integer:
  The number of contiguous subarrays whose sum is exactly $k$.

---

## Constraints

* $1 \leq \text{T} \leq   100$,
* $1 \leq \text{arr.length} \leq   10^5$,
* $-1000 \leq \text{arr}[i] \leq 1000$,
* $-10^7 \leq \text{k} \leq 10^7$

---

## Examples

**Example 1**

**Input**

```text
5
4 5
2 3 -1 4
4 1
1 -1 1 1
5 3
1 2 1 -1 1
3 0
0 0 0
6 -2
-1 -1 2 -2 1 -1
```

**Output**

```text
1
5
4
6
5
```

**Explanation**

#### For the first test case:
Let us look at some of the potential subarrays:

* `[2, 3]` -> sum = 5
* `[3, -1, 4]` -> sum = 6 (not valid)
* `[2, 3, -1, 4]` -> sum = 8 (not valid)
* `[2, 3, -1]` -> sum = 4 (not valid)
* `[-1, 4, 2]` (invalid, not contiguous)
  -> Valid ones are `[2,3]` and `[-1,4,2]` -> but since only contiguous are allowed, final valid = `[2,3]`.

We can check that the only valid subarray is `[2,3]` so the answer is 1.

#### For second test case:
Valid subarrays:

* `[1]` (first element)
* `[1, -1, 1]`
* `[-1, 1, 1]`
* `[1]` (second last element)
* `[1]` (last element)

**Separated test cases**

#### Test case 1

**Input for this case**

```text
4 5
2 3 -1 4
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4 1
1 -1 1 1
```

**Output for this case**

```text
5
```



#### Test case 3

**Input for this case**

```text
5 3
1 2 1 -1 1
```

**Output for this case**

```text
4
```



#### Test case 4

**Input for this case**

```text
3 0
0 0 0
```

**Output for this case**

```text
6
```



#### Test case 5

**Input for this case**

```text
6 -2
-1 -1 2 -2 1 -1
```

**Output for this case**

```text
5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

You are given an array of integers and a target integer `k`.
The task is to **find the total number of contiguous subarrays** whose sum equals exactly `k`.

A subarray is a **non-empty contiguous sequence of elements** within the array.

---

## Example

**Input:**

```
nums = [1, 2, 1, -1, 1], k = 3
```

**Output:**

```
4
```

**Explanation:**
The subarrays whose sum is 3 are:

1. `[1, 2]`
2. `[1, 2, 1, -1]`
3. `[2, 1]`
4. `[2, 1, -1, 1]`

---

## Naive Approach (Brute Force)

* Generate **all possible subarrays** using two nested loops.
* For each subarray, compute the sum and check if it equals `k`.

### Time Complexity:

O(n²), where n is the array length.

### Space Complexity:

O(1) (ignoring input storage).

✔️ This works for small input sizes, but becomes too slow when n can be up to 20,000.

---

## Optimized Approach (Prefix Sum + Hash Map)

### Key Observation:

Let’s denote:

* `prefix_sum[i]` = sum of the first i elements of the array.

If at any point,

```
prefix_sum[j] - prefix_sum[i] == k
```

then the subarray from index `i + 1` to `j` sums to `k`.

### Steps:

1. Initialize a hash map to store the frequency of prefix sums.
   Start with `{0: 1}` to handle cases where a prefix sum itself equals `k`.

2. Iterate through the array, maintaining a running `prefix_sum`.

3. At each element:

   * Check if `(prefix_sum - k)` exists in the map:

     * If yes, add its frequency to the count of subarrays.
   * Update the map to increment the frequency of the current `prefix_sum`.

4. Return the total count.

---

## Example Walkthrough

**Input:**

```
nums = [1, 1, 1], k = 2
```

* Initialize map: `{0: 1}`
* prefix\_sum = 0, count = 0

Step by step:

1. Add first element (1): prefix\_sum = 1 → (1 - 2) = -1 → Not in map → Update map: `{0:1, 1:1}`
2. Add second element (1): prefix\_sum = 2 → (2 - 2) = 0 → Found in map (freq = 1) → count = 1 → Update map: `{0:1,1:1,2:1}`
3. Add third element (1): prefix\_sum = 3 → (3 - 2) = 1 → Found in map (freq = 1) → count = 2 → Update map: `{0:1,1:1,2:1,3:1}`

**Answer = 2**

---

## Complexity Analysis

* **Time Complexity:** O(n) — Single pass through the array.
* **Space Complexity:** O(n) — For storing prefix sums in the hash map.

---

## Edge Cases

* Single element → `[5]`, target = 5 → Answer: 1
* All zeros → `[0,0,0,0]`, target = 0 → Many combinations → Answer: 10
* All negatives → `[-1, -1, -1]`, target = -2 → Answer: 2
* Large numbers near boundaries → `[10^7, -10^7, 10^7]`, target = 10^7 → Answer: 2
* Large input size → Array of 20,000 elements → Should run in reasonable time.

---

## conclusion

* The brute-force method is simple but inefficient for large inputs.
* The **prefix sum + hash map approach** is optimal, running in O(n) time and handling negative numbers, zeros, and large arrays effectively.
* This is a classic use of prefix sums for subarray sum problems, combining efficiency and clarity.

</details>
