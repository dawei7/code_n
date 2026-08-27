# Guided Example: Sort Vowels by Frequency

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "leetcode"}`
- **Required output:** `"leetcedo"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting of lowercase English characters.

The objective is to compute `"leetcedo"` from `{"s": "leetcode"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Collecting frequency and first-occurrence order together

The set `st = set("aeiou")` provides constant-time vowel membership checks.

While scanning `s` from left to right, the source maintains:

- `cnt[c]`, the total number of occurrences of vowel `c` seen so far; and
- `vowels`, the distinct vowel types in order of first appearance.

When a vowel `c` is encountered for the first time, `c not in cnt` is true and the source appends it to `vowels`. Every occurrence then increments `cnt[c]`.

At the end:

$$
\texttt{cnt}[c]=\operatorname{frequency}(c)
$$

for each present vowel, and the list order records exactly the first-occurrence tie-breaker.

Consonants are ignored during this stage because neither their identities nor positions influence vowel frequencies.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "leetcode"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why a stable frequency sort gives both ordering rules

The source sorts `vowels` with key `-cnt[c]`. Negating the count makes higher frequencies receive smaller keys and therefore appear first.

Only frequency is included in the explicit key. The first-occurrence tie rule is preserved by Python's stable sort: when two vowel types have equal keys, their relative order after sorting is the same as before sorting. Since the original `vowels` list was built in first-occurrence order, tied types remain in precisely the required order.

For example, in `"baeiou"` every vowel count is one. The key ties all five types, so stable sorting leaves `[a,e,i,o,u]` unchanged.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The source sorts `vowels` with key `-cnt[c]`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: What the sorted type list means

Suppose the sorted type order is

$$
c_1,c_2,\ldots,c_t.
$$

The final vowel sequence must contain:

- `cnt[c1]` copies of $c_1$;
- then `cnt[c2]` copies of $c_2$;
- and so on.

All occurrences of a more frequent type come before all occurrences of a less frequent type because ordering is defined by the type's global frequency, not by individual occurrence positions. Equal-frequency types appear in first-occurrence order as entire groups.

The source does not explicitly allocate this expanded sequence. It generates the groups while refilling.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"leetcedo"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "leetcode"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"leetcedo"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Build an explicit vowel pool:** Repeating each:** - **Build an explicit vowel pool:** Repeating each sorted type by its count and consuming that list is straightforward but allocates another $O(N)$ sequence; the source reuses the counter as group state.
- **Sort every vowel occurrence:** This costs $O(V\log V)$ for $V$ vowels and needs a tie key per occurrence, while sorting at most five types is enough.
- **Fixed five-element arrays:** Counts and first positions can be stored by vowel index instead of a `Counter`, with the same asymptotic bounds.
- **No vowels:** `vowels` remains empty, the refill loop changes nothing, and the original string is returned.
- **One vowel type:** Sorting is trivial, and every vowel position receives that same type.
- **Equal frequencies:** Stable sorting preserves first-occurrence type order.
- **Repeated consonants:** They are never touched, regardless of their frequencies.
- **All characters vowels:** Every position is refilled, producing the complete grouped vowel stream.
- **Frequency order is non-increasing:** Higher counts come first because the key is negative; using the positive count would reverse the requirement.
- **Lowercase contract:** The membership set contains only lowercase vowels, matching the documented alphabet.
- **Required library name:** Standalone execution needs `Counter` from Python's `collections` module.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $N=\lvert\texttt{s}\rvert$. The source scans the string twice and joins an $N$-character list once, costing
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
