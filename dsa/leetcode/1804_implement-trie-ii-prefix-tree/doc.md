# Implement Trie II (Prefix Tree)

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/implement-trie-ii-prefix-tree/) |
| Frontend ID | 1804 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Design, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Design a trie that stores a multiset of lowercase words. Inserting the same word repeatedly creates multiple occurrences rather than leaving a single membership flag. The structure must report both exact-word multiplicity and the number of stored words sharing a requested prefix.

It must also erase one occurrence of a supplied word. Every erase call is guaranteed to name a word currently present, possibly with other occurrences remaining. Erasing one word must update all of its prefix counts without changing unrelated words.

### Function Contract

**Inputs**

- `Trie()` creates an empty word multiset.
- `insert(word)` adds one occurrence of a nonempty lowercase word.
- `countWordsEqualTo(word)` returns the number of stored occurrences exactly equal to `word`.
- `countWordsStartingWith(prefix)` returns the number of stored occurrences whose words begin with `prefix`.
- `erase(word)` removes one occurrence; that occurrence is guaranteed to exist.
- At most $Q=3\cdot10^4$ method calls are made, and each word or prefix has length $L$ between 1 and 2000.
- Let $S$ be the number of character nodes created for all distinct stored prefixes.

**Return value**

- Construction, insertion, and erasure return no value.
- Each count method returns a nonnegative integer.
- In the app-local sequence interface, return one result per operation and use `null` for methods with no return value.

### Examples

**Example 1**

- Operations: `["Trie","insert","insert","countWordsEqualTo","countWordsStartingWith","erase","countWordsEqualTo"]`
- Arguments: `[[],["apple"],["apple"],["apple"],["app"],["apple"],["apple"]]`
- Output: `[null,null,null,2,2,null,1]`

Two equal insertions contribute two exact and prefix occurrences; one erase removes only one.

**Example 2**

- Operations: insert `"app"` and `"apple"`, erase `"app"`, then query exact `"app"` and prefix `"app"`
- Output: `0` and `1`

Removing the shorter word does not remove the longer word that passes through the same nodes.

**Example 3**

- Operations: insert `"apple"` and `"apply"`, then count prefix `"appl"` and exact word `"app"`
- Output: `2` and `0`

A path may be a shared prefix without representing a complete stored word.

### Required Complexity

- **Time:** $O(L)$
- **Space:** $O(S)$

<details>
<summary>Approach</summary>

#### General

**Store two different counts at every node**

Each node keeps a terminal count for words ending there and a prefix count for word occurrences passing through it. These quantities answer different questions: the node for `"app"` may have terminal count zero while still having a positive prefix count because `"apple"` is stored.

**Update the whole path for insert and erase**

Insertion follows or creates one child per character and increments each reached node's prefix count, then increments the final terminal count. Erasure follows the guaranteed-existing path, decrements every reached prefix count, and decrements the final terminal count exactly once.

**Read the count at the completed path**

An exact query traverses the requested word and returns its final terminal count. A prefix query traverses the prefix and returns its final prefix count. If a required child is absent, the answer is zero.

After every update, a node's prefix count equals the number of current word occurrences containing that path, while its terminal count equals occurrences ending there. This invariant is initially true and each insert or erase changes exactly the affected path by one, proving all query results are correct.

#### Complexity detail

Every method traverses at most the $L$ characters in its argument, so it takes $O(L)$ time. The trie creates at most one node per distinct stored prefix and therefore uses $O(S)$ space. Nodes whose count becomes zero may be retained without changing this bound over the operation history.

#### Alternatives and edge cases

- **Hash map of complete words:** Exact counts are constant-time, but a prefix query must scan every distinct word and can become quadratic over a long operation sequence.
- **Boolean terminal markers:** They cannot represent repeated insertions or erase exactly one occurrence.
- **Duplicate insertion:** Increment all path counts and the terminal count for every occurrence.
- **Erase one duplicate:** Decrement counts by one, leaving other occurrences present.
- **Word that is another word's prefix:** Terminal and prefix counts must remain independent at the shared node.
- **Missing query path:** Return zero without creating nodes.
- **Zero-count retained nodes:** Queries remain correct because their stored counts are zero; physical pruning is optional.

</details>
