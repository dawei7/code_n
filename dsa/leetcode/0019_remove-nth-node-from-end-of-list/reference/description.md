## Description

Given the head of a non-empty singly linked list, remove its $n$th node when counted from the end. Count the tail as position 1, its predecessor as position 2, and continue toward the head. The input guarantees that $n$ names an existing node.

Remove exactly that node while preserving the relative order and links of every other value, then return the possibly updated head. Removing the original head changes the returned head; every other removal keeps it unchanged. The source illustration's first example is reproduced independently below. The fourth node is second from the end and is removed:

```text
Before: 1 -> 2 -> 3 -> 4 -> 5
                       ^ remove
After:  1 -> 2 -> 3 ------> 5
```
