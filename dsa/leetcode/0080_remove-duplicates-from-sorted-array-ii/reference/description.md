### 1. Description

Given an integer array `nums` sorted in **non-decreasing order**, remove some duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">**in-place**</a> such that each unique element appears **at most twice**. The **relative order** of the elements should be kept the **same**.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the **first part** of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k`* after placing the final result in the first *`k`* slots of *`nums`.

Do **not** allocate extra space for another array. You must do this by **modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a>** with $\mathcal{O}(1)$ extra memory.

### 2. Function Contract

**Inputs**

- `nums`: A non-decreasing integer array to compact in place.

**Return value**

Return $k$, the number of retained values after limiting each distinct value to at most two copies. The same call mutates `nums` in place so `nums[:k]` contains those retained values in non-decreasing order. Values at indices $k$ and beyond are unspecified.

### 3. Custom Judge

The judge will test your solution with the following code:

```
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be **accepted**.

### 4. Examples

#### Example 1

- **Input:** `nums = [1,1,1,2,2,3]`
- **Output:** $5, nums = [1,1,2,2,3,_]$
- **Explanation:** Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

#### Example 2

- **Input:** `nums = [0,0,1,1,1,1,2,3,3]`
- **Output:** $7, nums = [0,0,1,1,2,3,3,_,_]$
- **Explanation:** Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

### 5. Constraints

- $1 \le \text{nums.length} \le 3 * 10^{4}$

- $-10^{4} \le \text{nums}[i] \le 10^{4}$

- `nums` is sorted in **non-decreasing** order.
