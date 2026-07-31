## Description

A binary tree can be serialized by traversing it in preorder. Record the value of each non-null node, and record a sentinel such as `#` whenever the traversal encounters a null child.

For example, consider this tree:

```text
        9
      /   \
     3     2
    / \     \
   4   1     6
```

Its comma-separated preorder serialization is `"9,3,4,#,#,1,#,#,2,#,6,#,#"`, where every `#` marks a null pointer.

Given a comma-separated string `preorder`, return `true` when it is a valid preorder serialization of one binary tree; otherwise return `false`.

Every token is guaranteed to be either an integer or `#`, and the comma-separated format itself is valid. In particular, malformed text such as `"1,,3"` will not be supplied.
