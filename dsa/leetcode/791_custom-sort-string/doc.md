# Custom Sort String

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 791 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/custom-sort-string/) |

## Problem Description

### Goal

The distinct characters in string `order` define a custom relative ordering. Rearrange all characters of `s` so that whenever character `x` appears before character `y` in `order`, every occurrence of `x` appears before every occurrence of `y` in the result.

Return any permutation of `s` satisfying that rule. Characters not present in `order` may appear anywhere, and every input character occurrence must be preserved exactly once. Their relative ordering is otherwise unconstrained.

### Function Contract

**Inputs**

- `order`: a string of distinct lowercase letters defining their custom order.
- `s`: the lowercase string to rearrange.

**Return value**

- Any permutation of `s` that places characters named in `order` in the required relative order.

### Examples

**Example 1**

- Input: `order = "cba", s = "abcd"`
- Output: `"cbad"`
- Explanation: Ranked characters appear as `c`, then `b`, then `a`; unranked `d` may be placed freely.

**Example 2**

- Input: `order = "bcafg", s = "abcd"`
- Output: `"bcad"`
- Explanation: The characters shared with `order` follow `b`, `c`, `a`; `d` is unranked.

**Example 3**

- Input: `order = "kqep", s = "kqeep"`
- Output: `"kqeep"`
- Explanation: Repeated `e` characters stay together at their ranked position.

### Required Complexity

- **Time:** $O(m + n)$
- **Space:** $O(u)$

<details>
<summary>Approach</summary>

#### General

**Count before ordering**

Build a frequency table for the `n` characters of `s`. Then scan the `m` characters of `order`; for each one, append all of its occurrences and remove that entry from the table.

**Append characters without a custom rank**

After the ordered scan, every remaining frequency belongs to a character absent from `order`. Append those occurrences in any deterministic order. Their positions do not affect the custom constraint.

Every input occurrence is recorded once. Ranked occurrences are emitted exactly when their character is visited in `order`, so any two ranked character classes appear in the required relative order. The remaining occurrences are precisely the unranked characters and may be appended freely. Thus the result is both a permutation of `s` and a valid custom ordering.

#### Complexity detail

Counting `s`, scanning `order`, and emitting the `n` output characters takes $O(m + n)$ time. The frequency table stores `u` distinct characters from `s`, using $O(u)$ auxiliary space apart from the returned string.

#### Alternatives and edge cases

- **Rank-key sorting:** Sort `s` by a map from ordered characters to ranks; this is concise but takes $O(n \log n)$ time.
- **Fixed alphabet counts:** With lowercase English letters, a 26-element array replaces the hash table while preserving linear time.
- **Selection sorting by custom rank:** Repeatedly searching the remaining suffix is correct but takes $O(n^2)$ time.
- **No ranked characters in `s`:** Any permutation is valid; returning `s` unchanged is sufficient.
- **Repeated characters:** Emit the complete frequency at its single ranked position.
- **Order characters absent from `s`:** They contribute nothing and do not affect the output.
- **Unranked characters:** They may appear before, between, or after ranked groups as long as multiplicities are preserved.

</details>
