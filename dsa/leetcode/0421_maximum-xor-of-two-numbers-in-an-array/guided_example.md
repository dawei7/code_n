# Guided Example: Maximum XOR of Two Numbers in an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 10, 5, 25, 2, 8]}`
- **Required output:** `28`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer array `nums`, return *the maximum result of *$\text{nums}[i] XOR \text{nums}[j]$, where $0 \le i \le j < n$.

The objective is to compute `28` from `{"nums": [3, 10, 5, 25, 2, 8]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Maximize binary digits from most significant to least significant

XOR produces a `1` at a bit position when its two input bits differ and a `0` when they agree. To maximize the numeric XOR, the highest bit matters more than every lower bit combined. Therefore, for a fixed number `x`, the best partner should differ from `x` at the most significant possible bit; after that choice, it should differ at the next bit whenever possible, and so on.

A binary trie stores all input numbers by their bit prefixes and makes that greedy choice efficient. Each trie node has two child slots: child `0` represents a number with zero at the next bit, and child `1` represents a number with one. A root-to-leaf path records one complete 31-bit number.

The constraints limit values to $2^{31}-1$, so bit positions `30` down through `0` cover every possible value, including leading zeros. Using the same fixed width for all numbers is essential: trie depth then corresponds to the same bit significance for every path.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 10, 5, 25, 2, 8]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build the trie

`Trie.children` is a two-element list initialized to `[null, null]`. `__slots__ = ("children",)` prevents each node from needing an unrestricted instance dictionary; this reduces object overhead but does not change the algorithm.

To insert `x`, the loop visits bit positions from 30 down to 0. The expression `x >> i & 1` shifts bit `i` into the least-significant position and masks everything else, yielding either zero or one. If the corresponding child does not yet exist, a new `Trie` node is created. Moving to that child continues the prefix.

Shared prefixes reuse nodes. Duplicate numbers follow an existing complete path and require no new branches. After all insertions, every input value has a 31-level path from the root.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Search for the best partner of one number

`search(x)` starts at the root with `ans = 0`. At bit position `i`, let `v` be `x`'s bit. The preferred partner bit is `v ^ 1`, the opposite bit. If that child exists, choosing it makes XOR bit `i` equal to one, so the code executes `ans |= 1 << i` and follows the opposite branch.

If the opposite branch does not exist, every number with the already chosen prefix has the same bit `v` at this position. The XOR bit must be zero, and the search follows `children[v]` without modifying `ans`.

The fallback child is guaranteed to exist. At every level, the current node represents at least one inserted number, so if it lacks the opposite child it must have the same-bit child.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `28` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 10, 5, 25, 2, 8]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `28` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Check every pair:** Direct XOR comparison takes $O(n^2)$ time, which is too slow for up to $2\cdot10^5$ numbers.
- **Greedy prefix hash sets:** Build the maximum answer bit by bit and test whether two observed prefixes can realize each proposed prefix XOR. It also takes $O(nB)$ time and $O(n)$ space, but the trie gives a concrete best-partner path.
- **Insert and query incrementally:** Query each value against previously inserted values, then insert it. This avoids self-pairing and has the same bounds, but the chosen code cleanly separates construction and queries.
- **Variable-width paths without leading zeros:** Misaligned depths would compare bits of different significance. Fixed 31-bit paths avoid that error.
- **Single element:** The only legal pair is the value with itself, producing zero.
- **All values equal:** Every trie search follows identical bits and returns zero.
- **Zeros:** Zero is represented by 31 zero bits and participates normally.
- **Maximum allowed value:** Bit 30 is its highest possible set bit, so the `range(30, -1, -1)` loop covers it exactly.
- **Duplicate paths:** Insertion reuses existing nodes; duplicates do not increase the asymptotic node count or change the maximum.
- **Prefer lower-bit gains over a high bit:** This is never beneficial because bit $i$ outweighs all lower positions together, which is the foundation of the greedy search.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(nB)$. Let $n$ be the number of input values and let $B=31$ be the fixed number of processed bits. Insertion costs $O(B)$ per number, and search costs $O(B)$ per number. Total time is $O(nB)$, which is $O(n)$ because $B$ is fixed by the 31-bit constraint.
- **Auxiliary Space Complexity:** $O(nB)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
