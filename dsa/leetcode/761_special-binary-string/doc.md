# Special Binary String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 761 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Divide and Conquer, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/special-binary-string/) |

## Problem Description

### Goal

A binary string is special when it contains the same number of `1` and `0` characters and every prefix has at least as many `1`s as `0`s. The input string `s` is guaranteed to be special.

In one move, choose two consecutive, nonempty special substrings of `s` and swap their positions. You may perform the move any number of times. Return the lexicographically largest string obtainable while preserving the characters; every intermediate arrangement must arise through the allowed adjacent special-substring swaps.

### Function Contract

**Inputs**

- `s`: a special binary string.

**Return value**

- The lexicographically largest special string obtainable through any number of allowed adjacent-special-substring swaps.

### Examples

**Example 1**

- Input: `s = "11011000"`
- Output: `"11100100"`
- Explanation: Optimizing and reordering the special blocks inside the outer pair produces the larger string.

**Example 2**

- Input: `s = "10"`
- Output: `"10"`
- Explanation: The only nonempty special block cannot be improved.

**Example 3**

- Input: `s = "101100"`
- Output: `"110010"`
- Explanation: The top-level blocks `"10"` and `"1100"` can be swapped, and the longer block is lexicographically larger.

### Required Complexity

- **Time:** $O(n^2)$
- **Space:** $O(n^2)$

<details>
<summary>Approach</summary>

#### General

**Treat the string as balanced structure**

Interpret `1` as an opening parenthesis and `0` as a closing parenthesis. The special-string prefix condition is exactly the balanced-parentheses condition. Scanning a special string with a balance counter splits it whenever the balance returns to zero; these are its top-level primitive special blocks.

**Canonicalize from the inside out**

Every primitive block has the form `1 + inner + 0`, where `inner` is itself a sequence of special blocks. Recursively transform `inner` into its largest reachable form, then restore the outer `1` and `0`. This is necessary because swaps may occur at any nesting depth, not just between the original top-level blocks.

**Sort sibling blocks in descending order**

Allowed swaps let adjacent sibling special blocks be permuted arbitrarily. For any two strings `a` and `b`, placing the lexicographically larger one first gives the larger concatenation because neither special block can be a strict prefix of another special block: a completed block has balance zero, while every proper prefix of a primitive block has positive balance. Therefore, sorting all recursively canonicalized siblings in descending lexicographic order gives their largest possible concatenation.

The recursion makes every child optimal before its parent orders the children. Any reachable result consists of reachable forms of the same balanced children in some order; replacing each child by its recursive maximum and sorting those maxima cannot make the result smaller. Induction over the nesting structure therefore proves that the returned root string is the largest reachable string.

#### Complexity detail

Across nested recursive levels, scanning substrings, constructing immutable strings, and comparing canonical blocks can process the same characters repeatedly, giving an $O(n^2)$ bound for the input limits. Recursion, component lists, and intermediate strings use $O(n^2)$ space in the conservative worst case.

#### Alternatives and edge cases

- **Generate every allowed swap:** Exploring the reachability graph is correct for tiny strings but has exponential or worse state growth.
- **Repeatedly select the largest sibling:** This produces the same ordering but takes quadratic comparisons per sibling list instead of using a sort.
- **Sort only the original top-level blocks:** This misses improvements inside primitive blocks such as `"11011000"`.
- **Single primitive `"10"`:** It is already maximal.
- **Repeated identical blocks:** Reordering them has no effect, but they remain valid independent siblings.
- **Deeply nested input:** A string such as `"111000"` has one child at each level and remains unchanged.
- **Several top-level blocks:** Their optimized forms must be sorted even when no outer pair encloses the whole string.

</details>
