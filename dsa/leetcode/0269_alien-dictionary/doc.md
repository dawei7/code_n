# Alien Dictionary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 269 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, String, Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/alien-dictionary/) |

## Problem Description
### Goal
You are given words already sorted lexicographically according to an unknown alphabet. Infer precedence relationships from the first differing characters of adjacent words, while also accounting for every distinct character that appears even when no comparison constrains it.

Return any ordering of all observed characters consistent with the supplied dictionary. Several orders may be valid. Return an empty string when the constraints contain a cycle or when a longer word incorrectly appears before its exact prefix, since no alphabet can produce that order. Do not impose precedence from later differing positions after the first difference has already determined an adjacent-word comparison.

### Function Contract
**Inputs**

- `words`: dictionary words in alien lexicographic order

**Return value**

Any character ordering consistent with the dictionary, or `""` when the ordering is impossible.

### Examples
**Example 1**

- Input: `words = ["wrt","wrf","er","ett","rftt"]`
- Output: `"wertf"`

**Example 2**

- Input: `words = ["z","x","z"]`
- Output: `""`

**Example 3**

- Input: `words = ["abc","ab"]`
- Output: `""`

### Required Complexity

- **Time:** $O(c + e)$
- **Space:** $O(a + e)$

<details>
<summary>Approach</summary>

#### General

**Only the first difference between adjacent words constrains order**

Create a graph node for every observed character. For each adjacent word pair, the first differing characters define one directed edge. If the first word strictly extends an otherwise identical second word, the dictionary is invalid.

**Emit characters whose prerequisites are satisfied**

Track indegrees and repeatedly remove zero-indegree characters, decrementing their outgoing neighbors. A min-heap makes the app reference deterministic when several valid choices exist.

Every emitted character currently has no unmet predecessor. Removing it deletes exactly its satisfied outgoing constraints, so remaining indegrees count precisely the unmet prerequisites.

**Prefix invalidity and graph cycles cover both failure modes**

At the first unequal characters of adjacent words, the earlier word proves one directed precedence relation; later characters cannot add constraints because lexicographic comparison is already decided. If no difference exists, a longer word preceding its own prefix is impossible. For all other inputs, Kahn's algorithm emits only characters whose predecessors are already placed, so its complete result satisfies every edge. Failure to emit all nodes means the remaining constraints contain a cycle and no alphabet order exists.

#### Complexity detail

Adjacent comparisons inspect at most `c` total relevant characters and graph processing is $O(a + e)$ apart from the small deterministic heap factor. Graph and indegree storage use $O(a + e)$ space.

#### Alternatives and edge cases

- **Compare every word pair:** adds unnecessary quadratic work.
- **Ignore the prefix rule:** incorrectly accepts `["abc","ab"]`.
- Repeated words add no edge; isolated characters must still appear in the returned order.

</details>
