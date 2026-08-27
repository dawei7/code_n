# Guided Example: Memoize

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"fnName": "fib", "actions": ["call", "getCallCount"], "values": [[5], []]}`
- **Required output:** `[8, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a function `fn`, return a **memoized** version of that function.

The objective is to compute `[8, 1]` from `{"fnName": "fib", "actions": ["call", "getCallCount"], "values": [[5], []]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Cache by the complete ordered argument tuple

A memoized function should call `fn` only the first time a particular input tuple appears. Later calls with the same inputs must return the stored result.

For this problem, arguments are integers and the supported functions take either one or two arguments. The order matters: `sum(3, 2)` and `sum(2, 3)` must occupy different cache entries even though their mathematical results happen to match.

The solution converts the entire argument array to a JSON string and uses that string as a `Map` key.

Examples include:

- arguments `[2, 2]` become key `"[2,2]"`;
- arguments `[1, 2]` become `"[1,2]"`;
- arguments `[2, 1]` become `"[2,1]"`.

These strings preserve argument count, order, signs, and numeric values under the stated input domain.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"fnName": "fib", "actions": ["call", "getCallCount"], "values": [[5], []]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Create one private cache per memoized function

Calling `memoize(fn)` creates `const cache = new Map()` and returns an inner function.

The inner function closes over both `fn` and `cache`. Those references remain available after `memoize` returns, while callers cannot directly mutate the map.

Each separate call to `memoize` creates a separate map. Memoizing two different functions therefore cannot cause one function's result to be returned for the other, even if they receive identical arguments.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Calling `memoize(fn)` creates `const cache = new Map()` and ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Collect arbitrary arguments with rest syntax

The returned function is declared as `function(...args)`. Rest syntax gathers the invocation's positional arguments into a new array in their original order.

That array serves two purposes:

- `JSON.stringify(args)` creates the cache key;
- `fn(...args)` spreads the same values back into positional arguments for the original function.

The wrapper does not reverse, sort, or otherwise normalize arguments. This preserves the contract's distinction between $(a,b)$ and $(b,a)$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[8, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"fnName": "fib", "actions": ["call", "getCallCount"], "values": [[5], []]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[8, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Nested maps by argument:** Avoid serialization:** - **Nested maps by argument:** Avoid serialization and support identity-based objects, but add structure unnecessary for bounded integer tuples.
- **Concatenate with a delimiter:** Easy to implement incorrectly because signs, lengths, or delimiters can create collisions; JSON supplies unambiguous tuple syntax.
- **Cache by result:** Incorrect because different inputs may produce the same output and still require separate first calls.
- **Reversed sum arguments:** They serialize differently and must be cached separately.
- **Falsy cached result:** `cache.has` prevents accidental recomputation.
- **First call:** It always invokes `fn` and stores the returned value.
- **Repeated call:** It returns the stored result without invoking `fn`.
- **Separate memoized functions:** Each owns an independent closure cache.
- **Recursive work inside `fn`:** The wrapper caches the top-level result; it does not rewrite internal recursive calls.
- **Arbitrary objects:** Outside this problem's numeric scope, JSON serialization would not preserve strict identity and should not be used.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L)$. Let $a$ be the number of arguments and $L$ the length of their serialized representation. Creating the key takes $O(L)$ time, map lookup is expected $O(L)$ for hashing/comparison in a precise string-cost model, and a miss additionally pays the cost of `fn`.
- **Auxiliary Space Complexity:** $O(u)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
