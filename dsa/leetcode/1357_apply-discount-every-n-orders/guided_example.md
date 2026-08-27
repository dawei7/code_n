# Guided Example: Apply Discount Every n Orders

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "discount": 50, "products": [1, 2], "prices": [100, 200], "orders": [[[1], [1]]]}`
- **Required output:** `[100.0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a supermarket that is frequented by many customers. The products sold at the supermarket are represented as two parallel integer arrays `products` and `prices`, where the $$i^{\text{th}}$$ product has an ID of $\text{products}[i]$ and a price of $\text{prices}[i]$.

The objective is to compute `[100.0]` from `{"n": 3, "discount": 50, "products": [1, 2], "prices": [100, 200], "orders": [[[1], [1]]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Build a direct product-to-price map

The constructor creates `d = {a: b for a, b in zip(products, prices)}`. The two input arrays are parallel, so each zipped pair contains a product ID and its price. Product IDs are unique, making the dictionary a one-to-one catalog lookup.

Using a dictionary means the price of a bill item can be found by its ID without searching the catalog array. The constraints guarantee every ID supplied to `getBill` exists in the constructor’s product list.

The object also stores `n` and `discount`. `i` begins at zero and represents the number of customer positions advanced modulo `n`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "discount": 50, "products": [1, 2], "prices": [100, 200], "orders": [[[1], [1]]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Advance the customer cycle once per bill

At the start of every `getBill` call, the statement
`i = (i + 1) % n` advances the persistent counter.

Beginning from zero, the sequence is one, two, and so on through `n - 1`, then zero on the `n`th call. Consequently, `i == 0` is true precisely for customer numbers `n`, `2n`, `3n`, and so forth.

For `n = 3`, the first three calls produce counter values one, two, and zero. Only the third receives the discount. The next three calls repeat the same pattern, so the sixth also receives it.

The counter is updated per call rather than per product line. A customer buying many different products is still one order and advances the cycle once.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | At the start of every `getBill` call, the statement
`i = (i ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Compute the undiscounted subtotal

`zip(product, amount)` pairs each purchased product ID with its quantity. The generator expression multiplies `d[a]`, the unit price, by quantity `b` for every pair. `sum` adds those line totals into `x`.

The input arrays have equal lengths, and product IDs within one bill are unique. No line is accidentally truncated by `zip` under the contract, and no duplicate line needs consolidation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[100.0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "discount": 50, "products": [1, 2], "prices": [100, 200], "orders": [[[1], [1]]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[100.0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Catalog arrays with linear search:** Correct b:** - **Catalog arrays with linear search:** Correct but makes each bill line cost $O(P)$ instead of expected $O(1)$ lookup.
- **Countdown counter:** Initialize a counter to `n`, decrement per bill, apply the discount at zero, then reset. It expresses the same cycle without modulo.
- **One-based total customer count:** Increment an unbounded count and test `count % n == 0`. The checked-in counter keeps only the remainder.
- **`n == 1`:** Every increment wraps to zero, so every customer receives the discount.
- **Zero percent discount:** Discounted customers pay the same subtotal, but the cycle still advances normally.
- **One hundred percent discount:** Every designated customer pays zero.
- **Single bill line:** The same zipped subtotal formula handles it without a special case.
- **Different product order:** Dictionary lookup uses IDs, so bill lines need not follow catalog order.
- **Unique bill product IDs:** The contract prevents repeated IDs within one call, though summing repeated lines would still produce the same total quantity cost.
- **Floating-point tolerance:** Percentage division may produce a non-integer result; the accepted error tolerance covers normal floating arithmetic.
- **Persistent object state:** Creating a new `Cashier` resets the customer cycle, while repeated calls on the same object continue it.
- **Counter updated before the subtotal:** With valid input this changes only which customer number the current call represents. The first call correctly becomes customer one rather than customer zero.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P)$. Let $P$ be the number of catalog products and $L$ the number of line items in one bill.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
