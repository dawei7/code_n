## General

A multiset of characters can be rearranged into a palindrome exactly when at most one character has odd frequency. Represent only frequency parity with a 26-bit integer.

For each node $v$, define `mask[v]` as the parity mask of edge labels on the path from the root to $v$. The root mask is zero. If $x$ is a child of $v$, then

$$
\texttt{mask[x]} = \texttt{mask[v]} \mathbin{\mathtt{xor}} 2^{\texttt{s[x]}-mathtt{'a'}}.
$$

Build child lists from `parent` and compute these masks with an iterative depth-first traversal, avoiding recursion-depth limits on a long chain.

**Why root-path masks answer arbitrary path queries**

The paths from the root to $u$ and $v$ share every edge above their lowest common ancestor. XORing `mask[u]` and `mask[v]` includes each shared edge twice, so its parity cancels. The result is exactly the parity mask of the unique path between $u$ and $v$.

That path can form a palindrome when the XOR is zero or has exactly one set bit. Process node masks in any traversal order while storing frequencies of masks already seen. For a new mask $m$, add the number of previous masks equal to $m$, then add the frequencies of all 26 masks $m \mathbin{\mathtt{xor}} 2^b$. Finally record $m$ itself.

Every accepted previous mask differs in zero or one character parity, so every counted pair is valid. Conversely, every valid pair has one of those 27 differences and is found when its later-processed endpoint is visited. Thus each unordered pair is counted exactly once.

## Complexity detail

There are 26 one-bit neighbors to inspect for each of the $n$ nodes. Because the alphabet size is fixed, the running time is $O(26n)=O(n)$. Child lists, the traversal stack, and the mask-frequency table each use at most $O(n)$ space.

## Alternatives and edge cases

- **Enumerate every node pair:** Compute both prefix masks and test all $\binom{n}{2}$ XORs. It is correct but takes $O(n^2)$ time.
- **Lowest-common-ancestor queries:** Recover path character counts for each pair with LCA preprocessing. Pair enumeration remains quadratic and stores much more information than parity requires.
- **Recursive DFS:** The mask recurrence is identical, but a chain of $10^5$ nodes can exceed the language's recursion limit.
- **Single node:** There is no pair of distinct nodes, so the answer is zero.
- **Root character:** `s[0]` labels no edge and must never be toggled into a mask.
- **Even path length:** A path may still be valid with zero odd counts; the condition is not restricted to odd-length paths.
- **Large answer:** If every pair is valid, the result is $n(n-1)/2$, which requires a 64-bit integer in fixed-width languages.
- **Parent index order:** Build child lists rather than assuming a parent necessarily has a smaller numeric index than its child.
