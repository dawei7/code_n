# Rotate the array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | ROTATEARRAY |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [ROTATEARRAY](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/ROTATEARRAY) |

---

## Problem Statement

You are given an integer array $nums$. Rotate the array to the right by $k$ positions, where $k$ is a non-negative integer. \
***For example***: \
Given the array [10, 20, 30, 40, 50], rotating it two times to the right results in: \
First rotation - [50, 10, 20, 30, 40] \
Second rotation - [40, 50, 10, 20, 30] \
You need to implement a solution that operates **in-place** and uses only **$O(1)$** additional space.

You don’t need to print any values; simply edit the values of the array.

## Function Declaration

### Function Name

$rotate$ – This function rotates an array to the right by $k$ positions in-place.

### Parameters

* $nums$ : An array of integers.
* $k$ : A non-negative integer representing the number of right rotations.

### Return Value

* This function does **not** return anything.
* The array $nums$ is modified in-place.

## Constraints

* $1 \leq nums.length \leq 10^5$
* $−2^\text{31} \leq nums[i] \leq 2^\text{31} − 1$
* $0 \leq k \leq 10^5$
* Rotation must be done using **O(1)** extra space

#### Follow up:

* Can you think of multiple approaches to solve this problem? (There are at least **three** different strategies.)

---

## Input Format

* The first line contains two integers $N$ and $K$ — the size of the array and the number of right rotations.
* The second line contains $N$ space-separated integers representing the array elements.

---

## Output Format

* Print the rotated array in a line (space-separated).

---

## Constraints

* 1 <= nums.length <= 10^5
* -2^31 <= nums[i] <= 2^31 - 1
* 0 <= k <= 10^5

---

## Examples

**Example 1**

**Input**

```text
5 2
10 20 30 40 50
```

**Output**

```text
40 50 10 20 30
```

**Explanation**

rotate 1 step to the right: [50,10,20,30,40]
rotate 2 steps to the right: [40,50,10,20,30]

**Example 2**

**Input**

```text
5 3
7 8 9 1 2
```

**Output**

```text
9 1 2 7 8
```

**Explanation**

rotate 1 step to the right: [2,7,8,9,1]
rotate 2 steps to the right: [1,2,7,8,9]
rotate 3 steps to the right: [9,1,2,7,8]

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

You are given an array `nums` of size `n` and an integer `k`. The task is to **rotate the array to the right by `k` steps**.

Rotation means that each element is shifted to the right by one index, and the last element moves to the first position.

---

## Example

**Input:**

```
nums = [1, 2, 3, 4, 5, 6, 7], k = 3
```

**Output:**

```
[5, 6, 7, 1, 2, 3, 4]
```

Explanation:

* After 1st rotation → `[7, 1, 2, 3, 4, 5, 6]`
* After 2nd rotation → `[6, 7, 1, 2, 3, 4, 5]`
* After 3rd rotation → `[5, 6, 7, 1, 2, 3, 4]`

---

## Key Observations

1. Rotating by `k` steps where `k >= n` is equivalent to rotating by `k % n`.

   * Example: rotating by `n` or `2n` returns the same array.

2. A naive approach would perform one rotation at a time, resulting in `O(n * k)` time complexity, which is inefficient for large `k`.

3. We need an **efficient `O(n)` solution** with **constant extra space**.

---

## Efficient Approach: Reversal Algorithm

We can solve the problem in **3 steps using array reversal**:

1. **Reverse the whole array.**

   * Example: `[1, 2, 3, 4, 5, 6, 7]` → `[7, 6, 5, 4, 3, 2, 1]`

2. **Reverse the first `k` elements.**

   * With `k = 3`: `[7, 6, 5, 4, 3, 2, 1]` → `[5, 6, 7, 4, 3, 2, 1]`

3. **Reverse the remaining `n - k` elements.**

   * Final result: `[5, 6, 7, 1, 2, 3, 4]`

---

## Complexity Analysis

* **Time Complexity:**

  * Each reversal is `O(n)`.
  * Total = `O(n)`

* **Space Complexity:**

  * Only constant extra space is used for swapping.
  * `O(1)`

---

## Edge Cases to Consider

1. `n = 0` → empty array should remain empty.
2. `n = 1` → single element array remains unchanged.
3. `k = 0` → no rotation needed.
4. `k` is a multiple of `n` → array remains unchanged.
5. Very large `k` → reduced to `k % n`.

---

## Conclusion

The **reversal method** is an elegant and efficient solution to the rotate array problem. It reduces the problem to a sequence of **three reversals** and works in `O(n)` time with `O(1)` extra space.

</details>
