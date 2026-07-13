# Prime Arrangements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1175 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [prime-arrangements](https://leetcode.com/problems/prime-arrangements/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/prime-arrangements/).

### Goal
Count permutations of the numbers `1` through `n` where prime numbers occupy prime-numbered positions. Positions are 1-indexed. Return the count modulo `1_000_000_007`.

### Function Contract
**Inputs**

- `n`: Upper bound of the permutation range.

**Return value**

Number of valid permutations modulo `1_000_000_007`.

### Examples
**Example 1**

- Input: `n = 5`
- Output: `12`

**Example 2**

- Input: `n = 100`
- Output: `682289015`

**Example 3**

- Input: `n = 1`
- Output: `1`

---

## Solution
### Approach
Count how many numbers from `1` to `n` are prime; call this count `p`. Those `p` prime values can be permuted among the `p` prime positions in `p!` ways, and the remaining values can be permuted among the remaining positions in `(n - p)!` ways.

Compute `p`, then return `p! * (n - p)!` modulo `1_000_000_007`.

### Complexity Analysis
- **Time Complexity**: `O(n * sqrt(n))` with direct primality checks, or `O(n log log n)` with a sieve.
- **Space Complexity**: `O(1)` for direct checks, or `O(n)` with a sieve.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
