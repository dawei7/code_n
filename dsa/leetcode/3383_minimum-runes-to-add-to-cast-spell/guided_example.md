# Guided Example: Minimum Runes to Add to Cast Spell

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 6, "crystals": [0], "flowFrom": [0, 1, 2, 3], "flowTo": [1, 2, 3, 0]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Alice has just graduated from wizard school, and wishes to cast a magic spell to celebrate. The magic spell contains certain **focus points** where magic needs to be concentrated, and some of these focus points contain **magic crystals** which serve as the spell's energy source. Focus points can be linked through **directed runes**, which channel magic flow from one focus point to another.

The objective is to compute `2` from `{"n": 6, "crystals": [0], "flowFrom": [0, 1, 2, 3], "flowTo": [1, 2, 3, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**First remove every focus point already powered by crystals.** Build directed adjacency list `g` from each `flowFrom` to matching `flowTo`. Every crystal node begins with `vis[x]=1` and enters a queue. `bfs` follows outgoing runes, marking every focus point that can already receive magic.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 6, "crystals": [0], "flowFrom": [0, 1, 2, 3], "flowTo": [1, 2, 3, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

After this traversal, nodes marked one require no new rune. Only the subgraph induced by `vis == 0` remains relevant.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Why one new rune can power an entire forward region.** If Alice adds a rune from any powered point into an unpowered node `u`, then `u` and every node reachable from it become powered. The question is therefore the minimum number of starting nodes whose forward-reachable sets cover the remaining directed graph.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 6, "crystals": [0], "flowFrom": [0, 1, 2, 3], "flowTo": [1, 2, 3, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Explicit Kosaraju or Tarjan SCCs:** Contract components and count unpowered sources directly; it is clearer but needs more machinery.
- **Iterative DFS:** It preserves finishing order while avoiding recursion-limit failure.
- **Add a rune to every unpowered node:** It is valid but ignores forward reachability and is not minimal.
- **All nodes crystal-reachable:** `seq` is empty and answer is zero.
- **Unpowered directed chain:** One rune at its source powers the whole chain.
- **Reverse chain selection:** Choosing the sink first would waste starts, which finishing order prevents.
- **Unpowered cycle:** One selected node powers the entire SCC.
- **Isolated node:** It contributes exactly one.
- **Duplicate crystal entries:** They can cause redundant initial queue pops but do not change reachability.
- **Edges into powered nodes:** DFS skips state-one destinations because they need no additional coverage.
- **No explicit added-rune endpoints:** The method returns only the minimum count.
- **State meanings:** Zero is unseen/unpowered, two is DFS-discovered/unpowered, and one is powered or covered.
- **Manifest wording:** SCCs justify the algorithm but are not explicitly contracted.
- **Required imports:** `deque`, `Deque`, and `List` must be available.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+m)$. Building the graph and all BFS/DFS traversals touch each node and directed edge only a constant number of times, so mathematical time is $O(n+m)$, where $m$ is the rune count.
- **Auxiliary Space Complexity:** $O(n + m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
