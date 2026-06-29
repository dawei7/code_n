# Missing number in permutation

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MISSINPERM |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [MISSINPERM](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/MISSINPERM) |

---

## Problem Statement

Given a **permutation** of $n$ distinct numbers chosen from the range $[0, n]$, find the **one missing number** that does not appear in the array.

## What is a Permutation?

A **permutation** is a rearrangement of elements in a set.

* Example: If the set is ${0, 1, 2, 3}$, then $[3, 1, 0, 2]$ is a permutation because it contains all elements exactly once in some order.
* In this problem, the array represents a **permutation of $n$ numbers** from $[0, n]$, except that one element is missing.

## Function Declaration

### Function Name

$missingNumber$ – This function finds the missing number in a permutation.

### Parameters

* $nums$ : An array of $n$ distinct integers taken from the range $[0, n]$.

### Return Value

* Returns a single integer — the **missing number** from the permutation.

## Constraints

* $1 \leq T \leq 100$
* $n == nums.length$
* $1 \leq n \leq 10^4$
* $0 \leq nums[i] \leq n$
* All elements in $nums$ are unique

## Follow-up

Can you solve this in **O(n) time** and **O(1) extra space**?

---

## Input Format

* The first line contains a single integer $T$ — the number of test cases.
* For each test case:

  * The first line contains a single integer $N$ — the size of the array.
  * The second line contains $N$ space-separated integers representing the permutation array.

---

## Output Format

* For each test case, print the **missing number** on a new line.

---

## Constraints

* n == nums.length
* 1 <= n <= 10^4
* 0 <= nums[i] <= n
* All elements in `nums` are **unique**

---

## Examples

**Example 1**

**Input**

```text
3
2
2 0
4
4 2 1 0
3
1 2 3
```

**Output**

```text
1
3
0
```

**Explanation**

* In the first test case the numbers should form a permutation of `[0,1,2]`, but `1` is missing.
* In the second test case the numbers should form a permutation of `[0, 1, 2, 3, 4]`, but `3` is missing.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
2
2 0
```

**Output for this case**

```text
1
```



#### Test case 2

**Input for this case**

```text
4
4 2 1 0
```

**Output for this case**

```text
3
```



#### Test case 3

**Input for this case**

```text
3
1 2 3
```

**Output for this case**

```text
0
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

You are given an array containing `n` distinct numbers taken from the range `0` to `n`. Since one number is missing from this range, the task is to find and return the missing number.

---

## Key Observations

1. The array has `n` numbers, but the full range `0...n` contains `n+1` numbers.
2. Therefore, exactly one number from `0` to `n` is missing in the array.
3. The problem essentially reduces to comparing the sum or pattern of the full range with what we currently have.

---

## Approaches

### 1. **Mathematical Summation (Efficient and Simple)**

* The sum of the first `n` natural numbers (from `0` to `n`) can be calculated using the formula:

  $$
  \text{Sum}(0...n) = \frac{n \cdot (n+1)}{2}
  $$
* Compute the sum of elements in the given array.
* The missing number is simply the difference:

  $$
  \text{Missing} = \text{Sum}(0...n) - \text{Sum of array}
  $$

**Complexity:**

* Time: `O(n)` (single pass to calculate array sum)
* Space: `O(1)` (no extra space required)

---

### 2. **XOR Approach (Bit Manipulation)**

* XOR has a useful property: `a ^ a = 0` and `a ^ 0 = a`.
* If we XOR all numbers from `0` to `n` and also XOR all elements in the array, the common numbers cancel out.
* The remaining value will be the missing number.

**Steps:**

1. Initialize `xor = 0`.
2. XOR all numbers from `0` to `n`.
3. XOR all elements of the array with it.
4. The result is the missing number.

**Complexity:**

* Time: `O(n)`
* Space: `O(1)`

---

### 3. **Sorting and Linear Scan**

* Sort the array.
* Scan through indices: if at any index `i`, `nums[i] != i`, then `i` is the missing number.
* If no mismatch is found, the missing number is `n`.

**Complexity:**

* Time: `O(n log n)` (due to sorting)
* Space: `O(1)` or `O(n)` depending on the sorting algorithm.

---

## Best Choice

The **summation approach** is the most straightforward and widely used, with optimal time and space complexity.
The **XOR approach** is equally efficient but less intuitive.
The **sorting approach** is not optimal and should only be used if sorting is required for other reasons.

</details>
