# Sentence Similarity

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 734 |
| Difficulty | Easy |
| Topics | Array, Hash Table, String |
| Official Link | [LeetCode](https://leetcode.com/problems/sentence-similarity/) |

## Problem Description
### Goal
Given two sentences represented as arrays of words and a list of unordered similar-word pairs, determine whether the sentences are similar. Similar sentences must contain the same number of words and are compared at matching positions.

At every position, the two words must either be identical or appear together in one explicitly listed pair. Direct similarity is symmetric but not transitive for this problem: two separate listed links do not imply a third relationship through an intermediate word. Return `True` only when every aligned position satisfies the rule.

### Function Contract
**Inputs**

- `sentence1`: the first ordered list of words
- `sentence2`: the second ordered list of words
- `similarPairs`: unordered word pairs that are declared directly similar

**Return value**

- `True` exactly when the sentences have the same number of words and all aligned positions satisfy the direct similarity rule

### Examples
**Example 1**

- Input: `sentence1 = ["great","acting","skills"], sentence2 = ["fine","drama","talent"], similarPairs = [["great","fine"],["drama","acting"],["skills","talent"]]`
- Output: `true`

**Example 2**

- Input: `sentence1 = ["great"], sentence2 = ["great"], similarPairs = []`
- Output: `true`

**Example 3**

- Input: `sentence1 = ["great"], sentence2 = ["fine"], similarPairs = [["great","good"],["good","fine"]]`
- Output: `false`

### Required Complexity

- **Time:** $O(n+p)$
- **Space:** $O(p)$

<details>
<summary>Approach</summary>

#### General

**Reject incompatible sentence lengths first**

Similarity compares words at the same positions; no insertion, deletion, or shifting is allowed. Therefore sentences with different lengths are immediately dissimilar regardless of the supplied pairs.

**Index direct relationships symmetrically**

Insert each listed pair `(left, right)` into a hash set in both orientations. The input relationship is symmetric, so either word may appear in either sentence. This preprocessing turns every later direct-pair test into expected constant time.

**Check aligned words without taking a transitive closure**

For every aligned `(first, second)`, accept the position if the strings are equal or if `(first, second)` is in the set. Otherwise return `False`; if every position passes, return `True`. A chain such as `great ~ good` and `good ~ fine` does not imply `great ~ fine`, because this problem defines only explicit pair similarity.

**Why the decision matches the definition**

Equal lengths establish a one-to-one alignment. The loop accepts a position using exactly one of the two permitted conditions: reflexive equality or a listed symmetric pair. Encountering neither condition proves the sentences dissimilar at that position. If no such counterexample exists, every alignment satisfies the definition, so the sentences are similar.

#### Complexity detail

Let `n` be the sentence length and `p` the number of listed pairs. Building the set takes $O(p)$ expected time and space, and checking the alignment takes $O(n)$ expected time. Total time is $O(n+p)$ and auxiliary space is $O(p)$.

#### Alternatives and edge cases

- **Scan the pair list per position:** this uses no hash index beyond the input but can take $O(np)$ time.
- **Adjacency map of sets:** mapping each word to all directly similar words gives the same expected bounds and avoids storing two-tuple keys.
- **Union-find or graph search:** connecting transitive chains solves Sentence Similarity II, but produces incorrect `True` answers for this direct-only relation.
- **Different lengths:** return `False` before examining word pairs.
- **Identical aligned words:** they are always similar even when absent from `similarPairs`.
- **Reversed pair orientation:** `["a","b"]` also permits an aligned pair `("b","a")`.
- **Duplicate listed pairs:** hash-set insertion naturally ignores repetitions.
- **Unused relationships:** pairs involving no aligned words do not affect the result.

</details>
