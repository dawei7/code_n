## General

**Process original adjacency without losing links**

At an original node `current`, its original successor is `current.next`. Compute the greatest common divisor of their values, create a node containing that result, and splice it between them. The inserted node points to the saved successor, while `current.next` points to the inserted node.

After insertion, moving only one link would land on the new node and incorrectly treat it as an original endpoint. Advance two links to the saved successor instead. Thus each loop iteration processes exactly one edge from the original list, and the traversal stops when the current original node has no successor.

**Why every inserted value is correct**

Euclid's algorithm repeatedly replaces a pair $(a,b)$ by $(b, a \bmod b)$ until the second value is zero. This transformation preserves the set of common divisors, so the final nonzero value is $\gcd(a,b)$. Applying it to the two endpoints before changing their adjacency gives the required value for that original edge.

The splice preserves both original nodes and connects exactly one new node between them. Advancing past that node ensures no extra node is inserted around it. Consequently, all and only the $n-1$ original adjacent pairs receive one correct GCD node, and the original head remains the head of the result.

## Complexity detail

Let $n$ be the original node count and $V$ the largest node value. The traversal processes $n-1$ pairs. Euclid's algorithm takes $O(\log V)$ time per pair in the worst case, giving $O(n \log V)$ total time.

The modified list contains $n-1$ newly allocated nodes, so the returned structure uses $O(n)$ additional space. Apart from these required result nodes, the algorithm keeps only a pointer and temporary arithmetic values, using $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Build a separate output list:** This is straightforward but needlessly copies all original nodes instead of splicing only the required new ones.
- **Convert to an array first:** Computing adjacent GCDs in an array is correct, but serialization and reconstruction add another linear data structure and discard the linked-list advantage.
- **Trial-divisor GCD:** Scanning candidate divisors can take $O(V)$ time per pair, slower than Euclid's logarithmic arithmetic.
- A one-node list enters no loop and is returned unchanged.
- Equal adjacent values insert that same value because $\gcd(x,x)=x$.
- Coprime adjacent values insert `1`.
- Advance to `current.next.next` after each splice so inserted nodes are never processed as original nodes.
- The input is guaranteed nonempty, so the native method may begin directly at `head`.
