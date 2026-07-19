# Super Palindromes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 906 |
| Difficulty | Hard |
| Topics | Math, String, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/super-palindromes/) |

## Problem Description
### Goal
A positive integer is a palindrome when its decimal digits read the same from left to right and from right to left. It is a super-palindrome when the integer itself is a palindrome and it is also the square of a positive integer whose decimal representation is a palindrome. Both properties are required; a palindromic square with a non-palindromic square root does not qualify.

Two positive integers, `left` and `right`, are provided as decimal strings. Count the super-palindromes whose values lie in the inclusive range from `left` through `right`.

### Function Contract
Let $L=\operatorname{int}(\texttt{left})$, $R=\operatorname{int}(\texttt{right})$, and

$$
m=\left\lfloor\sqrt{R}\right\rfloor.
$$

**Inputs**

- `left`: the decimal representation of $L$.
- `right`: the decimal representation of $R$.

Both strings contain only digits, have no leading zeros, and have lengths from $1$ through $18$. The represented values satisfy $1 \leq L \leq R \leq 10^{18}-1$.

**Return value**

Return the number of super-palindromes in the inclusive interval $[L,R]$.

### Examples
**Example 1**

- Input: `left = "4", right = "1000"`
- Output: `4`

The qualifying values are $4$, $9$, $121$, and $484$. Although $676$ is a palindrome, its square root $26$ is not a palindrome.

**Example 2**

- Input: `left = "1", right = "2"`
- Output: `1`

Only $1=1^2$ qualifies.
