# Ambiguous Coordinates

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 816 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Backtracking, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/ambiguous-coordinates/) |

## Problem Description

### Goal

A coordinate pair was originally written as `(x, y)`, but its comma, decimal points, and spaces were erased while the outer parentheses and digit order remained. Given that compressed string, reconstruct every coordinate that could have produced it by restoring exactly one comma and optionally one decimal point on either side.

Each restored number must use ordinary decimal notation: a multi-digit integer part cannot begin with `0`, and a fractional part cannot end with `0`. Forms such as `00`, `01`, `1.0`, `.5`, and `5.` are therefore invalid, while `0`, `0.5`, and `10` are valid. Return every valid formatted pair; their order does not matter.

### Function Contract

**Inputs**

- `s`: a string of digits enclosed in parentheses. Its interior contains between two and ten digits.

**Return value**

- All possible strings in the form `(x, y)`, in any order, where neither number has an invalid leading zero, and a fractional number has no trailing zero.

### Examples

**Example 1**

- Input: `s = "(123)"`
- Output: `["(1, 23)","(1, 2.3)","(12, 3)","(1.2, 3)"]`
- Explanation: Each interior split supplies the comma, and each side may contain at most one legal decimal point.

**Example 2**

- Input: `s = "(00011)"`
- Output: `["(0, 0.011)","(0.001, 1)"]`
- Explanation: Leading-zero rules eliminate every other placement.

**Example 3**

- Input: `s = "(0123)"`
- Output: `["(0, 123)","(0, 12.3)","(0, 1.23)","(0.1, 23)","(0.1, 2.3)","(0.12, 3)"]`
- Explanation: A multi-digit whole part cannot begin with zero, but `0` followed by a nonzero fractional suffix is valid.

### Required Complexity

- **Time:** $O(n^3 + nK)$
- **Space:** $O(n^2 + nK)$

<details>
<summary>Approach</summary>

#### General

**Choose the comma before choosing decimal points**

Remove the outer parentheses and try each of the $n - 1$ splits between consecutive digits. The prefix and suffix are independent number fragments. Generate every legal textual number for each fragment, then take their Cartesian product and format each pair as a coordinate.

**Classify a fragment by its boundary zeros**

A one-digit fragment always has one representation. For a longer fragment:

- if it begins and ends with `0`, it has no valid representation;
- if it begins with `0`, its only possible form is `0.` followed by the remaining digits;
- if it ends with `0`, only its integer form is valid;
- otherwise, its integer form and every internal decimal position are valid.

These cases follow directly from the two forbidden patterns: a multi-digit integer part may not start with zero, and a fractional part may not end with zero. They also generate every allowed form, because a number can contain at most one decimal point and every internal position is considered whenever neither boundary rule forbids it.

For each comma split, pairing all legal left and right forms produces exactly the coordinates using that comma. Different comma or decimal positions produce different strings, so collecting the products across all splits is complete and introduces no duplicates.

**Keep validation local to each side**

Rejecting a fragment before forming coordinate pairs avoids enumerating combinations that a leading or trailing zero has already made impossible. This is especially important for inputs dominated by zeros.

#### Complexity detail

Let `n` be the number of interior digits and `K` the number of returned coordinates. Across all comma splits, constructing the possible left and right representations costs $O(n^3)$ in the worst case because strings are copied. Formatting the `K` output strings costs $O(nK)$, for total $O(n^3 + nK)$ time. Temporary representations for one split occupy $O(n^2)$ characters, while the returned strings occupy $O(nK)$ space.

#### Alternatives and edge cases

- **Enumerate all marker placements, then validate:** Trying every comma and both decimal positions is straightforward but spends time constructing candidates whose boundary zeros make them immediately invalid.
- **Backtracking over punctuation:** A recursive generator can choose comma and decimal markers, but it needs the same validity rules and is less direct for a fixed maximum of three markers.
- **All nonzero digits:** Every comma split and every internal decimal position is legal, producing the largest output.
- **Fragment equal to `0`:** The single zero is valid; only multi-digit leading zeros are forbidden.
- **Leading and trailing zero together:** A multi-digit fragment such as `00` or `010` has no representation.
- **Output order:** Any order is valid, so the judge compares the coordinate strings as an unordered collection.

</details>
