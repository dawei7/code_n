## General

Use a slow pointer that advances one node and a fast pointer that advances two. Stop when the fast pointer is at the tail of an odd-length cycle or immediately before the tail of an even-length cycle. At that moment, the slow pointer is the final node of the first half.

Save `slow.next` as the second head. For an even length, advance the fast pointer once more so it denotes the original tail; for an odd length it already denotes the tail. Then set `slow.next` to the original head and `fast.next` to the second head, closing the two halves into independent cycles.

The fast pointer covers the cycle twice as quickly as the slow pointer, so the stopping condition places the slow pointer after exactly $\lceil n/2 \rceil$ nodes. No node values or relative links within either segment change. Replacing only the two boundary links therefore yields precisely the required ordered cycles.

## Complexity detail

The pointer traversal visits $O(n)$ nodes, and rewiring takes constant time, for $O(n)$ total time. Only a fixed number of node references are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Count then traverse:** One pass can find the length and a second can reach both split points in $O(n)$ time and $O(1)$ space, but the two-pointer pass is more direct.
- **Copy values into new nodes:** This preserves the displayed values but uses $O(n)$ extra space and needlessly discards the original nodes.
- A two-node cycle must become two one-node self-cycles.
- For odd lengths, the first cycle contains exactly one more node than the second.
- Duplicate values cannot be used to detect whether a pointer has completed the cycle; node identity determines closure.
