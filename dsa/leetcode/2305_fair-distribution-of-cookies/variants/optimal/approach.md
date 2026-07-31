## General

**Search assignments with large bags first**

Sort the bags in descending order, keep one running load per child, and
recursively assign the next bag to each possible child. Large early decisions
raise the current maximum quickly, which makes the incumbent upper bound useful
sooner without changing the set of complete distributions.

**Prune branches that cannot improve the answer**

Initialize the best unfairness with the valid distribution that gives every
bag to one child. If a partial assignment's largest load is already at least
that best value, positive remaining bags cannot reduce it, so discard the
branch. At a complete assignment, replace the incumbent with its maximum load.

**Remove symmetric choices**

At one recursion depth, children with equal current loads are interchangeable.
Try only one child for each distinct load. In particular, after trying the
first empty child there is no reason to try another empty child.

Every labeled assignment appears in the unpruned recursion. Bound pruning
removes only branches whose unfairness can no longer beat an already valid
answer, and symmetry pruning retains an equivalent representative with the
same load multiset. Therefore at least one representative of every potentially
optimal distribution reaches a leaf, and the smallest recorded maximum is the
minimum unfairness.

## Complexity detail

Let $n=\lvert\texttt{cookies}\rvert$. Without pruning, each bag has $k$
possible recipients, giving $O(k^n)$ worst-case time. Sorting contributes
$O(n\log n)$ and does not dominate. The recursion stack uses $O(n)$ space and
the child loads plus per-level symmetry sets use $O(nk)$ total live auxiliary
space in this implementation; because $k\le n\le8$, this remains tightly
bounded by the source contract.

## Alternatives and edge cases

- **Subset dynamic programming:** Precompute subset sums and partition masks among children; this avoids labeled symmetry but uses exponential table space.
- **Binary-search an unfairness threshold:** Feasibility still requires a bin-packing backtrack, adding an outer logarithmic search.
- **Give all bags to one child:** This is always valid and supplies a simple initial upper bound, but is rarely optimal.
- **One child per bag:** When `k == n`, the answer is the largest bag.
- **Empty child:** The contract permits a child to receive no bags; forcing every load positive would remove legal distributions.
- **Duplicate bag sizes:** Bags remain distinct assignments even when their sizes agree, while equal child-load states may still be skipped symmetrically.
- **Indivisible bags:** A bag cannot be split to equalize loads, so the average load is only a lower bound.
- **Large bag:** The answer can never be smaller than the largest single bag.
