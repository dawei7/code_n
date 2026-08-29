# Guided Example: Valid Digit Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 101, "x": 0}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n` and a digit `x`.

The objective is to compute `true` from `{"n": 101, "x": 0}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Removing digits from the right

For a nonnegative integer $n$ with at least two digits:

$$
n\bmod10
$$

is its rightmost decimal digit, and

$$
\left\lfloor\frac n{10}\right\rfloor
$$

is the remaining prefix after removing that digit.

The loop runs while `n > 9`. Therefore, it keeps extracting rightmost digits only while more than one decimal digit remains. Each iteration:

- compares `n % 10` with `x`; and
- performs `n //= 10` to discard the inspected digit.

When the loop stops, `n` is between 0 and 9 and is exactly the original leading digit.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 101, "x": 0}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What \(has_x\) records

The Boolean `has_x` begins false. The update



makes it true as soon as any extracted non-leading digit equals $x$. Once true, the logical `or` keeps it true for all remaining iterations.

At loop termination:

$$
\texttt{has\_x}
\iff
x\text{ appeared in at least one non-leading position}.
$$

The source does not need the number or locations of occurrences. The requirement asks only whether at least one exists.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the leading digit is deliberately excluded from \(has_x\)

Suppose the leading digit equals $x$. The number is invalid regardless of whether $x$ appears again later. Recording the leading occurrence as satisfying the containment rule would not be enough; the start restriction still has to reject it.

By stopping before the last digit and returning



the source states the exact two facts needed:

- a non-leading occurrence exists; and
- the remaining leading digit differs from $x$.

This is equivalent to the original wording. If the number contains $x$ and does not start with $x$, at least one occurrence must necessarily be non-leading. Conversely, a non-leading occurrence together with a different leading digit satisfies both conditions.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 101, "x": 0}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **String conversion:** `sx = str(x); s = str(n); return sx in s and s[0] != sx` is direct and also linear in the digit count, but allocates a decimal string.
- **Track the original leading digit separately:** One can first find the highest power of ten, but the source obtains the leading digit naturally by repeated division.
- **Single-digit number equal to \(x\):** It contains $x$ but starts with $x$, so it is invalid; `has_x` remains false.
- **Single-digit number different from \(x\):** It does not contain $x$ and is invalid.
- **Zero with \(x=0\):** Its sole occurrence is leading, so it fails.
- **Several internal occurrences:** The first match makes `has_x` true; later matches do not change the result.
- **Leading and internal occurrences:** The leading equality still rejects the number, as required.
- **Occurrence only at the end:** The first loop iteration detects it.
- **Occurrence only immediately after the leading digit:** The final loop iteration before termination detects it.
- **Digit \(x=0\):** Arithmetic extraction handles internal zeros, while ordinary decimal representation has no leading zeros to consider.
- **Nonnegative-input requirement:** The remainder/division loop is designed for $n\ge0$; negative representations would introduce a sign and different floor-division behavior.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(D)$. Let $D$ be the number of decimal digits of the original `n`. The loop runs $D-1$ times for a multi-digit number and zero times for a single-digit number. Each iteration performs constant arithmetic and Boolean work.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
