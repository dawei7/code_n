# Design Add and Search Words Data Structure

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 211 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | String, Depth-First Search, Design, Trie |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/design-add-and-search-words-data-structure/) |

## Problem Description
### Goal
Implement a stateful dictionary that receives lowercase words through `addWord(word)` and answers full-pattern queries through `search(pattern)`. Added words remain available for all later operations, and words with common prefixes or different lengths must coexist independently.

Within a search pattern, a lowercase letter must match that exact character, while each dot `.` matches any one character. Dots do not match zero or several characters, so a successful word must have exactly the same length as the pattern. Return whether at least one stored word matches the entire pattern; matching only a prefix is insufficient. Produce booleans for searches and no result for additions.

### Function Contract
**Inputs**

- `operations`: app commands `["addWord", word]` and `["search", pattern]`

**Return value**

Boolean results for searches in command order.

### Examples
**Example 1**

- Add `bad`, `dad`, `mad`; search `.ad`
- Output: `True`

**Example 2**

- Search `pad` after those additions
- Output: `False`

**Example 3**

- Search `b..` after adding `bad`
- Output: `True`

### Required Complexity

- **Time:** $O(B^L)$
- **Space:** $O(T)$

<details>
<summary>Approach</summary>

#### General

Store words in a trie exactly as in an ordinary prefix dictionary: each character is an edge, and a terminal marker distinguishes complete words from prefixes. Wildcard search changes only how a query traverses that structure.

Use depth-first search over `(trie_node, pattern_index)` states:

- For a literal character, follow only the matching child. If it is absent, that branch fails.
- For `.`, recurse into every child because the wildcard matches exactly one arbitrary character.
- When `pattern_index` reaches the pattern length, succeed only if the current node is terminal.

The final terminal test enforces full-word length. After adding `bad`, pattern `b.` does not match because it consumes only two trie edges, while `b..` can follow `b -> a -> d` and ends at a terminal node.

For `.ad` after adding `bad`, `dad`, and `mad`, the first wildcard branches to `b`, `d`, and `m`; the remaining literal edges `a` and `d` complete at terminal nodes. The search may stop as soon as any branch succeeds.

At search state `(node, i)`, the node is reachable by exactly the stored prefixes matching the first `i` pattern characters along that branch. A literal transition preserves only paths with the required character; a wildcard transition enumerates all and only possible single-character choices. By induction, reaching the pattern end enumerates exactly full-length matching trie paths. Requiring a terminal node makes those paths correspond exactly to stored words, so the returned boolean is correct.

#### Complexity detail

Adding a word of length `L` takes $O(L)$ time. A literal-only search also takes $O(L)$. In the worst case, wildcards explore branching factor `B` across `L` levels, $O(B^L)$ states, though the finite trie bounds work by its stored nodes. Trie storage is $O(T)$ for `T` inserted characters, and recursive search uses up to $O(L)$ call-stack depth.

#### Alternatives and edge cases

- Scanning every stored word repeats comparisons and ignores shared prefixes.
- Grouping words by length can reduce wildcard candidates, but a trie prunes failed prefixes earlier.
- Treating `.` as a literal child violates the search grammar.
- Searches before any insertion fail. Multiple dots can create broad branching.
- A pattern must match the whole word, not merely a prefix or substring.

</details>
