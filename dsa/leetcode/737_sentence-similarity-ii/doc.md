# Sentence Similarity II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 737 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Depth-First Search, Breadth-First Search, Union-Find |
| Official Link | [LeetCode](https://leetcode.com/problems/sentence-similarity-ii/) |

## Problem Description
### Goal
Given two sentences as arrays of words and a list of similar-word pairs, determine whether the sentences are similar. They must have the same number of words and are compared at matching positions.

Similarity is reflexive, symmetric, and transitive: a word is similar to itself, pair direction does not matter, and a chain of listed relationships places all connected words in one similarity group. Return `True` only when every aligned word pair is identical or connected through such a group; otherwise return `False`.

### Function Contract
**Inputs**

- `sentence1`: the first ordered list of words
- `sentence2`: the second ordered list of words
- `similarPairs`: word pairs that connect words into similarity groups

**Return value**

- `True` exactly when the sentences have equal length and each aligned pair contains identical words or words connected through one similarity group

### Examples
**Example 1**

- Input: `sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]`
- Output: `true`

**Example 2**

- Input: `sentence1 = ["I","love","leetcode"], sentence2 = ["I","love","onepiece"], similarPairs = [["manga","onepiece"],["platform","anime"],["leetcode","platform"],["anime","manga"]]`
- Output: `true`

**Example 3**

- Input: `sentence1 = ["great"], sentence2 = ["fine"], similarPairs = [["great","good"],["fine","excellent"]]`
- Output: `false`

### Required Complexity

- **Time:** $O((n+p) \alpha(w))$
- **Space:** $O(w)$

<details>
<summary>Approach</summary>

#### General

**Interpret similarity pairs as graph connectivity**

Treat every word as a vertex and every listed pair as an undirected edge. Symmetry permits traversing an edge either way, and transitivity means two different words are similar exactly when they lie in the same connected component. Identical words remain similar even if they do not appear in the graph.

**Build components with disjoint-set union**

Create a parent and size entry for each word encountered in a pair. For every pair, find both representatives and merge smaller components under larger ones. `find` compresses parent paths so future operations approach constant amortized time.

**Compare only aligned component representatives**

Reject unequal sentence lengths. At each aligned position, identical strings pass immediately. For different strings, both must occur in the disjoint-set structure and their representatives must match; otherwise return `False`. If every position passes, return `True`.

**Why component equality is sufficient and necessary**

Every union joins exactly the endpoints of a declared similarity edge, so all words given one representative are connected by a chain of declared pairs and are similar by transitivity. Conversely, processing every edge causes all vertices on any such chain to be merged, so similar words obtain the same representative. The aligned checks therefore accept exactly the word pairs allowed by the relationship.

#### Complexity detail

Let `n` be the sentence length, `p` the number of pairs, and `w` the number of distinct paired words. Union by size with path compression makes all unions and finds take $O((n+p) \alpha(w))$ time, where `α` is the inverse Ackermann function. The parent and size maps use $O(w)$ space.

#### Alternatives and edge cases

- **One component traversal up front:** build adjacency sets and label every connected component once; this also takes linear graph time and supports constant-time aligned checks.
- **Search per aligned pair:** breadth-first or depth-first search answers connectivity directly but can revisit the same graph for many positions and take $O(n(w+p))$ time.
- **Direct-pair hash set:** checking only listed pairs ignores transitive chains and solves Sentence Similarity I instead.
- **Different lengths:** return `False` before building or querying alignments.
- **Identical words:** equality is reflexively similar even when the word never appears in `similarPairs`.
- **Disconnected paired words:** appearing somewhere in the graph is insufficient; representatives must match.
- **Duplicate and reversed pairs:** repeated unions do not change the resulting components.
- **Unpaired different words:** two distinct absent words are not similar.

</details>
