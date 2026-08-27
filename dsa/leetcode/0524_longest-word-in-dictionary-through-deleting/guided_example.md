# Guided Example: Longest Word in Dictionary through Deleting

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abpcplea", "dictionary": ["ale", "apple", "monkey", "plea"]}`
- **Required output:** `"apple"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s` and a string array `dictionary`, return *the longest string in the dictionary that can be formed by deleting some of the given string characters*. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

The objective is to compute `"apple"` from `{"s": "abpcplea", "dictionary": ["ale", "apple", "monkey", "plea"]}` while avoiding redundant calculations and unnecessary overhead.

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

Deleting characters from `s` while preserving the survivors' order is exactly the definition of forming a subsequence. The task can therefore be restated: among all dictionary words that are subsequences of `s`, choose the longest, breaking equal-length ties by lexicographically smallest value.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abpcplea", "dictionary": ["ale", "apple", "monkey", "plea"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The solution scans the dictionary once. A two-pointer helper tests each candidate, and `ans` stores the best eligible word seen so far.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The solution scans the dictionary once.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Test whether one word can be formed.** The helper is called as `check(t, s)`, where its first parameter is the dictionary candidate and its second parameter is the source string. Inside the helper those parameters are locally named `s` and `t`, respectively; keeping the call direction in mind avoids confusing which string may be deleted.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"apple"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abpcplea", "dictionary": ["ale", "apple", "monkey", "plea"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"apple"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sort candidates first:** Sorting by decreasing:** - **Sort candidates first:** Sorting by decreasing length and increasing lexicographic order allows returning the first eligible word, but costs sorting time and may mutate or copy the dictionary.
- **Generate all subsequences of `s`:** There can be $2^S$ deletion choices, so generation is infeasible and creates many strings absent from the dictionary.
- **Precompute next-occurrence positions:** It can accelerate many subsequence queries, but uses extra space and is unnecessary under the stated optimal manifest.
- **Candidate longer than `s`:** The source pointer ends before the candidate pointer, so the helper returns false.
- **Candidate equal to `s`:** Every character matches in order, making it eligible.
- **Repeated letters:** Each match consumes a later source position, so multiplicity and order are handled correctly.
- **Several longest eligible words:** The `ans > t` comparison retains the lexicographically smallest.
- **Later better candidate:** The running-best invariant allows it to replace an earlier answer regardless of dictionary order.
- **Ineligible lexicographically small word:** Eligibility is checked first, so ordering cannot promote a word that cannot be formed.
- **No eligible word:** The unchanged initial empty string is the required result.
- **Duplicate dictionary entries:** Rechecking may repeat work but cannot change the final answer incorrectly.
- **Source characters skipped at either end:** The source pointer naturally ignores unmatched prefix, interior, and suffix characters.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S+L)$. Let $D$ be the number of dictionary words, $S=\lvert s\rvert$, and $L$ be the maximum dictionary-word length. One helper call advances its source pointer at most $S$ times and its candidate pointer at most $L$ times; because both advance within the same loop, the cost is $O(S+L)$ and, for an eligible candidate, $L\le S$. Across all words, the stated dominant bound is $O(DS)$ under the natural eligibility/check model and matches the manifest.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
