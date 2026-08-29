# Guided Example: Map Sum Pairs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["MapSum", "insert", "sum", "insert", "sum"], "arguments": [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]}`
- **Required output:** `[null, null, 3, null, 5]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design a map that allows you to do the following:

The objective is to compute `[null, null, 3, null, 5]` from `{"operations": ["MapSum", "insert", "sum", "insert", "sum"], "arguments": [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Store each prefix's answer inside a trie

A `sum(prefix)` query asks for all keys beginning with the same character sequence. In a trie, all such keys pass through the node representing that prefix.

The exact implementation stores an aggregate `val` at every non-root trie node:

`node.val = sum of the current values of all inserted keys that pass through this node`.

With this invariant, a prefix query only has to follow its characters and return the aggregate at the final node. It does not traverse all descendant keys during the query.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["MapSum", "insert", "sum", "insert", "sum"], "arguments": [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Trie structure

Each node has:

- a 26-element `children` array for lowercase letters;
- an integer `val` for the prefix aggregate.

Character `c` maps to `ord(c) - ord("a")`. The source guarantees lowercase English letters, so every index is between zero and twenty-five.

A path from the trie root spells a prefix. Several keys with the same beginning share those nodes and therefore contribute to the same aggregates.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why overwriting a key needs a delta

`insert(key, val)` overrides the old value when the key already exists. Simply adding the new `val` along the path would double-count the old contribution.

The separate dictionary `d` stores the current exact value for every full key. The update amount is:

`x = new_value - old_value`.

The code obtains the old value as `d[key]`. Because `d` is a `defaultdict(int)`, a never-inserted key has old value zero.

After computing `x`, it stores the new full-key value in `d` and adds only `x` to every trie node on the key's path.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, null, 3, null, 5]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["MapSum", "insert", "sum", "insert", "sum"], "arguments": [[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, null, 3, null, 5]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Brute-force dictionary scan:** Store full key-value pairs and test `key.startswith(prefix)` for every query. Insert is simple, but a query can inspect every key and character.
- **Prefix hash map:** During insertion, update a hash-map total for every prefix using the same delta. Queries become expected `O(P)` to hash the prefix or effectively constant after string hashing, but repeated prefix strings consume storage.
- **Trie with descendant traversal at query time:** Store values only at terminal nodes and sum descendants for each query. This makes queries proportional to the matching subtree instead of prefix length.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(IK + QP)$. Let `K` be a key length and `P` a queried prefix length.
- **Auxiliary Space Complexity:** $O(IK)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
