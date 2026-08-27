# Guided Example: Largest Prime from Consecutive Prime Sum

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 500000}`
- **Required output:** `398771`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n`.

The objective is to compute `398771` from `{"n": 500000}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Notice that the allowed sums are prefixes, not arbitrary prime ranges

The consecutive sequence must start at 2. If the primes are

$$
p_1=2,\ p_2=3,\ p_3=5,\ldots,
$$

then the only candidate sums are

$$
S_j=p_1+p_2+\cdots+p_j.
$$

There is no choice of a later starting prime. Once the prime sequence is known, the candidates form one strictly increasing list of prefix sums. The task becomes: keep the prefix sums that are themselves prime, then find the largest retained value not exceeding `n`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 500000}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Precompute primality through the fixed domain limit

The source sets `mx = 500000`, the maximum legal input, and creates a Boolean array `is_prime` of length `mx + 1`. It explicitly marks zero and one false because neither is prime.

It then performs a Sieve of Eratosthenes. For each `i` from 2 through `mx`:

- if `is_prime[i]` is still true, `i` is appended to `primes`;
- every multiple from `i*i` onward is marked false.

Starting at `i*i` is sufficient. A smaller multiple `i*q` with `q<i` already has the smaller factor `q` and was marked during an earlier sieve step. Avoiding those repeated writes is what gives the sieve its near-linear $O(M\log\log M)$ behavior.

If `i*i > mx`, Python's range is empty, but `i` is still correctly appended when it remains prime. By the time the scan reaches such an `i`, every possible composite has already been marked by a factor no larger than its square root.

After this loop, `is_prime[x]` answers primality for every value in the legal domain, and `primes` contains those primes in increasing order.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The source sets `mx = 500000`, the maximum legal input, and ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build only prime prefix sums

The source initializes cumulative total `t=0` and result-candidate list `s=[0]`. It then visits the prime list in order:

`t += x`

adds the next consecutive prime, so after processing `p_j`, `t=S_j`.

If `t > mx`, the loop stops. All primes are positive, so every later prefix sum would be even larger and also outside every legal query.

When `t <= mx`, the sieve lookup `is_prime[t]` determines whether this allowed sum is itself prime. Only prime totals are appended to `s`.

For the first few prefixes:

- $2=2$ is prime and is stored;
- $2+3=5$ is prime and is stored;
- $2+3+5=10$ is composite and is skipped;
- $2+3+5+7=17$ is prime and is stored.

Skipping a composite prefix sum does not reset `t`. The next candidate must still include every consecutive prime from 2, so accumulation continues from the same running total.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `398771` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 500000}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `398771` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Trial-divide every potential value:** Repeated:** - **Trial-divide every potential value:** Repeated primality checks are simpler for tiny bounds but much slower than one shared sieve across the full domain.
- **Sieve only through the current `n`:** This saves work for a single small query and matches the manifest wording, but does not reuse a fixed global table.
- **Sum an arbitrary consecutive prime interval:** That solves a different problem; the required sequence always starts from 2.
- **Reset after a composite prefix sum:** Composite status of one total does not end the sequence. Later, longer prefix sums may be prime, as 10 is followed by 17.
- **Return the largest prime at most `n`:** A prime is eligible only if it is also one of the cumulative sums from 2.
- **`n=1`:** No positive candidate fits, so the zero sentinel is returned.
- **`n=2`:** The one-term sum 2 qualifies.
- **Bound between candidates:** Binary search returns the previous stored candidate, not the insertion position itself.
- **Bound exactly equal to a candidate:** `bisect_right` places the insertion point after equal values, so that candidate is included.
- **Prefix sum above 500,000:** The construction stops permanently because all later sums are larger.
- **Zero in `s`:** It is a fallback marker, not a claim that zero is prime.
- **Repeated method calls:** They share the already-built read-only sieve and candidate list.
- **Inputs above the documented ceiling:** The fixed table is not designed to establish correctness beyond 500,000.
- **Module initialization cost:** It is paid before the method call and must not be mistaken for an $O(\log C)$ complete-program cost.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M)$. Let $M=500000$ be the fixed preprocessing limit and let $C$ be the number of stored prime prefix-sum candidates, including the sentinel.
- **Auxiliary Space Complexity:** $O(\log C)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
