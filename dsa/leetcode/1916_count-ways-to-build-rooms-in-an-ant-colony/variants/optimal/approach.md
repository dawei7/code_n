## General
**View valid orders as tree linear extensions**

For every node $v$, let $s_v$ be the number of rooms in its subtree, including $v$. A classic hook-length identity for rooted trees gives the number of parent-before-child orders:

$$
\frac{N!}{\prod_v s_v}.
$$

To see why, consider a node whose child subtrees have sizes $s_1,\ldots,s_t$. The node itself must come first within its subtree. The valid orders inside the child subtrees can then be interleaved in

$$
\frac{(s_1+\cdots+s_t)!}{s_1!\cdots s_t!}
$$

ways while preserving each child's internal order. Multiplying this recurrence down the tree cancels the child factorials and leaves the hook-length formula.

**Compute subtree sizes without recursion**

Build child lists from `prevRoom`. Starting at room `0`, produce a parent-before-child traversal order iteratively. Process every non-root room in reverse order, adding its accumulated size to its parent. This remains safe for a chain of $10^5$ rooms, where recursive DFS could exceed Python's call-stack limit, and it does not assume parent indices are numerically smaller than child indices.

**Divide modulo the prime**

Compute $N!$ and the product of all subtree sizes modulo $M=10^9+7$. Every subtree size is positive and smaller than $M$, so the product is invertible. Fermat's little theorem gives its inverse as `pow(product, M - 2, M)`. Multiplying the factorial by this inverse yields the required residue.

## Complexity detail
Building the tree, producing the traversal order, accumulating subtree sizes, and multiplying the factors each take $O(N)$ time. Modular exponentiation costs $O(\log M)$, which is constant with respect to $N$, so total time is $O(N)$. Child lists, order, and subtree sizes use $O(N)$ space.

## Alternatives and edge cases
- **Merge child counts with binomial coefficients:** A postorder DFS can multiply child answers and interleaving combinations directly; it is also $O(N)$ with precomputed factorials but needs recursion safeguards or an explicit stack.
- **Enumerate topological orders:** Backtracking over currently available rooms is exact only for tiny trees and grows exponentially.
- **Recompute every subtree:** Running a traversal from each node is correct but takes $O(N^2)$ time on a chain.
- **Chain:** Every room has only one possible successor, so the answer is one.
- **Star:** Once the root is built, its $N-1$ children may appear in any order, giving $(N-1)!$.
- **Arbitrary labels:** A parent may have a larger numeric ID than its child; traversal order, not numeric order, controls accumulation.
