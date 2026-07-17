# Smallest String With A Given Numeric Value

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1663 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/) |

## Problem Description
### Goal
Assign each lowercase letter its 1-indexed alphabet position: `a` has value 1, `b` has value 2, through `z` with value 26. The numeric value of a string is the sum of all its character values; for example, `"abe"` has value $1+2+5=8$.

Given a required length `n` and numeric value `k`, construct the lexicographically smallest lowercase string having exactly that length and sum. The constraints guarantee that at least one such string exists. Lexicographic comparison uses the first position where two equal-length strings differ.

### Function Contract
**Inputs**

- `n`: the required string length, where $1 \le n \le 10^5$.
- `k`: the required numeric value, where $n \le k \le 26n$.

**Return value**

Return the lexicographically smallest length-$n$ lowercase string whose character values sum to $k$.

### Examples
**Example 1**

- Input: `n = 3, k = 27`
- Output: `"aay"`

Its value is $1+1+25=27$, and keeping the extra value at the right makes the prefix smallest.

**Example 2**

- Input: `n = 5, k = 73`
- Output: `"aaszz"`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Begin with the smallest possible string.** Fill all $n$ positions with `a`. This contributes value $n$, leaving `remaining = k - n` additional value to distribute. Each position can absorb at most 25 more before reaching `z`.

**Spend extra value from right to left.** At the last position, add as much as possible, up to 25, then continue toward the front until no value remains. Concentrating increases at later positions preserves smaller letters at every earlier position for as long as feasibility allows.

**Why the greedy placement is lexicographically minimal.** Suppose an alternative places some positive increase at an earlier position while a later position is not yet `z`. Moving one unit of value from the earlier character to the later one preserves the total sum and length but makes the first differing position smaller. Therefore no optimal string can have such a pair. The required form is consequently some `a` prefix, at most one partially increased character, and a suffix of `z` characters—exactly what right-to-left allocation produces.

#### Complexity detail

Creating and joining the $n$ output characters takes $O(n)$ time. The allocation loop visits at most $n$ positions, so total time remains $O(n)$. The mutable character array used to build the required output occupies $O(n)$ space.

#### Alternatives and edge cases

- **Direct quotient construction:** Divide `k - n` by 25 to determine the number of trailing `z` characters and the optional middle character, then assemble the same greedy form.
- **Left-to-right feasibility checks:** Try letters in order while reserving enough capacity for the suffix. This is correct, but recomputing suffix capacity by scanning remaining positions can cost $O(n^2)$.
- **Largest letters first at the front:** This satisfies the sum but produces a lexicographically large string.
- When $k=n$, every character is `a`.
- When $k=26n$, every character is `z`.
- A remainder divisible by 25 needs no partially increased middle character.
- For $n=1$, the answer is the single letter whose value is `k`.
- The output length itself imposes an $\Omega(n)$ time and space requirement for materializing the returned string.

</details>
