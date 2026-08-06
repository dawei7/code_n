## Description

Serialization converts a data structure into a sequence that can be stored in a file or memory buffer, sent over a
network, and later reconstructed in the same or another computing environment.

Design algorithms to serialize and deserialize an N-ary tree. Each node in this rooted tree has at most $N$
children. `serialize(root)` must turn the tree into a string, and `deserialize(data)` must rebuild the original tree
structure from that string.

The encoding format is unrestricted as long as the round trip is exact. For example, the first source diagram is
the following 3-ary tree, which could be written as `[1 [3[5 6] 2 4]]`:

| Parent | Ordered children |
|---:|---|
| 1 | 3, 2, 4 |
| 3 | 5, 6 |
| 2 | none |
| 4 | none |
| 5 | none |
| 6 | none |

Another valid choice is LeetCode's level-order format, in which `null` separates consecutive child groups. The
second source diagram is completely represented here:

| Parent | Ordered children |
|---:|---|
| 1 | 2, 3, 4, 5 |
| 2 | none |
| 3 | 6, 7 |
| 4 | 8 |
| 5 | 9, 10 |
| 6 | none |
| 7 | 11 |
| 8 | 12 |
| 9 | 13 |
| 10 | none |
| 11 | 14 |
| 12 | none |
| 13 | none |
| 14 | none |

That tree can be serialized as
`[1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]`. Neither suggested
format is mandatory; any unambiguous stateless representation is acceptable.
