## Description

A singly linked list has a head, but you are given only the particular `node` that must be deleted—**not access to the head**. All list values are unique, and the supplied node is guaranteed not to be the tail.

Deleting the node does not mean deallocating that object. After the operation, all of these observable properties must hold:

- The original value of `node` no longer appears in the list.
- The list contains one fewer node.
- Values before `node` retain their order.
- Values after `node` retain their order.
