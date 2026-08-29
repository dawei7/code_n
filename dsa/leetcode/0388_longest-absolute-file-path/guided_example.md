# Guided Example: Longest Absolute File Path

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"input": "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"}`
- **Required output:** `20`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Suppose we have a file system that stores both files and directories. An example of one system is represented in the following picture:

The objective is to compute `20` from `{"input": "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The serialization gives depth, not full paths

Each newline-separated entry supplies two pieces of information:

- its leading tab count is its depth in the hierarchy;
- the remaining characters are its file or directory name.

Depth zero is at the root. An entry at depth one is inside the most recent directory at depth zero, an entry at depth two is inside the most recent directory at depth one, and so on. The serialization does not include `/` separators because tabs and line order already encode parent relationships. The algorithm must reconstruct only the path lengths, not the path strings themselves.

The exact solution scans `input` with one index `i` and maintains a stack `stk`. Every stack entry is the cumulative absolute-path length of a directory on the current ancestor chain. If the stack contains values for depths `0` through `d - 1`, then `stk[-1]` is the path length to the parent of an entry at depth `d`.

Storing lengths rather than strings avoids repeated concatenation and makes each new path length a constant-time arithmetic calculation once the current name has been read.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"input": "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Parsing one entry’s depth

At the beginning of an entry, `ident` starts at zero. The loop consumes leading tab characters, incrementing both `ident` and the input index. After this loop, `ident` is exactly the entry’s depth, and `i` points to the first character of its nonempty name.

Tabs are indentation markers only when they appear at the beginning of an entry. The input grammar uses them that way, so the parser does not need to consider a tab as part of a name. The positive-name-length guarantee ensures that a valid line does not end immediately after its tabs.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Parsing the name and recognizing files

The variables `cur` and `isFile` begin as zero and `false`. The next loop advances until a newline or the end of the string. It increments `cur` for every name character, so at first `cur` is the name length alone. If any character is `.`, it sets `isFile = true`.

This dot test relies on the stated representation: file names have `name.extension`, whereas directory names consist only of letters, digits, and spaces. Under that grammar, containing a dot is equivalent to being a file. The algorithm does not need to validate where the dot occurs or split the extension because only total path length matters.

After the name loop, `i += 1` skips the newline. When the final entry ends at the end of `input`, `i` is already `n`; incrementing once to `n + 1` is harmless because the outer condition `i < n` then fails.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `20` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"input": "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `20` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Map from depth to cumulative length:** Store the latest path length for each depth in a dictionary or array. Each entry can read its parent from `depth - 1` and overwrite its own depth. This is also $O(n)$ time and $O(d)$ space; the stack more directly represents the active ancestor chain.
- **Build complete path strings:** Concatenating parent paths and names is easy to visualize but stores and repeatedly copies characters that the answer never returns. Keeping only lengths is more memory-efficient.
- **Split into lines first:** `input.split('\n')` simplifies entry parsing but allocates a list and copies or references all line substrings, using $O(n)$ extra space. The exact pointer scan avoids that allocation and retains the $O(d)$ auxiliary bound.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of the serialized input and $d$ be the maximum directory depth.
- **Auxiliary Space Complexity:** $O(d)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
