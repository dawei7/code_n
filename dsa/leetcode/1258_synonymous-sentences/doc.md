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

### Required Complexity

- **Time:** $O(P\alpha(V)+KW)$
- **Space:** $O(V+KW)$

<details>
<summary>Approach</summary>

#### General

Synonym pairs define an undirected graph, and interchangeable words are exactly its connected components. Build those components with union-find: create a parent entry for every word and union the endpoints of each pair. Here, $\alpha$ denotes the inverse Ackermann function from amortized union-find analysis.

**Build sorted choices for each component**

After all unions, group every synonym word by its representative and sort each component's words. For a text word present in the structure, its available replacements are that sorted component; for any other word, its only choice is itself.

**Generate sentences directly in lexical order**

Process text positions from left to right and enumerate each position's choices in ascending order. Depth-first Cartesian-product traversal then emits complete token sequences lexicographically: every sentence under an earlier word choice precedes all sentences under a later choice at the first differing position. Join each completed sequence with single spaces.

Union-find supplies transitive equivalence, and the Cartesian product makes one independent choice at every position, so every valid sentence is produced. Each token sequence is unique because component word lists contain distinct words.

#### Complexity detail

The $P$ unions take $O(P\alpha(V))$ amortized time. Producing $K$ sentences of $W$ words requires $O(KW)$ output work, which dominates component sorting under the small vocabulary limits. Including the returned strings and traversal state, space is $O(V+KW)$.

#### Alternatives and edge cases

- **Graph search for each text word:** Repeated BFS or DFS finds the same components but revisits synonym edges for repeated words.
- **Generate then globally sort:** It is correct but adds $O(K\log K)$ sentence comparisons after output generation.
- **Only direct pairs:** Ignoring transitivity misses valid replacements connected through intermediate synonyms.
- **No synonym pairs:** The only result is the unchanged input sentence.
- **Repeated text word:** Each occurrence is replaced independently, so one component may contribute choices at several positions.
- **Words outside the graph:** Preserve them exactly as written with one available choice.

</details>
