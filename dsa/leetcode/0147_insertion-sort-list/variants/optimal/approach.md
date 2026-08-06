## General
**A dummy head makes every insertion position uniform**

Keep the processed nodes in a sorted chain after `dummy`. A node smaller than the current minimum can then be inserted after the dummy just like any interior insertion, without replacing a special head variable.

For each `current` node, first save `following = current.next` so the untouched suffix remains reachable. Starting from `dummy`, advance `position` while the next sorted value is less than or equal to `current.val`. Splice `current` after `position`, then continue from `following`.

Before every iteration, the chain after `dummy` contains exactly the already processed nodes in non-decreasing order, and `current` begins the untouched original suffix. The scan stops after all values no greater than the inserted value and before the first larger value, so the splice preserves sorted order. Saving the suffix before rewiring and transferring exactly one existing node preserves membership. When `current` becomes null, every original node appears once in the sorted chain. Using `<=` also places a new equal value after earlier equal values, making the sort stable.

## Complexity detail
The $i$th insertion can scan $O(i)$ sorted nodes, so the worst-case total is $O(n^2)$ time. A dummy node and a constant number of references use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Merge sort:** sorts a linked list in $O(n \log n)$ time, but this problem specifically requests insertion sort.
- **Copy values to an array:** permits library sorting but uses $O(n)$ extra space and does not demonstrate node insertion.
- **Swap node values:** can order values but does not preserve the stronger node-relinking interpretation.
- A one-node legal input is already sorted; the implementation also handles a null app-local head.
- Equal values remain in their original relative order because the scan advances through existing equals.
- Already sorted input is the quadratic worst case for this forward scan, while reverse-sorted input inserts each node near the front.
