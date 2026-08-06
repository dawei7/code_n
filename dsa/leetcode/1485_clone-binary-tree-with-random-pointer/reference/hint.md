## Hint

1. Traverse the tree while maintaining a hash table from each original node to
   a newly allocated `NodeCopy`.
2. Traverse the originals again and use that table to reproduce every `left`,
   `right`, and `random` link among the copies.
