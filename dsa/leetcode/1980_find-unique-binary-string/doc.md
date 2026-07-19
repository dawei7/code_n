# Find Unique Binary String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1980 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Backtracking |
| Official Link | [LeetCode](https://leetcode.com/problems/find-unique-binary-string/) |

## Problem Description
### Goal
You are given `n` distinct binary strings in the array `nums`. The array
contains exactly `n` strings, and every string has exactly `n` characters,
each either `0` or `1`.

Construct and return any binary string of length `n` that does not occur in
`nums`. Several strings may satisfy the requirement; no lexicographic,
numeric, or other tie-breaking rule is imposed. The returned value only needs
to be missing from the supplied collection; it does not need to identify or
represent every other binary string that is absent.

### Function Contract
**Inputs**

- `nums`: a list of $N$ distinct binary strings, where $1 \le N \le 16$.
- Every entry has length $N$ and contains only `0` and `1`.

**Return value**

- Any length-$N$ binary string absent from `nums`.

### Examples
**Example 1**

- Input: `nums = ["01", "10"]`
- Output: `"11"`

**Example 2**

- Input: `nums = ["00", "01"]`
- Output: `"10"`

**Example 3**

- Input: `nums = ["111", "011", "001"]`
- Output: `"000"`

### Required Complexity
- **Time:** $O(N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Flip the main diagonal**

Build an output character for every index $i$ from `0` through `N - 1`.
Inspect the character `nums[i][i]`: write `1` when that diagonal character is
`0`, and write `0` when it is `1`.

This construction is always defined because the array has $N$ rows and each
row has length $N$. It also produces exactly $N$ binary characters.

**Why the constructed string is absent**

Compare the result with input row `nums[i]`. At position $i$, the result
contains the complement of `nums[i][i]`, so the two strings differ at that
position. This argument applies independently to every input row. The result
therefore differs from all $N$ supplied strings and must be a valid missing
binary string.

The construction is a finite form of Cantor's diagonal argument: rather than
searching the much larger space of $2^N$ candidates, it certifies one new
string through one deliberate mismatch per listed row.

#### Complexity detail

The algorithm reads one diagonal character and writes one output character
for each of the $N$ rows, taking $O(N)$ time. The returned string contains
$N$ characters and therefore uses $O(N)$ space; aside from that output, only
constant auxiliary state is required.

#### Alternatives and edge cases

- **Enumerate binary values:** Store the inputs and test candidates from zero
  upward. This is correct, but may inspect many candidates and does not exploit
  the square input structure.
- **Backtracking:** Generate bits until finding an absent leaf. It can explore
  an exponential candidate tree even though a direct construction exists.
- **Random generation:** Repeated trials eventually may find a missing value,
  but provide neither deterministic time nor a direct correctness guarantee.
- For `N = 1`, complementing the sole input bit returns the only other binary
  string.
- Input order may change which diagonal answer is produced, but every produced
  answer remains valid.
- The result must have exactly $N$ characters and contain no character other
  than `0` or `1`.
- Returning any absent string is correct; matching one illustrative example is
  not required.

</details>
