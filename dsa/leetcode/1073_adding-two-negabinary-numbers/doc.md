# Adding Two Negabinary Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1073 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/adding-two-negabinary-numbers/) |

## Problem Description

### Goal

Arrays `arr1` and `arr2` represent two numbers in base $-2$. Each array contains binary digits ordered from most significant to least significant. Thus, for example, `[1, 1, 0, 1]` represents

$$
(-2)^3+(-2)^2+(-2)^0=-3.
$$

Each input has no leading zeros: it is either `[0]` or begins with `1`. Add the represented numbers and return their sum in the same most-significant-bit-first base-$-2$ format, again using only zeros and ones and no leading zeros except for the representation `[0]` itself.

### Function Contract

**Inputs**

- `arr1`: an $A$-digit base-$-2$ representation, where $1 \le A \le 1000$.
- `arr2`: a $B$-digit base-$-2$ representation, where $1 \le B \le 1000$.
- Every digit is `0` or `1`, and neither input has a leading zero unless it is exactly `[0]`.

**Return value**

- A most-significant-bit-first array representing the sum in base $-2$, with no leading zeros unless the sum is zero.

### Examples

**Example 1**

- Input: `arr1 = [1, 1, 1, 1, 1], arr2 = [1, 0, 1]`
- Output: `[1, 0, 0, 0, 0]`
- Explanation: The inputs represent 11 and 5, while the output represents 16.

**Example 2**

- Input: `arr1 = [0], arr2 = [0]`
- Output: `[0]`

**Example 3**

- Input: `arr1 = [0], arr2 = [1]`
- Output: `[1]`
