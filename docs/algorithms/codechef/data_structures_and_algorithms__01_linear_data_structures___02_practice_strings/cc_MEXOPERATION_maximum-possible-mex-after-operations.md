# Maximum Possible MEX After Operations

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | MEXOPERATION |
| Difficulty Band | Practice Strings |
| Path | Data Structures and Algorithms |
| Lesson | Strings |
| Official Link | [MEXOPERATION](https://www.codechef.com/practice/course/strings/STRINGSPRO/problems/MEXOPERATION) |

---

## Problem Statement

You are given an integer array nums of length N and an integer value.

- In one operation, you may add or subtract value from any element of the array any number of times (including zero).
- Each element can be modified independently, and values may become negative.
- Your task is to determine the maximum possible MEX of the array after performing these operations.

**The MEX (Minimum EXcluded number) of an array is the smallest non-negative integer that is not present in the array.**

---

## Function Declaration

### Function Name
$findMaxMex$

### Parameters

* $nums$ : A reference to an integer array of size $N$.
* $value$ : An integer that can be added to or subtracted from any array element any number of times.

### Return Value

* Returns an integer representing the **maximum possible MEX** that can be achieved after performing any number of operations.

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N, value \leq 10^5$
- $-10^9 \leq nums[i] \leq 10^9$

---

## Input Format

* The first line contains a single integer $T$ — the number of test cases.
* For each test case:
  * The first line contains two integers $N$ and $value$ — the size of the array and the operation value.
  * The second line contains $N$ integers — the elements of the array $nums$.

---

## Output Format

* For each test case, print a single integer — the **maximum possible MEX** after performing the operations.

---

## Constraints

- $1 \le T \le 10$
- $1 \le N,\ \text{value} \le 10^{5}$
- $-10^{9} \le \text{nums}[i] \le 10^{9}$

---

## Examples

**Example 1**

**Input**

```text
2
6 5
1 -10 7 13 6 8
6 7
1 -10 7 13 6 8
```

**Output**

```text
4
2
```

**Explanation**

**Test Case 1 :**
  nums = [1, -10, 7, 13, 6, 8], value = 5

  Chef can perform the following operations:

  * Add **5** twice to `-10` -> `0`
  * Subtract **5** once from `7` -> `2`
  * Subtract **5** twice from `13` -> `3`

  The resulting array can be:

  ```
  [1, 0, 2, 3, 6, 8]
  ```

  The smallest missing non-negative integer (**MEX**) is **4**.

**Test Case 2 :**
  nums = [1, -10, 7, 13, 6, 8], value = 7

  Possible operation:

  * Subtract **7** once from `7` -> `0`

  The resulting array can be:

  ```
  [1, -10, 0, 13, 6, 8]
  ```
  The smallest missing non-negative integer (**MEX**) is **2**.

**Separated test cases**

#### Test case 1

**Input for this case**

```text
6 5
1 -10 7 13 6 8
```

**Output for this case**

```text
4
```



#### Test case 2

**Input for this case**

```text
6 7
1 -10 7 13 6 8
```

**Output for this case**

```text
2
```



---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

# Problem Understanding

You are given:

- An integer array `nums` of length **N**
- An integer `value`

In one operation, you may **add or subtract** `value` **any number of times** (including zero) to any element of `nums`.

Your goal is to find the **maximum possible MEX** (**Minimum EXcluded number**) of the array after performing any number of allowed operations.

---

# Intuition

Notice that when we can add or subtract `value` any number of times,\
each number can be **converted to any number that shares the same remainder modulo** `value`.

Example:\
If `value = 5`, then all numbers with remainder `2` (like 2, 7, 12, -3, …) belong to the same “class”.

Thus, to form numbers `0, 1, 2, …` consecutively,\
we only need to **track how many times each remainder appears**.

---

# Approach

Create a **frequency array** `freq` of size `value` to count how many numbers belong to each remainder class.

`freq[r] = number of elements with (num % value == r)`

Start from **mex = 0**, and for each next number:

- Compute its remainder → `rem = mex % value`
- If we have at least one number with that remainder (`freq[rem] > 0`):

   - Use it (decrement `freq[rem]`)
   - Increment `mex`

- Otherwise → we can’t form this number → stop

Return `mex`

---

# Complexity Analysis

| Type                 | Explanation                                      | Complexity     |
| -------------------- | ------------------------------------------------ | -------------- |
| **Time Complexity**  | One pass for counting + one pass for MEX finding | **O(N + MEX)** |
| **Space Complexity** | Frequency array of size `value`                  | **O(value)**   |

</details>
