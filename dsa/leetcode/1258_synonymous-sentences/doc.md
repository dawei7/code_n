# Synonymous Sentences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1258 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Backtracking, Sort, Union-Find |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/synonymous-sentences/) |

## Problem Description

### Goal

You are given pairs of synonymous lowercase words and a sentence `text`. Synonymy is transitive: when one word is synonymous with a second and the second with a third, all three belong to the same interchangeable group.

Create every sentence obtainable by independently replacing any word in `text` with any word from its synonym group. Words absent from the synonym pairs remain unchanged. Preserve the original word positions and single-space separation, include the original sentence, and return all distinct generated sentences in lexicographically ascending order.

### Function Contract

**Inputs**

- `synonyms`: $P$ pairs `[a, b]` declaring `a` and `b` synonymous.
- `text`: a nonempty sentence whose words are separated by single spaces.
- Let $W$ be the number of words in `text`, $V$ the number of distinct words in `synonyms`, and $K$ the number of generated sentences.

**Return value**

- Return all $K$ sentences reachable through transitive synonym substitutions, sorted lexicographically.

### Examples

**Example 1**

- Input: `synonyms = [["happy","joy"],["sad","sorrow"],["joy","cheerful"]]`, `text = "I am happy today but was sad yesterday"`
- Output: the six combinations using `cheerful`, `happy`, or `joy` and `sad` or `sorrow`, in lexicographic order.

**Example 2**

- Input: `synonyms = [["a","b"],["b","c"]]`, `text = "a is c"`
- Output: all nine ordered combinations from the transitive group `{a, b, c}` at both replaceable positions.

**Example 3**

- Input: `synonyms = []`, `text = "no replacements"`
- Output: `["no replacements"]`
