## General

**Let each pointer traverse both list lengths**

Start `first` at `headA` and `second` at `headB`. Advance each pointer by one node. When `first` reaches `None`,
redirect it to `headB`; when `second` reaches `None`, redirect it to `headA`. Stop when the references are identical,
including when both become `None` for disjoint lists.

Suppose the private prefixes have lengths $a$ and $b$ and the shared suffix has length $c$. The first pointer's
concatenated route is A then B, while the second pointer's route is B then A. Reaching the shared suffix on the
second list takes $a + c + b$ steps for the first route and $b + c + a$ for the second, which are equal. Switching
heads therefore cancels the original prefix-length difference without measuring either list.

If an intersection exists, the equally aligned pointers meet at its first shared node. If the lists are disjoint,
each pointer traverses exactly $m + n$ nodes and they reach `None` together. The loop compares object identity with
`is`, so separate nodes carrying equal values cannot produce a false match.

Neither pointer assignment changes a `next` link. The original list structures are therefore preserved exactly as
the contract requires.

## Complexity detail

Each pointer traverses at most both lists once, giving $O(m + n)$ time for list lengths $m$ and $n$. Only the two
moving node references are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Store nodes from one list in a set:** finds the first shared identity in linear time but uses $O(m)$ auxiliary
  space.
- **Measure both lengths first:** can advance the longer prefix and then walk in lockstep with the same asymptotic
  bounds, but requires separate length passes.
- **Compare node values:** is incorrect because different node objects may hold the same value.
- The two heads may already reference the same node, in which case the loop returns immediately.
- Equal-length private prefixes need no special case.
- Once acyclic singly linked lists share one node, they necessarily share the complete suffix after it.
- Disjoint lists converge at the shared `None` reference.
