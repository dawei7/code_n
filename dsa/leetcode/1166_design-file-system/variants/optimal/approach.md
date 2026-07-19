## General
**Store complete paths as keys.** Maintain a hash map from each successfully created path string to its integer value. Full paths are already unique identifiers, so a separate tree node is unnecessary for the required operations.

**Validate only the immediate parent.** For `createPath(path, value)`, first reject `path` when it is already a key. Locate its final `/`; the prefix before that slash is the immediate parent. An empty prefix means the parent is the implicit root, so a one-component path is allowed. A non-empty parent must already be in the map. Only after both checks pass should `paths[path] = value` be performed, which prevents failed creations from changing state.

**Use the same map for lookup.** `get(path)` returns the mapped value when present and `-1` otherwise. Because creation requires the immediate parent, every stored nested path has a complete chain of previously created ancestors. Existing keys are never reassigned, so their associated values remain stable.

## Complexity detail
Hashing a path and finding its final separator cost time proportional to that path's length. Summed over all method calls, the expected total time is $O(S)$. The map stores at most one copy of every successfully created path, whose combined length is at most $S$, so its space use is $O(S)$.

## Alternatives and edge cases
- **Trie by components:** A trie naturally represents the hierarchy and also achieves linear work in the path text, but it needs node and child-map machinery that the two requested operations do not require.
- **Linear list of paths:** Searching every previously created path is correct but can take quadratic time across many operations.
- **Missing parent:** Creating a nested path fails even if all components are syntactically valid; no intermediate directory is created automatically.
- **Duplicate path:** A second creation fails and must not replace the original value.
- **One-component path:** Its parent prefix is empty, representing the implicit root, so it can be created in an empty system.
- **Missing lookup:** `get` returns `-1` and does not create the requested path.
