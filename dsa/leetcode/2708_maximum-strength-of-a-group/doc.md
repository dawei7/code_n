# Maximum Strength of a Group

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2708 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Backtracking, Greedy, Bit Manipulation, Sorting, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [maximum-strength-of-a-group](https://leetcode.com/problems/maximum-strength-of-a-group/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/maximum-strength-of-a-group/).

### Goal
Given an array of integers `nums`, find the maximum possible "strength" of any non-empty subsequence. The strength of a subsequence is defined as the product of all its elements.

### Function Contract
**Inputs**

- `nums`: A list of integers. The length of `nums` is between 1 and 18. Each element `nums[i]` is between -10 and 10.

**Return value**

- An integer representing the maximum strength achievable from a non-empty subsequence of `nums`.

### Examples
**Example 1**

- Input: `nums = [3, -1, 0, -2]`
- Output: `6`
- Explanation: The subsequence `[3, -1, -2]` has a product of `3 * (-1) * (-2) = 6`. Other subsequences like `[3]` (product 3), `[-1, -2]` (product 2), `[0]` (product 0) yield smaller or equal strengths.

**Example 2**

- Input: `nums = [-1, -2, -3]`
- Output: `6`
- Explanation: The subsequence `[-2, -3]` has a product of `(-2) * (-3) = 6`. Other subsequences like `[-1, -2, -3]` (product -6) or `[-1]` (product -1) yield smaller strengths.

**Example 3**

- Input: `nums = [0, 0, 0]`
- Output: `0`
- Explanation: Any non-empty subsequence will contain at least one zero, resulting in a product of 0.

**Example 4**

- Input: `nums = [-5]`
- Output: `-5`
- Explanation: The only non-empty subsequence is `[-5]`, with a product of -5.

**Example 5**

- Input: `nums = [-5, 0]`
- Output: `0`
- Explanation: The subsequence `[0]` has a product of 0. The subsequence `[-5]` has a product of -5. 0 is greater than -5.

---

## Solution
### Approach
This problem can be solved using a **Greedy Approach**. The strategy is to maximize the product by including as many numbers as possible, with special handling for negative numbers and zeros:

1.  **Separate Numbers**: Categorize all numbers into three groups: positive numbers, negative numbers, and count of zeros.
2.  **Product of Non-Zeros**: Calculate the product of all non-zero numbers.
3.  **Handle Negative Count**:
    *   If there is an **even** count of negative numbers, their product will be positive. Including all of them (along with all positive numbers) will yield the maximum possible positive product.
    *   If there is an **odd** count of negative numbers, their product (and thus the total product of all non-zero numbers) will be negative. To achieve a positive product (which is generally greater than any negative product), we must exclude one negative number. To maximize the resulting positive product, we should remove the negative number that has the smallest absolute value (i.e., the largest negative number, closest to zero).
4.  **Handle Edge Cases**:
    *   If the input array contains only zeros (e.g., `[0, 0, 0]`), the maximum strength is 0.
    *   If the input array contains only one negative number and some zeros (e.g., `[-5, 0]`), the maximum strength is 0 (from the subsequence `[0]`).
    *   If the input array contains only one negative number and no zeros or positives (e.g., `[-5]`), the maximum strength is that negative number itself.

The algorithm prioritizes forming a positive product. If a positive product can be formed, it will always be greater than 0 (unless the product is 0 itself, which is handled by specific cases). If only negative products are possible (e.g., `[-5]`), then the largest negative product is chosen.

### Complexity Analysis
- **Time Complexity**: `O(N log N)`
    - Separating numbers into lists takes `O(N)` time.
    - Sorting the list of negative numbers takes `O(M log M)` time, where `M` is the count of negative numbers. In the worst case, `M = N`, so this is `O(N log N)`.
    - Calculating the product of numbers takes `O(N)` time.
    - Given `N` is up to 18, `N log N` is very efficient.
- **Space Complexity**: `O(N)`
    - Storing positive and negative numbers in separate lists requires `O(N)` space in the worst case (e.g., all numbers are positive or all are negative).

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    positives = []
    negatives = []
    zero_count = 0

    for num in nums:
        if num > 0:
            positives.append(num)
        elif num < 0:
            negatives.append(num)
        else:
            zero_count += 1

    # Case 1: All numbers are zeros.
    # E.g., nums = [0, 0, 0] -> max strength is 0 (from [0])
    if not positives and not negatives:
        return 0

    # Case 2: Only one negative number, no positives, and some zeros.
    # In this scenario, the only way to get a non-negative product is to use a zero.
    # E.g., nums = [-5, 0, 0] -> max strength is 0 (from [0])
    if not positives and len(negatives) == 1 and zero_count > 0:
        return 0

    # Case 3: Only one negative number, no positives, and no zeros.
    # The only non-empty subsequence is the number itself.
    # E.g., nums = [-5] -> max strength is -5 (from [-5])
    if not positives and len(negatives) == 1 and zero_count == 0:
        return negatives[0]

    # General case: Calculate product of all non-zero numbers,
    # then adjust based on negative count to maximize.
    current_product = 1

    for p in positives:
        current_product *= p

    # Sort negatives to easily find the largest negative (closest to zero)
    # if we need to remove one to make the product positive.
    negatives.sort()

    for n in negatives:
        current_product *= n

    # If there's an odd number of negatives, the current_product will be negative.
    # To maximize the strength, we aim for a positive product.
    # We achieve this by removing one negative number. To minimize the reduction
    # in the absolute value of the product, we remove the negative number
    # closest to zero (which is the largest value in the sorted `negatives` list).
    if len(negatives) % 2 != 0:
        current_product //= negatives[-1]

    # At this point, current_product is guaranteed to be the maximum possible
    # positive product (or 1 if only positives/even negatives, or the result
    # of the edge cases handled above). If there were zeros, and we found a
    # positive product, that positive product is always greater than 0.
    # The only time 0 would be the answer is if all non-zero products were negative
    # AND there was a zero, which is covered by Case 2.

    return current_product
```
</details>
