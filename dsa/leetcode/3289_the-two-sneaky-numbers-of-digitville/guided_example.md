# Guided Example: The Two Sneaky Numbers of Digitville

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [0, 1, 1, 0]}`
- **Required output:** `[1, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

In the town of Digitville, there was a list of numbers called `nums` containing integers from `0` to $n - 1$. Each number was supposed to appear **exactly once** in the list, however, **two** mischievous numbers sneaked in an *additional time*, making the list longer than usual.<!-- notionvc: c37cfb04-95eb-4273-85d5-3c52d0525b95 -->

The objective is to compute `[1, 0]` from `{"nums": [0, 1, 1, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

**Use the unusually strong frequency guarantee.** The input is built from every integer in the range $[0,n-1]$ appearing once, after which exactly two of those values are added one extra time. Therefore exactly two values have frequency two, and every other value has frequency one. The task is not to reconstruct an unknown complicated distribution; it is simply to identify the two frequency-two entries.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [0, 1, 1, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The exact source expresses that observation with `Counter(nums)`. A `Counter` is a mapping from each distinct value to the number of times it occurs. Constructing it performs one pass over `nums`. For a simple example, if `nums = [0, 1, 1, 0]`, the mapping is logically `{0: 2, 1: 2}`. For a larger example such as `[0, 1, 2, 3, 2, 1]`, the counts of $1$ and $2$ are two while the counts of $0$ and $3$ are one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The exact source expresses that observation with `Counter(nu... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The list comprehension `[x for x, v in cnt.items() if v == 2]` then visits every distinct key-count pair. It includes the key `x` exactly when its count `v` equals two. By the construction guarantee, this condition holds for precisely the two sneaky numbers, so the returned list has exactly the required two values.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [0, 1, 1, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Seen set plus duplicate list:** On the first o:** - **Seen set plus duplicate list:** On the first occurrence, insert the value into a set; on the second, append it to the result. This avoids storing explicit counts but still takes expected $O(N)$ time and $O(N)$ auxiliary space. It also matches the manifest summary more closely than the exact source does.
- **Boolean or integer array:** Since every value lies in $[0,n-1]$, an array indexed by value can record whether each number has appeared. This gives deterministic $O(N)$ time and $O(n)$ space without hashing.
- **In-place sign marking:** Many duplicate problems mark an index by negating an array entry. Here zero needs special handling, input mutation may be undesirable, and the clean range guarantee makes counting easier to explain and safer to use.
- **Algebra with sums and squares:** The excess sum gives the sum of the two sneaky numbers, while an excess square-sum can derive their product and then the two roots. Python avoids overflow, but fixed-width languages need careful integer sizing, and the method is less robust and less transparent than counting.
- **XOR partitioning:** XORing the full input with $0$ through $n-1$ leaves the XOR of the two duplicates. A distinguishing set bit can partition both collections and recover each duplicate in $O(N)$ time and $O(1)$ auxiliary space. It is more space-efficient but considerably less beginner-friendly.
- **Sorting:** After sorting, equal adjacent values reveal the two duplicates. This costs $O(N\log N)$ time and either mutates the input or uses $O(N)$ space for a copy, so it gives up the linear-time advantage.
- **Smallest legal input:** When $n=2$, the input length is four and both values $0$ and $1$ are duplicated. The counter returns both; there is no special boundary case.
- **Duplicates next to each other or far apart:** Position and separation do not matter. Counting aggregates occurrences regardless of where they appear.
- **Zero as a sneaky value:** Zero is an ordinary dictionary key and needs no special treatment, unlike some arithmetic or sign-marking techniques.
- **Unsorted return order:** The problem accepts any order. If an external caller demands increasing order, it could sort the two-element result in constant asymptotic time, but that behavior is not required by this contract.
- **Malformed frequency greater than two:** The exact `v == 2` filter would exclude a value occurring three times. This is acceptable only because the stated input construction rules that case out; changing the contract would require changing the predicate.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ denote `len(nums)`. Because the array contains the $n$ base values plus two extra values, $N=n+2$, so using either symbol gives the same asymptotic result. Building the counter reads all $N$ elements once and takes expected $O(N)$ time with Python's hash table. Iterating through `cnt.items()` visits exactly $n$ distinct keys, which is also $O(N)$. The total expected time is $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
