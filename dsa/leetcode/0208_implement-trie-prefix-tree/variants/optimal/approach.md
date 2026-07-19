## General
A trie represents prefixes as paths. Each node stores a mapping from a possible next character to a child node plus a terminal marker saying whether a complete inserted word ends there. The root represents the empty prefix.

Insertion starts at the root and follows the word one character at a time, creating a child only when the corresponding edge is absent. After the final character, mark that node terminal. Shared prefixes automatically share nodes: inserting `apple` and then `app` reuses the first three edges and only adds a terminal marker at the existing `app` node.

`search` and `startsWith` use the same path traversal. If any requested edge is absent, both fail. If the entire path exists, `startsWith` succeeds immediately because some inserted path includes that prefix; `search` succeeds only when the final node is terminal.

That terminal distinction is central. After inserting `apple`, the path for `app` exists, but `search("app")` is false until `app` itself is inserted. Marking every prefix as a word would conflate the two operations.

After processing `i` characters during insertion or lookup, the current node represents exactly the length-`i` prefix. Insertion creates every missing edge on the word's path and marks exactly its endpoint, so all and only inserted words have terminal endpoints. A successful full path therefore proves the query is a prefix of an inserted word, while the additional terminal test proves exact insertion. Missing an edge proves no inserted word can contain that requested prefix path.

## Complexity detail
An operation on a string of length `L` follows or creates one edge per character, taking expected $O(L)$ time with hash-map children. Across inserted words containing `T` total characters, at most `T` non-root nodes are created, so storage is $O(T)$; shared prefixes reduce the actual count.

## Alternatives and edge cases
- A hash set gives expected constant-time exact-word lookup after hashing, but answering arbitrary prefix queries requires scanning words or maintaining another index.
- A sorted array supports prefix-range binary searches, but dynamic insertion can require shifting elements.
- Fixed-size child arrays can improve lookup constants for a small known alphabet while using more space per node.
- Repeated insertion is idempotent. A shorter word may be inserted after its longer extension, and a prefix need not itself be terminal.
- Queries on an empty trie fail unless an empty-word contract explicitly marks the root terminal.
