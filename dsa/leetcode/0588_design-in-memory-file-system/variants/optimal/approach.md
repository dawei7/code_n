## General

A file system is naturally hierarchical. Every path component chooses one child inside the current directory, so a trie-like tree mirrors the domain:

- the root trie node represents `/`;
- each key in a node’s `children` dictionary is one immediate file or directory name;
- the mapped trie node represents that child;
- `isFile` distinguishes file nodes from directory nodes;
- `content` stores a file’s appended content fragments.

Using one node type for both files and directories makes path traversal uniform. The same dictionary lookup advances through either kind; the type flag matters only when interpreting the final node.

**The node fields**

Every new `Trie` begins as a directory-like node:

- `name = None` because directories do not need their own name for current operations;
- `isFile = False`;
- `content = []`;
- `children = {}`.

Child names live as dictionary keys in the parent. A file additionally saves its own final name because `ls(filePath)` must return a one-element list containing that name.

File content is a list of fragments rather than one repeatedly concatenated string. `addContentToFile` appends a new content string in constant amortized list time. `readContentFromFile` performs one `''.join(...)` when the complete value is requested. This avoids copying the entire existing file on every append, which repeated immutable-string concatenation could do.

**Walking or creating a path with `insert`**

Absolute paths begin with `/`. Splitting `/a/b/c` on slash produces an initial empty component followed by `a`, `b`, and `c`, so the loop intentionally uses `ps[1:]`.

For every component `p`:

```python
if p not in node.children:
    node.children[p] = Trie()
node = node.children[p]
```

Existing nodes are reused; missing nodes are created. This behavior exactly supports `mkdir`, which must create all absent intermediate directories. At the end, `node.isFile = isFile` assigns the requested final type. If this is a file insertion, `node.name = ps[-1]` records the basename. The final node is returned so the caller can modify it immediately.

`mkdir(path)` simply calls `insert(path, False)`. `addContentToFile(filePath, content)` calls `insert(filePath, True)`, then appends `content` to the returned node’s fragment list. If the file already exists, traversal reaches the same node and preserves earlier fragments; if it is new, insertion creates the final node.

The contract guarantees valid operations and says a file’s parent directory exists. The general insertion routine would create missing intermediates anyway, but correctness does not depend on handling invalid file parents.

**Finding an existing path with `search`**

`search("/")` returns the root directly. For any other absolute path, it walks the same components through `children`. If a component is absent, it returns `None`.

The public contract says queried paths exist, so `None` is mainly defensive. `ls` turns it into an empty list; `readContentFromFile` assumes the found node is valid, as allowed by the contract.

**Listing files and directories**

After searching:

- if the node is a file, `ls` returns `[node.name]`;
- if it is a directory, it sorts and returns `node.children.keys()`.

A directory listing includes only immediate children, not all descendants. Those immediate child keys already combine file names and directory names because the trie uses one namespace per directory, matching the guarantee that the same name will not occur twice in one directory.

Sorting happens at query time, so dictionary insertion order never affects the required lexicographic result. Listing the empty root initially sorts an empty key view and returns `[]`.

**Following the sample**

The fresh root has no children, so `ls("/")` is empty. `mkdir("/a/b/c")` creates node `a` under root, `b` under `a`, and `c` under `b`. Adding content to `/a/b/c/d` reaches or creates `d`, marks it as a file, saves name `d`, and appends `"hello"`.

The root’s only immediate child is `a`, so `ls("/")` returns `["a"]` rather than every nested name. Searching for `/a/b/c/d` reaches the file, and joining its one fragment returns `"hello"`. A later append of `" world"` would leave two fragments and reading would return `"hello world"`.

**Why the design is correct**

Maintain the invariant that each reachable trie node corresponds to exactly one absolute path, and its child dictionary contains exactly the immediate entries beneath that path. Construction establishes this for root. Each insertion step reuses the unique child for a name or creates exactly one, preserving the invariant down the path.

`mkdir` therefore makes every requested directory component reachable. File insertion reaches exactly the file path, marks that node, and appends fragments in call order, so joining them equals all supplied content concatenated chronologically. Search follows the unique component sequence and reaches exactly the named node.

For a file, the saved basename is the required listing. For a directory, child keys are exactly its immediate entries, and sorting gives lexicographic order. Each public operation consequently satisfies its contract while sharing one consistent representation.

## Complexity detail

Let $L$ be the number of characters in a path, $P$ its number of components, $k$ the number of immediate children listed, $C$ the amount of file content processed, and $S$ the total stored state.

Splitting a path costs $O(L)$, and traversing $P$ dictionary edges takes expected $O(P)$. `mkdir` and the path portion of file operations therefore cost $O(L+P)$ expected time. Appending a content object to the fragment list is amortized $O(1)$ after the input string already exists, while eventually storing/reading $C$ characters is naturally charged as $O(C)$.

Directory `ls` additionally copies/sorts $k$ names, taking $O(k\log k)$ comparisons plus output cost. File `ls` returns one name. Reading joins all stored fragments and takes $O(C)$ time for the file’s total content because the returned string must contain those characters.

All trie nodes, dictionary entries, names, and content fragments together occupy $O(S)$ space. A single traversal uses references and a split component list bounded by the path size. These operation-specific costs fit the manifest summary $O(P+k\log k+C)$ time and $O(S)$ total space, with path-character scanning understood as part of parsing.

## Alternatives and edge cases

- **Separate file and directory maps:** A directory node can keep one child-directory dictionary and one filename-to-content dictionary. Type checks become implicit, but traversal logic is split across two namespaces.
- **Ordered child map:** Maintaining names in sorted order can reduce listing sort work, but insertion becomes more expensive and Python’s ordinary dictionary plus query-time sorting is simpler at this scale.
- **Flat path map:** Store every absolute path as a key. Direct lookup is easy, but listing immediate children and creating hierarchical intermediates requires prefix parsing and extra indexing.
- **Repeated string concatenation:** Updating one immutable string with `old + content` can repeatedly copy growing files. Fragment lists defer copying until reading.
- **Root path:** `search("/")` must return root without trying to traverse an empty component.
- **Empty directory:** Its child dictionary is empty, so `ls` returns an empty list.
- **Listing a file:** Return only its basename, not its content or children.
- **Intermediate creation:** `mkdir` creates every missing component, not just the last directory.
- **Appending to an existing file:** `insert` reuses the file node, and `append` preserves all earlier fragments.
- **Lexicographic order:** Sorting dictionary keys at `ls` time is required; insertion order is irrelevant.
- **File/directory name collision:** The contract forbids identical names in one directory, allowing one unified child dictionary.
- **Valid-operation guarantee:** Reading assumes the path names a file. Robust production code might raise an explicit error for missing or wrong-type nodes.
- **Input mutation:** Operations mutate only the in-memory trie state, which is the intended persistent object behavior across method calls.
