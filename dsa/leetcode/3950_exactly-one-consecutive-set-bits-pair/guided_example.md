# Guided Example: Exactly One Consecutive Set Bits Pair

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 100000}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n`.

The objective is to compute `false` from `{"n": 100000}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Read one bit at a time

The expression

`cur = n & 1`

extracts the least significant bit:

- an odd `n` has `cur = 1`;
- an even `n` has `cur = 0`.

After inspecting that bit, the source executes

`n = n >> 1`.

Right shift discards the bit just processed and moves the next binary position into the least significant place. Repeating these two operations visits every bit exactly once from right to left.

The parameter `n` is only a local integer binding. Shrinking it does not mutate caller-owned data because Python integers are immutable.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 100000}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Remember the neighboring bit

`pre` stores the bit processed during the preceding loop iteration. Since traversal moves through consecutive bit positions, `pre` and `cur` always represent one adjacent pair in the original binary representation.

Before the first real bit, `pre` is initialized to zero. This behaves like an implicit leading zero below the least significant position and cannot create a false `11` match.

The chained comparison

`pre == cur == 1`

is true exactly when both neighboring bits are one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `pre` stores the bit processed during the preceding loop ite... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Distinguish one pair from two pairs

`vis` means that an adjacent `11` pair has already been encountered.

When a pair is found:

- if `vis` is false, the source sets it to true and continues;
- if `vis` is already true, this is a second pair and the source returns false immediately.

After every iteration, `pre = cur` prepares the next adjacent comparison.

When all set bits have shifted out and `n` becomes zero, the loop ends. Returning `vis` distinguishes the two remaining cases:

- false means no adjacent pair ever appeared;
- true means exactly one appeared, because a second would already have returned false.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 100000}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Shift-and-AND mask:** `pairs = n & (n >> 1)` m:** - **Shift-and-AND mask:** `pairs = n & (n >> 1)` marks all adjacent `11` pairs. Testing `pairs != 0 and pairs & (pairs - 1) == 0` checks whether exactly one marked position exists. This is the manifest's summarized algorithm, not the source.
- **Convert to a binary string:** Count occurrences of `"11"` with overlapping positions. A naive non-overlapping substring count can mishandle `"111"`, and string allocation is unnecessary.
- **Count runs of ones:** A run of length $r$ contributes $r-1$ adjacent pairs, not merely one run. The source's pairwise scan avoids that confusion.
- **`n = 0`:** The loop is skipped and `vis` is false, correctly reporting no pair.
- **One set bit:** No neighboring set bit exists, so the result is false.
- **Exactly two consecutive ones:** They create one pair and return true if no other pair occurs.
- **Three consecutive ones:** They create two overlapping pairs and return false.
- **Two separated `11` runs:** The first sets `vis` and the second triggers the early false return.
- **Leading zeroes:** Standard binary representation omits them, and adding leading zeroes would never create a new `11` pair anyway.
- **Trailing zero bits:** They are processed normally and separate any later set bit from the previous one.
- **Early exit:** Once two pairs exist, unprocessed higher bits cannot restore validity, so returning immediately is safe.
- **Local right shifts:** Rebinding `n` has no external side effect.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L)$. Let $L$ be the number of bits in `n`, with $L=1$ for the representation of zero. For positive input, the loop runs once per significant bit, so time is $O(L)=O(\log(n+1))$. It may terminate earlier after finding a second pair.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
