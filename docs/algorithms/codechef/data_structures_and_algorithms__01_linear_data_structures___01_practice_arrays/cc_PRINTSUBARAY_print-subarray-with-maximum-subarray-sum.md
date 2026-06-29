# Print subarray with maximum subarray sum

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | PRINTSUBARAY |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [PRINTSUBARAY](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/PRINTSUBARAY) |

---

## Problem Statement

Given an integer array $nums$, find the longest contiguous subarray (containing at least one element) with the largest sum and **print the elements of that subarray**.

#### Note:
If two or more sub arrays have the same length and same max sum then you should return the leftmost array.

## **Function Declaration**

### **Function Name**

$maxSubArray$ – This function finds the **longest contiguous subarray** (with at least one element) that has the **maximum possible sum**, and returns the elements of that subarray.
If multiple subarrays have the **same maximum sum and same length**, the function returns the **leftmost** such subarray.

### **Parameters**

* $nums$ : A reference to a vector of integers representing the array.

  * Each element can be negative, zero, or positive.

### **Return Value**

* Returns an array containing the elements of the contiguous subarray that:

  * Has the **maximum subarray sum**.
  * If multiple subarrays achieve this sum, the function returns the **longest** one.
  * If still tied, returns the **leftmost** such subarray.

## **Constraints**

* $1 \leq nums.length \leq 10^5$
* $-10^4 \leq nums[i] \leq 10^4$
* The solution must run in **O(N)** time due to input size.

---

## Input Format

* The first line contains a single integer $T$ — the number of test cases.
* For each test case:

  * The first line contains an integer $N$ — the size of the array.
  * The next line contains $N$ space-separated integers representing the array elements.

---

## Output Format

* For each test case, print the elements of the **longest maximum-sum subarray** on a new line.

---

## Constraints

* 1 <= nums.length <= 10^5

* -10^4 <= nums[i] <= 10^4

---

## Examples

**Example 1**

**Input**

```text
2
6
4 -1 2 1 -5 4
5
1 2 -1 -2 5
```

**Output**

```text
4 -1 2 1
1 2 -1 -2 5
```

**Explanation**

* For the first test case the subarray from index `0` to `3` has the largest sum = `6`.
* The second test case the subarray from index `0` to `4` has the largest sum = `5`.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6
4 -1 2 1 -5 4
```

**Output for this case**

```text
4 -1 2 1
```



#### Test case 2

**Input for this case**

```text
5
1 2 -1 -2 5
```

**Output for this case**

```text
1 2 -1 -2 5
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

You are given an integer array `nums`.
Your task is to find the contiguous subarray (at least one element) that has the **maximum sum**, and **print the elements of that subarray**.

---

## Key Observations

1. A subarray must be **contiguous**, meaning you cannot skip elements.
2. If all numbers are negative, the maximum subarray is just the **largest (least negative) single element**.
3. If there are positive numbers, we need to maximize the sum by choosing an optimal window of consecutive elements.
4. A brute force approach would check all possible subarrays (`O(n^2)` or `O(n^3)`), which is **too slow** for `n` up to `10^5`.

Thus, we need an **efficient algorithm**.

---

## Algorithm (Kadane’s Algorithm with Tracking)

We use **Kadane’s Algorithm**, which runs in **O(n)**.

### Steps:

1. Initialize:

   * `maxSum = nums[0]` → best sum so far.
   * `currSum = nums[0]` → current running sum.
   * `start, end, tempStart` → to track indices of the subarray.

2. Iterate over the array:

   * At each index `i`, decide:

     * Extend the current subarray (`currSum + nums[i]`), OR
     * Start a new subarray at `i` (`nums[i]`).
   * Update `currSum` accordingly.
   * If starting new, reset `tempStart = i`.

3. If `currSum > maxSum`, update:

   * `maxSum = currSum`
   * `start = tempStart`
   * `end = i`

4. At the end, the subarray from `start` to `end` is the answer.

---

## Example Walkthrough

**Input:**

```
nums = [4, -1, 2, 1, -5, 4]
```

**Step-by-step:**

* Start: `currSum = 4`, `maxSum = 4`, subarray = `[4]`
* i=1 → add -1 → `currSum = 3`, still better than just -1 → subarray `[4, -1]`
* i=2 → add 2 → `currSum = 5`, update max → subarray `[4, -1, 2]`
* i=3 → add 1 → `currSum = 6`, update max → subarray `[4, -1, 2, 1]`
* i=4 → add -5 → `currSum = 1`, no update
* i=5 → add 4 → `currSum = 5`, no update

Final Answer: Subarray = `[4, -1, 2, 1]`, Max Sum = `6`.

---

## Complexity Analysis

* **Time Complexity:** `O(n)` (single pass through the array).
* **Space Complexity:** `O(1)` extra space (only variables for indices and sums).

---

## Edge Cases

1. **Single element array** → The array itself is the answer.

   * Input: `[5]` → Output: `[5]`
2. **All negative numbers** → Choose the largest single element.

   * Input: `[-3, -7, -2, -8]` → Output: `[-2]`
3. **Mixed numbers with big negatives** → Algorithm correctly skips the large negative block.

   * Input: `[2, 3, -10, 4, 5]` → Output: `[4, 5]`
4. **Large array (up to 10^5 elements)** → Kadane’s runs in linear time efficiently.

---

## Final Notes

* This is a classic dynamic programming problem.
* Kadane’s Algorithm is the optimal solution for **maximum subarray sum**.
* With index tracking, we can also **recover and print the subarray**.

</details>
