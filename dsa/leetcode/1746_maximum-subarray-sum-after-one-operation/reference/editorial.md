
## Solution

---

### Overview

Given an array `nums`, we can replace exactly one element $\text{nums}[i]$ with its square, $\text{nums}[i] * \text{nums}[i]$. Our goal is to find the maximum possible sum of any subarray after making this replacement.

A straightforward approach to this problem would be to square each element at a time and calculate the maximum subarray sum for the resulting array. However, this method has a time complexity of $O(n^2)$, which would lead to a TLE (Time Limit Exceeded) error for the problem's constraints.

To build a better understanding of the concept, you might want to start with a simpler version of the problem: finding the maximum subarray sum for a fixed array. You can try it here:  [53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/description/).

---

### Approach 1: MaxLeft and MaxRight

#### Intuition

First, it's important to see that squaring an element outside the final maximum-sum subarray doesn't help. Squaring increases the value of an element, so it makes sense only to square an element that is part of the subarray contributing to the maximum sum.

This means the result subarray will look like this:
-   A prefix of unchanged elements from `nums` (possibly empty).
-   A single squared element $\text{nums}[i] * \text{nums}[i]$.
-   A suffix of unchanged elements from `nums` (possibly empty).

Therefore, we calculate for each index `i`, the maximum sum of a subarray ending just before the index `i` and the maximum sum of a subarray starting just after the index `i`. By combining these two subarrays with the squared element $\text{nums}[i] * \text{nums}[i]$ and taking the greatest total sum, we get the answer.

#### Algorithm

-   Initialize `n` to the size of the `nums` array.
-   Initialize two arrays of `n` elements, named `maxLeft` and `maxRight`, to store the maximum sum of the subarrays ending just before and starting just after each element.
-   Set $\text{maxLeft}[0]$ to `0`; no subarray ends before the first element.
- Iterate through the array from left to right to compute `maxLeft`:
  - For each `i` from 1 to $n - 1$:
- Calculate $\text{maxLeft}[i]$ as the maximum of:
      - The sum of the current subarray ending at $i - 1$.
      - 0 (indicating no subarray).
-   Set $maxRight[n - 1]$ to `0`; no subarray starts after the last element.
- Iterate through the array from right to left to compute `maxRight`:
  - For each `i` from $n - 2$ to 0:
- Calculate $\text{maxRight}[i]$ as the maximum of:
      - The sum of the current subarray starting at $i + 1$.
      - 0 (indicating no subarray).
-   Initialize `maxSum` to `0`.
- Iterate through each element in the array to compute the result:
  - For each `i` from 0 to $n - 1$:
- Compute the sum of:
      - The maximum sum of subarrays ending before `i` ($\text{maxLeft}[i]$).
      - The square of $\text{nums}[i]$ (representing the modified value).
      - The maximum sum of subarrays starting after `i` ($\text{maxRight}[i]$).
- Update `maxSum` to the maximum of its current value and the computed sum.
-   Return `maxSum`.

#### Implementation

```python
class Solution:
    def maxSumAfterOperation(self, nums: list[int]) -> int:
        n = len(nums)

        # Arrays to store the maximum sum of subarrays ending before and starting after each element
        max_left = [0] * n
        max_right = [0] * n

        # No subarray ends before the first element, so set max_left[0] to 0
        max_left[0] = 0
        for i in range(1, n):
            # Compute max_left[i]: the maximum subarray sum ending just before nums[i]
            max_left[i] = max(max_left[i - 1] + nums[i - 1], 0)

        # No subarray starts after the last element, so set max_right[n - 1] to 0
        max_right[n - 1] = 0
        for i in range(n - 2, -1, -1):
            # Compute max_right[i]: the maximum subarray sum starting just after nums[i]
            max_right[i] = max(max_right[i + 1] + nums[i + 1], 0)

        # Initialize the maximum sum as 0
        max_sum = 0

        # Iterate over each element in the array
        for i in range(n):
            # Calculate the maximum sum by combining the best left and right subarrays found for each element
            max_sum = max(max_sum, max_left[i] + nums[i] ** 2 + max_right[i])

        return max_sum
```

#### Complexity Analysis

Let $n$ be the length of the array.

- Time complexity: $O(n)$

    We loop over the array three times and perform constant-time operations on each iteration. Therefore, the time complexity of the algorithm is $O(n)$.

- Space complexity: $O(n)$

    We are creating two arrays `maxLeft` and `maxRight`, each of size $n$ to store the maximum sum of a subarray ending just before and starting exactly after each index. That's why the algorithm requires $O(n)$ extra space.

---

### Approach 2: Top-Down Dynamic Programming

#### Intuition

For each element in the array, we have two main options:

1. **Option 1: Do not square the element**

When we choose not to square the element, it contributes its original value as it is. We recursively calculate the maximum sum we can get from the subarray starting at the next index:

-   If this sum is positive, we add it to the value of the current element.

-   If not, the remaining subarray does not help increase the maximum subarray sum. In this case, we take the current element alone as the best option, meaning we stop expanding the subarray to the right and just return the current element's value.

2. **Option 2: Square the element**

We can only choose this option if none of the previous elements has been squared. When this holds, we can either get the square of the current element alone or incremented by the greatest sum of a subarray starting from the next index (only if it is positive).

Since for each element, we are exploring two options (square the element or not), the approach results in a time complexity of $O(2^n)$ due to the recursive branching. However, this complexity can be reduced to polynomial time using dynamic programming and storing previously computed results in a memoization table to prevent redundant calculations.

> For a more comprehensive understanding of dynamic programming, check out the [Dynamic Programming Explore Card 🔗](https://leetcode.com/explore/learn/card/dynamic-programming/). This resource provides an in-depth look at dynamic programming, explaining its key concepts and applications with a variety of problems to solidify understanding of the pattern.

#### Algorithm

- Initialize `n` to the size of `nums` and create a DP table `dp` of size `n x 2` with initial values set to `-1`.

- Initialize `maxSum` to 0 to keep track of the maximum sum found during recursion.

- Call the recursive helper function `getMaxSumHelper(0, nums, true, dp, maxSum)` to start processing from the first element with the option to square it.

- `getMaxSumHelper` function:
  - If `index` is equal to the size of `nums`, return `0` (base case: end of the array).

  - If the result for the current state ($\text{dp}[index][canSquare]$) is already computed, return it.

  - **Case 1: Skip squaring the current element**:
- Recursively call $getMaxSumHelper(index + 1, nums, canSquare, dp, maxSum)$ to get the sum for the next element without squaring the current element.
- Set `maxSumWithoutSquare` to the value of $\text{nums}[index]$ if we don't square it, adding the result of the next sum if positive.

  - **Case 2: Square the current element if allowed**:
- If `canSquare` is true, square $\text{nums}[index]$ and set `maxSumWithSquare` to the squared value.
- Recursively call $getMaxSumHelper(index + 1, nums, false, dp, maxSum)$ to calculate the sum for the next element without the option to square further.
- Add the result of the next sum if positive.

  - Update `maxSum` if either of the two cases provides a better sum.

  - Store the result for the current state ($\text{dp}[index][canSquare]$) and return the maximum of the two options (`maxSumWithSquare` and `maxSumWithoutSquare`).

- Return the value of `maxSum` after processing all elements.

#### Implementation

```python
class Solution:
    def maxSumAfterOperation(self, nums):
        n = len(nums)
        # Initialize a DP table to store results of subproblems.
        dp = [[-1, -1] for _ in range(n)]

        max_sum = [0]

        # Call the recursive helper function to compute the result.
        self._get_max_sum_helper(0, nums, True, dp, max_sum)

        return max_sum[0]

    def _get_max_sum_helper(self, index, nums, can_square, dp, max_sum):
        if index == len(nums):
            return 0  # Base case: if we reach the end of the array, return 0.

        # If the result is already computed for this state, return it.
        if dp[index][1 if can_square else 0] != -1:
            return dp[index][1 if can_square else 0]

        # Case 1: Skip squaring the current element.
        next_sum_without_square = self._get_max_sum_helper(
            index + 1, nums, can_square, dp, max_sum
        )
        max_sum_without_square = nums[
            index
        ]  # The value itself if we don't square it.
        if next_sum_without_square > 0:
            max_sum_without_square += (
                next_sum_without_square  # Accumulate if positive.
            )

        # Case 2: Square the current element if allowed.
        max_sum_with_square = 0
        if can_square:
            max_sum_with_square = (
                nums[index] * nums[index]
            )  # Square the current element.
            next_sum_with_square = self._get_max_sum_helper(
                index + 1, nums, False, dp, max_sum
            )  # Don't square further.
            if next_sum_with_square > 0:
                max_sum_with_square += (
                    next_sum_with_square  # Accumulate if positive.
                )

        # Update the global max_sum if we find a better one.
        max_sum[0] = max(
            max_sum[0], max(max_sum_with_square, max_sum_without_square)
        )

        # Store the result in dp table and return the maximum of the two options.
        dp[index][1 if can_square else 0] = max(
            max_sum_with_square, max_sum_without_square
        )
        return dp[index][1 if can_square else 0]
```

#### Complexity Analysis

Let $n$ be the length of the array.

- Time complexity: $O(n)$

    We call the `getMaxSumHelper` function for each element twice, one when we are allowed to square it and one when we are not. Since on each separate call, the function performs constant-time operations, the time complexity of the algorithm is $O(n)$.

- Space complexity: $O(n)$

    We are creating an array `dp` of size $2n$ to store the results after each call. Additionally, the recursion depth can grow up to $O(n)$ in size, contributing to the space complexity. Therefore, the solution requires $O(n)$ extra space.

---

### Approach 3: Bottom-Up Dynamic Programming

#### Intuition

After exploring different options using a recursive approach, switching to an iterative dynamic approach becomes much easier. The key step is replacing the recursive function with a table, ensuring that all required states are computed before using them.

Let’s define a 2D table $\text{dp}[n][2]$, where:

- $\text{dp}[index][0]$ represents the maximum sum of a subarray ending at `index` with no squared elements.
- $\text{dp}[index][1]$ represents the maximum sum of a subarray ending at `index` with exactly one squared element.

To calculate $\text{dp}[index][0]$ (subarray with no squared elements), we have two options:

- Start a new subarray with just the current element.
- Continue the maximum subarray sum from the previous index, without squaring the element.

So, we choose the maximum of these two options:
$\text{dp}[index][0] = max(dp[index - 1][0] + \text{nums}[index], \text{nums}[index])$.

For $\text{dp}[index][1]$ (subarray with exactly one squared element), we have three choices:

- Square the current element by itself: $\text{nums}[index] * \text{nums}[index]$.
- Continue the previous subarray (without a squared element) but square the current element: $dp[index - 1][0] + \text{nums}[index] * \text{nums}[index]$.
- Continue the previous subarray that already had one squared element, adding the current element as-is: $dp[index - 1][1] + \text{nums}[index]$.

Again, we set $\text{dp}[index][1]$ to the maximum of these three choices.

The final answer is the maximum of all $\text{dp}[index][1]$ values, since we want exactly one squared element in our subarray.

#### Algorithm

- Initialize `n` to the size of the `nums` array.
- Initialize `maxSumWithoutSquare` and `maxSumWithSquare` to store the maximum sums:
  - `maxSumWithoutSquare` starts with the first element of `nums`.
  - `maxSumWithSquare` starts with the square of the first element of `nums`.
  - Initialize `maxSum` as `maxSumWithSquare` (to keep track of the overall maximum sum).
- Iterate through the array starting from index 1:
  - For each element, compute three possible options for the maximum sum with squaring:
- Option 1: Square the current element.
- Option 2: Square the current element and add it to the previous `maxSumWithoutSquare`.
- Option 3: Add the current element to `maxSumWithSquare`.
- Update `maxSumWithSquare` to the maximum of these options.
  - Compute two options for the maximum sum without squaring:
- Option 1: Start a new subarray with the current element.
- Option 2: Continue the previous subarray by adding the current element to `maxSumWithoutSquare`.
- Update `maxSumWithoutSquare` to the maximum of these two options.
  - Update `maxSum` to the maximum of the current `maxSum` and `maxSumWithSquare`.
- Return `maxSum`.

#### Implementation

```python
class Solution:
    def maxSumAfterOperation(self, nums: list[int]) -> int:
        n = len(nums)  # Get the size of the input array.

        # Initialize a DP table
        dp = [[0, 0] for _ in range(n)]

        # Base case
        dp[0][0] = nums[
            0
        ]  # Maximum sum with no squared element is just the first element.
        dp[0][1] = (
            nums[0] * nums[0]
        )  # Maximum sum with the first element squared.

        max_sum = dp[0][1]

        for index in range(1, n):
            # Option 1: Start a new subarray.
            # Option 2: Continue the previous subarray.
            dp[index][0] = max(nums[index], dp[index - 1][0] + nums[index])

            # Option 1: Start a new subarray.
            # Option 2: Square the current element.
            # Option 3: Do not square the element.
            dp[index][1] = max(
                max(
                    nums[index] * nums[index],
                    dp[index - 1][0] + nums[index] * nums[index],
                ),
                dp[index - 1][1] + nums[index],
            )

            # Update max_sum
            max_sum = max(max_sum, dp[index][1])

        return max_sum
```

#### Complexity Analysis

Let $n$ be the length of the array.

- Time complexity: $O(n)$

    We iterate over the array once to fill the values of the `dp` table. Therefore, the algorithm runs in $O(n)$ time.

- Space complexity: $O(n)$

    Just like in the previous approach, we are creating an array, `dp`, of size $2n$ to store the greatest sums up to each index with and without squaring an element. This results in a $O(n)$ space complexity.

---

### Approach 4: Space-optimized Dynamic Programming

#### Intuition

Looking back at our earlier approach, we can see that $\text{dp}[index][0]$ and $\text{dp}[index][1]$ only depend on the values from the previous index, $index - 1$. This means that once we calculate $\text{dp}[index]$, we no longer need the values for earlier indices. Therefore, keeping them in memory is unnecessary and wastes space.
So, instead of creating an entire array, we can use just two variables, `maxSumWithoutSquare` and `maxSumWithSquare`, to represent $\text{dp}[index][0]$ and $\text{dp}[index][1]$. These variables are updated in each iteration.

#### Algorithm

- Initialize `n` to the size of the `nums` array.
- Initialize `maxSumWithoutSquare` and `maxSumWithSquare` to store the maximum sums:
  - `maxSumWithoutSquare` starts with the first element of `nums`.
  - `maxSumWithSquare` starts with the square of the first element of `nums`.
  - Initialize `maxSum` as `maxSumWithSquare` (to keep track of the overall maximum sum).

- Iterate through the array starting from index 1:
  - For each element, compute three possible options for the maximum sum with squaring:
- Option 1: Square the current element.
- Option 2: Square the current element and add it to the previous `maxSumWithoutSquare`.
- Option 3: Add the current element to `maxSumWithSquare`.
- Update `maxSumWithSquare` to the maximum of these options.

  - Compute two options for the maximum sum without squaring:
- Option 1: Start a new subarray with the current element.
- Option 2: Continue the previous subarray by adding the current element to `maxSumWithoutSquare`.
- Update `maxSumWithoutSquare` to the maximum of these two options.

  - Update `maxSum` to the maximum of the current `maxSum` and `maxSumWithSquare`.

- Return `maxSum`.

#### Implementation

```python
class Solution:
    def maxSumAfterOperation(self, nums: list[int]) -> int:
        n = len(nums)  # Get the size of the input array.

        # Initialize variables to store the maximum sums.
        max_sum_without_square = nums[0]
        max_sum_with_square = nums[0] * nums[0]
        max_sum = max_sum_with_square

        for index in range(1, n):
            # Option 1: Square the current element.
            # Option 2: Add the square of the current element to the previous sum without a square.
            # Option 3: Add the current element to the previous sum with a square.
            max_sum_with_square = max(
                max(
                    nums[index] * nums[index],
                    max_sum_without_square + nums[index] * nums[index],
                ),
                max_sum_with_square + nums[index],
            )

            # Option 1: Start a new subarray.
            # Option 2: Continue the previous subarray.
            max_sum_without_square = max(
                nums[index], max_sum_without_square + nums[index]
            )

            # Update max_sum to track the global maximum sum with exactly one squared element.
            max_sum = max(max_sum, max_sum_with_square)

        return max_sum
```

#### Complexity Analysis

Let $n$ be the length of the array.

- Time complexity: $O(n)$

    We iterate over the array once and on each iteration we perform some constant-time operations (additions and comparisons) to update the `maxSumWithSquare` and `maxSumWithoutSquare` variables. Therefore, the time complexity is $O(n)$.

- Space complexity: $O(1)$

    We only define a fixed number of variables which does not depend on the input size.

---