# Trie Insert and Search

| | |
|---|---|
| **ID** | `trie_01` |
| **Category** | trie |
| **Complexity (required)** | $O(M)$ Time, $O(M)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/) |

## Problem statement

A Trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings.
Implement the `Trie` class:
- `insert(word)`: Inserts the string `word` into the trie.
- `search(word)`: Returns `true` if the string `word` is in the trie (i.e., was inserted before), and `false` otherwise.
- `startsWith(prefix)`: Returns `true` if there is a previously inserted string `word` that has the prefix `prefix`, and `false` otherwise.

**Input:** Sequences of method calls with strings.
**Output:** Booleans for search operations.

## When to use it

- To perform blazing-fast dictionary lookups and prefix matching.
- It is significantly faster than a Hash Table when dealing with strings that share common prefixes, as it never computes hashes and saves massive amounts of memory.

## Approach

**1. The Node Structure:**
Unlike a Binary Tree which has a `left` and `right` pointer, a Trie node can have up to 26 children (one for each letter of the English alphabet).
Each node contains:
- `children`: A Hash Map or Array of size 26 mapping characters to child `TrieNode`s.
- `is_end_of_word`: A boolean flag. Just because a node exists doesn't mean it's a word! If we insert `"apple"`, the node for `'p'` exists, but `"app"` is not a word in our dictionary until we explicitly insert it!

**2. Insertion:**
Start at the root. For every character in the word:
- If the character doesn't exist in the current node's `children`, create a new `TrieNode` for it.
- Move the current pointer down to that child node.
When the word ends, mark the final node we landed on as `is_end_of_word = True`.

**3. Searching for a Word:**
Start at the root. For every character in the word:
- If the character doesn't exist in `children`, the word is not in the dictionary! Return `False`.
- Move the pointer down.
When the word ends, we check the node we landed on. Are we returning `True`? NO!
What if we inserted `"apple"`, and we search for `"app"`? We successfully traverse down the tree, but `"app"` is not a valid word!
We must return `curr.is_end_of_word`!

**4. Searching for a Prefix:**
Identical to searching for a word. However, when the prefix ends, we do NOT care if it's the end of a word! The fact that the path existed at all means the prefix is valid! Return `True`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for trie_01: Trie Insert and Search.

Build a trie from the words, then return True iff target is in it.
"""


def solve(words, n, target):
    children = []
    is_end = []

    def new_node():
        children.append({})
        is_end.append(False)
        return len(children) - 1

    root = new_node()
    for w in words:
        cur = root
        for ch in w:
            nxt = children[cur].get(ch)
            if nxt is None:
                nxt = new_node()
                children[cur][ch] = nxt
            cur = nxt
        is_end[cur] = True
    cur = root
    for ch in target:
        if ch not in children[cur]:
            return False
        cur = children[cur][ch]
    return is_end[cur]
```

</details>

## Walk-through

`insert("apple")`
- Root has no 'a'. Add `TrieNode` at 'a'. Move to 'a'.
- 'a' has no 'p'. Add `TrieNode` at 'p'. Move to 'p'.
...
- Flag 'e' node as `is_end_of_word = True`.

`search("apple")`
- Trace 'a' -> 'p' -> 'p' -> 'l' -> 'e'.
- Path exists. `curr.is_end_of_word` is True. Returns `True`. ✓

`search("app")`
- Trace 'a' -> 'p' -> 'p'.
- Path exists. `curr.is_end_of_word` is False. Returns `False`. ✓

`startsWith("app")`
- Trace 'a' -> 'p' -> 'p'.
- Path exists. Returns `True`. ✓

`insert("app")`
- Trace 'a' -> 'p' -> 'p' (nodes already exist, so we just traverse).
- Flag 'p' node as `is_end_of_word = True`.

`search("app")`
- Trace 'a' -> 'p' -> 'p'.
- Path exists. `curr.is_end_of_word` is True! Returns `True`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(M)$ | $O(1)$ |
| **Average** | $O(M)$ | $O(M)$ |
| **Worst** | $O(M)$ | $O(M)$ |

Where M is the length of the string being inserted or searched.
Every operation (insert, search, startsWith) requires traversing exactly M nodes. Looking up a character in the `children` Hash Map takes $O(1)$ constant time.
Total Time complexity is strictly $O(M)$. This is faster than Binary Search Trees $O(M log N)$, and comparable to Hash Tables but without hash collisions!
Space complexity for insertion is $O(M)$ if no part of the word shares a prefix with existing words (we must create M new nodes). For search operations, space is $O(1)$.

## Variants & optimizations

- **Array vs Hash Map (`children[26]`):** If you are only dealing with lowercase English letters, using an array `children = [None] * 26` is mathematically faster because calculating an array index `ord(char) - ord('a')` is faster than hashing a string key. However, it takes drastically more memory because every node reserves 26 empty slots even if it only has 1 child.

## Real-world applications

- **Search Engine Auto-Complete:** When you type "algo" into Google, it uses `startsWith("algo")` on a massive distributed Trie, finds the `"o"` node, and runs a BFS to return the 10 most popular subtrees (words) attached below it!
- **Spell Checkers:** Squiggly red underlines in Microsoft Word are calculated by tracing your typed word through an English dictionary Trie.

## Related algorithms in cOde(n)

- **[trie_02 - Word Count with Prefix](trie_02_word-count-with-prefix.md)** — A minor modification to augment the nodes with counter variables.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
