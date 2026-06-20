# Word Count with Prefix

| | |
|---|---|
| **ID** | `trie_02` |
| **Category** | trie |
| **Complexity (required)** | $O(M)$ Time, $O(M)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 7/10 |
| **GeeksForGeeks Equivalent** | [Find the count of words with a given prefix](https://www.geeksforgeeks.org/find-count-of-words-with-a-given-prefix/) |

## Problem statement

Given a list of strings (a dictionary) and a `prefix` string, find the total number of valid dictionary words that start with the given `prefix`.
You must be able to perform this query thousands of times efficiently.

**Input:** A dictionary of strings, and a target `prefix`.
**Output:** An integer representing the count of words matching the prefix.

## When to use it

- To optimize real-time auto-complete systems where you need to show the user how many results match their current typed query before they hit Enter.
- An elegant demonstration of how Tries can be augmented with mathematical states.

## Approach

**1. The Naive Approach ($O(N \times M)$):**
You could loop through all N words in the dictionary and use `.startswith(prefix)`. This takes $O(M)$ time per word.
If the dictionary has 100,000 words, this takes massive CPU cycles for a single query.

**2. The Inefficient Trie Search ($O(V)$):**
You could insert all words into a standard Trie. You traverse down the `prefix`. When you reach the end of the prefix, you run a massive Depth First Search (DFS) downwards through all remaining child branches, explicitly counting every node where `is_end_of_word == True`.
This is faster than the naive approach, but it still requires traversing hundreds of nodes if the prefix matches thousands of words!

**3. The Augmented Trie ($O(M)$):**
If we want to know how many words exist in the subtree below a specific node, why don't we just KEEP TRACK OF IT when we build the tree?!
We augment our `TrieNode` class with a new integer property: `prefix_count`.
When we insert a word like `"apple"`, as we traverse down the nodes `'a'`, `'p'`, `'p'`, `'l'`, `'e'`, we physically increment `prefix_count += 1` on EVERY SINGLE NODE we pass through!
When we later query `"app"`, we traverse down to `'p'`. We DO NOT do a DFS! We just return `curr.prefix_count`! It instantly tells us exactly how many words passed through this node during insertion!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for trie_02: Word Count with Prefix.

Count the words in the trie that start with prefix.
"""


def solve(words, n, prefix):
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
    for ch in prefix:
        if ch not in children[cur]:
            return 0
        cur = children[cur][ch]
    count = 0

    def dfs(i):
        nonlocal count
        if is_end[i]:
            count += 1
        for nxt in children[i].values():
            dfs(nxt)

    dfs(cur)
    return count
```

</details>

## Walk-through

Dictionary: `["apple", "apply", "ape", "bat"]`.

**Building the Trie:**
- `insert("apple")`: 
  `'a'` (count 1) -> `'p'` (count 1) -> `'p'` (count 1) -> `'l'` (count 1) -> `'e'` (count 1).
- `insert("apply")`: 
  `'a'` (count 2) -> `'p'` (count 2) -> `'p'` (count 2) -> `'l'` (count 2) -> `'y'` (count 1).
- `insert("ape")`: 
  `'a'` (count 3) -> `'p'` (count 3) -> `'e'` (count 1).
- `insert("bat")`: 
  `'b'` (count 1) -> `'a'` (count 1) -> `'t'` (count 1).

**Querying:**
`count_prefix("ap")`
- Go to `'a'`.
- Go to `'p'`.
- The node `'p'` has `prefix_count = 3`.
- Returns `3` instantly! ✓ (Matches "apple", "apply", "ape").

`count_prefix("appl")`
- Go to `'a'`, `'p'`, `'p'`, `'l'`.
- The node `'l'` has `prefix_count = 2`.
- Returns `2` instantly! ✓ (Matches "apple", "apply").

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(M)$ | $O(1)$ |
| **Average** | $O(M)$ | $O(M)$ |
| **Worst** | $O(M)$ | $O(M)$ |

Insertion takes $O(M)$ time where M is the length of the string.
Querying takes $O(P)$ time where P is the length of the prefix.
There is absolutely zero dependence on the size of the dictionary (N) during the query phase! An $O(M)$ query time is mathematically optimal and instantaneous.
Space complexity is $O(M)$ per inserted word to build the nodes, but queries take $O(1)$ space.

## Variants & optimizations

- **Word Deletion:** If you need to support removing words from the dictionary, you just trace the word and DECREMENT `prefix_count -= 1` on every node! (See `trie_04`).
- **Most Popular Auto-Complete:** Instead of storing an integer count, store a `max_score` and a `popular_string`! As you insert words, if their popularity score is higher than the node's `max_score`, overwrite the node with the new best string. When a user queries a prefix, you can return the #1 most popular auto-complete suggestion in exactly $O(1)$ time after tracing the prefix!

## Real-world applications

- **SQL `LIKE 'app%'` Analytics:** Optimizing backend query planners when finding the total frequency of text column records that start with a specific substring.

## Related algorithms in cOde(n)

- **[trie_01 - Trie Insert/Search](trie_01_trie-insert-and-search.md)** — The foundational data structure that enables this augmentation.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
