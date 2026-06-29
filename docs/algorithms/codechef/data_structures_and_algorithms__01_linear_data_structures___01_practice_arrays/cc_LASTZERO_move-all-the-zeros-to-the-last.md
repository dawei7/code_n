# Move all the zeros to the last

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | LASTZERO |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [LASTZERO](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/LASTZERO) |

---

## Problem Statement

You are given an integer array $nums$. Your task is to **shift all the zeroes to the end** of the array, while keeping the **relative order of the non-zero elements unchanged**.

**Important:** The transformation must be done **in-place** without using an extra array.

## Function Declaration

### **Function Name**

$moveZeroes$ — This function shifts all zeroes in the array to the end, while preserving the order of the remaining elements.

### Parameters

$nums$: A reference to a array of integers.

* The array contains both zero and non-zero integers.
* You must modify the array directly (in-place), without allocating another array.

### Return Value

This function returns **void**.
The rearranged elements must be stored directly inside the original $nums$ array.

`The input and output formats provided below are only for testing with custom inputs.`

## Constraints
* $1 \leq \text{T} \leq 10$
* $1 \leq \text{nums.length} \leq 10^4$
* $-2^{31} \leq \text{nums}[i] \leq 2^{31} - 1$

---

## Input Format

The first line contains a single integer
**T** — the number of test cases.

For each test case:

* The first line contains an integer
  **N** — the length of the array.
* The second line contains **N** space-separated integers representing the array.

---

## Output Format

* For each test case, print the modified array after all zeroes have been moved to the end.
* If the array has only non-zero numbers, print it unchanged.

---

## Examples

**Example 1**

**Input**

```text
3
7
4 0 5 0 0 7 8
5
0 2 0 0 9
1
3
```

**Output**

```text
4 5 7 8 0 0 0 
2 9 0 0 0 
3
```

**Separated test cases**

#### Test case 1

**Input for this case**

```text
7
4 0 5 0 0 7 8
```

**Output for this case**

```text
4 5 7 8 0 0 0
```



#### Test case 2

**Input for this case**

```text
5
0 2 0 0 9
```

**Output for this case**

```text
2 9 0 0 0
```



#### Test case 3

**Input for this case**

```text
1
3
```

**Output for this case**

```text
3
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

You are given an array of integers. The task is to move all the zeroes in the array to the end, while keeping the **relative order of the non-zero elements unchanged**.

For example:

* Input: `[0, 1, 0, 3, 12]`
* Output: `[1, 3, 12, 0, 0]`

---

## Key Insights

1. We want to **preserve the order** of non-zero elements.
2. Simply pushing zeroes to the end without reordering others won’t work.
3. A naïve solution (removing zeroes and appending them later) may require extra space, but the problem can be solved **in-place** with **O(1) extra space**.

---

## Approach

### Step 1: Use a pointer for the "insertion position"

* Keep a pointer `index` that tells us where the next non-zero element should go.
* Initially, `index = 0`.

### Step 2: Traverse the array

* For each element:

  * If it is **non-zero**, place it at `nums[index]` and increment `index`.
  * If it is zero, skip it.

### Step 3: Fill remaining positions with zeroes

* After placing all non-zero elements, all positions from `index` to the end of the array must be filled with zeroes.

---

## Example Walkthrough

Input: `[0, 1, 0, 3, 12]`

* Start with `index = 0`.
* Traverse array:

  * `0` → skip.
  * `1` → place at `nums[0]`, increment `index = 1`.
  * `0` → skip.
  * `3` → place at `nums[1]`, increment `index = 2`.
  * `12` → place at `nums[2]`, increment `index = 3`.
* Now array looks like `[1, 3, 12, 3, 12]`.
* Fill remaining positions with zeroes: `[1, 3, 12, 0, 0]`.

---

## Complexity Analysis

* **Time Complexity:** `O(n)`

  * Each element is visited once in the traversal.
  * Filling zeroes also takes at most `O(n)`.
* **Space Complexity:** `O(1)`

  * Only a constant amount of extra variables are used.

---

## Edge Cases to Consider

1. **All zeroes** → Input: `[0, 0, 0]` → Output: `[0, 0, 0]`.
2. **No zeroes** → Input: `[1, 2, 3]` → Output: `[1, 2, 3]`.
3. **Single element** → `[0]` → `[0]` or `[5]` → `[5]`.
4. **Large arrays** with mixed zero and non-zero values to test efficiency.

---

✅ This approach is **optimal** (linear time, in-place, stable order).

</details>
