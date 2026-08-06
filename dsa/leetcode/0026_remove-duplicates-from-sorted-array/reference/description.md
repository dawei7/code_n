## Description

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">**in-place**</a> such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**.

Consider the number of *unique elements* in `nums` to be `k**​​​​​​​**`​​​​​​​. <meta charset="UTF-8" />After removing duplicates, return the number of unique elements `k`.

<meta charset="UTF-8" />The first `k` elements of `nums` should contain the unique numbers in **sorted order**. The remaining elements beyond index `k - 1` can be ignored.

**Custom Judge:**

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
