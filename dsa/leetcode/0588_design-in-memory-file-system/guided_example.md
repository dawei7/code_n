# Guided Example: Design In-Memory File System

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": [["mkdir", "/b"], ["mkdir", "/a"], ["mkdir", "/c"], ["ls", "/"]]}`
- **Required output:** `[["a", "b", "c"]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design a data structure that simulates an in-memory file system.

The objective is to compute `[["a", "b", "c"]]` from `{"operations": [["mkdir", "/b"], ["mkdir", "/a"], ["mkdir", "/c"], ["ls", "/"]]}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: The node fields

Every new `Trie` begins as a directory-like node:

- `name = null` because directories do not need their own name for current operations;
- `isFile = false`;
- `content = []`;
- `children = {}`.

Child names live as dictionary keys in the parent. A file additionally saves its own final name because `ls(filePath)` must return a one-element list containing that name.

File content is a list of fragments rather than one repeatedly concatenated string. `addContentToFile` appends a new content string in constant amortized list time. `readContentFromFile` performs one `''.join(...)` when the complete value is requested. This avoids copying the entire existing file on every append, which repeated immutable-string concatenation could do.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": [["mkdir", "/b"], ["mkdir", "/a"], ["mkdir", "/c"], ["ls", "/"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Walking or creating a path with `insert`

Absolute paths begin with `/`. Splitting `/a/b/c` on slash produces an initial empty component followed by `a`, `b`, and `c`, so the loop intentionally uses `ps[1:]`.

For every component `p`:



Existing nodes are reused; missing nodes are created. This behavior exactly supports `mkdir`, which must create all absent intermediate directories. At the end, `node.isFile = isFile` assigns the requested final type. If this is a file insertion, `node.name = ps[-1]` records the basename. The final node is returned so the caller can modify it immediately.

`mkdir(path)` simply calls `insert(path, false)`. `addContentToFile(filePath, content)` calls `insert(filePath, true)`, then appends `content` to the returned node’s fragment list. If the file already exists, traversal reaches the same node and preserves earlier fragments; if it is new, insertion creates the final node.

The contract guarantees valid operations and says a file’s parent directory exists. The general insertion routine would create missing intermediates anyway, but correctness does not depend on handling invalid file parents.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Finding an existing path with `search`

`search("/")` returns the root directly. For any other absolute path, it walks the same components through `children`. If a component is absent, it returns `null`.

The public contract says queried paths exist, so `null` is mainly defensive. `ls` turns it into an empty list; `readContentFromFile` assumes the found node is valid, as allowed by the contract.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[["a", "b", "c"]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": [["mkdir", "/b"], ["mkdir", "/a"], ["mkdir", "/c"], ["ls", "/"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[["a", "b", "c"]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

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
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let $L$ be the number of characters in a path, $P$ its number of components, $k$ the number of immediate children listed, $C$ the amount of file content processed, and $S$ the total stored state.
- **Auxiliary Space Complexity:** $O(S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
