# Guided Example: Number of Different Subsequences GCDs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [6, 10, 3]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array `nums` that consists of positive integers.

The objective is to compute `5` from `{"nums": [6, 10, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Test each possible GCD value directly

Every nonempty subsequence GCD is a positive integer no larger than the largest array value `mx`. The solution tests every candidate `x` from 1 through `mx`.

The crucial question is: how can we determine whether some subsequence has GCD exactly $x$ without enumerating subsequences?

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [6, 10, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Only multiples of `x` can participate

If a sequence has GCD $x$, every selected number must be divisible by $x$. Therefore all possible members of such a subsequence come from input values that are multiples of $x$.

The solution stores distinct input values in set `vis` and scans potential multiples:

`x, 2*x, 3*x, ...` up to `mx`.

Whenever a multiple is present, it is folded into running GCD `g`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If a sequence has GCD $x$, every selected number must be div... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the GCD of all present multiples is the decisive test

Let $A_x$ be the set of input values divisible by $x$, and let

$$
g_x=\gcd(A_x).
$$

If $g_x=x$, selecting one occurrence of every distinct value in $A_x$ forms a valid subsequence whose GCD is exactly $x$. So $x$ is achievable.

If $g_x>x$, every value in $A_x$ is divisible by $g_x$. Any subsequence using only those values also has every member divisible by $g_x$, so its GCD cannot be the smaller value $x$. Values outside $A_x$ are not divisible by $x$ and cannot belong to a sequence with GCD $x$.

Thus $x$ appears as a subsequence GCD if and only if the GCD of all present multiples of $x$ equals $x$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [6, 10, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate all subsequences:** There are $2^n-1:** - **Enumerate all subsequences:** There are $2^n-1$ nonempty subsequences, which is impossible.
- **Maintain GCDs of subsequences ending at each index:** It can also compress repeated GCD values, but the multiples test exploits the bounded value domain directly.
- **Boolean presence array:** It replaces expected hash membership with deterministic indexing at $O(M)$ space.
- **Count duplicates separately:** It is unnecessary because multiplicity does not create new GCD values.
- **Candidate appears directly:** A singleton containing value $x$ immediately proves GCD $x$.
- **Candidate absent:** It may still be achievable, such as 2 from values 6 and 10.
- **No present multiple:** Running GCD remains zero and the candidate is rejected.
- **Only one present multiple:** The candidate works only if that value equals $x$.
- **Early GCD equality:** Once `g == x`, later multiples cannot change it away from $x$.
- **Value one present:** Singleton one proves GCD one immediately.
- **GCD one without value one:** Several larger values may still reduce the running GCD to one.
- **All values equal:** Only that value is achievable as a subsequence GCD.
- **Subsequence order:** Original order never changes the GCD of chosen occurrences.
- **Positive inputs:** Candidate zero is irrelevant and never tested.
- **Maximum bound:** No subsequence GCD can exceed the largest selected value, so testing through $M$ is exhaustive.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+M\log M)$. Let $n$ be the input length and $M=\max(\texttt{nums})$. Building `vis` and finding $M$ take expected $O(n)$ time.
- **Auxiliary Space Complexity:** $O(M)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
