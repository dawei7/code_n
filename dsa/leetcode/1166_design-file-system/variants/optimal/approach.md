## General

**Represent path components as trie edges**

A path is hierarchical. For `"/leet/code"`, component `"leet"` is a child of the implicit root, and `"code"` is a child of the `"leet"` node.

Each `Trie` object represents one existing path node. Its `children` dictionary maps a component name to the next node, and `v` stores the integer associated with the complete path ending at that node.

The `FileSystem` constructor creates one root trie node. The root is implicit: `"/"` is not a valid user-created path and has no stored application value. Its default `v = -1` is therefore only a sentinel.

**Split a valid absolute path into components**

Every valid path begins with `"/"`. For `"/leet/code"`, `split("/")` produces `["", "leet", "code"]`. The initial empty string comes from the leading slash.

The implementation ignores that first element by using slices beginning at index one. The contract guarantees valid paths with no empty internal components and no root-only path, so the last component is always a real lowercase name.

**Validate the complete parent chain before creation**

`insert` traverses `ps[1:-1]`, which contains every component except the leading empty part and the new path's final name. These are exactly the components of the immediate parent path.

For each parent component `p`, the method checks `p in node.children`. If any component is absent, the immediate parent cannot exist, so creation returns false without adding anything.

This traversal performs no mutation. A failed creation therefore cannot accidentally create partial directories. For `"/c/d"` in an empty system, component `"c"` is missing at the root and the method returns false; it does not silently create `"/c"`.

For a one-component path such as `"/a"`, `ps[1:-1]` is empty. The traversal stays at the implicit root, which is the permitted parent. This correctly allows top-level paths to be created directly.

**Reject an already existing final path**

After reaching the parent node, `ps[-1]` is the new path's final component. If it is already in `node.children`, that exact path exists and creation must return false.

Otherwise, `node.children[ps[-1]] = Trie(v)` creates one new node with the supplied value, and the method returns true.

The code never overwrites an existing value. A second call for the same path fails even if it supplies a different value, matching the create-only contract.

**Retrieve by following every component**

`search` begins at the implicit root and traverses `w.split("/")[1:]`. If a component edge is missing, the complete path does not exist and it returns `-1`.

If all edges exist, the final node is exactly the requested path and `node.v` is returned.

Every created path receives a positive value under the constraints, so `-1` cannot be confused with a stored result.

**Trace the second example**

Creating `"/leet"` has no explicit parent component, so it adds a child of the root with value one.

Creating `"/leet/code"` then finds `"leet"`, sees that `"code"` is new, and adds it with value two. Searching that path follows both edges and returns two.

Creating `"/c/d"` fails because root has no `"c"` child. Searching `"/c"` also finds no edge and returns `-1`.

**Why the operations are correct**

The trie invariant is that a component path exists in the file system if and only if its full sequence of component edges exists from the root, and the final node stores its associated value.

Creation checks every edge of the parent sequence before adding exactly one final edge. It succeeds precisely when the parent exists and the final edge does not, which is exactly the allowed condition. Since checks precede mutation, failure preserves the invariant.

Search follows the same unique component sequence. A missing edge proves no such created path exists; reaching the final node proves it does and returns the stored value. Thus both public operations implement their contracts.

## Complexity detail

Let `L` be the number of characters in one path. Splitting the path and traversing its components takes `O(L)` time in total, assuming expected constant-time dictionary access per component. Both `createPath` and `get` therefore take `O(L)` expected time.

Across an operation sequence whose total path-character count is `S`, total processing time is `O(S)`.

Each successful creation adds one trie node and one component key under its parent. Persistent nodes and key text across all stored paths require at most `O(S)` space. Temporary split component lists for one call use `O(L)` space and are covered by the overall `O(S)` bound.

## Alternatives and edge cases

- **Store complete paths in one dictionary:** Creation can derive the parent string and test both full keys. This is simpler and has expected `O(L)` string-processing time; the trie explicitly models hierarchy and shares component navigation.
- **Create missing parent nodes automatically:** That violates the contract. A path may be added only when its immediate parent already exists.
- **Overwrite an existing final node:** `createPath` is not an update operation, so an existing path must make the call fail without changing its value.
- **Top-level path:** The implicit root counts as its parent, so `"/a"` may be created in an empty system.
- **Missing intermediate component:** The operation fails before mutation, leaving no partial path behind.
- **Existing parent with new child:** Traversal succeeds and exactly one child node is created.
- **Duplicate path:** The final-component membership check returns false even when the proposed value matches the existing value.
- **Get a missing path:** The first missing edge returns `-1`.
- **Positive stored values:** They make the `-1` missing sentinel unambiguous.
- **Shared prefixes:** Paths such as `"/a/b"` and `"/a/c"` reuse the same `"/a"` node and diverge only at the last edge.
- **Valid-path guarantee:** The code relies on the leading slash and nonempty lowercase components, so it does not validate malformed input.
