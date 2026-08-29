# Guided Example: Count Words Obtained After Adding a Letter

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"startWords": ["ant", "act", "tack"], "targetWords": ["tack", "act", "acti"]}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two **0-indexed** arrays of strings `startWords` and `targetWords`. Each string consists of **lowercase English letters** only.

The objective is to compute `2` from `{"startWords": ["ant", "act", "tack"], "targetWords": ["tack", "act", "acti"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Encode a letter set as a 26-bit integer

Assign bit $0$ to `'a'`, bit $1$ to `'b'`, and so on through bit $25$ for `'z'`. For a character `c`, the expression `1 << (ord(c) - 97)` creates an integer with only that character’s bit set. The code builds a word’s mask with `sum(1 << (ord(c) - 97) for c in w)`.

Usually bit masks are combined with bitwise OR. Summation is equally correct here because the constraints guarantee no letter repeats within a word. Every added power of two occupies a different bit, so no carries occur. For example, `"act"` maps to the bits for `a`, `c`, and `t` regardless of the letters’ order.

Two words containing exactly the same letters produce the same mask. That is desirable because arbitrary rearrangement makes them interchangeable for this problem.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"startWords": ["ant", "act", "tack"], "targetWords": ["tack", "act", "acti"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Store all possible predecessor masks

The set comprehension converts every string in `startWords` and stores its mask in `s`. A set provides expected $O(1)$ membership testing. If multiple start words have the same letter set in different orders, they collapse to one mask, but multiplicity is irrelevant: a target only asks whether any qualifying start word exists, and start words are not consumed or changed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Reverse the mandatory addition

For each target word `w`, the solution first computes its complete mask `x`. It then tries every character `c` in that target and evaluates `x ^ (1 << (ord(c) - 97))`.

The target contains `c` exactly once, so its bit is currently set in `x`. XOR with the same one-bit mask turns that bit off and leaves every other bit unchanged. The result is exactly the letter set obtained by deleting `c` from the target.

If that reduced mask occurs in `s`, there is a start word containing all the target’s other letters and not containing `c`. Appending `c` is legal because it was absent from the start word. The resulting letter set equals the target’s, and arbitrary rearrangement can place those letters in the target’s order. The target is therefore obtainable.

The solution increments `ans` and immediately executes `break`. A target must be counted once even if several different deletions match start words. Breaking prevents multiple successful predecessor choices from counting the same target repeatedly.

If none of the target’s deletions produces a stored start mask, no conversion can form it. Any legal conversion adds one of the target’s letters; reversing that addition would have appeared among the tested deletions. The target contributes nothing.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"startWords": ["ant", "act", "tack"], "targetWords": ["tack", "act", "acti"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort every word:** Sorting converts each word to an order-independent canonical string, after which every one-letter deletion can be tested. This is simpler conceptually but costs $O(\ell\log\ell)$ per word instead of linear mask construction.
- **Store sorted start words by length:** This can narrow candidates but still requires building deletion strings or sorting target variants. Bit removal is constant time after the target mask is built.
- **Try adding letters to every start word:** Each start has up to 26 possible additions, and generated results could be stored. This can work, but reversing the operation from each target tests only its own at most 26 letters and directly enforces the one-letter difference.
- **Bitwise OR instead of sum:** OR is the conventional mask construction and would produce the same result. Summation is safe only because no word contains a repeated letter.
- **Repeated letter outside the contract:** With duplicates, summing the same bit twice could carry into another bit and XOR deletion would no longer represent removing one occurrence. The uniqueness guarantee is essential to the exact encoding.
- **One-letter target:** Removing its only letter yields mask zero. It can match only an empty start word, but start words have minimum length one, so such a target is never obtainable.
- **Target length 26:** Every lowercase letter is already present. It can be formed from a 25-letter start word by adding its unique missing letter, and the deletion loop checks all 26 possibilities.
- **Same word in both arrays:** Equality alone does not qualify because one new letter must be appended. The deletion-based test correctly demands a predecessor with one fewer letter.
- **Anagram start words:** They map to the same mask. Collapsing them in `s` loses no useful information because only existence matters.
- **Duplicate target words:** Each array entry is checked independently. If a target value appears multiple times and is obtainable, each occurrence increments `ans` once.
- **Several matching predecessors:** The `break` ensures one target contributes exactly one to the count even if deleting different letters finds different start masks.
- **Missing predecessor:** Exhausting all target letters proves failure because every legal conversion has exactly one added letter that could be reversed.
- **Start words remain reusable:** The algorithm never removes masks from `s`. This matches the note that checking one target does not consume or modify a start word.
- **Letter order:** Masks deliberately erase order because the conversion permits arbitrary rearrangement after appending.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Define $L$ as the sum of the lengths of every word in `startWords` and `targetWords`. Building all start masks processes each start character once. For a target of length $\ell$, building `x` costs $O(\ell)$ and trying every possible deleted character costs another $O(\ell)$ expected time because each set lookup is expected $O(1)$. Summed across all words, total expected time is $O(L)$.
- **Auxiliary Space Complexity:** $O(s)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
