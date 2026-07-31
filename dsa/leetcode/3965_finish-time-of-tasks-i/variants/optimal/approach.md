## General

The finish time of a task depends only on the finish times of its children, so every child must be processed before its parent. Build a child list from the already directed parent-child edges. Starting from root `0`, record any traversal order by appending each visited task's children. Reversing that order is a valid postorder for this dependency: descendants always appear before the ancestor that appended them.

Allocate one finish-time entry per task. A leaf receives `baseTime[task]`. For a non-leaf, scan its already computed child values for `earliest` and `latest`. Substituting the definition of `ownDuration` gives

$$
\text{finish}[i]
= \text{latest} + (\text{latest}-\text{earliest}) + \texttt{baseTime[i]}
= 2\,\text{latest}-\text{earliest}+\texttt{baseTime[i]}.
$$

This stores exactly the value defined by the contract for every node. The reverse traversal begins with leaves and deeper descendants, so an induction over that order proves that all child values used by a task are correct. The computed value for root `0` is therefore the requested finish time.

The traversal is iterative. That detail is material because a valid tree may be a chain of 100,000 tasks, which exceeds Python's ordinary recursion depth even though the recurrence itself is linear.

## Complexity detail

Creating the child lists examines the $n-1$ edges once. The forward traversal visits every task once, and the reverse pass scans each child list once in total. The running time is $O(n)$. The child lists, traversal order, and finish array occupy $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Recursive postorder DFS:** It mirrors the recurrence directly and is also $O(n)$, but an unbalanced 100,000-node tree can overflow the language call stack.
- **Rescan all edges for each task:** This avoids adjacency lists but repeats parent-child discovery and can take $O(n^2)$ time.
- **One child:** `earliest` and `latest` are equal, so the parent's finish time is the child finish time plus its own base duration.
- **One task:** Root `0` is also a leaf, so the answer is simply `baseTime[0]`.
- **Arbitrary edge order and labels:** The input pairs need not be grouped by parent or sorted by task number; the explicit traversal determines dependency order.
- **Large finish values:** Python integers preserve the guaranteed sub-$2^{53}$ result without overflow or rounding.
