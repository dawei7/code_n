# Guided Example: Function Composition

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"functionSpecs": ["addOne", "square", "double"], "x": 4}`
- **Required output:** `65`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of functions `[f1, f_2, f_3, ..., f_n]`, return a new function `fn` that is the **function composition** of the array of functions.

The objective is to compute `65` from `{"functionSpecs": ["addOne", "square", "double"], "x": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Composition applies the rightmost function first

For functions listed as:

$$
[f_0,f_1,\ldots,f_{n-1}],
$$

their composition is:

$$
f_0(f_1(\cdots f_{n-1}(x)\cdots)).
$$

Although $f_0$ is written first in the mathematical expression, it executes last. Evaluation begins with the function at the final array index and proceeds backward.

The solution returns a new function that performs exactly this right-to-left evaluation whenever it is called.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"functionSpecs": ["addOne", "square", "double"], "x": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Capture the function array in a closure

`compose(functions)` does not evaluate any supplied function immediately. It returns `function(x) { ... }`.

That returned function closes over `functions`, so it can use the list later when the caller supplies an input value. This separates composition construction from composition evaluation:

- construction chooses which functions participate;
- invocation chooses the initial value and runs the chain.

The exact closure holds a reference to the input array rather than copying it. Under normal challenge use the array is not changed after composition.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Carry one current result

At invocation time, `result` starts as `x`. The loop begins at `functions.length - 1` and decrements down to zero.

Each iteration performs:

`result = functions[index](result)`.

The output of the current function becomes the input to the next function on its left. Only one intermediate value is needed because once a function has consumed the previous result, that earlier value has no further role.

After index zero runs, `result` is the full nested expression and is returned.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `65` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"functionSpecs": ["addOne", "square", "double"], "x": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `65` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`reduceRight`:** Naturally expresses right-to-left accumulation but adds a callback layer and is no clearer than the loop.
- **Recursive composition:** Mirrors the nested formula but uses $O(n)$ call-stack space.
- **Left-to-right loop:** Computes the reverse composition and is generally incorrect.
- **Empty function list:** The loop is skipped and input is returned unchanged.
- **Single function:** It is invoked once and its output is returned.
- **Noncommuting functions:** Their listed order must be preserved exactly.
- **Repeated invocation:** Each call initializes a fresh local result.
- **Function-array mutation:** Because the closure retains the original array reference, later external mutations would affect future calls.
- **Thrown error:** The wrapper does not catch it; an exception from a supplied function propagates immediately.
- **Method receiver:** The exact solution does not forward `this` because the challenge functions are argument-only.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n=\texttt{functions.length}$. Each invocation calls every function once, so assuming each supplied function is $O(1)$, evaluation takes $O(n)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
