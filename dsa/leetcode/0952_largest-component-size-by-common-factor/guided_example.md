# Guided Example: Largest Component Size by Common Factor

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [4, 6, 15, 35]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array of unique positive integers `nums`. Consider the following graph:

The objective is to compute `4` from `{"nums": [4, 6, 15, 35]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn shared factors into connectivity

Two input values have an edge when they share any factor greater than one. Connected components may also form transitively: four and six share factor two, while six and fifteen share factor three, so all three values belong to one component even though four and fifteen are coprime.

Union-Find is designed to maintain exactly this kind of gradually discovered connectivity.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [4, 6, 15, 35]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use numeric factors as connector nodes

The Union-Find structure has one index for every integer from zero through `max(nums)`. Input values and their factors live in the same parent array.

For every input value `v`, the solution tries divisors `i` from two while `i <= v // i`. This integer form checks through the square root without floating-point rounding.

When `v % i == 0`, both `i` and `v // i` are factors. The code performs:

- `union(v, i)`;
- `union(v, v // i)`.

The factor indices act as invisible connector vertices. If two different input values share factor `f`, both become united with index `f` and therefore with each other.

The factor need not be prime. Connecting through composite factors is still correct because sharing a composite factor certainly means sharing a factor greater than one. Trial division also discovers prime factors through divisor pairs.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The Union-Find structure has one index for every integer fro... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why both factors of a divisor pair are joined

Suppose `v = 35` and the trial divisor reaches five. The paired factor is seven. Another input value might share seven but not five, so joining only the trial divisor would miss that connection.

Adding both `i` and `v // i` ensures every proper factor discovered by trial division can serve as a connector.

For a perfect square, both expressions may be equal. The second union is then redundant but harmless.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [4, 6, 15, 35]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Prime-factorize each value:** Divide out each :** - **Prime-factorize each value:** Divide out each discovered prime and union values through a map from prime to representative. This avoids a Union-Find array sized by `M` but requires careful factorization.
- **Compare every pair with gcd:** It directly follows the graph definition but costs `O(N^2 log M)` time.
- **Sieve smallest prime factors:** Preprocessing through `M` makes repeated factorization fast and is useful for many values.
- **All values prime:** Unless one prime divides another input composite, primes remain singleton components.
- **Value one:** It is always isolated because it has no permitted common factor.
- **Perfect squares:** Repeated union with the same square-root factor is harmless.
- **Transitive components:** Direct gcd greater than one is not required between every pair; Union-Find preserves paths.
- **Unique inputs:** Counter entries count different input values without duplicate-value complications.
- **Large maximum with few values:** The `O(M)` parent array may be wasteful; a dictionary-backed factor Union-Find is an alternative.
- **No union by size:** Path compression keeps operations efficient, though adding rank or size would provide the standard strongest bound.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N sqrt(M)$. Let `N` be the number of input values and `M = max(nums)`.
- **Auxiliary Space Complexity:** $O(N + M)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
