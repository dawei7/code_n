# Sign of the Product of an Array

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/sign-of-the-product-of-an-array/) |
| Frontend ID | 1822 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Define the sign of a number to be `1` when it is positive, `-1` when it is negative, and `0` when it equals zero. The integer array `nums` determines a product formed from all of its elements.

Return the sign of that complete product. Only the three-way sign classification is requested, not the potentially very large product itself. A single zero makes the product zero; otherwise, its sign depends on whether the number of negative factors is even or odd.

### Function Contract

**Inputs**

- `nums`: an integer array of length $n$, where $1 \le n \le 1000$.
- Every value satisfies $-100 \le \texttt{nums[i]} \le 100$.

**Return value**

- Return `1` if the product of all values is positive, `-1` if it is negative, or `0` if it is zero.

### Examples

**Example 1**

- Input: `nums = [-1,-2,-3,-4,3,2,1]`
- Output: `1`

Four negative factors give the nonzero product a positive sign.

**Example 2**

- Input: `nums = [1,5,0,2,-3]`
- Output: `0`

The zero factor makes the complete product zero.

**Example 3**

- Input: `nums = [-1,1,-1,1,-1]`
- Output: `-1`

There are three negative factors, so the product is negative.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Track only the information that affects the sign**

Start with sign `1`, the multiplicative sign identity. Scan the values once. A positive value changes nothing. Each negative value reverses the current sign, which records the parity of all negative factors seen so far without storing their count or multiplying their magnitudes.

**Return immediately when a zero appears**

Any product containing zero is zero regardless of all remaining factors. On encountering zero, return `0`; no later value can change that outcome. If the scan finishes without zero, return the accumulated `1` or `-1`.

**Why sign toggling matches multiplication**

Multiplying by a positive factor preserves a nonzero product's sign, while multiplying by a negative factor reverses it. The maintained state applies exactly these transitions in array order. Zero is handled by its absorbing-product rule. Therefore the final state equals the sign function applied to the mathematical product.

#### Complexity detail

In the no-zero case, all $n$ values are examined once; an earlier zero can only reduce the work. Time is $O(n)$. The algorithm stores one sign value and the current array element, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Multiply every value:** It is mathematically direct, but fixed-width languages may overflow and arbitrary-precision multiplication performs unnecessary work on a growing integer.
- **Recompute every prefix sign:** Rechecking the array from its beginning for each successive prefix eventually obtains the full sign, but repeats work and takes $O(n^2)$ time.
- **Count negative values:** Counting and checking parity is also $O(n)$ and correct, provided zero is handled separately.
- **Zero anywhere:** Return zero even when the number of negative values before or after it is odd.
- **All positive values:** The sign remains `1`.
- **Even negative count:** Pairs of negative factors cancel their sign changes.
- **Odd negative count:** One unpaired sign reversal leaves `-1`.
- **Boundary values:** `-100` and `100` affect only sign; their magnitudes need not be multiplied.
- **Single element:** Return that element's sign classification directly through the same scan.

</details>
