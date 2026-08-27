# Guided Example: The Number of Weak Characters in the Game

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"properties": [[5, 5], [6, 3], [3, 6]]}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are playing a game that contains multiple characters, and each of the characters has **two** main properties: **attack** and **defense**. You are given a 2D integer array `properties` where $\text{properties}[i] = [\text{attack}_{i}, \text{defense}_{i}]$ represents the properties of the $$i^{\text{th}}$$ character in the game.

The objective is to compute `0` from `{"properties": [[5, 5], [6, 3], [3, 6]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Sort so one strict inequality is automatic

A character is weak only if another character has strictly greater attack and strictly greater defense. The source sorts `properties` by key `(-attack, defense)`:

- larger attack appears earlier;
- among equal attack, smaller defense appears earlier.

During the subsequent left-to-right scan, earlier rows never have smaller attack. The running value `mx` stores the greatest defense seen among those earlier rows.

If current defense `x` is less than `mx`, some earlier row has greater defense. The tie ordering is designed so that this witness must also have strictly greater attack.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"properties": [[5, 5], [6, 3], [3, 6]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why equal attack must be ordered by increasing defense

Characters with equal attack cannot dominate one another, no matter how their defenses compare. They must not create false weak counts.

Within one attack group, defenses are scanned from smallest to largest. Earlier same-attack defenses are therefore at most the current defense. They cannot make `x < mx` true.

If `mx` is greater than the current defense, its value cannot have come solely from an earlier character in the same attack group; it must have been established by a previously scanned group with larger attack. That row has both strictly greater attack and defense, providing a valid witness.

For example, equal-attack characters `(5,3)` and `(5,7)` are scanned in that order. When defense three is seen, defense seven has not yet entered `mx`, so the first character is not incorrectly labeled weak because of an equal-attack peer.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Characters with equal attack cannot dominate one another, no... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Update the answer and maximum

The line `ans += x < mx` relies on Python Booleans behaving as integers: true contributes one and false contributes zero.

After testing, `mx = max(mx, x)` incorporates the current defense for later characters. It is safe to update after the test because a character cannot witness its own weakness.

Defense values are positive, so initializing `mx=0` ensures the first character cannot be counted.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"properties": [[5, 5], [6, 3], [3, 6]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Attack-frequency suffix maximum:** Store maxim:** - **Attack-frequency suffix maximum:** Store maximum defense at each attack, build suffix maxima, and test against strictly higher attacks in $O(N+K)$ time and $O(K)$ space.
- **Brute-force pair comparison:** Takes $O(N^2)$ time and repeats dominance checks.
- **Wrong tie order:** Descending attack and descending defense scanned left-to-right can let equal attacks falsely dominate.
- **Equal attack, different defense:** Neither is weak because attack must be strictly greater.
- **Equal defense, different attack:** Lower attack is not weak because defense must also be strictly greater.
- **Duplicate property pairs:** They never dominate one another and are treated identically.
- **One globally strongest character:** It can cause many later weak counts through `mx`.
- **Tradeoff characters:** Higher attack but lower defense does not establish weakness.
- **Strict comparison:** Use `x < mx`, not `x <= mx`.
- **Positive defenses:** Make zero a safe initial maximum.
- **Boolean arithmetic:** In Python, adding the comparison increments by exactly zero or one.
- **Input side effect:** The exact source reorders `properties`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the number of characters. Sorting costs $O(N\log N)$ time, and the scan costs $O(N)$, so total time is $O(N\log N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
