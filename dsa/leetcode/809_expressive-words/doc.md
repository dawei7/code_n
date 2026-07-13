# Expressive Words

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 809 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/expressive-words/) |

## Problem Description

### Goal

A word is stretchy relative to target string `s` when it can be made equal to `s` by repeatedly extending groups of identical consecutive characters. One extension adds copies of a group's character so that the resulting group has length at least `3`.

Given candidate array `words`, return how many entries are stretchy. Character-group order must match `s`; a candidate group may remain unchanged, or it may be lengthened only when the corresponding target group is at least three characters long. Characters cannot be deleted, replaced, or moved between groups.

### Function Contract

**Inputs**

- `s`: the nonempty lowercase target string.
- `words`: a list of nonempty lowercase candidate words.

**Return value**

- The number of candidates that can be stretched into `s` under the group-expansion rule.

### Examples

**Example 1**

- Input: `s = "heeellooo", words = ["hello","hi","helo"]`
- Output: `1`
- Explanation: `hello` can expand its `e` and `o` groups, while the other candidates have incompatible character groups.

**Example 2**

- Input: `s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]`
- Output: `3`
- Explanation: Both target runs have length five, so every shorter positive run of the matching character can expand to it.

**Example 3**

- Input: `s = "abcd", words = ["abc"]`
- Output: `0`
- Explanation: Stretching cannot introduce the missing `d` group.

### Required Complexity

- **Time:** $O(c)$
- **Space:** $O(c)$

<details>
<summary>Approach</summary>

#### General

**Compress strings into character runs**

Represent a string as consecutive `(character, count)` groups. Encode the target once, then encode each candidate. Stretching can change only a run's count, so a candidate must have exactly the same sequence of group characters as the target.

**Check the only legal count changes**

For matching groups with target length `target_count` and word length `word_count`, reject when the word run is longer because stretching cannot delete characters. If the counts differ, the target run must have length at least three; a target run of length one or two cannot be the result of a stretch and therefore requires exact equality.

When every group passes, independently expanding each shorter word run to its target count constructs `s`, so the candidate is expressive. Conversely, any legal stretch preserves group order and characters, never shrinks a run, and can create a count difference only in a target group of length at least three. The tests are therefore necessary and sufficient.

#### Complexity detail

Let `c` be the total number of characters in `s` and all candidates. Run-length encoding and comparing each group processes $O(c)$ characters overall. The target groups and one candidate's groups require at most $O(c)$ auxiliary space in the worst case.

#### Alternatives and edge cases

- **Two pointers per candidate:** Scan target and word runs directly without materializing candidate groups; this uses constant per-word space but rescans the target for every word.
- **Regular expressions:** Pattern construction can express stretchable groups, but escaping and exact group-length semantics are less transparent.
- **Repeated suffix slicing:** Rebuilding the unprocessed suffix after every group is correct but can take $O(n^2)$ time on many short runs.
- **Exact word:** No stretching is required, so it is always accepted.
- **Target run shorter than three:** Its candidate run must have exactly the same length.
- **Candidate run longer than target:** It cannot be shortened and must be rejected.
- **Character-group mismatch:** Missing, extra, or reordered groups cannot be repaired by stretching.

</details>
