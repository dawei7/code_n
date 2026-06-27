# Number of Beautiful Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2748 |
| Difficulty | Easy |
| Topics | Array, Hash Table, Math, Counting, Number Theory |
| Official Link | [number-of-beautiful-pairs](https://leetcode.com/problems/number-of-beautiful-pairs/) |

## Problem Description & Examples
### Goal
Given a 0-indexed array of positive integers `nums`, determine the total number of "beautiful pairs" of indices `(i, j)` such that `0 <= i < j < nums.length`. 

A pair of indices `(i, j)` is considered **beautiful** if the first digit of `nums[i]` and the last digit of `nums[j]` are coprime (i.e., their greatest common divisor is 1).

### Function Contract
**Inputs**

- `nums`: `List[int]` - An array of positive integers.

**Return value**

- `int` - The total number of beautiful pairs in the array.

### Examples
**Example 1**

- Input: `nums = [2, 5, 1, 4]`
- Output: `5`
- Explanation: 
  - For `i = 0` (`nums[0] = 2`, first digit is 2):
    - `j = 1` (`nums[1] = 5`, last digit is 5): `gcd(2, 5) = 1` (Beautiful)
    - `j = 2` (`nums[2] = 1`, last digit is 1): `gcd(2, 1) = 1` (Beautiful)
    - `j = 3` (`nums[3] = 4`, last digit is 4): `gcd(2, 4) = 2` (Not beautiful)
  - For `i = 1` (`nums[1] = 5`, first digit is 5):
    - `j = 2` (`nums[2] = 1`, last digit is 1): `gcd(5, 1) = 1` (Beautiful)
    - `j = 3` (`nums[3] = 4`, last digit is 4): `gcd(5, 4) = 1` (Beautiful)
  - For `i = 2` (`nums[2] = 1`, first digit is 1):
    - `j = 3` (`nums[3] = 4`, last digit is 4): `gcd(1, 4) = 1` (Beautiful)
  - Total beautiful pairs = 5.

**Example 2**

- Input: `nums = [11, 21, 12]`
- Output: `2`
- Explanation:
  - For `i = 0` (`nums[0] = 11`, first digit is 1):
    - `j = 1` (`nums[1] = 21`, last digit is 1): `gcd(1, 1) = 1` (Beautiful)
    - `j = 2` (`nums[2] = 12`, last digit is 2): `gcd(1, 2) = 1` (Beautiful)
  - For `i = 1` (`nums[1] = 21`, first digit is 2):
    - `j = 2` (`nums[2] = 12`, last digit is 2): `gcd(2, 2) = 2` (Not beautiful)
  - Total beautiful pairs = 2.

---

## Underlying Base Algorithm(s)
The naive approach is to check all $O(N^2)$ pairs of indices. However, we can optimize this to $O(N)$ using a **frequency counting / hash map** approach.

Since the first digit of any positive integer can only be a single digit from `1` to `9`, we can maintain a frequency array `count` of size 10. As we iterate through the array from left to right:
1. For the current number `num`, we extract its last digit: `last_digit = num % 10`.
2. We iterate through all possible first digits `d` from `1` to `9`. If `gcd(d, last_digit) == 1`, we add `count[d]` (the number of times we have seen `d` as a first digit so far) to our total beautiful pairs.
3. We then extract the first digit of the current number and increment its frequency in our `count` array.

This single-pass approach avoids nested loops over the array, reducing the time complexity significantly.

---

## Complexity Analysis
- **Time Complexity**: $O(N)$ where $N$ is the length of `nums`. For each element, we perform a constant number of operations (at most 9 GCD checks).
- **Space Complexity**: $O(1)$ auxiliary space, as the frequency array size is fixed at 10 (digits 1 through 9).
