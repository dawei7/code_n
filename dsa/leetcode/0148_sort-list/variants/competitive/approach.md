## General

**Divide near the middle, then merge**

The competitive source is top-down merge sort. Its recursive contract is:

> `sortList(head)` returns a sorted chain containing exactly the nodes reachable from `head`.

An empty chain and a one-node chain already satisfy that contract, so they are returned unchanged.

Longer chains are cut into two near-equal parts. Each part is recursively sorted, and `mergeTwoLists` combines the two sorted results.

**Track the predecessor needed to cut**

`fast` and `slow` both start at the head, while `prev` starts at `None`.

Each loop iteration:

- assigns the old `slow` to `prev`;
- advances `fast` two steps;
- advances `slow` one step.

When fast can no longer take a full iteration, `slow` begins the right half and `prev` is the final node of the left half.

`prev.next = None` severs the connection. For an even-sized list, the halves are equal. For an odd-sized list, this convention gives the right half one extra node.

The tuple assignment evaluates all old pointer expressions before updating variables, so fast and slow advances correspond to the same iteration.

The base case ensures `prev` is a real node whenever the split code runs.

**Why cutting before recursion cannot be skipped**

Before the cut, `head` still reaches `slow` and all later nodes. Calling `sortList(head)` at that point would pass essentially the original list again and fail to reduce the problem.

After `prev.next = None`, the left chain ends at `prev` and the right begins at `slow`. They are disjoint, nonempty, and smaller than the original.

Balanced halves keep recursion depth logarithmic rather than linear.

**Merge through a dummy anchor**

After the recursive calls return `sorted_l1` and `sorted_l2`, both inputs to `mergeTwoLists` are non-decreasing.

The helper creates a dummy and uses `cur` as the merged tail. While both lists remain, it compares their front values.

When `l1.val <= l2.val`, the compact assignment attaches `l1` after `cur`, advances `cur` to that node, and advances `l1` to its old successor. The other branch performs the symmetric operation for `l2`.

Python evaluates the right-hand side before pointer assignments, so the old successor is not lost when `cur.next` changes.

Once one input is empty, the helper attaches the other input’s whole remainder. Its values are already sorted and no competing values remain.

**Why local front choices yield a globally sorted list**

The front of a sorted chain is its smallest remaining element. Therefore, the smaller of the two current fronts is the smallest node not yet merged.

Appending it preserves sorted order. Repeating this choice until one chain is exhausted constructs a non-decreasing prefix, and the remaining chain can follow it without violating order.

Each chosen node is removed conceptually from exactly one input and linked once into the output. No data node is allocated or omitted.

The `<=` tie rule selects the left-half node first. Combined with stable recursive merges, this preserves the original relative order of equal values.

For `[4,2,1,3]`, recursive cuts eventually sort `[4,2]` into `[2,4]` and `[1,3]` stays `[1,3]`. Merging fronts chooses one, two, three, and four.

**Structural induction covers the full sort**

Base-case chains are sorted. For any longer chain, the algorithm forms two smaller chains; assuming recursive calls sort them correctly, the merge proof yields a sorted union of exactly their nodes. Since those halves partition the original, the returned list is the sorted original.

## Complexity detail

Let $n$ be the node count.

Each recursion level scans a total of $O(n)$ nodes to find midpoints and merge halves. Near-halving produces $O(\log n)$ levels. Total time is $O(n\log n)$.

Each merge uses constant local pointer storage and one dummy node. Nevertheless, recursive calls create $O(\log n)$ simultaneously active stack frames, so actual auxiliary space is $O(\log n)$.

The source comment correctly states stack space $O(\log n)$, while the variant manifest incorrectly claims $O(1)$. This exact source does not satisfy the follow-up’s constant-space target.

## Alternatives and edge cases

- **Iterative bottom-up merge sort:** Repeatedly merge adjacent runs of doubling size. It attains the requested $O(n\log n)$ time and $O(1)$ auxiliary space.
- **Insertion sort:** It can be constant-space and stable but degrades to $O(n^2)$ time.
- **Copy into an array:** Sorting values or node references is convenient but uses $O(n)$ memory.
- **Quicksort:** It can relink partitions but has quadratic worst cases and less natural linked-list pivots.
- **Empty and one-node inputs:** Both return through the base case.
- **Two nodes:** The split makes two one-node lists, and one merge orders them.
- **Odd node count:** The right side gets one extra node; recursion depth remains logarithmic.
- **Equal values:** The left-first `<=` choice preserves stability.
- **Tuple assignments:** Sequential translations need saved successor variables to avoid losing the remaining chain.
- **Node helper representation:** Recursive `__repr__` is unused and could recurse deeply on a long list.
- **Manifest mismatch:** Constant-space claims apply to bottom-up merge sort, not this top-down recursive source.
