# Guided Example: Circular Sentence

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"sentence": "leetcode exercises sound delightful"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **sentence** is a list of words that are separated by a** single** space with no leading or trailing spaces.

The objective is to compute `true` from `{"sentence": "leetcode exercises sound delightful"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce the sentence to word boundaries

A sentence is circular when every word's last character matches the next word's first character, including the connection from the final word back to the first. Characters inside a word do not affect this condition.

The exact solution calls `sentence.split()` to create the word list `ss`. Under the stated input format, words are separated by one space with no spaces at either end, so this produces exactly the intended words.

For each pair consisting of index `i` and word `s`, the generator checks

`s[-1] == ss[(i+1)%n][0]`.

Here `s[-1]` is the last character of the current word, while index zero selects the first character of the next word.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"sentence": "leetcode exercises sound delightful"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Modulo makes the last edge wrap around

For every index except the last, `i+1` is the ordinary next word index. At `i=n-1`, the expression `(i+1)%n` becomes `n%n=0`, selecting the first word.

This treats the words as vertices arranged on a cycle. There are exactly `n` required directed connections:

$$
0\to1,\ 1\to2,\ \ldots,\ n-2\to n-1,\ n-1\to0.
$$

The modulo expression covers all of them with one uniform rule and no separate final comparison.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For every index except the last, `i+1` is the ordinary next ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why `all` expresses the contract

Python's `all` returns true only if every Boolean produced by the generator is true. Therefore, the method returns true precisely when all neighboring boundary comparisons succeed.

If one comparison fails, `all` short-circuits immediately and returns false; later comparisons cannot repair a broken circular link. If every comparison succeeds, each required link in the definition has been verified, so the sentence is circular.

This gives a direct correctness argument in both directions. A true return means each current word passed its equality with the next word, including wraparound. A genuinely circular sentence makes every generated equality true, so `all` returns true.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"sentence": "leetcode exercises sound delightful"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Direct space scan:** Check the character befor:** - **Direct space scan:** Check the character before each space against the character after it, plus the final-to-first comparison. This avoids the word list and achieves $O(1)$ auxiliary space.
- **Explicit word loop:** A regular loop can return false at the first mismatch and true afterward; it is equivalent to `all`.
- **Single word:** Compare its last and first characters; do not automatically return true.
- **Case difference:** Uppercase and lowercase characters must compare unequal.
- **Wraparound link:** Forgetting the last-word-to-first-word comparison accepts non-circular chains.
- **No leading or trailing spaces:** The contract ensures every word extracted from valid input is non-empty.
- **Short-circuit:** One failed boundary is sufficient to return false.
- **All boundaries equal:** Then every required edge is present and true is returned.
- **Input mutation:** `split()` creates new objects but does not modify the original string.
- **Manifest mismatch:** Space complexity must follow the materialized `ss` list in the actual source.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L)$. Let $L$ be the number of characters in `sentence` and $w$ the number of words. Splitting scans the sentence in $O(L)$ time. The generator checks $w$ word boundaries, so its work is $O(w)$ and is bounded by $O(L)$. Total time is $O(L)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
