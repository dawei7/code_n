# Guided Example: Create Hello World Function

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"args": []}`
- **Required output:** `"Hello World"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Write a function `createHelloWorld`. It should return a new function that always returns `"Hello World"`.

The objective is to compute `"Hello World"` from `{"args": []}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Return behavior, not the string immediately

`createHelloWorld` is a function factory. Its result must be another function.

Calling the outer function creates and returns that inner callable. Only when the caller invokes the returned function does it evaluate:

`return "Hello World"`.

Returning the string directly from the outer function would fail the interface because the caller expects to invoke the result.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"args": []}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The inner function is constant

The returned function always produces the same exact string literal:

`"Hello World"`.

Its output does not depend on:

- arguments;
- call count;
- prior calls;
- receiver object;
- external mutable state.

Mathematically, it is a constant function:

$$
f(x)=\texttt{"Hello World"}
$$

for every possible argument tuple $x$.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Accept and ignore arbitrary arguments

The function is declared with `...args`. Rest syntax accepts any number of supplied arguments and gathers them into an array.

The body never reads `args`. Therefore:

- `f()` returns the required string;
- `f({}, null, 42)` returns the same string;
- argument types and values cannot change behavior.

JavaScript would also allow undeclared extra arguments if the function had no parameters. The rest parameter merely makes the variadic acceptance explicit in the exact solution.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"Hello World"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"args": []}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"Hello World"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Arrow function:** `return () => "Hello World"` is equivalent and more concise.
- **Return the string from the outer function:** Incorrect because the requested result must be callable.
- **Use supplied arguments:** Incorrect because output must be constant.
- **No arguments:** Returns the exact literal.
- **Many arguments:** They are accepted and ignored.
- **Null or object arguments:** They are not inspected or mutated.
- **Repeated calls:** Every call returns the same string.
- **Multiple created functions:** They are different function objects with identical behavior.
- **Exact capitalization:** Must match `"Hello World"` exactly.
- **No persistent state:** The closure captures nothing needed for behavior.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The outer function allocates one function object in $O(1)$ time and space.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
