# Guided Example: Nested Array Generator

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [[[6]], [1, 3], []]}`
- **Required output:** `[6, 1, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a **multi-dimensional array** of integers, return a generator object which yields integers in the same order as **inorder traversal**.

The objective is to compute `[6, 1, 3]` from `{"arr": [[[6]], [1, 3], []]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Flatten lazily rather than building a flat array

The required order is recursive left-to-right traversal:

- visit each item of the current array in order;
- yield an integer immediately;
- recurse into a nested array at the position where it occurs.

The exact generator reproduces this order with an explicit stack. It yields one integer at a time and never constructs a complete flattened copy.

This is especially important when the consumer stops early: unvisited portions of the nested structure require no work.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [[[6]], [1, 3], []]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: A stack frame represents suspended array traversal

Each frame has:

- `array`: the current nested array;
- `index`: the next position in that array to inspect.

The stack begins with one frame for the outer input at index zero.

The top frame is always the array whose traversal is currently active. Frames below it represent parent arrays paused while a nested child is explored.

This explicitly models the call stack that a recursive DFS would otherwise use.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Each frame has:

- `array`: the current nested array;
- `ind... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Finish and pop exhausted arrays

At the beginning of each loop iteration, the code reads the top frame.

If:

`frame.index === frame.array.length`,

that array has no remaining values. The frame is popped, and the loop continues with its parent.

For the root frame, popping it empties the stack and terminates the generator.

An empty nested array is handled immediately: its new frame has index zero and length zero, so the next iteration pops it without yielding anything.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[6, 1, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [[[6]], [1, 3], []]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[6, 1, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Recursive generator with `yield*`:** Elegant b:** - **Recursive generator with `yield*`:** Elegant but risks call-stack overflow at depth $10^5$.
- **`flat(Infinity)`:** Simple but creates a full flattened array and defeats the no-copy follow-up.
- **Stack of raw values in reverse order:** Also iterative, but may push many siblings at once and use width-dependent rather than depth-only space.
- **Empty root array:** Its only frame pops and the generator finishes without yielding.
- **Empty nested array:** It contributes no integers and traversal resumes at the parent.
- **Deep singleton nesting:** Stack grows with depth but avoids language recursion.
- **Several sibling arrays:** Each is fully traversed before the next sibling.
- **Early consumer stop:** Unrequested values are never visited.
- **Index increment timing:** It must occur before descent or yield to prevent duplication.
- **Input preservation:** Frames hold references and indices but never modify arrays.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the total number of integer leaves plus array entries/containers visited. Each array item is read once, each frame is pushed and popped once, so full traversal takes $O(N)$ time.
- **Auxiliary Space Complexity:** $O(d)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
