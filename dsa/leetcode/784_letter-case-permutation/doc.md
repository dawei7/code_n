# Letter Case Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 784 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Backtracking, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/letter-case-permutation/) |

## Problem Description

### Goal

Given a string `s` containing English letters and decimal digits, independently choose the lowercase or uppercase form of every letter. Digits have no case and must remain unchanged at their original positions.

Return all distinct strings obtainable from those choices, in any order. Every letter position contributes its own binary choice regardless of the cases of other letters, while the character order and string length remain fixed.

### Function Contract

**Inputs**

- `s`: a nonempty string containing only English letters and decimal digits.

**Return value**

- A list containing all case permutations exactly once, in any order.

### Examples

**Example 1**

- Input: `s = "a1b2"`
- Output: `["a1b2","a1B2","A1b2","A1B2"]`
- Explanation: Each of the two letters has two independent case choices.

**Example 2**

- Input: `s = "3z4"`
- Output: `["3z4","3Z4"]`
- Explanation: Only `z` branches into two choices.

**Example 3**

- Input: `s = "12345"`
- Output: `["12345"]`
- Explanation: With no letters, the original digit string is the sole permutation.

### Required Complexity

- **Time:** $O(n \cdot 2^l)$
- **Space:** $O(n \cdot 2^l)$

<details>
<summary>Approach</summary>

#### General

**Branch only at letters**

Walk through a mutable character array. A digit has only one continuation, while a letter creates two recursive branches: place its lowercase form, then its uppercase form. When the index reaches the end, join the current characters into one complete result.

**Cover every independent choice once**

If the string contains `l` letters, a root-to-leaf path records one of the two case decisions at each letter and no decision at a digit. Every possible sequence of `l` binary choices therefore reaches one leaf, and two different paths differ at some letter, so they cannot emit the same string. This proves that all $2^{l}$ permutations are produced exactly once.

The algorithm restores a letter after exploring its branches, keeping the shared character buffer valid for the caller. No generated string needs to be searched for duplicates because the recursion tree itself establishes uniqueness.

#### Complexity detail

There are $2^{l}$ output strings, and materializing each length-`n` string takes $O(n)$, for $O(n \cdot 2^l)$ time. The returned strings occupy $O(n \cdot 2^l)$ space; the recursion and mutable buffer add $O(n)$ auxiliary space.

#### Alternatives and edge cases

- **Iterative expansion:** Start with one empty prefix and duplicate the prefix list at each letter; this has the same output-sensitive complexity.
- **Bitmask choices:** Map the set bits of a mask to uppercase choices for the `l` letter positions; this also enumerates exactly $2^{l}$ results.
- **Enumerate masks for every character:** Treating digits as branch positions performs unnecessary work exponential in `n` instead of `l`.
- **Duplicate filtering:** Generating candidates and scanning an output list before insertion can add quadratic work in the number of permutations.
- **No letters:** Return a one-element list containing the original string.
- **Initially uppercase letters:** Both normalized lowercase and uppercase variants must still appear.
- **Output order:** Any ordering is valid, but every permutation must occur exactly once.

</details>
