## General
**View decimal prefixes as an implicit trie**

Every positive integer is a path of decimal digits. A lexicographical traversal visits a prefix before its extensions, so after a number such as `12`, the next candidate is `120` when it does not exceed `n`. No trie needs to be stored because multiplying by ten descends to the first child.

**Climb when no child remains**

If `current * 10` is too large, move to the next sibling by adding one. A sibling is invalid when it exceeds `n` or ends in zero, the latter meaning that adding one carried beyond the current prefix's final digit. Repeatedly divide by ten until a prefix with a valid next sibling is reached, then increment it.

**Why the successor rule matches lexical order**

Descending chooses the smallest string having the current representation as a prefix. When descent is impossible, incrementing the last digit chooses the nearest unvisited sibling. If that sibling does not exist, removing trailing digits climbs to the nearest ancestor with one. These are exactly the preorder-successor moves in the decimal trie, so recording `n` successive nodes visits every value once in lexical order.

## Complexity detail
The loop emits one of the `n` values per iteration. Although one iteration can climb several digits, each climb corresponds to leaving a trie level previously entered, so the total traversal work is $O(n)$. Apart from the required output list and a few integers, the algorithm uses $O(1)$ space.

## Alternatives and edge cases
- **Convert all numbers to strings and sort:** is simple but costs $O(n \log n)$ time and $O(n)$ additional storage.
- **Recursive depth-first traversal:** also visits the implicit digit trie in $O(n)$ time, but uses $O(\log n)$ call-stack space.
- **Explicit trie construction:** reproduces the ordering but wastes $O(n \log n)$ digit storage.
- For $n < 10$, numeric and lexicographical order coincide.
- Crossing powers of ten requires descending before later single-digit siblings.
- Values ending in `9` can require climbing through several exhausted ancestors.
- The inclusive bound `n` must appear exactly once even when it lies inside a prefix subtree.
