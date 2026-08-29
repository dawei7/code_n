# Guided Example: Check If a String Contains All Binary Codes of Size K

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "00110110", "k": 2}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a binary string `s` and an integer `k`, return `true` *if every binary code of length* `k` *is a substring of* `s`. Otherwise, return `false`.

The objective is to compute `true` from `{"s": "00110110", "k": 2}` while avoiding redundant calculations and unnecessary overhead.

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

**Know exactly how many codes are required.** Each of the `k` positions has two choices, zero or one, so there are `2^k` distinct binary strings of length `k`. The expression `1 << k` computes this number by shifting binary one left `k` positions. The variable `m` is the required distinct-code count.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "00110110", "k": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Reject an impossible string before building anything.** A length-`n` string has exactly `n - k + 1` starting positions for a length-`k` substring. Even if every one were different, fewer positions than `2^k` cannot cover all codes. The condition `n - k + 1 < m` therefore proves failure immediately.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

This is a pigeonhole argument: every occurrence can contribute at most one distinct code. Passing the check does not prove success because occurrences can repeat; it only makes success numerically possible.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "00110110", "k": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Rolling binary mask:** Shift the previous code, mask to the lowest `k` bits, and add the new bit. This avoids slicing and reaches the manifest bounds.
- **Set of rolling integers:** Store integer window codes in a hash set rather than a Boolean array. It can use space proportional only to observed codes while retaining linear expected time.
- **Generate all binary strings:** Building the entire universe and removing observed strings is possible but performs unnecessary generation; the observed-set size already proves coverage.
- **Stop once all codes are found:** A loop can return true when the seen count reaches `m`. The stored comprehension always processes all windows after the feasibility check.
- **k greater than n:** Then the number of windows is nonpositive and the early check returns false.
- **Exactly enough windows:** Every window must be distinct for success; any duplicate forces failure.
- **k equals one:** The required codes are `0` and `1`. Both characters must occur.
- **All zeros:** Only one distinct code appears, so success occurs only where the universe itself has one code, which never happens for positive `k`.
- **Repeated occurrences:** The set counts a code once regardless of how many times it appears.
- **Overlapping substrings:** They are valid and must be included; advancing starts by one enumerates them.
- **Binary-alphabet guarantee:** It ensures there are exactly `2^k` possibilities. A larger alphabet would require a different universe size.
- **Large k:** `2^k` grows quickly, and the pigeonhole test often rejects before allocating the set.
- **String slicing:** Slices are copies in Python, so they affect both time and memory.
- **Hash collisions:** Python sets resolve collisions and preserve correctness; complexity uses expected hashing behavior.
- **Complexity reporting:** Use `O(nk)`-style time for this source and reserve `O(n)` for an implemented rolling code.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(2^k)$. Let `W = n - k + 1` be the number of windows. The comprehension creates and hashes `W` slices of length `k`, taking `O(Wk)` time in the standard Python string model. The final set-size check is constant time. Since `W <= n`, `O(nk)` is a simple upper bound.
- **Auxiliary Space Complexity:** $O(2^k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
