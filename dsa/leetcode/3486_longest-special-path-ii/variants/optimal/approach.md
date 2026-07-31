## General

**Turn each endpoint into a suffix problem**

During a depth-first traversal from root 0, the active recursion stack is exactly the ancestor path to the current node. Because every edge length is positive, the longest legal path ending at that node begins at the earliest depth whose suffix satisfies the value rule. Prefix distances then give its weighted length in constant time.

For each value, keep the depths where it occurs on the active path. A suffix is illegal in either of two ways:

- one value appears at least three times; or
- at least two different values each appear at least twice.

The earliest legal start must therefore lie after every third-from-last occurrence, and after the second-largest among all second-from-last occurrence depths. The largest third-from-last depth handles the first violation. The two largest second-from-last depths identify the second violation: the suffix may retain the value associated with the largest one, but it must exclude the earlier occurrence represented by the runner-up.

**Update only the value entering the path**

When a node with value `x` enters the recursion stack, only `x`'s occurrence summaries change. Its new second-from-last depth is its previous last occurrence, and its new third-from-last depth is its previous second-last occurrence.

Along a downward traversal those depths only increase. Consequently, the largest and second-largest second-occurrence summaries can be updated in constant time by comparing the changed value with the current top two. The maximum third-occurrence summary also needs one comparison. These small summaries are passed by value to child calls, so returning from a branch restores the parent's state automatically; only the per-value position stack needs an explicit pop.

Let `left` be one plus the greater of the largest third occurrence and the runner-up second occurrence. Then the path from depth `left` through the current node contains no triple and at most one duplicate pair. Starting any earlier would include the occurrence that certifies at least one violation, so this is the earliest—and therefore longest—legal suffix for this endpoint.

**Resolve the global tie correctly**

Compare the suffix length with the best length seen over all endpoints. A greater length replaces both result components. An equal length keeps the smaller node count. Since positive edge weights make any later start strictly shorter for the same endpoint, one suffix per endpoint is sufficient.

## Complexity detail

Let $n$ be the number of tree nodes. Constructing the adjacency list takes $O(n)$ time and space. DFS visits every node and edge once; each entry, summary update, prefix-distance calculation, and rollback takes $O(1)$ time. Total time is $O(n)$.

The adjacency list, occurrence stacks, prefix distances, and recursion stack collectively use $O(n)$ auxiliary space. Across all values, the occurrence stacks contain exactly the nodes on the current root path and never more than $n$ entries.

## Alternatives and edge cases

- **Heap or balanced multiset of occurrence depths:** supports the same boundary calculation but introduces an unnecessary $O(\log n)$ factor per update.
- **Enumerate every ancestor for every endpoint:** is straightforward but can take $O(n^2)$ time on a chain.
- **Ordinary unique-value sliding window:** solves the related version where every value must be distinct, but incorrectly rejects the one duplicate pair allowed here.
- **Third occurrence:** the start must move past the earliest of the last three occurrences of that value.
- **Two duplicate pairs:** the start must move past the earlier occurrence of whichever pair has the second-latest such occurrence.
- **Separate branches:** occurrence stacks are rolled back after each child, so values in sibling branches never contaminate one another.
- **Tie breaking:** the second result component is the minimum node count, not the number of maximum-length paths.
