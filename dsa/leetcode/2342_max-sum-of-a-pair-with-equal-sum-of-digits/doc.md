# Max Sum of a Pair With Equal Sum of Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2342 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [max-sum-of-a-pair-with-equal-sum-of-digits](https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/).

### Goal
Given an array of positive integers, find two distinct numbers within the array that have the same sum of their digits. Among all such pairs, identify the pair whose sum is the largest, and return this maximum sum. If no such pair exists in the array, return -1.

### Function Contract
**Inputs**

- `nums`: A list of positive integers.

Constraints: `1 <= nums.length <= 10^5`, `1 <= nums[i] <= 10^9`.

**Return value**

- An `int` representing the maximum sum of a pair with equal digit sums, or -1 if no such pair exists.

### Examples
**Example 1**

- Input: `nums = [18,43,36,13,7]`
- Output: `54`
  - Explanation:
    - `18` has digit sum `1+8=9`.
    - `43` has digit sum `4+3=7`.
    - `36` has digit sum `3+6=9`.
    - `13` has digit sum `1+3=4`.
    - `7` has digit sum `7`.
    - The pairs with equal digit sums are:
      - `(18, 36)`: Both have a digit sum of 9. Their sum is `18 + 36 = 54`.
    - The maximum sum found is 54.

**Example 2**

- Input: `nums = [10,12,19,14]`
- Output: `-1`
  - Explanation:
    - `10` has digit sum `1+0=1`.
    - `12` has digit sum `1+2=3`.
    - `19` has digit sum `1+9=10`.
    - `14` has digit sum `1+4=5`.
    - No two numbers in the array have the same sum of digits. Therefore, -1 is returned.

**Additional Example**

- Input: `nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]`
- Output: `31`
  - Explanation:
    - Many numbers share digit sums. For example:
      - `(1, 10)` both have digit sum 1. Sum = 11.
      - `(2, 11)` both have digit sum 2. Sum = 13.
      - `(3, 12)` both have digit sum 3. Sum = 15.
      - ...
      - `(11, 20)` both have digit sum 2. Sum = 31.
    - The maximum sum among all such pairs is `11 + 20 = 31`.

---

## Solution
### Approach
The core idea involves grouping numbers by their sum of digits and then efficiently finding the two largest numbers within each group.

1.  **Digit Sum Calculation:** For each number in the input array, we need a helper function to calculate the sum of its digits. This involves repeatedly taking the number modulo 10 to get the last digit and then integer dividing by 10 until the number becomes zero.

2.  **Hash Table (Dictionary/Map) for Grouping:** A hash table (e.g., Python's `dict` or `defaultdict`) is used to store numbers, where the keys are the digit sums and the values are collections of numbers that yield that specific digit sum.

3.  **Maintaining Top Two Elements:** Instead of storing all numbers for a given digit sum and then sorting or iterating through them later, an optimized approach is to maintain only the two largest numbers encountered so far for each digit sum directly within the hash table's value. When a new number is processed:
    *   If it's greater than the current largest number for its digit sum, it becomes the new largest, and the old largest becomes the second largest.
    *   If it's not greater than the largest but is greater than the current second largest, it becomes the new second largest.
    This ensures that for each digit sum, we always have the two largest numbers readily available.

4.  **Maximization:** After processing all numbers and populating the hash table with the two largest numbers for each digit sum, iterate through the hash table's values. For any digit sum where at least two numbers were recorded (i.e., the second largest number is valid/non-placeholder), calculate their sum and update a global maximum sum variable.

### Complexity Analysis
- **Time Complexity**: `O(N * log M)`
    - `N` is the number of elements in the `nums` array.
    - `M` is the maximum value of an element in `nums` (up to `10^9`).
    - Calculating the sum of digits for each number takes `O(log M)` time, as it depends on the number of digits. Since there are `N` numbers, this step is `O(N * log M)`.
    - Storing and updating the two largest numbers in the hash table for each digit sum takes `O(1)` on average per number. Across all `N` numbers, this is `O(N)`.
    - Iterating through the hash table to find the maximum pair sum takes `O(D)` time, where `D` is the number of distinct digit sums (which is at most `9 * 9 = 81` for numbers up to `10^9`, a constant factor).
    - The dominant factor is `O(N * log M)`.
- **Space Complexity**: `O(N)`
    - In the worst case, if all numbers have distinct digit sums, the hash table will store `N` entries, each potentially holding two numbers.
    - If many numbers share the same digit sum, the hash table will store fewer distinct keys, but the total number of elements stored (the two largest for each key) could still be proportional to `N` if `N` is small relative to the number of distinct digit sums, or `O(D)` where `D` is the number of distinct digit sums (a constant) if `N` is large and many numbers share digit sums. However, the `defaultdict` stores `[0,0]` for each digit sum, and we iterate through `N` numbers. The number of distinct digit sums is small (max 81 for 10^9). So, the space is `O(D)` for the map keys, but `O(N)` if we consider the total space needed to store the numbers if we were storing lists. With the optimized approach of storing only two numbers per digit sum, the space is `O(min(N, D_max))` where `D_max` is the maximum possible digit sum (e.g., 81). Since `D_max` is a constant, this is effectively `O(1)` for the map itself, but `O(N)` if we consider the input `nums` array. The question usually refers to auxiliary space. The auxiliary space is `O(D_max)`, which is `O(1)` effectively. Let's stick to `O(N)` as a safe upper bound if we consider the possibility of `N` distinct digit sums, though practically it's `O(D_max)`. Given the problem constraints, `N` can be `10^5`, `D_max` is `81`. So `O(D_max)` is more accurate for the map itself. However, standard practice for `N` elements is `O(N)` if the map could grow with `N`. Let's clarify: the map stores at most `D_max` entries, each storing 2 integers. So it's `O(D_max)` which is `O(1)` auxiliary space.

Let's re-evaluate Space Complexity:
The `digit_sum_largest_two` dictionary will store at most `D_max` entries, where `D_max` is the maximum possible sum of digits for a number up to `10^9`. The maximum sum of digits for `999,999,999` is `9 * 9 = 81`. So, `D_max` is a small constant. Each entry stores two integers. Therefore, the auxiliary space complexity is `O(D_max)`, which simplifies to `O(1)` because `D_max` is a constant.

- **Time Complexity**: `O(N * log M)`
- **Space Complexity**: `O(1)` (auxiliary space, as the number of distinct digit sums is constant)

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import defaultdict

def get_digit_sum(n: int) -> int:
    """
    Calculates the sum of digits for a given positive integer.
    """
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def solve(nums: list[int]) -> int:
    """
    Finds the maximum sum of a pair of numbers from `nums` that have an equal sum of digits.

    Args:
        nums: A list of positive integers.

    Returns:
        The maximum sum of such a pair, or -1 if no such pair exists.
    """
    max_pair_sum = -1

    # digit_sum_largest_two: A dictionary where keys are digit sums,
    # and values are lists [largest_num, second_largest_num] encountered so far
    # for that digit sum. Initialized with [0, 0] as numbers are positive.
    digit_sum_largest_two = defaultdict(lambda: [0, 0])

    for num in nums:
        s = get_digit_sum(num)

        # Update the two largest numbers for the current digit sum 's'
        if num > digit_sum_largest_two[s][0]:
            # If 'num' is greater than the current largest,
            # the old largest becomes the new second largest.
            digit_sum_largest_two[s][1] = digit_sum_largest_two[s][0]
            digit_sum_largest_two[s][0] = num
        elif num > digit_sum_largest_two[s][1]:
            # If 'num' is not greater than the largest but is greater than the second largest,
            # it becomes the new second largest.
            digit_sum_largest_two[s][1] = num

    # Iterate through the stored pairs (largest, second_largest) for each digit sum
    for largest_num, second_largest_num in digit_sum_largest_two.values():
        # A valid pair exists if 'second_largest_num' is greater than 0.
        # (Since all input numbers are positive, 0 indicates that either
        # no number or only one number was found for this digit sum).
        if second_largest_num > 0:
            current_pair_sum = largest_num + second_largest_num
            max_pair_sum = max(max_pair_sum, current_pair_sum)

    return max_pair_sum
```
</details>
