## Description

Given a string `s`, partition `s` such that every substring of the partition is a **palindrome**. Return *all possible palindrome partitioning of *`s`.
### Function Contract

**Inputs**

- `s`: The non-empty lowercase string to partition.

**Return value**

Return all partitions whose contiguous pieces are palindromes. Outer result order is not significant; substring order within a partition is.

### Examples
#### Example 1

- **Input:** `s = "aab"`
- **Output:** `[["a","a","b"],["aa","b"]]`
#### Example 2

- **Input:** `s = "a"`
- **Output:** `[["a"]]`
### Constraints

- $1 \le \text{s.length} \le 16$

- `s` contains only lowercase English letters.