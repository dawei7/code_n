# Apply Substitutions

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3481 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Depth-First Search, Breadth-First Search, Graph Theory, Topological Sort |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/apply-substitutions/) |

## Problem Description

### Goal

The list `replacements` defines a mapping from one-letter keys to string values. A placeholder has the form `%X%`, where `X` is a mapped key. Replacement values may themselves contain placeholders, so resolving one key can depend on resolving other keys first.

Expand every placeholder recursively and return the fully substituted `text`. Every referenced key is present, replacement dependencies contain no cycle, and the returned string must contain no placeholders. A key's expansion has the same meaning wherever that key is referenced.

### Function Contract

**Inputs**

- `replacements`: A list of unique `[key, value]` entries. Each `key` is one uppercase English letter, and each non-empty `value` has length at most 8 and may contain valid placeholders.
- `text`: Every mapping key written once as a placeholder, in an arbitrary order, with adjacent placeholders separated by underscores.

There are between 1 and 10 replacement entries. Consequently, `text.length == 4 * replacements.length - 1`. Every placeholder refers to a supplied key, and the dependency graph is acyclic.

**Return value**

Return `text` after recursively replacing every placeholder with its fully expanded mapped value.

### Examples

#### Example 1

- **Input:** `replacements = [["A", "abc"], ["B", "def"]]`, `text = "%A%_%B%"`
- **Output:** `"abc_def"`

Both mapped values are literal, so their placeholders can be replaced directly.

#### Example 2

- **Input:** `replacements = [["A", "bce"], ["B", "ace"], ["C", "abc%B%"]]`, `text = "%A%_%B%_%C%"`
- **Output:** `"bce_ace_abcace"`

The value for `C` contains `%B%`; expanding that dependency changes `abc%B%` into `abcace` before it is inserted into the final text.
