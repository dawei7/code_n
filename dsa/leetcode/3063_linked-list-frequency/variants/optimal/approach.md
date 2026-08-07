## General
Given the `head` of a linked list containing `k` **distinct** elements, return *the head to a linked list of length *`k`* containing the frequency of each **distinct** element in the given linked list in **any order**.*, the algorithm executes a single-pass linear scan through input elements. It utilizes a hash map (`dict`) to store element values and their indices/frequencies for $O(1)$ fast access, linked list node pointers (`val`, `next`) to process sequential node chains.

## Complexity detail
- **Time Complexity**: $O(n)$ — Operation count bound.
- **Space Complexity**: $O(k)$ — Auxiliary memory allocation bound.
