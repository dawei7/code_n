# Remove Duplicates from Sorted Array

---

| Field | Value |
|---|---|
| Source | CodeChef |
| Code | REMOVEDUPLIC |
| Difficulty Band | Practice Arrays |
| Path | Data Structures and Algorithms |
| Lesson | Arrays |
| Official Link | [REMOVEDUPLIC](https://www.codechef.com/practice/course/arrays/ARRAYSPRO/problems/REMOVEDUPLIC) |

---

## Problem Statement

Chef has an integer array $nums$ sorted in **non-decreasing order**.\
Chef wants to remove all **duplicate elements** from the array **in-place** such that each unique element appears **only once**.

The **relative order** of the elements should remain the same.

After removing the duplicates, let the number of unique elements be $K$.\
The first $K$ elements of the array should contain the unique elements in their original order.\
The values beyond the first $K$ elements do not matter.\
Your task is to help Chef find $K$ and print the first $K$ elements of the modified array.

## **Function Declaration**

### **Function Name**

$removeDuplicates$ – Removes duplicate elements from a sorted array in-place.

### **Parameters**

* $nums$ : A list/array of integers sorted in non-decreasing order.

### **Return Value**

* Returns an **integer K** — the number of unique elements. \
  The first $K$ positions of $nums$ must contain these unique values.

## Constraints:

* $1 \leq N \leq 3 × 10^4$
* $–100 \leq nums[i] ≤ 100$
* $nums$ is sorted in **non-decreasing** order.

---

## Input Format

* $N$ → size of array
* Next line → **N sorted integers**

---

## Output Format

* Print $K$
* Print the **first K unique elements** of the modified array

---

## Examples

**Example 1**

**Input**

```text
6
1 1 2 2 3 3
```

**Output**

```text
3
1 2 3
```

**Explanation**

`nums = [1,1,2,2,3,3]` -> After removing duplicates: `[1, 2, 3, _, _, _]`.\
Here, `K = 3`, and the first three elements are `1 2 3`.

**Example 2**

**Input**

```text
5
0 0 1 1 1
```

**Output**

```text
2
0 1
```

**Explanation**

`nums = [0,0,1,1,1]` -> After removing duplicates: `[0, 1, _, _, _]`.\
Here, `K = 2`, and the first two elements are `0 1`.

---

<details class="codechef-official-editorial">
<summary>Official Editorial</summary>

## Problem Restatement

You are given a sorted array `nums` of size `N`. You need to remove duplicates **in-place** such that each unique element appears **once**, while keeping the **relative order** intact. Finally, output the number of unique elements `K` and the first `K` elements.

---

## Key Observations

The array is already sorted in **non-decreasing order**, so duplicates will always appear **next to each other**.

Since we must solve it **in-place**, no extra array can be used (O(1) space).

---

## Approach

We maintain two pointers:
- `i` → iterates through the array
- `j` → position of the last unique element

Steps:
- Start with `j = 0`.
- For each element `nums[i]` from index `1` to `N-1`:
   - If `nums[i] != nums[j]`, increment `j` and set `nums[j] = nums[i]`.
- At the end, the number of unique elements = `j + 1`.

---

##  Complexity Analysis

- **Time Complexity**: `O(N)`
   - The array is traversed once with a single loop.
- **Space Complexity**: `O(1)`
   - Only a constant number of extra variables (`i`, `j`) are used.

This is the **optimal solution**.

</details>
