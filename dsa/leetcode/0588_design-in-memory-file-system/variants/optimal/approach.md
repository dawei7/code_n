## General
**Represent path components as trie edges**

Use one node for the root. Each directory node stores a hash map from an immediate child name to its child node. Splitting an absolute path on `/` yields the sequence of edges to follow, so path traversal depends on depth rather than the total number of stored entries.

**Distinguish files from directories**

A node whose content field is `None` is a directory. A file node holds a list of appended text fragments. Keeping fragments avoids repeatedly copying all earlier content on every append; reading joins them in write order.

**Share one path walker**

A helper starts at root and follows every nonempty path component. In creation mode it inserts missing nodes, which gives `mkdir` its recursive behavior and creates a file node's path before content is attached.

**Implement listing according to node type**

When the target is a file, return only the path's final component. When it is a directory, sort and return its immediate child names. Descendants are not included in a directory listing.

**Why operations preserve filesystem semantics**

Each absolute component sequence maps to exactly one trie route, so distinct sibling names cannot collide and repeated traversal reaches the same node. Directory creation adds only missing edges, file appends preserve fragment order at the terminal node, and reads concatenate precisely those fragments. Listing consults exactly the terminal node's type and children, producing the required file or directory behavior.

## Complexity detail
Let `P` be the number of path components traversed, `k` the number of immediate children returned by a directory listing, and `C` the content length read or appended. Hash-map traversal is $O(P)$ expected time; directory listing costs $O(k \log k)$; content work costs $O(C)$. Total stored nodes, names, and content occupy $O(S)$ space.

## Alternatives and edge cases
- **Flat maps keyed by full paths:** can support direct file lookup, but directory listing needs either a separate child index or a scan of stored paths.
- **Sorted child arrays:** make listing immediate but insertion and lookup among many siblings can take $O(k)$ per component.
- **Single growing content string:** is simple, but repeated appends can repeatedly copy existing content and become quadratic in total written length.
- **Root path:** has no components and lists root's immediate children.
- **Recursive directory creation:** one `mkdir` call may create several missing ancestors.
- **Listing a file:** returns a one-element list containing its basename.
- **Repeated append:** preserves all content in call order.
- **Empty directory:** returns an empty list.
- **Lexicographic listing:** sort names only when a directory is listed; insertion order is irrelevant.
- **Shared prefixes:** paths reuse the same ancestor nodes and diverge only at the first different component.
