# Guided Example: Find Maximum Number of String Pairs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["cd", "ac", "dc", "ca", "zz"]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** array `words` consisting of **distinct** strings.

The objective is to compute `2` from `{"words": ["cd", "ac", "dc", "ca", "zz"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Process words from left to right

A legal pair requires $i<j$. When current word `w=words[j]` is processed, every word recorded in `cnt` comes from an earlier index and automatically satisfies the index order.

The partner needed for `w` is its reversal `w[::-1]`. The code adds how many such earlier words have been seen:

`ans += cnt[w[::-1]]`.

Only afterward does it record the current word with `cnt[w] += 1`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["cd", "ac", "dc", "ca", "zz"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why update order matters

Recording `w` before checking would let a palindromic word such as `"aa"` match itself at the same index. That is illegal because a pair needs two distinct indices with the earlier one strictly smaller.

Checking first ensures the current occurrence can pair only with previous occurrences.

Under the problem's distinct-word guarantee, there is at most one previous occurrence of any reversal, so the added count is zero or one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why every reverse pair can be counted independently

Every word has exactly one reversal. If `"ab"` pairs with `"ba"`, neither word can be the reversal partner of a third distinct string: the reversal of `"ab"` is uniquely `"ba"` and vice versa.

Thus discovered pairs cannot compete for the same word. There is no need to remove matched words from the Counter or solve a general matching problem.

The distinctness guarantee is central to this exact simplicity. With duplicate words, counts and one-use constraints would require consuming available occurrences carefully.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["cd", "ac", "dc", "ca", "zz"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Hash set:** Sufficient under distinctness; check the reversal and then insert the current word.
- **Nested pair scan:** Direct but costs $O(n^2)$ time.
- **Remove a matched reversal:** Unnecessary for distinct words because no third word can need the same unique partner.
- **Palindromic word:** Cannot pair with itself and cannot have a duplicate under the constraints.
- **Reversal absent:** The word contributes no pair.
- **All words in reversal classes:** The answer is half the number of nonpalindromic words.
- **Check before insert:** Prevents illegal self-pairing.
- **Fixed length two:** Makes reversal constant time.
- **Distinctness removed:** The exact Counter accumulation would overcount combinations relative to one-use pairing.
- **Input order:** Only determines which endpoint discovers a pair; the final maximum is order-independent.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of words. Every word undergoes one constant-length reversal, one expected $O(1)$ Counter lookup, and one expected $O(1)$ update. Total expected time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
