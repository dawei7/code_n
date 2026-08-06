## Description

You are given a node from a circular singly linked list whose values are sorted in non-descending cyclic order. The supplied `head` may refer to any node in the cycle, so it is not necessarily the node with the smallest value. Insert a new node containing `insertVal` while keeping the list circular and sorted.

When several links are valid insertion locations, any one of them may be chosen. For a nonempty input, return the exact node originally supplied as `head`. If the input is empty, create a one-node circular list whose node points to itself and return that new node.
