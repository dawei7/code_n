# Guided Example: Calculator with Method Chaining

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"actions": ["Calculator", "add", "subtract", "getResult"], "values": [10, 5, 7]}`
- **Required output:** `8`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design a `Calculator` class. The class should provide the mathematical operations of addition, subtraction, multiplication, division, and exponentiation. It should also allow consecutive operations to be performed using method chaining. The `Calculator` class constructor should accept a number which serves as the initial value of `result`.

The objective is to compute `8` from `{"actions": ["Calculator", "add", "subtract", "getResult"], "values": [10, 5, 7]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Keep one mutable running result

The calculator represents a sequence of operations, so it needs state that survives from one method call to the next. The constructor stores the initial number in `this.result`. Every arithmetic method reads that current value, applies one operation, and writes the new value back to the same property.

There is no expression tree and no delayed evaluation. A chain is evaluated from left to right as ordinary JavaScript method calls, and each method immediately updates the shared calculator instance.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"actions": ["Calculator", "add", "subtract", "getResult"], "values": [10, 5, 7]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why returning this enables chaining

Consider:

`new Calculator(10).add(5).subtract(7).getResult()`.

The constructor creates one object with result ten. Calling `add(5)` changes its result to fifteen. Crucially, `add` returns `this`, which is the same calculator object. JavaScript can therefore look up `subtract` on that returned object and continue the chain.

`subtract(7)` changes the same result to eight and again returns the instance. Finally, `getResult()` returns the number eight rather than the calculator because the chain is finished and the caller wants the answer.

If an arithmetic method returned the numeric result instead of `this`, the next method lookup would be attempted on a number and the fluent chain would break.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Addition and subtraction

`add(value)` uses `this.result += value`. Under the contract, `value` and the stored result are numbers, so this is numeric addition rather than string concatenation.

`subtract(value)` similarly uses `this.result -= value`. Both methods then return `this`.

The state after each call becomes the input to the next call. Operations are not rearranged because arithmetic expressions such as subtraction are order-sensitive.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `8` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"actions": ["Calculator", "add", "subtract", "getResult"], "values": [10, 5, 7]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `8` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Return numbers from arithmetic methods:** Performs the calculation but breaks method chaining because the next calculator method is no longer available.
- **Create a new Calculator per operation:** Can provide immutable chaining, but allocates $O(q)$ objects over a chain instead of mutating one instance.
- **Store an operation list and evaluate later:** Adds unnecessary memory and postpones errors such as division by zero.
- **Division by zero:** Throws before changing `result`.
- **Negative zero divisor:** `-0 === 0`, so it is rejected too.
- **Floating-point values:** Results follow JavaScript number semantics and may contain small representation error covered by the accepted tolerance.
- **Negative exponent:** JavaScript exponentiation produces a reciprocal when mathematically defined.
- **Zero exponent:** A finite nonzero current result becomes one; JavaScript's precise edge semantics govern special values.
- **Repeated getResult:** Merely reads the state and returns the same number until another operation mutates it.
- **Aliased instance:** Every reference observes updates because methods return and mutate the same object.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(q)$. Each constructor, getter, addition, subtraction, multiplication, and division call performs a constant number of JavaScript number operations, so it takes $O(1)$ time. Exponentiation is treated as a primitive JavaScript number operation under the problem's numeric model and is also summarized as $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
