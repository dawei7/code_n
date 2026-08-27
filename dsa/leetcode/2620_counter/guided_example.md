# Guided Example: Counter

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 10, "calls": ["call", "call", "call"]}`
- **Required output:** `[10, 11, 12]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `n`, return a `counter` function. This `counter` function initially returns `n` and then returns 1 more than the previous value every subsequent time it is called (`n`, $n + 1$, $n + 2$, etc).

The objective is to compute `[10, 11, 12]` from `{"n": 10, "calls": ["call", "call", "call"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A returned function needs persistent private state

`createCounter(n)` finishes before the returned counter is called. Nevertheless, each future call must remember the value left by the previous call.

JavaScript closures provide exactly this behavior. A function retains access to variables from the lexical environment in which it was created, even after the outer function has returned.

The inner anonymous function closes over parameter `n`. That binding becomes the counter's private mutable state.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 10, "calls": ["call", "call", "call"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand what the outer call creates

Calling `createCounter(10)` performs two conceptual actions:

1. create a lexical binding `n` initialized to ten;
2. create and return an inner function that references that binding.

Because the returned function still needs `n`, JavaScript keeps the binding alive. It is not copied anew on every counter call, and it is not discarded when `createCounter` returns.

The caller receives only the function, not direct access to the enclosed variable. This gives simple encapsulation: the sequence can advance through calls, but outside code cannot normally assign the private `n` binding directly.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Calling `createCounter(10)` performs two conceptual actions:... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Postfix increment returns before advancing

The function body is:

`return n++;`

The postfix increment operator has two linked effects:

- the expression's value is the old value of `n`;
- the stored binding is then incremented by one.

Therefore, with initial $n=10$:

- first call evaluates to ten, then stores eleven;
- second call evaluates to eleven, then stores twelve;
- third call evaluates to twelve, then stores thirteen.

This order exactly matches the requirement that the first result be the supplied starting value.

Using prefix increment `++n` without adjusting initialization would be wrong because the first call would return $n+1$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[10, 11, 12]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 10, "calls": ["call", "call", "call"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[10, 11, 12]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit local state variable:** Copy `n` into:** - **Explicit local state variable:** Copy `n` into `let current = n` and return `current++`; behavior and complexity are the same.
- **Increment before return:** Initialize to $n-1$, then use prefix increment. This works but is less direct.
- **Class instance:** A class with a field and method models the state but adds unnecessary syntax for one operation.
- **Global variable:** Incorrect because separately created counters would interfere.
- **Negative start:** Postfix increment naturally produces the required increasing sequence through zero.
- **Zero calls:** The closure is created, but its state is never changed or observed.
- **Multiple counters:** Each factory call captures a separate binding.
- **Extra call arguments:** They are ignored and do not affect state.
- **Prefix versus postfix:** `n++` returns the old value; `++n` would return the incremented value.
- **Encapsulation:** The captured binding is not exposed as a writable public object property.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Creating a counter allocates one function and one captured numeric binding, so creation takes $O(1)$ time and $O(1)$ space.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
