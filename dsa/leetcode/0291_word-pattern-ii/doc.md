# Word Pattern II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 291 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Backtracking |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/word-pattern-ii/) |

## Problem Description
### Goal
Given a symbolic `pattern` and a target string `s`, assign each distinct pattern character a nonempty substring. Replacing pattern characters from left to right with their assigned strings must concatenate to exactly `s`, consuming every target character in order.

Return `True` when such an assignment exists. The mapping must be consistent and bijective: repeated pattern characters reuse the identical substring, while different characters cannot receive the same substring. Substrings may have different lengths and may repeat internally, but none may be empty. Return `False` when every possible boundary assignment leaves unmatched text or violates either mapping direction.

### Function Contract
**Inputs**

- `pattern`: the sequence of symbolic characters to replace
- `s`: the complete target string

**Return value**

`True` when a bijective substitution reconstructs `s`; otherwise `False`.

### Examples
**Example 1**

- Input: `pattern = "abab", s = "redblueredblue"`
- Output: `true`

**Example 2**

- Input: `pattern = "aaaa", s = "asdasdasdasd"`
- Output: `true`

**Example 3**

- Input: `pattern = "aabb", s = "xyzabcxzyabc"`
- Output: `false`

### Required Complexity

- **Time:** $O(2^n)$
- **Space:** $O(n + p)$

<details>
<summary>Approach</summary>

#### General

**Why this is not ordinary pattern matching**

The pattern does not say where one replacement ends and the next begins. For `pattern = "ab"`, every split of `s` into two nonempty pieces is initially possible. The algorithm must discover both the boundaries and the character assignments, which naturally leads to backtracking.

**The search state**

Two indices describe how much of each input has been consumed. A character-to-substring map remembers established meanings, while a set of used substrings enforces the reverse direction of the bijection.

If the next pattern character is already mapped, there is no branching: its known substring must occur at the current target position. If it is new, each nonempty prefix of the remaining target is a possible assignment, except prefixes already used by another character.

**Leave enough text for the suffix**

A candidate cannot consume characters needed by later pattern positions. For each remaining occurrence, an assigned character needs the full length of its known substring and an unassigned character needs at least one character. This lower bound limits the last candidate endpoint and cuts off impossible branches before recursion.

For `pattern = "abab"` and `s = "redblueredblue"`, a successful branch assigns `a -> "red"` and `b -> "blue"`. The final two pattern positions then perform direct prefix checks; they do not branch again.

**Why the search is complete**

Any valid substitution determines a sequence of substring endpoints. When the search first encounters a character, it tries the endpoint used by that substitution; later occurrences follow the stored value. Therefore the valid sequence is among the explored branches. A branch is accepted only when both inputs end together, so partial or overlong matches cannot succeed.

#### Complexity detail

There can be exponentially many partitions, giving exponential worst-case time in target length `n`. The recursion and live assignments use $O(n + p)$ space.

#### Alternatives and edge cases

- Enumerating complete partitions before checking assignments repeats work that early consistency checks avoid.
- A forward map alone is insufficient because two different characters could receive the same substring.
- Empty assignments must never be tried.

</details>
