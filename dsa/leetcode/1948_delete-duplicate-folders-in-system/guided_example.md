# Guided Example: Delete Duplicate Folders in System

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"paths": [["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]}`
- **Required output:** `[["d"], ["d", "a"]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Due to a bug, there are many duplicate folders in a file system. You are given a 2D array `paths`, where $\text{paths}[i]$ is an array representing an absolute path to the $i^{\text{th}}$ folder in the file system.

The objective is to compute `[["d"], ["d", "a"]]` from `{"paths": [["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Build the file system as a trie

Each path shares prefixes with other paths, so a trie is the natural tree representation. The virtual `root` represents `/`. Its `children` dictionary maps a folder name to the corresponding child node.

For each input path, the code walks its names from the root. `children` is a `defaultdict(Trie)`, so accessing `cur.children[name]` creates a new node when the name is absent. The subsequent `is null` check is therefore redundant in this exact source—the access already guarantees a `Trie` object—but it does not change behavior.

When insertion finishes, every physical folder appears exactly once in the trie, and its children represent its immediate subfolders.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"paths": [["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Describe a folder by its complete child structure

Two folders are identical based on their nonempty set of named subfolders and all descendant structure. The folder's own name does not matter; only each child's name and structure matters.

The first DFS is postorder. It recursively obtains every child's serialization, wraps it with the child name as `name(serialization)`, sorts these child pieces, and concatenates them. Sorting is essential because dictionary insertion order is not part of folder identity. Two folders with the same children inserted in different orders must receive the same serialization.

Folder names contain only lowercase letters, while parentheses provide structural delimiters, so representations such as `a(b())` cannot be confused with a different arrangement of names and descendants.

A leaf returns the empty string immediately and is not registered in `g`. This precisely implements the “same non-empty set of subfolders” condition: empty folders are not duplicates merely because both have no children.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Mark every occurrence of a repeated nonempty structure

`g` maps each previously unseen nonempty serialization to one representative node. When the same serialization appears again, the code marks both the current node and that representative as deleted.

If a third or later copy appears, `g[s]` still refers to the first representative, which is already marked. The assignment marks the new node as well. Thus every occurrence of a structure seen at least twice is marked, not just one pair.

The DFS computes all serializations before the deletion traversal begins. Marked children remain part of their ancestors' serialization during this phase. This preserves the required one-time behavior: folders that would become identical only after deletions are not newly marked.

The virtual root is serialized too, but it cannot share a serialization with a proper contained subtree: its represented child forest strictly contains more nodes than any structurally identical proper descendant could. It serves only as the traversal entry and is never added to the returned paths.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[["d"], ["d", "a"]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"paths": [["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[["d"], ["d", "a"]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Assign integer subtree IDs:** Intern sorted tuples of child-name and child-ID pairs instead of retaining long strings. This avoids large serialization copies while preserving structural equality.
- **Delete while serializing:** This is wrong because ancestors must be compared using the original structure; deletion runs only once.
- **Treat leaves as duplicates:** The definition requires a nonempty subfolder set, so empty serializations must not be counted.
- **Same structure under different folder names:** The node's own name is excluded from its serialization, so such folders are correctly considered identical.
- **Different child insertion order:** Sorting child pieces gives the same canonical representation.
- **Third duplicate:** The representative remains in `g`, and every later matching node is marked on discovery.
- **Duplicate ancestor:** The second DFS stops at it, automatically removing all descendants whether or not they are independently marked.
- **Folders become equal after deletion:** They remain because all markings were completed before anything was skipped.
- **No duplicate nonempty structures:** No `deleted` flag is set, and all original paths are collected.
- **Mutable path list:** Appending `path[:]` stores a snapshot; appending `path` itself would corrupt earlier answers during backtracking.
- **Input parent guarantee:** Every nonroot folder's parent path exists, so trie insertion represents a complete folder hierarchy.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(F\log F)$. Let $F$ denote the total input size measured across folder-name occurrences, and let $A$ be the total length of all serialization strings stored across nodes.
- **Auxiliary Space Complexity:** $O(F)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
