# Guided Example: Design In-Memory File System

We trace the step-by-step hierarchical prefix tree (Trie) directory representation, path tokenization along delimiter boundaries (`path.split('/')`), recursive directory creation (`mkdir`), file node differentiation (`isFile`, `name`, `content`), lexicographically sorted directory listing (`ls`), and content append/read mechanics on representative file system operations:

- **Input:**
  ```text
  FileSystem fs = new FileSystem()
  fs.ls("/")
  fs.mkdir("/a/b/c")
  fs.addContentToFile("/a/b/c/d", "hello")
  fs.ls("/")
  fs.readContentFromFile("/a/b/c/d")
  ```
- **Required outputs:**
  - `fs.ls("/")` $\implies$ `[]`
  - `fs.mkdir("/a/b/c")` $\implies$ `null`
  - `fs.addContentToFile("/a/b/c/d", "hello")` $\implies$ `null`
  - `fs.ls("/")` $\implies$ `["a"]`
  - `fs.readContentFromFile("/a/b/c/d")` $\implies$ `"hello"`
- **Trie-Based Hierarchical Architecture:**
  - Each filesystem entity (directory or file) is a node in an $N$-ary prefix tree (Trie):
    - `children`: Hash map mapping child component names to child Trie nodes.
    - `isFile`: Boolean flag indicating whether the node is a regular file (`true`) or a directory (`false`).
    - `name`: String storing the base filename if `isFile == true`.
    - `content`: Array/buffer of strings holding the accumulated file text.
  - Path resolution:
    - Path `"/a/b/c"` splits into components: `["", "a", "b", "c"]`.
    - Skipping the empty root prefix yields sequence `["a", "b", "c"]`.
    - Traversal steps: Root $\to$ child `"a"` $\to$ child `"b"` $\to$ child `"c"`.
- **Step-by-Step Operation Trace:**
  - **Operation 1: `fs.ls("/")`:**
    - Target: Root directory `/`.
    - Inspect root node:
      - `isFile = false` (directory).
      - `children = {}` (empty).
    - Return sorted keys:
      $$
      \text{Result} = \mathbf{[]}
      $$
  - **Operation 2: `fs.mkdir("/a/b/c")`:**
    - Target path: `"/a/b/c"`.
    - Token components: `["a", "b", "c"]`.
    - **Traverse/Create component `"a"`:**
      - `"a"` not in `root.children` $\implies$ instantiate new directory node `"a"`.
      - Advance pointer to node `"a"`.
    - **Traverse/Create component `"b"`:**
      - `"b"` not in `node_a.children` $\implies$ instantiate new directory node `"b"`.
      - Advance pointer to node `"b"`.
    - **Traverse/Create component `"c"`:**
      - `"c"` not in `node_b.children` $\implies$ instantiate new directory node `"c"`.
      - Advance pointer to node `"c"`.
    - Target directory `/a/b/c` created with all intermediate parent folders!
    - Return: `null`.
  - **Operation 3: `fs.addContentToFile("/a/b/c/d", "hello")`:**
    - Path components: `["a", "b", "c", "d"]`.
    - Traverse `root -> "a" -> "b" -> "c"` (all exist from previous step).
    - At node `"c"`, child `"d"` does not exist:
      - Create child node `"d"`.
      - Mark `isFile = true`.
      - Record base name: `name = "d"`.
    - Append content to node `"d"`'s buffer:
      $$
      \text{content} = [\text{"hello"}]
      $$
    - Return: `null`.
  - **Operation 4: `fs.ls("/")`:**
    - Target: Root directory `/`.
    - Inspect root node:
      - `isFile = false`.
      - `children` contains key `"a"`.
    - Return sorted list of children keys:
      $$
      \text{Result} = \mathbf{["a"]}
      $$
  - **Operation 5: `fs.readContentFromFile("/a/b/c/d")`:**
    - Navigate down path: `root -> "a" -> "b" -> "c" -> "d"`.
    - Node `"d"` found:
      - `isFile == true`.
      - Concatenate content segments: `''.join(["hello"])`.
    - Return:
      $$
      \mathbf{\text{"hello"}}
      $$
- **Listing a Specific File Path (`fs.ls("/a/b/c/d")`):**
  - Node `"d"` has `isFile == true`.
  - File listing rule: Return a list containing **only the file's own name**:
    $$
    [\text{"d"}]
    $$
- **Appending Additional Content:**
  - Calling `fs.addContentToFile("/a/b/c/d", " world")`:
    - Buffer becomes `["hello", " world"]`.
    - Subsequent read returns `"hello world"`.

This instance demonstrates filesystem namespace modeling via directory tries, mathematically proves why path segmentation reduces filesystem queries to linear string component lookups, and derives $O(L)$ runtime per operation where $L$ is path depth.

---

## 1. Instance & Teaching Goal

Implement an in-memory file system with four core primitives:
1. `ls(path)`: If path is a file, return `[file_name]`. If directory, return all contained file and folder names in lexicographical order.
2. `mkdir(path)`: Create directory and any missing intermediate directories.
3. `addContentToFile(filePath, content)`: Create file if absent, append text to existing content.
4. `readContentFromFile(filePath)`: Return entire file content as a string.

```text
Filesystem Hierarchy:
  / (root)
  └── a/
      └── b/
          └── c/
              └── d (file, content: "hello")

Actions:
  ls("/") -> ["a"]
  ls("/a/b/c/d") -> ["d"]
  readContentFromFile("/a/b/c/d") -> "hello"
```

### The $N$-ary Path Prefix Tree (Trie)
- A filesystem is naturally a tree where each node represents a directory or file.
- The path separator `/` delineates edges in the tree.
- By structuring nodes with `children: dict[str, TrieNode]`:
  - Path lookups take time proportional only to the number of path segments, completely independent of total filesystem size!

---

## 2. Conceptual Foundation & Invariants

### 1. Node Structure:
- `children`: dictionary mapping child names to child nodes.
- `isFile`: boolean flag.
- `name`: filename string (set when `isFile == True`).
- `content`: list of string chunks (for $O(1)$ amortized appends).

### 2. Path Tokenization:
Given `path = "/a/b/c"`:
- `path.split('/')` produces `["", "a", "b", "c"]`.
- The traversal iterates through `ps[1:]` = `["a", "b", "c"]`.

### 3. Listing Contract:
- If target node is a **file**:
  $$
  \text{return } [node.name]
  $$
- If target node is a **directory**:
  $$
  \text{return sorted}(node.children.keys())
  $$

> **Hierarchical Namespace Invariant.** Every path corresponds to a unique path in the Trie starting from the root node `/`, preserving strict folder containment without dangling references.

---

## 3. Step-by-Step Worked Execution

We trace the sample operations:

---

### Step 1: Initialize System
- `root` node created: `isFile = False, children = {}`.

---

### Step 2: `ls("/")`
- Root has no children.
- Returns `[]`.

---

### Step 3: `mkdir("/a/b/c")`
- At `/`: create child `"a"`.
- At `"a"`: create child `"b"`.
- At `"b"`: create child `"c"`.
- All marked with `isFile = False`.

---

### Step 4: `addContentToFile("/a/b/c/d", "hello")`
- Traverse `"a" \to "b" \to "c"`.
- Under `"c"`: create child `"d"`.
- Mark `"d"`: `isFile = True, name = "d"`.
- Append `"hello"` to `"d".content`.

---

### Step 5: `ls("/")`
- Root has child `"a"`.
- Returns `["a"]`.

---

### Step 6: `readContentFromFile("/a/b/c/d")`
- Locate `"d"`.
- Join content: `"".join(["hello"]) = "hello"`.

---

## 4. Complete Execution Trace

| Command | Path Target | Path Segments | Node State After Operation | Return Value |
|:---:|:---:|:---:|:---:|:---:|
| `ls` | `"/"` | `[]` | Root empty | `[]` |
| `mkdir` | `"/a/b/c"` | `["a", "b", "c"]` | Chain `a -> b -> c` created | `null` |
| `addContentToFile` | `"/a/b/c/d"` | `["a", "b", "c", "d"]` | Node `d` file created, content `"hello"` | `null` |
| `ls` | `"/"` | `[]` | Root has child `a` | **`["a"]`** |
| `readContentFromFile` | `"/a/b/c/d"` | `["a", "b", "c", "d"]` | Node `d` read | **`"hello"`** |

---

## 5. Boundary Cases & Failure Modes

- **Root Directory (`"/"`):** `search("/")` immediately returns `self.root` without segment traversal.
- **Deeply Nested Paths (`/x/y/z/w/v`):** Intermediate folders automatically created if missing.
- **Multiple Appends to Same File:** Appends accumulate into `content` list without overwriting.
- **Listing a File:** Explicitly returns `[file_name]`, NOT file content or empty list.

---

## 6. Traps & Common Anti-Patterns

- **Using a Flat Hash Map of Full Paths:** Storing `paths["/a/b/c/d"] = content` makes `ls` require scanning all keys in the filesystem, taking $O(N)$ time per list command. A Trie enables local $O(\text{children})$ listing.
- **Concatenating Strings with `+=` on Every Write:** String concatenation in Python copies memory ($O(C^2)$ for repeated appends). Appending string chunks to a list and calling `''.join()` upon read takes $O(C)$ total time.
- **Not Handling `ls` on Files Correctly:** Calling `ls` on `/a/b/c/d` must return `["d"]`, not `["hello"]` and not `[]`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $D$ be the depth of the path and $L$ be the length of the path string.
  - `mkdir`: $\mathcal{O}(D + L)$ string splitting and dictionary lookups.
  - `addContentToFile`: $\mathcal{O}(D + L + C)$ where $C$ is content length.
  - `readContentFromFile`: $\mathcal{O}(D + L + C)$ to traverse and join strings.
  - `ls`: $\mathcal{O}(D + L + K \log K)$ where $K$ is the number of files/folders in the directory.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(\text{Total path lengths} + \text{Total file content bytes})$ stored in the Trie.
