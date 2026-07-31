## General

**Make twins advance in the same direction**

Use slow and fast pointers to locate the start of the second half. Because the
length is guaranteed even, the slow pointer arrives exactly at node $n/2$
when the fast pointer reaches the end.

Reverse the second half in place. Its first node is now the original last
node, its second is the original second-to-last node, and so forth. A pointer
starting at the original head and a pointer starting at the reversed half can
therefore advance together through every twin pair. Add their values, retain
the greatest sum, and stop after the reversed half is exhausted.

The midpoint search covers every node position needed to divide the list, and
reversal puts node $n-1-i$ opposite node $i$. The final scan consequently
examines every twin pair exactly once, so its maximum is the required answer.

## Complexity detail

Let $n$ be the number of nodes. Finding the midpoint, reversing half the list,
and scanning the pairs each take $O(n)$ time overall. The pointer variables
use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Array of node values:** Copy all values and pair opposite indices. This is
  straightforward and takes $O(n)$ time but uses $O(n)$ extra space.
- **Stack for the first half:** Push values while finding the midpoint, then
  pop against the second half. It also requires $O(n)$ extra space.
- **Restart traversal for every twin:** Locating each opposite node from the
  head is correct but takes $O(n^2)$ time.
- With two nodes, their sum is the only candidate.
- The maximum may come from the outer pair, the middle pair, or any pair
  between them.
- Reversing the second half mutates the input list; callers that require the
  original structure can reverse it again afterward.
