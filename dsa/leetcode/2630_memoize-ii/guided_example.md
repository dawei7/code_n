# Guided Example: Memoize II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"fnName": "sum", "calls": [[2, 2], [2, 2], [1, 2]], "callPlan": null}`
- **Required output:** `{"lastValue": 3, "callCount": 2}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a function `fn`, return a **memoized** version of that function.

The objective is to compute `{"lastValue": 3, "callCount": 2}` from `{"fnName": "sum", "calls": [[2, 2], [2, 2], [1, 2]], "callPlan": null}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: General arguments require identity-aware keys

Unlike a numeric-only memoizer, this function may receive values of any type. Two object arguments count as identical only when they are the same reference under `===`.

Serialization is therefore not safe:

- two distinct empty objects both stringify as `"{}"` but are not identical;
- the same object reference must hit the same cache path;
- argument order and argument count must remain distinct.

The solution represents an argument tuple as a path through nested `Map` objects. Each path edge is keyed by one actual argument value, so JavaScript's map-key identity semantics do the matching.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"fnName": "sum", "calls": [[2, 2], [2, 2], [1, 2]], "callPlan": null}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The nested maps form a trie of argument sequences

`root` is a `Map` representing the empty argument prefix.

For arguments $(a_0,a_1,\ldots,a_{k-1})$, the wrapper walks:

$$
\texttt{root}
\xrightarrow{a_0}
M_1
\xrightarrow{a_1}
M_2
\cdots
\xrightarrow{a_{k-1}}
M_k.
$$

If an edge does not exist, `node.set(arg, new Map())` creates the next map. Tuples sharing a prefix share the corresponding initial maps.

For example, tuples `(objectA, 1)` and `(objectA, 2)` share the edge for `objectA` and diverge at their second arguments. Tuple `(objectB, 1)` begins on a different root edge if `objectB !== objectA`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `root` is a `Map` representing the empty argument prefix.

F... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Store the result at the terminal node

After every argument has been consumed, `node` represents exactly that full tuple. The solution needs a marker key that cannot be confused with another argument edge.

`const resultKey = Symbol('result')` creates a unique symbol held privately inside the closure. The terminal map stores the cached value under that symbol.

Even if a caller supplies another symbol with the same description, it has different identity. The closure's symbol is never exposed, so user inputs cannot intentionally reproduce it.

This design also distinguishes a tuple from its prefix. A result for one argument is stored at the map reached after one edge, while a two-argument tuple continues through a second edge from that same node.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"lastValue": 3, "callCount": 2}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"fnName": "sum", "calls": [[2, 2], [2, 2], [1, 2]], "callPlan": null}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"lastValue": 3, "callCount": 2}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **`JSON.stringify(args)`:** Incorrect for unrest:** - **`JSON.stringify(args)`:** Incorrect for unrestricted objects because distinct references can serialize identically.
- **Linear list of prior tuples:** Preserves identity but may require $O(ua)$ comparisons per call.
- **Weak-map hybrid:** Can allow object-key paths to be garbage-collected, but primitive keys still require ordinary maps and implementation becomes more complex.
- **Same object reused:** It follows the same map edge and produces cache hits.
- **Structurally equal new objects:** Their references differ, so they correctly follow different paths.
- **Argument order:** Each position is a separate trie level, so `(a,b)` differs from `(b,a)`.
- **Different arity with common prefix:** Results live at different terminal nodes or marker positions.
- **Zero arguments:** The cached result is stored directly on the root.
- **Falsy or undefined result:** Marker membership prevents recomputation.
- **Receiver-dependent function:** `this` is forwarded for execution but not included in the cache key, consistent with the stated argument-only identity contract.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(a)$. Let $a$ be the number of arguments in one call. The wrapper performs one expected $O(1)$ map operation per argument and one terminal lookup, for expected $O(a)$ cache-navigation time, plus the cost of `fn` on a miss.
- **Auxiliary Space Complexity:** $O(ua)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
