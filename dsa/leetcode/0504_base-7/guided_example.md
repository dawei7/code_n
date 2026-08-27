# Guided Example: Base 7

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": 100}`
- **Required output:** `"202"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `num`, return *a string of its **base 7** representation*.

The objective is to compute `"202"` from `{"num": 100}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

A positional base-seven number uses digits zero through six. If its digits from most significant to least significant are `d_k, d_{k-1}, ..., d_0`, its value is

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": 100}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

$$
d_k7^k+d_{k-1}7^{k-1}+\cdots+d_1 7+d_0.
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | $$
d_k7^k+d_{k-1}7^{k-1}+\cdots+d_1 7+d_0.
$$... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Repeated division by seven discovers these digits from the opposite direction: the remainder gives the least significant digit, and the quotient contains every more significant digit still to be found.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"202"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": 100}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"202"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Built-in base conversion:** Some languages pro:** - **Built-in base conversion:** Some languages provide formatting for arbitrary bases, but manual repeated division demonstrates the required representation and is portable.
- **Recursive digit extraction:** Recurse on `num // 7` and append the remainder while unwinding. It naturally produces high-to-low order but uses $O(\log N)$ call-stack depth.
- **Prepend every digit to a string:** This avoids a final reversal but repeatedly copying an immutable growing string can make the implementation quadratic in the number of digits.
- **Zero:** It must return `"0"` explicitly because the positive extraction loop would execute zero times.
- **Negative input:** Convert only the magnitude and add one leading minus sign; Python's negative remainder behavior should not be used as digit logic here.
- **Exact multiple of seven:** A zero remainder is a real interior or final digit and must be appended, as shown by decimal seven becoming `"10"`.
- **Single base-seven digit:** Values zero through six return their ordinary one-character decimal digit strings.
- **No leading zeros:** The final extracted quotient is from one through six for positive input, so reversal automatically places a nonzero leading digit.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log |num|)$. Let $N = |\textit{num}|$. For $N > 0$, each loop iteration divides the remaining magnitude by seven, so the number of iterations is $\lfloor\log_7 N\rfloor+1$. Digit extraction, reversal, and joining therefore take $O(\log N)$ time.
- **Auxiliary Space Complexity:** $O(\log |num|)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
