# Guided Example: Convert Object to JSON String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"value": {"y": 1, "x": 2}, "valuePlan": null}`
- **Required output:** `"{\"y\":1,\"x\":2}"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a value, return a valid JSON string of that value. The value can be a string, number, array, object, boolean, or null. The returned string should not include extra spaces. The order of keys should be the same as the order returned by `Object.keys()`.

The objective is to compute `"{\"y\":1,\"x\":2}"` from `{"value": {"y": 1, "x": 2}, "valuePlan": null}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Generate syntax while traversing the JSON tree

A valid JSON value is one of:

- null;
- string;
- number;
- Boolean;
- array;
- object.

Each category has a different textual representation. The helper `write(value)` identifies the category, appends the required tokens to one shared buffer, and recursively writes container children.

After the root value is complete, `output.join('')` combines all tokens exactly once into the final compact string.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"value": {"y": 1, "x": 2}, "valuePlan": null}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why a shared token buffer matters

Repeatedly building a string with recursive expressions such as:

`result = result + nextPart`

can copy the entire prefix many times because JavaScript strings are immutable. Depending on runtime optimizations, deeply or broadly nested output can risk superlinear copying.

The solution instead pushes small pieces into `output`:

- punctuation;
- keys;
- primitive text.

Appending array entries is amortized constant time, and one final join performs output assembly proportional to the final serialized length.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Handle null before the object branch

JavaScript's historical behavior reports:

`typeof null === "object"`.

Therefore, null must be tested first. The solution appends literal `"null"` and returns from that branch implicitly.

If null reached the ordinary object branch, `Object.keys(null)` would fail. The category order prevents this.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"{\"y\":1,\"x\":2}"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"value": {"y": 1, "x": 2}, "valuePlan": null}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"{\"y\":1,\"x\":2}"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Repeated string concatenation:** Correct in principle but can cause repeated prefix copying; a shared buffer gives a clear linear bound.
- **Explicit action stack:** Avoids recursion-depth limits while emitting the same token sequence.
- **Built-in `JSON.stringify`:** Exactly suited to the task but explicitly forbidden.
- **Null:** Must be handled before checking general object type.
- **Empty array:** Emits `[]` with no comma.
- **Empty object:** Emits `{}` with no member syntax.
- **Nested containers:** Recursive calls choose syntax independently at every level.
- **Object key order:** Iterating the `Object.keys` result preserves the required order.
- **String escaping:** The exact code relies on the alphanumeric-only constraint; general JSON strings would require escapes.
- **No extra spaces:** Only structural punctuation and value tokens are appended.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let $S$ be the length of the returned JSON string. Traversal visits each key, primitive representation, and delimiter once, and final joining copies the tokens into an $S$-character string. Time is $O(S)$.
- **Auxiliary Space Complexity:** $O(S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
