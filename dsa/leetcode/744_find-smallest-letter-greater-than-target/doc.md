# Find Smallest Letter Greater Than Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 744 |
| Difficulty | Easy |
| Topics | Array, Binary Search |
| Official Link | [LeetCode](https://leetcode.com/problems/find-smallest-letter-greater-than-target/) |

## Problem Description
### Goal
Given an array `letters` sorted in non-decreasing order and a character `target`, find the smallest character in the array that is lexicographically greater than `target`.

Return that character. If no stored character is strictly greater, wrap around and return the first character in `letters`. Duplicate letters may appear, equality does not qualify, and the input contains at least two different characters.

### Function Contract
**Inputs**

- `letters`: a nonempty nondecreasing list of lowercase English letters, possibly containing duplicates
- `target`: one lowercase English letter

**Return value**

- The first list value greater than `target`, or `letters[0]` when every value is less than or equal to `target`

### Examples
**Example 1**

- Input: `letters = ["c","f","j"], target = "a"`
- Output: `"c"`

**Example 2**

- Input: `letters = ["c","f","j"], target = "c"`
- Output: `"f"`

**Example 3**

- Input: `letters = ["x","x","y","y"], target = "z"`
- Output: `"x"`

### Required Complexity

- **Time:** $O(\log n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Search for an upper bound rather than an exact match**

The desired index is the first position whose letter is strictly greater than `target`. Maintain a half-open search range `[left, right)` over the sorted list. If `letters[mid] <= target`, neither `mid` nor anything left of it can be the answer, so move `left` to `mid+1`. Otherwise `mid` is a candidate and `right` moves to `mid`.

**Let duplicates fall on the rejected side**

Using `<=` is essential. Equal letters do not satisfy the strict condition, and moving past them ensures the search returns the first genuinely greater value even when the target appears many times.

**Apply circular wraparound after the search**

When the search finishes, `left` is either the upper-bound index or `n` if no letter is greater. Return `letters[left % n]`; the modulo leaves a valid index unchanged and maps the one-past-the-end sentinel to zero.

**Why the boundary is exact**

Throughout the search, every index before `left` is known to hold a value at most `target`, while every removed index at or after `right` holds a greater candidate. Convergence therefore places `left` at the smallest greater index. If that set is empty, convergence at `n` correctly triggers the specified first-letter wraparound.

#### Complexity detail

Binary search halves the remaining interval on each iteration, taking $O(\log n)$ time. It stores only index variables, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Standard-library upper bound:** `bisect_right(letters, target)` implements the same search and can be wrapped modulo the list length.
- **Linear scan:** return the first letter greater than the target; it is simple but takes $O(n)$ time when the answer is late or requires wraparound.
- **Target below the first letter:** the upper bound is index zero.
- **Target equals duplicates:** all equal copies must be skipped.
- **Target at or above the last letter:** no greater value exists, so return the first letter.
- **One distinct letter:** return that letter for every target at or above it.
- **Duplicate answer values:** the returned character is the same regardless of which identical occurrence begins the greater block.

</details>
