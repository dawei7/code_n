# Guided Example: Check if Object Instance of Class

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"fixture": {"value": "date-instance", "target": "Date"}}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a function that checks if a given value is an instance of a given class or superclass. For this problem, an object is considered an instance of a given class if that object has access to that class's methods.

The objective is to compute `true` from `{"fixture": {"value": "date-instance", "target": "Date"}}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use JavaScript's actual inheritance mechanism

JavaScript inheritance is based on prototype links. An object has access to methods placed on a constructor's `prototype` when that exact prototype object occurs somewhere in the object's prototype chain.

Therefore, checking whether `obj` is an instance of `classFunction` reduces to:

1. obtain the prototype chain appropriate for `obj`;
2. obtain `classFunction.prototype` as the target;
3. walk upward until the target is found or the chain ends.

This directly implements the problem's definition in terms of access to class methods and naturally handles subclasses.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"fixture": {"value": "date-instance", "target": "Date"}}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reject invalid inputs before reflection

The first condition is:

`obj == null || typeof classFunction !== "function"`.

The intentionally loose comparison `obj == null` is true for both `null` and `undefined` and false for ordinary values. Neither null nor undefined can be boxed into an object that exposes a useful class prototype for this contract, so the function returns false.

The second check ensures the proposed class is callable as a JavaScript function or class value. Without it, accessing its prototype as a class target would not represent a meaningful instance relationship. Inputs such as numbers, strings, objects, or undefined in the class position return false instead of causing misleading behavior.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first condition is:

`obj == null || typeof classFunctio... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Box primitive values

Ordinary `instanceof` reports `5 instanceof Number` as false because five is a primitive rather than a `Number` object. The problem deliberately wants true because JavaScript lets the primitive access `Number.prototype` methods through temporary boxing.

`Object(obj)` performs this boxing:

- a number becomes a temporary Number wrapper;
- a string becomes a String wrapper;
- a Boolean becomes a Boolean wrapper;
- a symbol or bigint receives its corresponding wrapper;
- an existing object is returned as an object.

Then `Object.getPrototypeOf(Object(obj))` obtains the first prototype in the relevant chain. For numeric five, that first prototype is `Number.prototype`, so the requested relationship can be found.

The code handles null and undefined before `Object(obj)` because their special coercion behavior should not be interpreted as boxing them into valid instances.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"fixture": {"value": "date-instance", "target": "Date"}}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Native `instanceof`:** Concise for objects, bu:** - **Native `instanceof`:** Concise for objects, but it rejects primitives such as five against `Number` and therefore does not meet this contract.
- **Compare `constructor` properties:** A constructor property can be overwritten or inherited and does not reliably prove prototype-chain membership.
- **Recursive prototype walk:** Correct but uses $O(h)$ call-stack space without improving clarity.
- **`null` and `undefined` object input:** Both return false before boxing.
- **Non-function class input:** It returns false rather than attempting an invalid class relationship.
- **Primitive number, string, or Boolean:** `Object(obj)` exposes the wrapper prototype required by the problem.
- **Subclass instance:** Walking the complete chain finds superclass prototypes.
- **Constructor passed as object:** A constructor function follows `Function.prototype`, not its own instance prototype.
- **Null-prototype object:** Its chain ends immediately and returns false.
- **Prototype identity:** Structurally similar prototype objects are not interchangeable; strict identity is required.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(h)$. Let $h$ be the number of prototype links from the boxed object to null. The loop examines at most $h$ prototypes, so time complexity is $O(h)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
