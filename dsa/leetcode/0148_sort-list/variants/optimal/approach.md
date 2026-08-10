## General

**Why merge sort fits a singly linked list**

Merge sort repeatedly divides the list into smaller lists, sorts those lists, and merges sorted pairs.

It is a strong fit here because:

- a list can be split by changing one `next` pointer;
- two sorted lists can be merged by relinking their front nodes;
- no random indexing is required;
- every recursion level processes all nodes in linear time.

The base case returns immediately for an empty list or one node. Such a list is already sorted and, importantly, cannot be split into two smaller nonempty lists.

**Find a balanced cut**

`slow` begins at `head`, while `fast` begins at `head.next`. On every loop, slow advances one node and fast advances two.

When fast reaches the end, slow is the last node of the left half. For an even length, the halves have equal size. For an odd length, the left half contains one extra node.

The source saves:

- `l1 = head`;
- `l2 = slow.next`.

It then performs `slow.next = None`. That cut is essential. Without it, the left recursive call would still contain the entire original suffix, so recursion would not shrink and could continue indefinitely.

After cutting, both lists are strictly smaller than the original whenever its length is at least two.

**Let recursion sort each independent half**

`self.sortList(l1)` returns the sorted left chain, and `self.sortList(l2)` returns the sorted right chain. The same divide step continues until every subproblem contains zero or one node.

At the bottom, those one-node lists are sorted. Merging them produces sorted two-node lists; merging those produces larger sorted lists. This bottom-up effect emerges naturally as recursive calls return.

**Merge by choosing the smaller front node**

`dummy` anchors the merged list, and `tail` points to its last attached node.

While both sorted halves remain:

- if `l1.val <= l2.val`, attach `l1` and advance it;
- otherwise attach `l2` and advance it;
- advance `tail` to the attached node.

The two input fronts are the smallest unmerged values in their respective lists. Choosing the smaller one therefore chooses the smallest value remaining overall.

When one half becomes empty, every node left in the other half is already sorted and no smaller candidate remains in the exhausted half. `tail.next = l1 or l2` attaches that complete remainder at once.

The dummy is skipped by returning `dummy.next`.

**Why merging preserves all nodes and sorted order**

At every step, exactly one existing node moves from the front of a half to the end of the merged prefix. No node is copied, discarded, or visited out of order within its own half.

The merged prefix is non-decreasing because each appended node is the smallest remaining front. The untouched suffixes remain sorted by the recursive guarantee. When both are exhausted or one remainder is attached, the complete chain is sorted.

Using `<=` chooses from the left half when values tie. Since recursive splitting preserves original order within each half, this makes the merge stable: equal-valued nodes retain their relative input order.

**Why the whole algorithm is correct**

For zero or one node, the returned chain is sorted and contains exactly the input nodes.

For a longer list, the cut produces two smaller disjoint chains containing all original nodes. By recursive reasoning, each returned half is sorted and preserves its nodes. The merge argument shows that combining them yields one sorted chain containing every node exactly once.

This induction over list length proves the result.

## Complexity detail

Let $n$ be the number of nodes.

Balanced splitting creates $O(\log n)$ recursion levels. At each level, midpoint scans and merges together touch $O(n)$ nodes across all subproblems. Total time is:

$$
O(n\log n).
$$

The merge itself relinks nodes and uses a constant number of pointers plus one dummy node. However, this is top-down recursion. The maximum call depth is $O(\log n)$, so actual auxiliary space is $O(\log n)$.

That contradicts the manifest’s $O(1)$ space claim. The selected source meets the time target but not the constant-memory follow-up. A bottom-up iterative merge sort is needed for true $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Bottom-up merge sort:** Merge runs of lengths `1, 2, 4, ...` iteratively. It keeps $O(n\log n)$ time and achieves $O(1)$ auxiliary space.
- **Insertion sort:** It is easy to relink in place but has $O(n^2)$ worst-case time.
- **Array conversion and sort:** It can use a library sort but requires $O(n)$ node/value storage and abandons linked-list-native merging.
- **Quicksort:** Partitioning a singly linked list is possible, but worst-case time is $O(n^2)$ and random pivot access is awkward.
- **Empty list:** The base case returns `None`.
- **One node:** It is returned unchanged.
- **Odd length:** The left half receives one extra node, but recursion remains balanced within one.
- **Equal values:** The `<=` branch makes the merge stable.
- **Cut integrity:** `slow.next = None` must happen before recursing to guarantee smaller, disjoint subproblems.
- **Runtime dependencies:** The source uses `Optional` without importing it. The platform supplies `ListNode`; standalone Python needs the type definition and `from typing import Optional`.
- **Manifest mismatch:** Recursive stack frames prevent this exact implementation from being constant-space.
