# Guided Example: GCD Sort of an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [7, 21, 3]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`, and you can perform the following operation **any** number of times on `nums`:

The objective is to compute `true` from `{"nums": [7, 21, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn legal swaps into connectivity

Two values can be swapped directly when they share a prime factor. Even when two values have gcd one, they may exchange positions indirectly through a chain of other values.

This means the important object is not an individual swap but a connected component in the graph where values connect through shared prime factors. Values in one connected component can be permuted through a sequence of swaps along component edges.

The source represents these components with Disjoint Set Union.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [7, 21, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Precompute distinct prime factors

`f[value]` is a list of distinct prime divisors. The outer sieve scans candidates from two through `mx = max(nums)`. If `f[i]` is already nonempty, some smaller prime divided `i`, so `i` is composite and is skipped as a prime candidate.

For a prime `i`, the inner loop visits every multiple `j` and appends `i` to `f[j]`. After the sieve, each value has exactly its distinct prime factors.

This is a factor-list version of the sieve of Eratosthenes and avoids trial-dividing every array occurrence independently.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Union each value with its prime-factor nodes

The DSU parent array `p` has nodes for numerical values and primes in the bounded domain. For every input value `i` and every factor `j` in `f[i]`, the assignment

`p[find(i)] = find(j)`

merges the value with that prime's component.

If two values share a factor, both become connected to the same prime node. If they are linked through several intermediate values and factors, transitive DSU connectivity captures that chain.

`find` uses path compression: after recursively locating the representative, it points the visited node directly to that root, accelerating later queries.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [7, 21, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Factor each number by trial division:** Avoids a full sieve when values are sparse, but repeated factorization can cost more.
- **Graph over array indices:** Connect indices sharing factors, but efficiently discovering those edges still needs factor buckets.
- **Attempt adjacent array swaps only:** The operation permits any two positions, and connectivity is over values, not neighboring indices.
- **Prime value:** Connects only through occurrences or other multiples of that prime.
- **Isolated value:** It can remain only where the sorted array requires the same component/value.
- **Transitive sharing:** Values need not have gcd greater than one directly if a chain connects them.
- **Duplicate values:** They share the same value node and are interchangeable.
- **Already sorted array:** Every position matches immediately and returns true.
- **Path compression:** Improves repeated representative queries.
- **No union by rank:** Correctness remains, though rank/size could improve robustness.
- **Values at maximum bound:** Fixed DSU allocation includes them safely.
- **Input preservation:** `sorted(nums)` creates a new target list and the original order is retained.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M\log\log M+N\log M+N\log N)$. Let $M=\max(\texttt{nums})$ and $N$ be array length. The factor sieve takes $O(M\log\log M)$ aggregate factor-appending work. Unioning all distinct factors costs $O(N\log M)$ as a simple upper bound, with near-constant inverse-Ackermann DSU operations. Sorting costs $O(N\log N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
