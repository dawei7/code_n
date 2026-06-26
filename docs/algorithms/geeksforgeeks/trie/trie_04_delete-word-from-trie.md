# Delete Word from Trie

| | |
|---|---|
| **ID** | `trie_04` |
| **Category** | trie |
| **Complexity (required)** | $O(M)$ Time, $O(M)$ Space |
| **Difficulty** | 7/10 |
| **Interview relevance** | 5/10 |
| **GeeksForGeeks Equivalent** | [Trie | (Delete)](https://www.geeksforgeeks.org/trie-delete/) |

## Problem statement

Given a standard Trie data structure and a string `word` that currently exists inside it, completely remove the string from the Trie.
You must ensure that removing this word does NOT accidentally destroy the prefixes of other valid words that share the same path!
If nodes become completely empty (no children and not the end of another word), they must be structurally deleted from memory to prevent memory leaks.

**Input:** A Trie `root` node, and a string `word`.
**Output:** The modified Trie structure with the word removed.

## When to use it

- To maintain highly dynamic prefix dictionaries where data frequently expires (like auto-complete caches).
- A rigorous test of Bottom-Up Post-Order DFS combined with careful pointer logic.

## Approach

**1. The Three Deletion Scenarios:**
When we want to delete `"apple"`, we traverse down to `'e'`. We uncheck its `is_end_of_word = False`. The word is now officially deleted from the dictionary!
But what about the nodes themselves?
1. **The node has other children:** If we delete `"apple"`, but `"apples"` exists, we CANNOT physically delete the `'e'` node! It is a critical bridge for `"apples"`! We stop.
2. **The node is the end of another word:** If we delete `"apples"`, we trace back to `'e'`. The `'e'` has no other children. Can we delete it? NO! Because `"apple"` is a valid word ending at `'e'`! We stop.
3. **The node is useless (Empty and Not a Word):** If we delete `"apple"`, and `"apples"` doesn't exist. `'e'` has no children, and it's no longer the end of a word. We physically `del` it from its parent's map! We move up to `'l'`. Does `'l'` have other children? No. Is it a word? No. We `del` it!

**2. The Bottom-Up DFS Deletion:**
Because we need to delete nodes from the BOTTOM of the Trie upwards (we can only delete `'l'` after we have successfully deleted `'e'`), we MUST use a recursive Post-Order DFS!
We recursively travel down the string until we hit the last character.
Then, as the recursion unwinds and travels UP, we apply our three checks:
If `len(node.children) == 0` AND `node.is_end_of_word == False`, we return `True` (signaling to the parent: "Hey, I am completely useless, delete me!").
The parent receives this signal and explicitly deletes that child from its Hash Map.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for trie_04: Delete Word from Trie.

Decrement per-node counts along the path. The word is
still present iff some other word shares the same path.
"""


def solve(words, n, target):
    children = []
    is_end = []
    count = []

    def new_node():
        children.append({})
        is_end.append(False)
        count.append(0)
        return len(children) - 1

    root = new_node()
    for w in words:
        cur = root
        count[cur] += 1
        for ch in w:
            nxt = children[cur].get(ch)
            if nxt is None:
                nxt = new_node()
                children[cur][ch] = nxt
            cur = nxt
            count[cur] += 1
        is_end[cur] = True
    cur = root
    count[cur] -= 1
    for ch in target:
        if ch not in children[cur]:
            return target in words
        cur = children[cur][ch]
        count[cur] -= 1
    cur = root
    for ch in target:
        if ch not in children[cur]:
            return False
        cur = children[cur][ch]
    return is_end[cur] and count[cur] > 0
```

</details>

## Walk-through

Trie currently contains: `"apple"`, `"ape"`.
Delete `"ape"`.

1. `dfs(root, depth=0)`. Follows `'a'`.
2. `dfs('a', depth=1)`. Follows `'p'`.
3. `dfs('p', depth=2)`. Follows `'e'`.
4. `dfs('e', depth=3)`.
   - `depth == len("ape")` (3).
   - `node.is_end_of_word = False`.
   - Does `'e'` have children? No. Returns `True`.
5. Back to `dfs('p', depth=2)`:
   - `should_delete_child` is `True`!
   - `del node.children['e']`.
   - Are we useless? `len(children) == 1` (it still has `'p'` for "apple").
   - Returns `False`.
6. Back to `dfs('a', depth=1)`:
   - `should_delete_child` is `False`.
   - Does nothing. Returns `False`.
7. Back to `root`:
   - `should_delete_child` is `False`. Does nothing.

Result: `"ape"` is gone. The `'e'` node was deleted from memory to save space. `"apple"` remains perfectly intact because `'p'` blocked the cascading deletion! ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(M)$ | $O(M)$ |
| **Average** | $O(M)$ | $O(M)$ |
| **Worst** | $O(M)$ | $O(M)$ |

The DFS traverses down exactly M nodes (the length of the word) and unwinds exactly M steps back up.
Hash map lookups and deletions `del dict[key]` take $O(1)$ constant time.
Total time complexity is mathematically strictly $O(M)$.
Space complexity is $O(M)$ to hold the recursive call stack of depth M.

## Variants & optimizations

- **Prefix Count Deletion ($O(M)$ Iterative):** If you are using the Augmented Trie (`trie_02`) that tracks `prefix_count`, deletion becomes massively easier and Iterative! You just iteratively travel down the word. At every node, you decrement `curr.prefix_count -= 1`. If `curr.prefix_count == 0`, you literally just `del` the child pointer and `return` instantly! Python's Garbage Collector will automatically reap the entire disconnected subtree! No recursion needed!

## Real-world applications

- **Network Routing Security:** Updating massive hardware Access Control List (ACL) IP subnets, dynamically dropping blacklisted IP blocks from the routing tables by deleting their shared prefixes in the hardware Trie.

## Related algorithms in cOde(n)

- **[trie_01 - Trie Insert/Search](trie_01_trie-insert-and-search.md)** — The fundamental architecture.
- **[tree_15 - BST Delete](../trees/tree_15_bst-delete.md)** — Compare this to standard Binary Search Tree deletion. Trie deletion is vastly more elegant because you never have to restructure or "rotate" nodes to fill gaps; you just truncate dead ends!

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
