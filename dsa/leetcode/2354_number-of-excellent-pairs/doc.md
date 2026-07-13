# Number of Excellent Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2354 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Binary Search, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [number-of-excellent-pairs](https://leetcode.com/problems/number-of-excellent-pairs/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/number-of-excellent-pairs/).

### Goal
Given an array of positive integers `nums` and a positive integer `k`, find the number of distinct pairs of numbers `(num1, num2)` such that both numbers exist in `nums`, and the sum of the number of set bits in their bitwise OR and bitwise AND is at least `k`.

Two pairs `(num1, num2)` and `(num3, num4)` are considered distinct if `num1 != num3` or `num2 != num4`.

### Function Contract
**Inputs**

- `nums`: `list[int]` — An array of positive integers.
- `k`: `int` — A positive integer representing the minimum required sum of set bits.

**Return value**

- `int` — The total number of distinct excellent pairs.

### Examples
**Example 1**

- Input: `nums = [1, 2, 3, 1]`, `k = 3`
- Output: `5`
- Explanation: The unique numbers in `nums` are `1`, `2`, and `3`. Their set bit counts (popcounts) are:
  - `1` (binary `01`): 1 set bit
  - `2` (binary `10`): 1 set bit
  - `3` (binary `11`): 2 set bits

  The excellent pairs are:
  - `(1, 3)` with set bit sum `1 + 2 = 3 >= 3`
  - `(3, 1)` with set bit sum `2 + 1 = 3 >= 3`
  - `(2, 3)` with set bit sum `1 + 2 = 3 >= 3`
  - `(3, 2)` with set bit sum `2 + 1 = 3 >= 3`
  - `(3, 3)` with set bit sum `2 + 2 = 4 >= 3`

  Total excellent pairs = 5.

**Example 2**

- Input: `nums = [5, 1, 1]`, `k = 10`
- Output: `0`
- Explanation: The unique numbers are `5` and `1`. The maximum possible sum of set bits for any pair is `2 + 2 = 4` (for `(5, 5)`), which is less than `10`. Thus, there are 0 excellent pairs.

**Example 3**

- Input: `nums = [1, 2, 4, 8]`, `k = 2`
- Output: `16`
- Explanation: The unique numbers are `1, 2, 4, 8`, each having exactly 1 set bit. Any pair of these numbers will have a set bit sum of `1 + 1 = 2 >= 2`. Since there are 4 unique numbers, there are `4 * 4 = 16` possible pairs, all of which are excellent.

---

## Solution
### Approach
The problem can be simplified using a fundamental bitwise identity:
$$\text{popcount}(a \text{ OR } b) + \text{popcount}(a \text{ AND } b) = \text{popcount}(a) + \text{popcount}(b)$$

### Why this identity holds:
For any bit position:
- If both numbers have `0`, both the OR and AND results have `0` at that position (sum of bits = 0).
- If one number has `1` and the other has `0`, the OR result has `1` and the AND result has `0` (sum of bits = 1).
- If both numbers have `1`, both the OR and AND results have `1` (sum of bits = 2).

In all cases, the sum of the bits in the OR and AND operations is exactly equal to the sum of the bits in the individual numbers.

### Algorithm Steps:
1. **Deduplicate**: Since we only care about distinct pairs of *values*, we first find the unique numbers in `nums` using a set.
2. **Count Set Bits**: For each unique number, compute its set bit count (popcount).
3. **Frequency Map**: Count the frequency of each popcount. Since $nums[i] \le 10^9 < 2^{30}$, the popcount will always be between $0$ and $30$.
4. **Count Pairs**: Iterate through all pairs of popcounts $(i, j)$ from $0$ to $30$. If $i + j \ge k$, add the product of their frequencies (`count[i] * count[j]`) to the total answer.

### Complexity Analysis
- **Time Complexity**: $\mathcal{O}(N \log(\max(\text{nums})))$ where $N$ is the length of `nums`. Finding unique elements and computing their set bits takes $\mathcal{O}(N)$ time. The final step of counting pairs takes $\mathcal{O}(30^2) = \mathcal{O}(1)$ operations.
- **Space Complexity**: $\mathcal{O}(U)$ where $U$ is the number of unique elements in `nums` (at most $N$), to store the unique elements in a set.

### Reference Implementations
<details>
<summary>python</summary>

```python
def solve(nums: list[int], k: int) -> int:
    # Deduplicate the input array to get unique numbers
    unique_nums = set(nums)

    # Count frequencies of each popcount (number of set bits)
    # Since nums[i] <= 10^9, the maximum number of set bits is 30.
    count = [0] * 31
    for x in unique_nums:
        count[bin(x).count('1')] += 1

    ans = 0
    # Iterate over all possible pairs of popcounts
    for i in range(31):
        for j in range(31):
            if i + j >= k:
                ans += count[i] * count[j]

    return ans
```
</details>
