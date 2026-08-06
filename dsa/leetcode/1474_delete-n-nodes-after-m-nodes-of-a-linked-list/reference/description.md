## Description

Given the `head` of a linked list and integers `m` and `n`, traverse the list
and remove nodes according to this repeating procedure:

1. Begin with `head` as the current node.
2. Keep the first `m` nodes starting at the current node.
3. Remove the following `n` nodes.
4. Repeat the keep and remove steps until the end of the list is reached.

Return the head of the modified list after these removals.
