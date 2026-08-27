# Guided Example: Split a String in Balanced Strings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "RLRRLLRLRL"}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

**Balanced** strings are those that have an equal quantity of `'L'` and `'R'` characters.

The objective is to compute `4` from `{"s": "RLRRLLRLRL"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Represent balance with one number

A substring is balanced when it contains the same number of `L` and `R` characters. Instead of maintaining two counts, the solution maintains their difference. The variable `l` increases by one for `L` and decreases by one for `R`. After reading a segment, `l == 0` exactly when the segment has equal counts.

At the beginning, `ans = l = 0` initializes both the number of completed balanced pieces and the running difference. The statement guarantees that every character is either `L` or `R`, so the code’s `else` branch can safely treat every non-`L` character as `R`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "RLRRLLRLRL"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: What the running balance means

Because the balance is zero whenever a piece ends, it can be read in either of two equivalent ways:

- It is the difference between the total numbers of `L` and `R` in the prefix processed so far.
- After the latest cut, it is the difference inside the unfinished current piece.

When `l` returns to zero, all characters since the previous cut form a balanced substring. The solution immediately counts that substring by incrementing `ans`. It then continues scanning; no explicit reset is necessary because `l` is already zero.

For `s = "RLRRLLRLRL"`, the balance values are \(-1,0,-1,-2,-1,0,-1,0,-1,0\). Zeros appear after prefixes of lengths 2, 6, 8, and 10. Cutting at those positions gives `"RL"`, `"RRLL"`, `"RL"`, and `"RL"`, so the returned count is four.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Because the balance is zero whenever a piece ends, it can be... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why making the earliest possible cut is safe

It might seem that an early balanced prefix should sometimes be merged with later characters to allow more pieces elsewhere. Merging cannot help the objective, which is to maximize the number of pieces. Once a prefix is balanced, taking it as its own piece leaves the remaining suffix balanced as well.

To see why, the entire input has equal total counts. Subtracting a prefix with equal counts leaves equal counts in the suffix. Thus an early cut never makes the remainder impossible to partition. Keeping that prefix attached to a later balanced portion can produce one larger balanced piece, but separating the two yields at least as many pieces.

There is also a clean upper-bound argument. In any valid split, each piece boundary occurs at the end of a globally balanced prefix. The first several balanced pieces together still contain equal total numbers of `L` and `R`, so the running prefix difference must be zero at every chosen boundary. Therefore, a valid split cannot contain more pieces than the number of zero-balance prefixes seen during the scan.

The algorithm cuts at every such zero prefix. Consecutive zero boundaries define substrings whose individual balance is zero minus zero, hence zero. It reaches the upper bound and is therefore optimal.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "RLRRLLRLRL"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two explicit counters:** Track counts of `L` a:** - **Two explicit counters:** Track counts of `L` and `R` separately and cut when they are equal. This remains \(O(n)\) time and \(O(1)\) space, but the signed difference expresses the condition with one state variable.
- **Stack simulation:** Push one symbol and cancel it with the other. It can detect balance but uses up to \(O(n)\) memory for information a single integer already captures.
- **Dynamic programming over cut positions:** Testing every balanced substring would be much more expensive. The zero-prefix characterization makes such optimization unnecessary.
- **One balanced piece only:** If the running difference returns to zero only at the final character, the maximum is one.
- **Alternating characters:** A string such as `"LRLRLR"` reaches zero every two characters, producing the maximum possible \(n/2\) pieces.
- **Input begins with either symbol:** The sign convention is arbitrary. Starting with `R` makes `l` negative, but only equality to zero matters.
- **Guaranteed final balance:** The problem promises that `s` itself is balanced, so the final character brings `l` to zero and all characters are included. Without that guarantee, the code would count balanced prefixes but leave an unbalanced suffix.
- **Even length:** Every balanced string has equal counts and therefore even length. The constraints need not state this separately because it follows from the guarantee.
- **Invalid characters:** The exact `else` branch treats anything other than `L` as `R`. This is correct only because the input alphabet is guaranteed to be exactly those two characters.
- **Returning boundaries:** If the task required the actual split, record the current index whenever `l` becomes zero. That would use \(O(ans)\) output space but would not change the greedy reasoning.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let \(n=\lvert\texttt{s}\rvert\). The loop reads every character once and performs constant work, so time complexity is \(O(n)\). Any correct algorithm needs to inspect the input in the worst case because changing an unread character can alter where balance is reached, making this linear bound optimal.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
