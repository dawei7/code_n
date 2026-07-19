## General
**Viewing random pointers as graph edges**

The `left` and `right` links alone form a tree, but adding `random` links turns the structure into a directed graph. Those extra edges can point backward, cross between subtrees, or cycle. A clone routine must therefore remember which original nodes already have copies; recursively following pointers without a map could duplicate nodes or loop forever.

**Creating one copy per original identity**

Maintain a dictionary `copies` keyed by original node identity. Begin with a fresh `NodeCopy` for `root` and place the original root on a work stack. Whenever an edge reaches an original node not yet in the dictionary, allocate its copy immediately, record it, and schedule that original node for processing.

Recording the mapping before exploring the new node is essential. If a self-pointer or cycle leads back to it, the existing clone is reused instead of allocating another object.

**Wiring all three pointer kinds**

For each popped original node, inspect `left`, `right`, and `random`. A null edge remains null. For a non-null target, obtain exactly one target clone from `copies` and assign that clone to the same field on the current copy.

Processing all edge kinds through the same rule preserves cross-subtree random links without relying on traversal order. The stack eventually empties because at most $N$ original identities can be inserted.

**Why the result is a deep copy**

The dictionary establishes a one-to-one correspondence from each reachable original node $u$ to one newly allocated copy $c(u)$. For every field $f$ among `left`, `right`, and `random`, the algorithm assigns null when $u.f$ is null and otherwise assigns $c(u.f)$. Thus all values and labeled edges are preserved.

Every assigned non-null pointer targets an object created in `copies`, never an original object. The returned root is therefore structurally equivalent to the input and shares no node identity with it.

**How the app-local encoding corresponds**

The encoded `nodes` array already expresses child placement through level-order positions and random edges through indices. The app-local reference creates a new outer list and a new pair for every non-null entry, retaining null slots and immutable index values. This is the serialization-level counterpart of allocating independent nodes while preserving all relationships; the platform-native artifact performs the actual object-graph construction.

## Complexity detail
Each of the $N$ nodes is allocated once, pushed at most once, and processed once. Examining its three pointer fields is constant work, so native cloning takes $O(N)$ time. The identity map, work stack, and $N$ new nodes use $O(N)$ space. Copying the encoded app representation also visits and allocates each position once, giving the same bounds.

## Alternatives and edge cases
- **Two-pass tree traversal:** First clone only the child structure and build an original-to-copy map; then traverse again to assign every random pointer. This is also $O(N)$ time and space, but requires two coordinated passes.
- **Recursive memoized DFS:** Create and memoize a copy before recursively cloning its three outgoing pointers. It is concise and cycle-safe with memoization, but a height-1000 tree can approach Python's recursion limit.
- **Clone child edges without a map:** This copies the binary-tree shape but cannot translate arbitrary random targets and may leave pointers into the original tree.
- **Match nodes by value:** Values need not be unique, so value-based lookup can connect a random edge to the wrong node.
- **Serialized equality alone:** Matching `[value, random_index]` output proves relationship equivalence but not object independence; the native solution must allocate distinct `NodeCopy` instances.
- **Empty tree:** Return null, represented by an empty app-local encoding.
- **Null random pointers:** Preserve them as null.
- **Self-random pointer:** The clone points to itself through the previously recorded mapping.
- **Random cycle:** Memoization prevents repeated allocation and preserves the cycle among copied nodes.
- **Cross-subtree pointer:** The target clone is found by identity regardless of child traversal order.
- **Duplicate values:** Identity-map keys distinguish nodes even when all values match.
- **Sparse child structure:** Null level-order slots remain null and do not become nodes.
