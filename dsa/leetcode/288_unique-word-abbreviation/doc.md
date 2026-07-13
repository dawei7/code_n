# Unique Word Abbreviation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 288 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/unique-word-abbreviation/) |

## Problem Description
### Goal
Construct a `ValidWordAbbr` index from a dictionary of words. A standard abbreviation keeps short words unchanged; for longer words it combines the first character, the count of omitted middle characters, and the last character. Different words can therefore share one abbreviation.

For `isUnique(word)`, return `True` when no distinct dictionary word has the same abbreviation as the query. It is also unique when all dictionary entries with that abbreviation are exactly the query word itself, including repeated copies. Return `False` when any different word collides. Process multiple queries against the same indexed dictionary without changing its contents.

### Function Contract
**Inputs**

- `dictionary`: words used to construct the abbreviation index
- `words`: offline app queries passed to `isUnique`

**Return value**

One boolean per query. Native `ValidWordAbbr(dictionary).isUnique(word)` is true when no distinct dictionary word shares the query abbreviation.

### Examples
**Example 1**

- Input: `dictionary = ["deer","door","cake","card"], words = ["dear","cart","cane","make"]`
- Output: `[false,true,false,true]`

**Example 2**

- Input: `dictionary = ["hello"], words = ["hello"]`
- Output: `[true]`

**Example 3**

- Input: `dictionary = ["a","a"], words = ["a","b"]`
- Output: `[true,true]`

### Required Complexity

- **Time:** $O(c + q)$
- **Space:** $O(c)$

<details>
<summary>Approach</summary>

#### General

**Canonicalize the abbreviation once**

Words of length two or less abbreviate to themselves. Longer words use first character, number of omitted middle characters, and last character.

**Record identity, not occurrence count**

For each abbreviation, store its sole distinct word while all insertions agree. If a different word shares it, mark the abbreviation ambiguous.

Each map value is either the only distinct dictionary word with that abbreviation or an ambiguity marker representing at least two distinct words.

**Absence or matching identity is exactly uniqueness**

If an abbreviation is absent, no dictionary word conflicts with the query. If it maps to the query word itself, repeated occurrences still represent only that identity and also cause no conflict. A stored different word or ambiguity marker proves that some distinct dictionary word shares the abbreviation. These cases exhaust the definition of uniqueness.

#### Complexity detail

Building scans total dictionary characters `c`; each query abbreviation and hash lookup is constant relative to its word length, for total query characters `q`. The map stores at most one entry per distinct abbreviation.

#### Alternatives and edge cases

- **Scan the dictionary for every query:** takes $O(cq)$ in aggregate.
- Empty dictionaries accept every query; short words remain uncompressed; duplicate dictionary entries count as one identity.

</details>
