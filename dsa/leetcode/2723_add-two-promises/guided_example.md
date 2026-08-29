# Guided Example: Add Two Promises

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"value1": 2, "delay1": 20, "value2": 5, "delay2": 60}`
- **Required output:** `{"value": 7, "completionTime": 60}`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two promises `promise1` and `promise2`, return a new promise. `promise1` and `promise2` will both resolve with a number. The returned promise should resolve with the sum of the two numbers.

The objective is to compute `{"value": 7, "completionTime": 60}` from `{"value1": 2, "delay1": 20, "value2": 5, "delay2": 60}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: An async function already returns the required new promise

Declaring `addTwoPromises` with `async` guarantees that calling it returns a promise. If the function body eventually returns a number, the runtime fulfills that returned promise with the number. If an awaited promise rejects or the body throws, the returned promise rejects with that reason.

Therefore the implementation needs only to obtain the two fulfillment values and return their arithmetic sum.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"value1": 2, "delay1": 20, "value2": 5, "delay2": 60}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Await the first input value

JavaScript evaluates the expression:

`(await promise1) + (await promise2)`

from left to right. It first reaches `await promise1`. If `promise1` is still pending, execution of this async function pauses without blocking the JavaScript thread. When `promise1` fulfills, its number becomes the left operand.

If `promise1` rejects, `await` throws inside the async function. Because there is no local `try/catch`, that exception automatically rejects the promise returned by `addTwoPromises`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Then obtain the second value

After the first value is available, evaluation reaches `await promise2`. If `promise2` has already fulfilled, retrieving its value continues through a promise microtask without waiting for its original timer or operation again. If it remains pending, the function pauses until it fulfills.

The two numeric fulfillment values are added using JavaScript's `+` operator, and `return` resolves the async function's promise with that sum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `{"value": 7, "completionTime": 60}` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"value1": 2, "delay1": 20, "value2": 5, "delay2": 60}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `{"value": 7, "completionTime": 60}` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`Promise.all` with destructuring:** Makes concurrent waiting explicit and is also correct, but allocates a small result array for only two fixed inputs.
- **Nested `then` calls:** Can produce the same sum but is usually less direct than `async` and `await`.
- **Manual Promise constructor:** Unnecessary because an async function already returns a promise and propagates awaited errors.
- **Second promise fulfills first:** Its value remains settled and is immediately available once evaluation reaches the second await.
- **First promise fulfills first:** The function then waits for the still-pending second promise.
- **Negative fulfillment value:** Numeric addition naturally handles it, such as $10+(-12)=-2$.
- **Zero values:** They require no special case.
- **Rejected first promise:** The returned async promise rejects and the addition is never evaluated.
- **Rejected second promise:** It rejects the returned promise when the second await observes it, outside the stated always-resolve contract.
- **Already fulfilled inputs:** Both awaits resume through promise microtasks and the result still arrives asynchronously as a promise fulfillment.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\max(T_1,T_2)$. The function manages exactly two fixed promises and performs one addition, so its own computational work is $O(1)$ and its explicit auxiliary state is $O(1)$. The async runtime retains a constant-size suspended execution state while awaiting.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
