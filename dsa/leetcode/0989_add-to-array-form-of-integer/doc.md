# Add to Array-Form of Integer

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 989 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/add-to-array-form-of-integer/) |

## Problem Description

### Goal

The array-form of a nonnegative integer stores its decimal digits from left to right. For example, the integer $1321$ has array-form `[1, 3, 2, 1]`.

Given an array-form integer `num` and a positive integer `k`, add `k` to the represented value and return the sum in the same array-form. The input contains no leading zero unless it represents zero itself, and the returned digit list must likewise be the ordinary decimal representation of the exact sum.

### Function Contract

**Inputs**

- `num`: a list of $N$ decimal digits, where $1\le N\le10^4$, each digit is from $0$ through $9$, and there are no unnecessary leading zeros.
- `k`: an integer satisfying $1\le\texttt{k}\le10^4$.

Let $D$ be the number of decimal digits in `k`, and define $L=\max(N,D)$.

**Return value**

- The decimal digits of the represented integer plus `k`, in left-to-right order.

### Examples

**Example 1**

- Input: `num = [1, 2, 0, 0], k = 34`
- Output: `[1, 2, 3, 4]`
- Explanation: $1200+34=1234$.

**Example 2**

- Input: `num = [2, 7, 4], k = 181`
- Output: `[4, 5, 5]`

**Example 3**

- Input: `num = [2, 1, 5], k = 806`
- Output: `[1, 0, 2, 1]`

### Required Complexity

- **Time:** $O(L)$
- **Space:** $O(L)$

<details>
<summary>Approach</summary>

#### General

**Use `k` as the initial carry:** Start at the final digit of `num`. Add that digit to the current carry, append `total % 10` to a reversed result, and update the carry with `total // 10`. Move one position left and repeat.

**Continue until both sources are exhausted:** The loop runs while an input digit remains or the carry is nonzero. Once `k` has been reduced to zero, the same operation copies remaining digits unless a previous addition still propagates a carry. If the carry remains after the most significant input digit, its decimal digits are emitted by further iterations.

At each step, the appended digit is the correct digit for the current decimal place because division by ten separates that place's remainder from everything that belongs farther left. Reversing the collected least-significant-first digits yields the exact conventional array-form of the sum.

#### Complexity detail

The loop processes at most $L+1$ decimal places, so time is $O(L)$. The returned digits use $O(L)$ space; counters and carry use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Convert the full array to an integer:** Repeatedly growing an arbitrary-precision integer performs increasingly expensive arithmetic and is unavailable in fixed-width languages for up to $10^4$ digits.
- **Convert through a decimal string:** Standard integer parsers may reject or overflow such a long value and obscure the simple digit-wise addition.
- **Carry through every digit:** Inputs made entirely of nines can add one extra leading digit.
- **Zero array-form:** `num = [0]` is valid and produces the ordinary digits of `k`.
- **`k` has more digits:** After all input digits are consumed, remaining carry digits are emitted normally.

</details>
