## General

**Store the answer for each prefix while building a trie**

After each typed character, the system needs the three lexicographically smallest products sharing the current prefix. A trie naturally represents all prefixes: following one child per character reaches the node for that prefix. The exact solution improves on a trie that would search an entire subtree at query time. Each node stores, in `v`, the indices of the first three suitable products. Querying a prefix can therefore retrieve its suggestions immediately.

This works only because products are inserted in lexicographic order. The public method begins with `products.sort()`. It then enumerates that sorted list, passing both product `w` and its sorted index `i` to `trie.insert`.

Each trie node has `children`, a fixed list of twenty-six child references corresponding to lowercase letters, and `v`, initially empty. Character `c` maps to index `ord(c) - ord('a')`. A missing child is created before traversal continues into it.

**Why retaining the first three inserted indices is sufficient**

While inserting a product, the algorithm visits the node for every nonempty prefix of that product. At each node it runs `if len(node.v) < 3: node.v.append(i)`. Because insertion follows the globally sorted product order, the first index appended at a prefix belongs to its lexicographically smallest matching product, the second to the next smallest, and the third to the third smallest.

Later matching products are lexicographically no smaller and cannot belong in an at-most-three suggestion list. The node deliberately ignores their indices. This prevents suggestion storage from growing with the number of products sharing a popular prefix.

For sorted products `mobile, moneypot, monitor, mouse, mousepad`, the node for prefix `m` records the first three indices, corresponding to `mobile`, `moneypot`, and `monitor`. The node for `mou` is visited only by `mouse` and `mousepad`, so it records those two.

The root stores no suggestions because the result is requested only after at least one character is typed. Insertion appends after descending to a character node, exactly matching those nonempty prefixes.

**Searching every typed prefix in one walk**

Method `search(w)` preallocates `ans` as one empty list per character of the search word. It then walks the trie once from the root. At character position `i`, if the required child exists, the search descends and assigns `ans[i] = node.v`. That stored list already represents the three smallest products matching `w[:i + 1]`.

If a required child is missing, the loop breaks. The current prefix matches no product, and extending a prefix can never create a match that did not exist for its shorter prefix. Because `ans` began with empty lists, the current position and all later positions correctly remain empty.

The walk does not restart at the root for every prefix. The node reached for the previous prefix is exactly the starting point needed for the next character, so all search prefixes together take time proportional to the search-word length.

**Turning stored indices back into product names**

The trie stores integer indices rather than duplicate strings. The final nested comprehension maps each index `i` in each stored vector `v` to `products[i]`. Since `products` is still in the same sorted order used during insertion, every index retrieves the intended name.

At most three indices occur in any `v`, so output conversion performs at most three lookups per typed character. The answer has exactly one inner list for each prefix, including empty lists after a failed prefix.

**Why the result is correct**

For any prefix represented by a trie node, exactly the products containing that prefix visit the node during insertion. They visit in lexicographic order because the full product list was sorted first. The node records precisely the first three visits, or all visits if fewer than three occur. It therefore stores exactly the required suggestion set in the required order.

During search, following the search word's characters reaches the unique node for each existing typed prefix, so the algorithm returns that node's correct list. A missing edge proves that no inserted product has the current prefix; all extensions are also impossible. Thus every output list is correct.

The input product strings are unique, so the stored indices cannot introduce duplicate suggestions. Sorting mutates the input `products` list, an observable detail that is acceptable for the challenge but worth knowing in a broader API.

## Complexity detail

Let $P$ be the number of products, $S$ the sum of all product lengths, $m$ the length of `searchWord`, and $L$ the maximum product length. Trie insertion visits $S$ characters and takes $O(S)$ time. Searching visits at most $m$ characters, and mapping at most three indices per prefix takes $O(m)$ time.

The exact source also calls Python's comparison sort. String comparisons may inspect up to $O(L)$ characters, so a simple worst-case bound for sorting is $O(PL\log P)$. More precisely, let $C_{\text{sort}}$ be the total characters examined across all sort comparisons; total exact time is $O(C_{\text{sort}}+S+m)$. The manifest's $O(S+m)$ bound omits this explicit sorting cost and would describe a situation where lexicographic insertion order were already available.

There are at most $S+1$ trie nodes. Each allocates twenty-six child slots and stores at most three indices, so the trie uses $O(S)$ space because the alphabet size is constant. Search creates $m$ inner result lists and returns at most $3m$ product references, using $O(m)$ output space. Overall space is $O(S+m)$ including output, plus Python's sorting workspace, which is at most linear in $P$ and is absorbed by $O(S)$ because every product is nonempty.

## Alternatives and edge cases

- **Sorted array plus binary search:** For each growing prefix, find its lower bound in sorted products and inspect the next three strings. This avoids trie memory but costs repeated logarithmic searches after the same sorting step.
- **Trie plus subtree DFS:** Mark terminal words and traverse children in alphabetical order for every prefix. It avoids storing suggestions at every node but may revisit large subtrees repeatedly unless traversal stops very carefully after three results.
- **Insert without sorting:** Then the first three indices reflect input order, not lexicographic order, and suggestions can be wrong.
- **Store every matching index:** It remains correct but can consume much more space for common prefixes; only the first three sorted visits are useful.
- **Prefix stops matching:** The first missing edge and every later prefix produce empty lists because extending a nonexistent prefix cannot restore a match.
- **One product:** Every prefix along that product returns the singleton product; a differing character makes the current and later results empty.
- **Search word longer than matching products:** Once the trie has no next child, remaining outputs stay empty.
- **Product equal to a typed prefix:** It remains a valid matching product because a string has itself as a prefix.
- **Shared long prefix:** Each node independently stores the same first few indices, trading linear trie memory for constant-time suggestions.
- **Input mutation:** `products.sort()` changes the caller's list order. Copy before sorting if an external API must preserve its input.
- **Lowercase alphabet guarantee:** The fixed child array and character arithmetic rely on every character being from `a` through `z`.
