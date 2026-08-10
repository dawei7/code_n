
## Solution

---

### Overview

We are given a list of numbers, `nums`, and a `target` value. Our task is to figure out how many ways we can add plus or minus signs in front of the numbers in `nums` to get the `target` value, while keeping the order of the numbers the same.

Let's consider an example where `nums = [2, 1]` and $target = 1$.

The possible expressions from this are:
1. $+2 - 1 = 1$ → **matches the target**.
2. $-2 + 1 = -1$ → does not match.
3. $+2 + 1 = 3$ → does not match.
4. $-2 - 1 = -3$ → does not match.

So, there’s only one way ($+2 - 1$) to get the target value `1`.

> Note: We need to use all the elements of the `nums` array.

---

### Approach 1: Brute Force

#### Intuition

Start by thinking about how we would manually solve this problem. We would consider each number and decide whether to add it or subtract it. This decision-making process can be modeled using recursion.

We start by defining a recursive function that takes the current index in the list, the current sum of the expression, and the target. For each number, we make two recursive calls: one where we add the number and one where we subtract it.

When we reach the end of the list (i.e., all numbers have been considered), we check if the current sum equals the target. If it does, we increment a counter that tracks the number of valid expressions for that route. We repeat this for every route and find the total number of ways.

While this works for small inputs, it becomes impractical for larger lists due to its exponential time complexity ($2^n$).

> For a more comprehensive understanding of recursion, check out the [Recursion Explore Card 🔗](https://leetcode.com/explore/learn/card/recursion-i/). This resource provides an in-depth look at recursion, explaining its key concepts and applications with a variety of problems to solidify understanding of the pattern.

#### Algorithm

- Initialize `totalWays` to 0 to track the number of ways to reach the target sum.

- Call `calculateWays` with the initial parameters: `nums`, $currentIndex = 0$, $currentSum = 0$, `target`, to start the recursive process.

- In the `calculateWays` function:
  - If `currentIndex` equals the length of `nums`:
- Check if `currentSum` matches `target`:
      - If yes, increment `totalWays` by 1 (a valid way to reach the target sum).
  - Otherwise:
- Include the number at `currentIndex` with a positive sign:
      - Recursively call `calculateWays` with $currentIndex + 1$ and $currentSum + \text{nums}[currentIndex]$.
- Include the current number at `currentIndex` with a negative sign:
      - Recursively call `calculateWays` with $currentIndex + 1$ and $currentSum - \text{nums}[currentIndex]$.

- Return `totalWays` after all recursive calls, representing the total number of ways to assign signs to reach the target sum.

#### Implementation

> Note: The Python3 solution gets a TLE.

```python
class Solution:
    def __init__(self):
        # Tracks the total number of ways to reach the target
        self.total_ways = 0

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.calculate_ways(nums, 0, 0, target)
        return self.total_ways

    def calculate_ways(
        self, nums: List[int], current_index: int, current_sum: int, target: int
    ):
        if current_index == len(nums):
            # Check if the current sum matches the target
            if current_sum == target:
                self.total_ways += 1
        else:

            # Include the current number with a positive sign
            self.calculate_ways(
                nums,
                current_index + 1,
                current_sum + nums[current_index],
                target,
            )

            # Include the current number with a negative sign
            self.calculate_ways(
                nums,
                current_index + 1,
                current_sum - nums[current_index],
                target,
            )
```

#### Complexity Analysis

Let $n$ be the size of the input array `nums`.

- Time complexity: $O(2^n)$

    The function `calculateWays` is a recursive function that branches out into two recursive calls at each step. This is because each element in the array can either be added or subtracted, leading to $2$ choices for each of the $n$ elements.

    This results in a binary tree of recursive calls, where each level of the tree corresponds to a position in the array `nums`. Since there are $n$ elements in the array, the maximum depth of the recursion tree is $n$. Therefore, the total number of recursive calls is $2^n$, leading to a time complexity of $O(2^n)$.

- Space complexity: $O(n)$

    The space complexity is determined by the depth of the recursion stack. In the worst case, the recursion stack can go as deep as $n$ levels (one level for each element in the array). Therefore, the space complexity is $O(n)$.

---

### Approach 2: Recursion with Memoization

#### Intuition

Building on the brute force approach, we can say that it has many subproblems that are being solved repeatedly. To understand this redundancy, let's consider a simple example.

Suppose we have the list `nums = [1, 1, 1, 1, 1]` and the target $target = 3$.

In the brute force approach, we would explore all possible combinations of signs:
- `+1 +1 +1 +1 +1`
- `+1 +1 +1 +1 -1`
- `+1 +1 +1 -1 +1`
- `+1 +1 -1 +1 +1`
- `+1 -1 +1 +1 +1`
- `-1 +1 +1 +1 +1`
- ...

Let's focus on a specific subproblem: reaching a sum of `2` using the first four numbers `[1, 1, 1, 1]`.

1. Combination 1: `+1 +1 +1 -1 +1`
   - The sum of the first three numbers is `3`.
   - The sum of the first four numbers is `2` (since $3 - 1 = 2$).

2. Combination 2: `+1 +1 -1 +1 +1`
   - The sum of the first three numbers is `1`.
   - The sum of the first four numbers is `2` (since $1 + 1 = 2$).

3. Combination 3: `+1 -1 +1 +1 +1`
   - The sum of the first three numbers is `1`.
   - The sum of the first four numbers is `2` (since $1 + 1 = 2$).

In each of these combinations, we encounter the subproblem of reaching a sum of `2` using the first four numbers multiple times. Specifically, the subproblem of reaching a sum of `2` using the first four numbers `[1, 1, 1, -1]` or `[1, 1, -1, 1]` is solved repeatedly.

Another example can be given with `nums = [a, b, c]`.

Here is the corresponding recursion tree:
```
├── (+a)
│   ├── (+b)^
│   │   ├── (+c)
│   │   └── (-c)
│   └── (-b)~
│       ├── (+c)
│       └── (-c)
└── (-a)
    ├── (+b)^
    │   ├── (+c)
    │   └── (-c)
    └── (-b)~
        ├── (+c)
        └── (-c)
```

As illustrated, the subtrees marked by $^$ and `~` are solved twice.

To avoid this redundancy, we introduce a memoization table (a 2D array) where $\text{memo}[index][currentSum]$ stores the number of ways to reach the target starting from the `index` with the `currentSum`.

Before making recursive calls, we check if the result for the current `index` and `currentSum` is already computed. If it is, we return the stored result instead of recalculating it. After computing the result for a given `index` and `currentSum`, we store it in the memoization table for future reference.

For example, after calculating the number of ways to reach a sum of `2` using the first four numbers, we store this result in the memoization table. The next time we encounter this subproblem, we simply retrieve the stored result instead of recalculating it. This reduces the time complexity from exponential to polynomial.

#### Algorithm

- Calculate `totalSum`, the sum of all elements in the array `nums`.
- Initialize a 2D array `memo` of size `[nums.length][2 * totalSum + 1]` to store intermediate results, and fill it with minimum value to indicate uncomputed states. Possible sums are shifted by `totalSum` to handle negative indices.

- Call `calculateWays` with the initial parameters: `nums`, $currentIndex = 0$, $currentSum = 0$, `target`, and `memo`.

- In the `calculateWays` function:
  - If `currentIndex` equals `nums.length`:
- Check if `currentSum` equals `target`:
      - Return 1 if they match, as this represents a valid way to reach the target sum.
      - Otherwise, return 0.

  - If the result for the current state (`currentIndex` and `currentSum`) is already computed in `memo`:
- Return the stored result from `memo`.

  - Recursively calculate the number of ways:
- Add the current number ($\text{nums}[currentIndex]$) to `currentSum` and call `calculateWays` for the next index.
- Subtract the current number ($\text{nums}[currentIndex]$) from `currentSum` and call `calculateWays` for the next index.

  - Store the sum of the results from both recursive calls in $\text{memo}[currentIndex][currentSum + totalSum]$ to avoid recomputing.
  - Return the stored result from `memo`.

- Return the result of the initial call to `calculateWays`, which represents the total number of ways to reach the target sum.

#### Implementation

> Instead of using the range $[-\text{totalSum}, +\text{totalSum}]$, which is not possible in an array due to negative indices, we shift the range by adding $\text{totalSum}$ to both the lower and upper bounds. This transformation changes the range to $[-\text{totalSum} + \text{totalSum}, \text{totalSum} + \text{totalSum}]$, which simplifies to $[0, 2 \times \text{totalSum}]$.

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.total_sum = sum(nums)
        memo = [
            [float("-inf")] * (2 * self.total_sum + 1) for _ in range(len(nums))
        ]
        return self.calculate_ways(nums, 0, 0, target, memo)

    def calculate_ways(
        self,
        nums: List[int],
        current_index: int,
        current_sum: int,
        target: int,
        memo: List[List[int]],
    ) -> int:
        if current_index == len(nums):
            # Check if the current sum matches the target
            return 1 if current_sum == target else 0
        else:
            # Check if the result is already computed
            if memo[current_index][current_sum + self.total_sum] != float(
                "-inf"
            ):
                return memo[current_index][current_sum + self.total_sum]

            # Calculate ways by adding the current number
            add = self.calculate_ways(
                nums,
                current_index + 1,
                current_sum + nums[current_index],
                target,
                memo,
            )

            # Calculate ways by subtracting the current number
            subtract = self.calculate_ways(
                nums,
                current_index + 1,
                current_sum - nums[current_index],
                target,
                memo,
            )

            # Store the result in memoization table
            memo[current_index][current_sum + self.total_sum] = add + subtract

            return memo[current_index][current_sum + self.total_sum]
```

#### Complexity Analysis

Let $n$ be the size of the input array `nums`.

- Time complexity: $O(n \cdot \text{totalSum})$

    In the worst case, the function `calculateWays` is called for each index in the array and each possible sum within the range $[-\text{totalSum}, \text{totalSum}]$. Since the sum can range from $-\text{totalSum}$ to $\text{totalSum}$, there are $2 \cdot \text{totalSum} + 1$ possible sums.

    Therefore, the total number of unique states (index, sum) is $n \times (2 \cdot \text{totalSum} + 1)$. Each state is computed once and stored in the memoization table, leading to a time complexity of $O(n \cdot \text{totalSum})$.

- Space complexity: $O(n \cdot \text{totalSum})$

    The space complexity is determined by the memoization table, which has dimensions $n \times (2 \cdot \text{totalSum} + 1)$. Additionally, the recursion stack can go as deep as $n$, but this is typically dominated by the space used by the memoization table. Therefore, the space complexity is $O(n \cdot \text{totalSum})$.

    The space complexity also includes the space used by the built-in functions, such as computing the sum and filling the rows. However, these operations are linear in terms of the input size and do not significantly affect the overall space complexity, which is dominated by the memoization table.

---

### Approach 3: 2D Dynamic Programming

#### Intuition

Dynamic programming (DP) is a technique that solves problems by breaking them down into simpler subproblems and solving each subproblem only once. We create a 2D DP table where $\text{dp}[index][sum]$ represents the number of ways to reach the sum `sum` using the first `index` numbers.

Suppose we have the list `nums = [1, 1, 1, 1, 1]` and the target $target = 3$.

We initialize the first row of the DP table. For the first number, there is exactly one way to reach the sum equal to the number itself (either by adding or subtracting it). In our example, we initialize $\text{dp}[0][1 + totalSum] = 1$ and $\text{dp}[0][-1 + totalSum] = 1$.

For each subsequent number, we update the DP table based on the previous row. For each possible sum, we add the number of ways to reach that sum by either adding or subtracting the current number. For example, if we are at the second number `1`, we update the DP table based on the first row:
- If the previous sum was `0` (i.e., $\text{dp}[0][0 + totalSum] = 1$), we can reach a sum of `1` by adding the current number ($1 + 1 = 2$) or a sum of `-1` by subtracting the current number ($1 - 1 = 0$).

We continue this process for each number in the list. The value at $dp[\text{nums.length} - 1][target + totalSum]$ gives the number of ways to reach the target sum using all numbers. This approach efficiently computes the number of valid expressions by leveraging the results of previously solved subproblems.

The animation below shows how various sums are generated, along with the corresponding indices. The example assumes that the sum values lie in the range of `-6` to `+6`, just for the purpose of illustration.

!?!../Documents/494/494_Target_Sum_slides.json:1280,720!?!

> For a more comprehensive understanding of dynamic programming, check out the [Dynamic Programming Explore Card 🔗](https://leetcode.com/explore/learn/card/dynamic-programming/). This resource provides an in-depth look at dynamic programming, explaining its key concepts and applications with a variety of problems to solidify understanding of the pattern.

#### Algorithm

- Compute `totalSum` as the sum of all elements in the `nums` array.
- Initialize a 2D `dp` array with dimensions `[nums.length][2 * totalSum + 1]` to represent possible sums shifted by `totalSum` (to handle negative indices).

- Set up the base case for the first row of the DP table:
  - Add 1 to $\text{dp}[0][\text{nums}[0] + totalSum]$ to account for adding the first number.
  - Add 1 to $\text{dp}[0][-\text{nums}[0] + totalSum]$ to account for subtracting the first number (handle duplicate cases).

- Iterate through the remaining numbers in the `nums` array:
  - For each possible sum `sum` in the range `-totalSum` to `totalSum`:
- If $dp[index - 1][sum + totalSum] > 0$ (i.e., the sum is achievable from previous numbers):
      - Add its value to $\text{dp}[index][sum + \text{nums}[index] + totalSum]$ (sum achieved by adding the current number).
      - Add its value to $\text{dp}[index][sum - \text{nums}[index] + totalSum]$ (sum achieved by subtracting the current number).

- Check if the absolute value of the `target` exceeds `totalSum`:
  - If yes, return 0 (the target is unachievable).
  - Otherwise, return $dp[\text{nums.length} - 1][target + totalSum]$, which contains the number of ways to achieve the `target`.

#### Implementation

> Like in the previous approach, we shift the range of possible sums by adding $\text{totalSum}$ to both the lower and upper bounds, in order to avoid negative indices.

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        dp = [[0] * (2 * total_sum + 1) for _ in range(len(nums))]

        # Initialize the first row of the DP table
        dp[0][nums[0] + total_sum] = 1
        dp[0][-nums[0] + total_sum] += 1

        # Fill the DP table
        for index in range(1, len(nums)):
            for sum_val in range(-total_sum, total_sum + 1):
                if dp[index - 1][sum_val + total_sum] > 0:
                    dp[index][sum_val + nums[index] + total_sum] += dp[
                        index - 1
                    ][sum_val + total_sum]
                    dp[index][sum_val - nums[index] + total_sum] += dp[
                        index - 1
                    ][sum_val + total_sum]

        # Return the result if the target is within the valid range
        return (
            0
            if abs(target) > total_sum
            else dp[len(nums) - 1][target + total_sum]
        )
```

#### Complexity Analysis

Let $n$ be the size of the input array `nums`.

- Time complexity: $O(n \cdot \text{totalSum})$

    The time complexity is determined by the nested loops in the function. The outer loop runs $n$ times (once for each element in `nums`), and the inner loop runs $2 \cdot \text{totalSum} + 1$ times (once for each possible sum from $-\text{totalSum}$ to $\text{totalSum}$).

    Therefore, the overall time complexity is $O(n \cdot \text{totalSum})$.

- Space complexity: $O(n \cdot \text{totalSum})$

    The space complexity is determined by the size of the DP table `dp`, which is a 2D array of size $n \times (2 \cdot \text{totalSum} + 1)$. Each entry in the DP table requires constant space, so the total space complexity is $O(n \cdot \text{totalSum})$.

    Additionally, the space complexity includes the space required for the input array `nums`, which is $O(n)$. However, since $O(n \cdot \text{totalSum})$ dominates $O(n)$, the overall space complexity is $O(n \cdot \text{totalSum})$.

---

### Approach 4: Space Optimized

#### Intuition

In the previous DP approach, the table $\text{dp}[index][sum]$ stores the number of ways to reach the sum `sum` using the first `index` numbers. Each entry in the table is calculated based on the entries from the previous row. Specifically, to calculate $\text{dp}[index][sum]$, we only need values from the previous row:
- $dp[index-1][sum - \text{nums}[index]]$ (subtracting the current number)
- $dp[index-1][sum + \text{nums}[index]]$ (adding the current number).

Suppose we have the list `nums = [1, 1, 1, 1, 1]` and the target $target = 3$.

In the 2D DP table, the calculation for $\text{dp}[2][3]$ (number of ways to reach a sum of `3` using the first three numbers) depends on:
- $\text{dp}[1][3 - 1]$ (number of ways to reach a sum of `2` using the first two numbers)
- $\text{dp}[1][3 + 1]$ (number of ways to reach a sum of `4` using the first two numbers)

This dependency shows that each row in the 2D DP table only depends on the previous row. Once we have calculated the values for $dp[index - 1]$, we no longer need the values from $dp[index - 2]$ or any earlier rows. Thus, instead of maintaining a full 2D table, we update a single array as we process each number in the list.

We initialize the DP array with the first number. For the first number `1`, we initialize $dp[1 + totalSum] = 1$ and $dp[-1 + totalSum] = 1$.

For each subsequent number, we create a new array and update it based on the previous array. This avoids the need to store the entire 2D table. For each possible sum, we update the new array by adding the number of ways to reach that sum by either adding or subtracting the current number. For example, if we are at the second number `1`, we update the new array based on the previous array:
- If the previous sum was `0` (i.e., $dp[0 + totalSum] = 1$), we can reach a sum of `1` by adding the current number ($0 + 1 = 1$) or a sum of `-1` by subtracting the current number ($0 - 1 = -1$).

We continue this process for each number in the list. The value at $dp[target + totalSum]$ gives the number of ways to reach the target sum using all numbers.

#### Algorithm

- Calculate the `totalSum` as the sum of all elements in the array `nums`.

- Create a `dp` array of size $2 * totalSum + 1$ to track the number of ways to achieve each possible sum, offset by `totalSum` to handle negative indices.

- Initialize the first row of the DP table:
  - Set $dp[\text{nums}[0] + totalSum] = 1$ for adding the first number.
  - Increment $dp[-\text{nums}[0] + totalSum]$ by 1 for subtracting the first number (handles duplicates).

- Iterate through the rest of the `nums` array:
  - For each index in `nums`, create a `next` array to represent the next state of the DP table.
  - For each possible `sum` in the range `[-totalSum, totalSum]`:
- If the current sum $dp[sum + totalSum]$ has valid ways:
      - Add the number at $\text{nums}[index]$ to the current sum and update $next[sum + \text{nums}[index] + totalSum]$.
      - Subtract the number at $\text{nums}[index]$ from the current sum and update $next[sum - \text{nums}[index] + totalSum]$.
  - Replace `dp` with `next` to move to the next state.

- After processing all numbers, check if the target is within the valid range of `[-totalSum, totalSum]`:
  - If the `target` is out of range, return 0 (no valid ways exist).
  - Otherwise, return $dp[target + totalSum]$, which gives the number of ways to achieve the target sum.

- The final result represents the number of ways to assign `+` or `-` to elements in `nums` to achieve the `target`.

#### Implementation

> Note: The line $dp[-\text{nums}[0] + totalSum] += 1$ ensures that if the first number is `0`, both `+0` and `-0` are counted as valid sums. This is crucial because for $\text{nums}[0] = 0$, both adding and subtracting `0` result in the sum of `0`.

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)
        dp = [0] * (2 * total_sum + 1)

        # Initialize the first row of the DP table
        dp[nums[0] + total_sum] = 1  # Adding nums[0]
        dp[-nums[0] + total_sum] += 1  # Subtracting nums[0]

        # Fill the DP table
        for index in range(1, len(nums)):
            next_dp = [0] * (2 * total_sum + 1)
            for sum_val in range(-total_sum, total_sum + 1):
                if dp[sum_val + total_sum] > 0:
                    next_dp[sum_val + nums[index] + total_sum] += dp[
                        sum_val + total_sum
                    ]
                    next_dp[sum_val - nums[index] + total_sum] += dp[
                        sum_val + total_sum
                    ]
            dp = next_dp

        # Return the result if the target is within the valid range
        return 0 if abs(target) > total_sum else dp[target + total_sum]
```

#### Complexity Analysis

Let $n$ be the size of the input array `nums`.

- Time complexity: $O(n \cdot \text{totalSum})$

    The algorithm iterates through each element of the array `nums` once, and for each element, it iterates through all possible sums from $- \text{totalSum}$ to $\text{totalSum}$. The `totalSum` is the sum of all elements in the array `nums`, which is $O(n)$ in terms of the number of elements.

    Therefore, the overall time complexity is $O(n \cdot \text{totalSum})$.

- Space complexity: $O(2 \cdot \text{totalSum}) \approx O(\text{totalSum})$

    The space complexity is dominated by the dynamic programming table, which stores values for sums in the range from `-totalSum` to `totalSum`. This means the DP table has a size of $2 \cdot \text{totalSum} + 1$, or $O(2 \cdot \text{totalSum})$.

    Additionally, there is an extra array `next` that is used to store the results of the next state, which also requires $O(2 \cdot \text{totalSum})$ space.

    Thus, the overall space complexity is $O(2 \cdot \text{totalSum}) \approx O(\text{totalSum})$.

---