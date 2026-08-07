### 1. Description

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">**in-place**</a> such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**.

Consider the number of *unique elements* in `nums` to be `k**​​​​​​​**`​​​​​​​. <meta charset="UTF-8" />After removing duplicates, return the number of unique elements `k`.

<meta charset="UTF-8" />The first `k` elements of `nums` should contain the unique numbers in **sorted order**. The remaining elements beyond index $k - 1$ can be ignored.

### 2. Function Contract

**Inputs**

- `nums`: The non-decreasing integer array to compact.

**Return value**

Return $k$, the number of distinct values written to the start of `nums`. The same call mutates `nums` in place, and `nums[:k]` is the non-decreasing prefix containing each distinct value once. Values at indices $k$ and beyond are unspecified.

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

- **Input:** `nums = [1,1,2]`
- **Output:** $2, nums = [1,2,_]$
- **Explanation:** Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
#### Example 2

- **Input:** `nums = [0,0,1,1,1,2,2,3,3,4]`
- **Output:** $5, nums = [0,1,2,3,4,_,_,_,_,_]$
- **Explanation:** Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

### 5. Constraints

- $1 \le \text{nums.length} \le 3 * 10^{4}$

- $-100 \le \text{nums}[i] \le 100$

- `nums` is sorted in **non-decreasing** order.