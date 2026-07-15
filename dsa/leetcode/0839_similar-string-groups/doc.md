# Similar String Groups

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 839 |
| Difficulty | Hard |
| Topics | Array, Hash Table, String, Depth-First Search, Breadth-First Search, Union-Find |
| Official Link | [LeetCode](https://leetcode.com/problems/similar-string-groups/) |

## Problem Description
### Goal
Two strings `X` and `Y` are similar when they are identical or when swapping letters at at most two distinct positions within `X` makes the strings equal. For example, `"tars"` is similar to `"rats"`, and `"rats"` is similar to `"arts"`, while `"star"` is not directly similar to any of those three.

Similarity links strings into connected groups. Thus `"tars"` and `"arts"` belong to the same group through `"rats"` even though they are not directly similar. Given `strs`, where every string has the same length and all strings are anagrams of one another, return the number of connected similarity groups.

### Function Contract
**Inputs**

- `strs`: a list of $g$ lowercase strings, with $1 \leq g \leq 300$.
- Every string has the same length $\ell$, where $1 \leq \ell \leq 300$.
- All strings in the list are anagrams of one another.

**Return value**

Return the number of connected components formed by direct-similarity links among the strings.

### Examples
**Example 1**

- Input: `strs = ["tars", "rats", "arts", "star"]`
- Output: `2`

The first three strings form one connected group, while `"star"` forms another.

**Example 2**

- Input: `strs = ["omv", "ovm"]`
- Output: `1`

**Example 3**

- Input: `strs = ["abcd", "badc"]`
- Output: `2`

The strings differ at four positions, so one swap cannot connect them.

### Required Complexity
- **Time:** $O(g^2\ell)$
- **Space:** $O(g)$

<details>
<summary>Approach</summary>

#### General

**Reduce one-swap similarity to mismatch counting**

Compare each unordered pair of strings character by character. Stop once more than two differing positions have been found. Identical strings have zero mismatches and are similar. Because the contract guarantees the strings are anagrams, exactly two mismatches must contain the same two letters in opposite order, so swapping those positions makes the strings equal. A pair with more than two mismatches is not directly similar.

**Merge links rather than materializing paths**

Create one disjoint-set component per list position. Whenever a pair is similar, union their representatives. Path compression and union by size keep later operations nearly constant. Direct similarity need not be transitive, but union-find deliberately computes its transitive closure: every chain of pairwise links receives one representative.

After all pairs have been considered, two indices have the same representative exactly when a similarity path connects their strings. Counting distinct representatives therefore gives precisely the number of required groups.

#### Complexity detail

There are $g(g-1)/2$ unordered pairs, and a similarity check examines at most $\ell$ characters. Disjoint-set operations contribute only an inverse-Ackermann factor, so the stated bound is $O(g^2\ell)$ time. Parent and component-size arrays use $O(g)$ space.

#### Alternatives and edge cases

- **Build an explicit graph and traverse it:** Pairwise checks followed by DFS or BFS have the same $O(g^2\ell)$ time but can require $O(g^2)$ space for all similarity edges.
- **Generate every one-swap neighbor:** Hashing list strings and trying position pairs can be attractive when $\ell$ is much smaller than $g$, but constructing and looking up all swapped candidates requires careful handling of duplicates and string-copy cost.
- **Repeated transitive-closure scans:** Rechecking reachability through every intermediate string is correct but can add a cubic factor in $g$.
- **Identical strings:** Zero mismatches qualifies as similar, so duplicate entries must be merged.
- **Two mismatches:** The anagram guarantee is what ensures the two differing characters cross-match after a swap.
- **Indirect membership:** Two strings with more than two mismatches may still share a group through intermediate strings.
- **Single string:** One isolated entry forms exactly one group.

</details>
