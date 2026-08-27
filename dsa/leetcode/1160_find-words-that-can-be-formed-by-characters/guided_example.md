# Guided Example: Find Words That Can Be Formed by Characters

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["cat", "bt", "hat", "tree"], "chars": "atach"}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of strings `words` and a string `chars`.

The objective is to compute `6` from `{"words": ["cat", "bt", "hat", "tree"], "chars": "atach"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Formation depends on character multiplicities

A word is good when `chars` supplies enough copies of every letter required by that word. Order is irrelevant: the available letters may be rearranged. What matters is frequency.

For example, one `t` in `chars` is not enough for a word containing two `t` characters, even if every other needed letter exists. A simple membership set would lose that multiplicity information, so the solution uses counters.

`cnt = Counter(chars)` maps each available lowercase letter to its number of copies. This counter is built once because the available inventory is the same for every word.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["cat", "bt", "hat", "tree"], "chars": "atach"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build the requirement counter for one word

For each word `w`, `wc = Counter(w)` records how many copies of each letter that word requires. The word is formable exactly when

`cnt[c] >= wc[c]`

for every character appearing in `w`.

The generator `cnt[c] >= v for c, v in wc.items()` produces one Boolean condition per distinct required character. `all(...)` returns true only when every requirement is satisfied.

Counter lookup returns zero for a missing key, so a letter absent from `chars` automatically fails a positive requirement. No separate membership check is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For each word `w`, `wc = Counter(w)` records how many copies... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Each word receives a fresh conceptual inventory

The phrase “each character can only be used once for each word” does not mean that letters consumed for one good word are unavailable to later words. Every word is tested independently against the original `chars`.

That is why the code never decrements `cnt`. It compares a temporary requirement counter to the unchanged inventory. If `"cat"` and `"hat"` are both individually formable, both lengths contribute even though their tests reuse the same available `a` and `t`.

Mutating one shared counter across the outer loop would answer a different problem about forming a collection of words simultaneously.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["cat", "bt", "hat", "tree"], "chars": "atach"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Use a 26-element integer array:** Converting l:** - **Use a 26-element integer array:** Converting letters to offsets gives the same `O(S)` time and constant space with lower hashing overhead. `Counter` expresses frequency intent more directly.
- **Sort every word and `chars`:** Sorted comparisons can test supply but add logarithmic sorting work and repeated processing of the same inventory.
- **Use sets:** A set records only presence and incorrectly accepts words that require more copies than available.
- **Decrement the shared inventory:** That prevents later words from reusing characters, contrary to the independent-per-word rule.
- **A repeated required letter:** Its full multiplicity must fit in `cnt`; one available copy cannot serve multiple positions.
- **A character absent from `chars`:** Counter lookup yields zero, so the word fails immediately when that requirement is checked.
- **Duplicate words in the input:** Each array entry is evaluated and contributes its length independently if good.
- **Empty contribution set:** If no word is good, `ans` remains zero.
- **A word shorter than `chars`:** Length alone does not guarantee formation; its exact character counts still matter.
- **A word equal to `chars` up to permutation:** All counts match and its complete length is included.
- **Lowercase alphabet:** This bound is what makes the counter storage asymptotically constant.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Define
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
