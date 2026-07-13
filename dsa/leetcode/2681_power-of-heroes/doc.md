# Power of Heroes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2681 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Dynamic Programming, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [power-of-heroes](https://leetcode.com/problems/power-of-heroes/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/power-of-heroes/).

### Goal
Given an array of positive integers `nums`, calculate the "power" for every non-empty subsequence. The power of a subsequence is defined as `(max_element^2 * min_element)`, where `max_element` is the largest value in the subsequence and `min_element` is the smallest value. The task is to find the sum of powers of all possible non-empty subsequences and return this total sum modulo `10^9 + 7`.

### Function Contract
**Inputs**

- `nums`: A list of integers, where `1 <= nums.length <= 10^5` and `1 <= nums[i] <= 10^9`.

**Return value**

- An integer representing the total sum of powers of all non-empty subsequences, modulo `10^9 + 7`.

### Examples
**Example 1**

- Input: `nums = [2, 1, 4]`
- Output: `141`
- Explanation:
  Sorted `nums` is `[1, 2, 4]`.
  Subsequences and their powers:
  - `[1]`: `1^2 * 1 = 1`
  - `[2]`: `2^2 * 2 = 8`
  - `[4]`: `4^2 * 4 = 64`
  - `[1, 2]`: `max=2, min=1` -> `2^2 * 1 = 4`
  - `[1, 4]`: `max=4, min=1` -> `4^2 * 1 = 16`
  - `[2, 4]`: `max=4, min=2` -> `4^2 * 2 = 32`
  - `[1, 2, 4]`: `max=4, min=1` -> `4^2 * 1 = 16`
  Total sum = `1 + 8 + 64 + 4 + 16 + 32 + 16 = 141`.

**Example 2**

- Input: `nums = [1, 2]`
- Output: `13`
- Explanation:
  Sorted `nums` is `[1, 2]`.
  Subsequences and their powers:
  - `[1]`: `1^2 * 1 = 1`
  - `[2]`: `2^2 * 2 = 8`
  - `[1, 2]`: `max=2, min=1` -> `2^2 * 1 = 4`
  Total sum = `1 + 8 + 4 = 13`.

**Example 3**

- Input: `nums = [1]`
- Output: `1`
- Explanation:
  Subsequence `[1]`: `1^2 * 1 = 1`. Total sum = `1`.

---

## Solution
### Approach
The core idea to solve this problem efficiently involves sorting the input array and then using a dynamic programming approach combined with properties of powers of 2.

1.  **Sorting:** First, sort the `nums` array in non-decreasing order. This is crucial because once sorted, for any subsequence `S`, its minimum element `min(S)` will always appear before its maximum element `max(S)` in the sorted array. This simplifies the calculation as we can iterate through the array and consider each element `nums[i]` as a potential maximum element for various subsequences.

2.  **Iterating and Calculating Contributions:**
    For each element `nums[i]` in the sorted array, we consider it as the *maximum* element of a set of subsequences.
    For a fixed `nums[i]` as the maximum element:
    *   **Case 1: `nums[i]` is the only element in the subsequence.**
        The subsequence is `[nums[i]]`. Its power is `nums[i]^2 * nums[i] = nums[i]^3`.
    *   **Case 2: `nums[i]` is the maximum, and `nums[j]` (where `j < i`) is the minimum element.**
        For such a subsequence, `nums[i]` is the maximum, `nums[j]` is the minimum. Any elements `nums[k]` where `j < k < i` can either be included or excluded from the subsequence. There are `i - j - 1` such elements. Thus, there are `2^(i - j - 1)` ways to choose these intermediate elements.
        The contribution for a specific `(nums[i], nums[j])` pair as (max, min) is `nums[i]^2 * nums[j] * 2^(i - j - 1)`.

3.  **Dynamic Programming / Prefix Sum Optimization:**
    The total contribution for a fixed `nums[i]` as the maximum element is:
    `nums[i]^3 + sum_{j=0}^{i-1} (nums[i]^2 * nums[j] * 2^(i - j - 1))`
    This can be rewritten as:
    `nums[i]^3 + nums[i]^2 * (sum_{j=0}^{i-1} nums[j] * 2^(i - 1 - j))`

    Let `S_i = sum_{j=0}^{i-1} nums[j] * 2^(i - 1 - j)`. This `S_i` represents the sum of `nums[j]` weighted by powers of 2, where `nums[j]` are candidates for the minimum element when `nums[i]` is the maximum.
    Notice the recurrence relation for `S_i`:
    `S_0 = 0` (for `i=0`, there are no elements before `nums[0]`)
    `S_i = nums[i-1] * 2^0 + nums[i-2] * 2^1 + ... + nums[0] * 2^(i-1)`
    `S_i = nums[i-1] + 2 * (nums[i-2] * 2^0 + ... + nums[0] * 2^(i-2))`
    `S_i = nums[i-1] + 2 * S_{i-1}` (all modulo `10^9 + 7`)

    So, we can maintain a running sum `current_sum_of_min_terms` that updates `S_i` for each `i`.
    The algorithm proceeds as follows:
    1. Sort `nums`.
    2. Initialize `total_power = 0` and `current_sum_of_min_terms = 0`.
    3. Iterate `i` from `0` to `n-1`:
        a. Let `num = nums[i]`.
        b. Calculate the power contribution for `num` as the maximum:
           `term_power = (pow(num, 3, MOD) + (pow(num, 2, MOD) * current_sum_of_min_terms) % MOD) % MOD`
        c. Add `term_power` to `total_power`.
        d. Update `current_sum_of_min_terms` for the next iteration:
           `current_sum_of_min_terms = (current_sum_of_min_terms * 2 + num) % MOD`
    4. Return `total_power`.

All calculations must be performed modulo `10^9 + 7` to prevent integer overflow.

### Complexity Analysis
- **Time Complexity**: `O(N log N)`
  - Sorting the `nums` array takes `O(N log N)` time.
  - The subsequent loop iterates `N` times. Inside the loop, all operations (exponentiation, multiplication, addition, modulo) take constant time.
  - Therefore, the dominant factor is sorting.
- **Space Complexity**: `O(1)`
  - If the sorting is done in-place (as `list.sort()` does in Python), the auxiliary space complexity is `O(1)`. If a new array is created for sorting, it would be `O(N)`.
  - The variables `total_power` and `current_sum_of_min_terms` use constant space.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int]) -> int:
    MOD = 10**9 + 7

    # Step 1: Sort the array
    nums.sort()

    total_power = 0

    # current_sum_of_min_terms will store sum_{j=0}^{i-1} (nums[j] * 2^(i-1-j))
    # This represents the weighted sum of previous elements that can act as minimums
    # when nums[i] is the maximum.
    current_sum_of_min_terms = 0

    for num in nums:
        # Calculate the power contribution for the current 'num' as the maximum element.
        # This includes two parts:
        # 1. When 'num' is the only element in the subsequence: num^3
        # 2. When 'num' is the maximum and some nums[j] (j < current index) is the minimum:
        #    sum_{j=0}^{i-1} (num^2 * nums[j] * 2^(i-1-j))
        #    This sum can be factored as num^2 * (sum_{j=0}^{i-1} nums[j] * 2^(i-1-j))
        #    The term in parentheses is exactly current_sum_of_min_terms.

        # Calculate num^3 % MOD
        num_cubed = pow(num, 3, MOD)

        # Calculate (num^2 * current_sum_of_min_terms) % MOD
        num_squared_times_min_terms = (pow(num, 2, MOD) * current_sum_of_min_terms) % MOD

        # Add these two parts to get the total contribution for the current 'num' as max
        current_num_contribution = (num_cubed + num_squared_times_min_terms) % MOD

        # Add to the overall total power
        total_power = (total_power + current_num_contribution) % MOD

        # Update current_sum_of_min_terms for the next iteration (i+1).
        # The new sum will be:
        # (nums[i] * 2^0) + (nums[i-1] * 2^1) + ... + (nums[0] * 2^i)
        # This is equivalent to (current_sum_of_min_terms * 2 + nums[i])
        current_sum_of_min_terms = (current_sum_of_min_terms * 2 + num) % MOD

    return total_power
```
</details>
