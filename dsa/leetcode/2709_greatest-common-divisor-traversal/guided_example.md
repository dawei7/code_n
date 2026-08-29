# Guided Example: Greatest Common Divisor Traversal

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [2, 3, 6]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** integer array `nums`, and you are allowed to **traverse** between its indices. You can traverse between index `i` and index `j`, $i \neq j$, if and only if $gcd(\text{nums}[i], \text{nums}[j]) > 1$, where `gcd` is the **greatest common divisor**.

The objective is to compute `true` from `{"nums": [2, 3, 6]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Replace pairwise gcd edges with prime-factor connectors

Two positive integers have gcd greater than one exactly when they share at least one prime factor.

Instead of comparing every pair of indices, the solution creates an implicit bipartite connectivity model:

- one node for each array index;
- one auxiliary node for each possible prime factor.

Index `i` is connected to auxiliary prime node $p$ when $p$ divides `nums[i]`.

Two indices sharing a prime then join through the same auxiliary node, and longer chains of shared primes represent legal traversal sequences.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [2, 3, 6]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Precompute distinct prime factors

Global dictionary `p` maps each value up to `mx = 100010` to a list of its distinct prime factors.

For each number `x`, trial division starts at two. When factor `i` divides the working value `v`, it is appended once, then all copies of that factor are divided out.

If the reduced `v` remains greater than one after the loop, that remainder is prime and is appended.

Removing repeated powers is correct because connectivity needs to know only whether a prime divides the number, not its exponent.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Union-Find stores connected components

`UnionFind` maintains parent array `p` and component sizes.

`find` follows parents to a root and applies path compression, making future queries faster. `union` finds both roots and attaches the smaller component beneath the larger one, using `size`.

If roots already match, no work is needed because the nodes are already connected.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [2, 3, 6]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Smallest-prime-factor sieve:** Builds factors in near $O(M\log\log M)$ preprocessing and realizes the manifest's intended bound.
- **Compare every pair gcd:** Can require $O(n^2\log M)$ time and materialize a dense graph.
- **Map each prime to its first index:** Can union indices directly without allocating auxiliary prime nodes.
- **Single index:** Always connected, even when its value is one.
- **One with other values:** One has no legal edge and makes the answer false.
- **Repeated values:** Their common prime factors connect them naturally.
- **Prime values:** Each connects to its own prime auxiliary node.
- **Coprime groups:** Remain separate and make the root set larger than one.
- **Indirect bridge:** A composite value can connect groups sharing different factors.
- **Prime exponents:** Repeated powers are irrelevant; each distinct factor is stored once.
- **Global preprocessing:** Its cost is paid at module import and reused by calls.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M+F)$. Let $M$ be the fixed precomputation ceiling and $F$ the total number of distinct prime-factor entries stored through that ceiling. The module-level trial division costs a safe $O(M^{3/2})$ time and $O(M+F)$ space.
- **Auxiliary Space Complexity:** $O(M + n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
