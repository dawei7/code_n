## General

The supplied node does not identify how many list elements precede it. Follow `prev` pointers until reaching the unique node whose `prev` is `None`; that node is the list head.

Starting from the recovered head, follow `next` pointers to the tail and append each visited value to the result. The backward phase guarantees that no prefix of the list is omitted, and the forward phase visits every node in exactly head-to-tail order. Because a well-formed doubly linked list connects each adjacent pair in both directions, the two phases cover the complete list regardless of which node was supplied.

## Complexity detail

Let $n$ be the number of nodes. If the supplied node has $p$ predecessors, the backward walk takes $O(p)$ time and the forward walk takes $O(n)$ time, for $O(n)$ overall. The returned array requires $O(n)$ space; excluding that required output, the pointer traversal uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Walk forward immediately:** This loses every node before the supplied position unless the supplied node happens to be the head.
- **Recursive traversal:** Recursion can collect the list but adds $O(n)$ call-stack space and risks unnecessary depth limits.
- **Supplied head:** The backward phase performs zero moves, then the ordinary forward scan returns the list.
- **Supplied tail:** The backward phase crosses the whole list before the forward scan reconstructs the required order.
- **Single node:** Both pointers are `None`, so its value is appended once.
