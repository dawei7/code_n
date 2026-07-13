# Product of Array Except Self

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 238 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/product-of-array-except-self/) |

## Problem Description
### Goal
Given an integer array `nums` of at least two elements, construct an output of the same length. At each index `i`, the output value must equal the product of every input element except `nums[i]` itself. The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

Return all position-specific products without using division, and compute them in linear time. Zero values follow the same rule: one zero makes every other position's product zero, while two or more zeroes make all products zero. The output array does not count toward the constant-extra-space target, but do not allocate additional storage that grows with the input beyond that returned result.

### Function Contract
**Inputs**

- `nums`: a list of at least two integers

**Return value**

A list where position `i` contains the product of every `nums[j]` for which $j \ne i$.

### Examples
**Example 1**

- Input: `nums = [1,2,3,4]`
- Output: `[24,12,8,6]`

**Example 2**

- Input: `nums = [-1,1,0,-3,3]`
- Output: `[0,0,9,0,0]`

**Example 3**

- Input: `nums = [2,3]`
- Output: `[3,2]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Split every answer around its index**

For index `i`, the answer is the product of values strictly to its left times the product of values strictly to its right.

**Store left products directly in the result**

Scan left to right while maintaining the product seen so far. Store that product at each index before multiplying by the current value.

**Fold in right products on the return pass**

Scan right to left with a second running product. Multiply each stored prefix by the current suffix, then extend the suffix with the current input value.

During the first pass, output index `i` equals the product of `nums[0:i]`. During the second, the suffix variable equals the product of values after `i`; their multiplication therefore excludes exactly `nums[i]`.

Every index other than `i` lies uniquely to its left or right, so the two running products include every required factor exactly once and omit the current factor. This remains valid when values are zero or negative.

#### Complexity detail

Two linear scans take $O(n)$ time. Excluding the required output array, only two scalar products are stored, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Division by the total product:** violates the contract and needs special handling for zeros.
- **Recompute each product independently:** takes $O(n^2)$ time.
- One or multiple zeros and negative signs are handled naturally by prefix/suffix multiplication.

</details>
