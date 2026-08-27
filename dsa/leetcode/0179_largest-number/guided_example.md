# Guided Example: Largest Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [10, 2]}`
- **Required output:** `"210"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a list of non-negative integers `nums`, arrange them such that they form the largest number and return it.

The objective is to compute `"210"` from `{"nums": [10, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Compare concatenation orders, not numeric values alone

Sorting the integers in ordinary descending order is not sufficient. With
three and 30, placing three first gives `"330"`, while placing 30 first gives
`"303"`. The better order depends on both complete decimal strings.

After converting every value to text, define that `a` should precede `b` when:

$$
\texttt{a+b}>\texttt{b+a}.
$$

Both compared strings have the same total length, so lexicographic string
comparison is equivalent to numeric comparison of those two nonnegative
concatenations without risking integer overflow.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [10, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the pairwise rule gives a global maximum

Consider any proposed output with adjacent pieces `a` then `b`. Everything
before them is a common prefix and everything after them is a common suffix.
If `a+b < b+a`, swapping just those two pieces makes the entire result larger
at the first differing position.

Therefore an optimal arrangement cannot contain an adjacent inversion under
this rule. Sorting removes all such inversions. Once every adjacent pair is in
the preferred order, no exchange can improve the concatenation, and the sorted
sequence is globally maximal.

The relation is a valid ordering when equality is treated correctly. One way
to see transitivity is to compare the infinite repetitions of each finite
string; `a+b` versus `b+a` gives the same relative order as those periodic
extensions.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Consider any proposed output with adjacent pieces `a` then `... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Adapt the comparator to Python sorting

Python 3 sorting normally accepts a key function, not a two-argument
comparator. `cmp_to_key` wraps a comparator result in objects whose ordering
methods Python's sort can use.

The source lambda returns positive one when `a+b < b+a`, telling the ascending
sort that `a` belongs after `b`. Otherwise it returns negative one, telling it
to place `a` before `b`. This produces the desired largest-first sequence for
strictly unequal comparisons.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"210"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [10, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"210"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Three-way comparator:** Return `-1`, `0`, or `:** - **Three-way comparator:** Return `-1`, `0`, or `1` from comparing `b+a` with `a+b`; this repairs tied-order consistency.
- **Repeated-string sort key:** With bounded digit length, repeating strings to a common comparison length can work, but a true comparator states the rule exactly.
- **Ordinary descending sort:** Fails for shared-prefix pairs such as three and 30.
- **All zeros:** Collapse the joined representation to one `"0"`.
- **One number:** Its decimal string is returned, with zero normalized normally.
- **Duplicate numbers:** They compare equivalent and may appear in either relative order.
- **Periodic ties:** `"12"` and `"1212"` concatenate equally in both orders.
- **Large final number:** It remains a string, avoiding numeric overflow.
- **Nonnegative guarantee:** No minus signs complicate concatenation ordering.
- **Missing imports:** `List` and `cmp_to_key` must be supplied.
- **Comparator contract:** Equality must return zero even when either tied order has the same final text.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(nk\log n)$. Let $n$ be the number of values and $k$ the maximum decimal digit count.
- **Auxiliary Space Complexity:** $O(nk)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
