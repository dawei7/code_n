## Description

Given the heads `headA` and `headB` of two singly linked lists, return the node where the lists first intersect. Return `null` if they do not share any node.

Intersection is based on node identity: from the intersection onward, both links lead through the same node objects.

```text
list A: a1 -> a2 --\
                     c1 -> c2 -> c3
list B: b1 -> b2 --/
                     ^ first shared node
```

The complete linked structure in every test case is acyclic.
