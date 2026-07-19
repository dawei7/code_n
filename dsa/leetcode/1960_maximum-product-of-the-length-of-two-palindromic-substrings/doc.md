# Maximum Product of the Length of Two Palindromic Substrings

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1960 |
| Difficulty | Hard |
| Topics | String, Rolling Hash, Manacher's Algorithm |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings/) |

## Problem Description
### Goal
Given a zero-indexed lowercase string `s`, choose two non-intersecting
substrings. Both chosen substrings must be palindromes of odd length, and the
first must end before the second begins.

More precisely, choose indices $i\le j<k\le l$ so that `s[i:j + 1]` and
`s[k:l + 1]` are odd-length palindromes. Return the maximum possible product
of their lengths. A substring is contiguous, and a palindrome reads identically
from left to right and right to left.

### Function Contract
**Inputs**

- `s`: a lowercase English string of length $N$, where
  $2\le N\le10^5$.

**Return value**

- The maximum product of the lengths of two non-overlapping odd-length
  palindromic substrings.

### Examples
**Example 1**

- Input: `s = "ababbb"`
- Output: `9`

**Example 2**

- Input: `s = "zaaaxbbby"`
- Output: `9`

**Example 3**

- Input: `s = "racecarxaba"`
- Output: `21`

### Required Complexity
- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Find every maximal odd palindrome**

Use Manacher's algorithm to compute `radius[center]`, the number of positions
from the center through one endpoint of the longest odd palindrome at that
center. Its full length is `2 * radius[center] - 1`. The algorithm reuses the
mirror radius inside the rightmost palindrome already discovered, then
expands only beyond that known boundary. Across the entire string, boundary
expansions take linear time.

**Record the best palindrome around every split**

For each center's maximal palindrome, record its length at its exact start and
end. Shrinking a palindrome by removing both endpoints gives another odd
palindrome, so a backward pass propagates an ending length two positions
shorter to the preceding endpoint. A forward maximum pass then makes
`ending[i]` the longest palindrome ending at or before `i`.

Apply the symmetric propagation to build `starting[i]`, the longest palindrome
starting at or after `i`. Every pair of non-overlapping substrings is separated
by some split between `i` and `i + 1`. Multiplying `ending[i]` by
`starting[i + 1]` gives the best pair crossing that split; taking the maximum
over all splits therefore considers an optimal pair and never combines
intersecting substrings.

#### Complexity detail

Manacher's scan, both endpoint-propagation passes, and the final split scan are
all linear in $N$, giving $O(N)$ time. The radius, ending, and starting arrays
each contain $N$ integers, so the auxiliary space is $O(N)$.

#### Alternatives and edge cases

- **Expand around every center independently:** This directly enumerates all
  odd palindromes and is easy to verify, but a uniform string requires
  $O(N^2)$ expansions.
- **Rolling hashes with binary search:** Forward and reverse hashes can test
  palindrome radii in $O(\log N)$ per center, giving $O(N\log N)$ time with
  collision considerations unless multiple robust moduli are used.
- Even-length palindromes do not qualify, even when they are longer than every
  odd palindrome nearby.
- A one-character substring is an odd palindrome, so every valid input of
  length at least two has a feasible product.
- The two chosen substrings may touch at a split, but their index ranges may
  not overlap.

</details>
