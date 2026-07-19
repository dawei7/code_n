## General
**Count before changing any links**

Traverse the original list once and store the frequency of every node value in a hash table. The decision for a node depends on occurrences that may appear anywhere later in the unsorted list, so filtering during the first encounter would not yet have enough information.

**Filter nodes with a second traversal**

Use a dummy node immediately before the original head. Keep a pointer to the last retained node and inspect its successor. When the successor's value has frequency greater than 1, bypass it by assigning its next node to the retained predecessor's `next`. Do not advance the predecessor, because several removable nodes may be consecutive. Otherwise, advance to the unique node.

The dummy predecessor makes removal at the original head identical to removal in the middle. Returning `dummy.next` also naturally yields an empty list if every node was bypassed.

**Why exactly the correct nodes survive**

The first traversal records each value's occurrence count in the untouched original list. During the second traversal, a node is bypassed if and only if that count exceeds one. Therefore every occurrence of every repeated value is removed, rather than retaining an arbitrary first copy. Nodes with count one are never bypassed, and link rewiring only skips removed nodes, so all unique nodes remain in their original order.

## Complexity detail
The two traversals each visit at most $n$ nodes and hash-table operations take expected constant time, giving $O(n)$ total time. The frequency table contains at most $n$ distinct values and uses $O(n)$ space. Link filtering itself uses only constant pointer space.

## Alternatives and edge cases
- **Keep the first occurrence:** A standard deduplication set solves a different problem; here every occurrence of a repeated value must be deleted.
- **Compare each node with the full list:** It avoids a frequency table but takes $O(n^2)$ time.
- **Sort values first:** Sorting would lose the linked list's structural order unless extra mapping is retained, and it adds unnecessary $O(n\log n)$ work.
- **Nonconsecutive duplicates:** Counts must cover the whole unsorted list, not just adjacent runs.
- **Duplicate head value:** Remove all matching nodes and return the first later unique node.
- **Duplicate tail value:** Earlier occurrences of the tail's value must also have been removed.
- **Consecutive removable nodes:** Keep the predecessor fixed while bypassing each one.
- **All values repeated:** Return an empty list.
- **All values unique:** Preserve the original head and every link.
- **Single node:** Its value occurs once, so return that node unchanged.
