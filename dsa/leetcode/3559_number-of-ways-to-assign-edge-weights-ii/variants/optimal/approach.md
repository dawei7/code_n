## General

Root the tree at node `1`. One iterative traversal records every node's depth and immediate parent. Build a binary-lifting table in which `ancestor[k][v]` is the $2^k$-th ancestor of `v`. Each row follows from the preceding row by taking two jumps of half the length.

For query nodes `u` and `v`, first lift the deeper node until both depths match. If the nodes differ, examine ancestor powers from largest to smallest and lift both whenever their proposed ancestors differ. Their immediate parent is then the lowest common ancestor (LCA). If its depth is $h$, the path length is

$$
d=\text{depth}(u)+\text{depth}(v)-2h.
$$

When $d=0$, the path is empty and no assignment has odd cost. Otherwise, the path has $2^d$ assignments. Toggling any fixed path edge between weights `1` and `2` bijectively pairs an even-cost assignment with an odd-cost assignment, so exactly half are valid: $2^{d-1}$. Modular exponentiation produces the required count.

## Complexity detail

Let $n$ be the number of nodes and $q=\lvert\texttt{queries}\rvert$. Building the tree and recording depths costs $O(n)$. The ancestor table costs $O(n\log n)$ time and space. Each LCA and modular power computation costs $O(\log n)$, so all queries cost $O(q\log n)$. Total time is $O((n+q)\log n)$ and space is $O(n\log n)$, excluding the output.

## Alternatives and edge cases

- **Traverse the path for every query:** A BFS or parent walk per query is correct but can take $O(nq)$ time on a long path with many endpoint queries.
- **Enumerate assignments:** Trying $2^d$ weight combinations is unnecessary because the parity-toggle bijection gives the count directly.
- **Linear parent climb:** Lifting one parent at a time uses less preprocessing but may cost $O(n)$ per query on a deep tree.
- **Same-node query:** Its path contains no edges; the sole empty assignment has cost zero, so the answer is zero rather than a negative power of two.
- **Ancestor and descendant:** After depth alignment the nodes may already coincide, in which case that node is the LCA.
- **LCA at the root:** The distance formula works unchanged when the path crosses between different root branches.
- **Unordered edges:** Rooting is established by traversal, not by the order or orientation of the input pairs.
- **Modulo:** Use modular exponentiation for every nonempty path to avoid constructing exponentially large integers.
