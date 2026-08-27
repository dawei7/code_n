# Guided Example: Immutability Helper

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"obj": {"a": 1, "nested": {"b": 2}}, "mutations": [[]]}`
- **Required output:** `[{"a": 1, "nested": {"b": 2}}]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Creating clones of immutable objects with minor alterations can be a tedious process. Write a class `ImmutableHelper` that serves as a tool to help with this requirement. The constructor accepts an immutable object `obj` which will be a JSON object or array.

The objective is to compute `[{"a": 1, "nested": {"b": 2}}]` from `{"obj": {"a": 1, "nested": {"b": 2}}, "mutations": [[]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Provide mutation syntax without mutating the base

`ImmutableHelper` stores the original JSON object in `this.obj`. Each call to `produce` gives the mutator a proxy that appears writable, but writes are redirected into lazily created shallow copies.

The key optimization is structural sharing. A small edit deep in the object should copy only:

- the container that directly changes;
- every ancestor container needed to connect that changed container back to the root.

Unchanged sibling objects and arrays remain shared with the original because they are immutable from the mutator's perspective.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"obj": {"a": 1, "nested": {"b": 2}}, "mutations": [[]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Create fresh draft state for every production

Each `produce` call creates a root state whose `base` is `this.obj`.

A state stores:

- `base`, the original container represented by this draft node;
- `copy`, initially `null` and later a shallow writable copy;
- `parent` and `parentKey`, which locate this node inside its parent;
- `children`, a map caching draft states for accessed nested containers;
- `proxy`, the object exposed to mutator code.

These states belong only to the current call. A later `produce` begins again from the same original object, so previous produced changes do not accumulate.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Each `produce` call creates a root state whose `base` is `th... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Read from the base until a copy exists

The proxy's `get` trap chooses:

`state.copy === null ? state.base : state.copy`.

Before any write to that container, reads come directly from the immutable base. After its first write, reads come from the copy and therefore observe the mutator's changes.

This distinction is essential for code such as `proxy.val = proxy.val + 1`: the right side reads the current value, and the later read sees the assigned value.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[{"a": 1, "nested": {"b": 2}}]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"obj": {"a": 1, "nested": {"b": 2}}, "mutations": [[]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[{"a": 1, "nested": {"b": 2}}]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Deep-clone before every mutator:** Simple and :** - **Deep-clone before every mutator:** Simple and correct, but copies the entire object even for one small edit or no edit.
- **Mutate then restore the original:** Fragile in the presence of exceptions and aliases, and it violates immutability during execution.
- **Eagerly proxy and clone every node:** Preserves behavior but loses lazy work proportional to actual access and change.
- **No writes:** Returns the exact original object reference.
- **Top-level write:** Copies only the root container.
- **Deep write:** Copies the changed container and each ancestor path, while sharing siblings.
- **Multiple writes to one container:** Reuse its first shallow copy.
- **Arrays:** `slice` preserves element order and length while creating a writable container copy.
- **New primitive key:** The set trap adds it to the copied object without touching the base.
- **Null and primitives:** Returned directly because no deeper mutation is possible.
- **Repeated `produce` calls:** Each starts from `this.obj`, so results are independent.
- **Contract restrictions:** Deletion, mutating array methods, and assigning new object values are intentionally outside the supported mutator behavior.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(a+c)$. Let $a$ measure draft property accesses and created proxy states, and let $c$ be the total number of array elements and object properties copied across containers that become changed. Proxy/map work is expected $O(a)$, while shallow copying costs $O(c)$. Total time is $O(a+c)$.
- **Auxiliary Space Complexity:** $O(c)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
