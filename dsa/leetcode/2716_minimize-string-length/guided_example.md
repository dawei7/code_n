# Guided Example: Minimize String Length

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aaabc"}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, you have two types of operation:

The objective is to compute `3` from `{"s": "aaabc"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce the problem to how many character kinds must survive

The operations describe positions, directions, and the closest equal character, so the process initially looks as though it requires a careful simulation. The key simplification is to ask what can happen to one letter independently of every other letter.

Suppose the string contains several copies of `'a'`. Choosing any surviving `'a'` lets us delete the closest `'a'` on one side whenever such a copy exists. The operation never changes an `'a'` into another letter, and deleting an `'a'` has no direct effect on the number of copies of `'b'`, `'c'`, or any other character. Therefore each distinct character can be analyzed separately.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aaabc"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why every distinct character contributes at least one

An operation deletes an occurrence of character `c` only by choosing another occurrence of that same `c`. Consequently, deleting a copy requires a different copy to act as the anchor. Once only one `c` remains, there is no second `c` to its left or right, so that last occurrence cannot be removed.

This gives an unavoidable lower bound: every character that appears in the original string must appear at least once in the final string. If the input contains $D$ distinct letters, no legal sequence can make the length smaller than $D$.

This is stronger than merely observing that the operations preserve character values. It explains the exact obstruction: the final occurrence has no equal partner that could delete it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | An operation deletes an occurrence of character `c` only by ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why all duplicate occurrences really can be deleted

The lower bound is useful only if it is attainable. Fix one character `c` that occurs $r$ times. If $r>1$, select any occurrence that has another `c` on its left or right. The corresponding operation removes the closest equal occurrence on that side, reducing the count from $r$ to $r-1$.

Repeat while at least two copies remain. At every intermediate count greater than one, some pair of occurrences exists. Take the left occurrence of any adjacent pair of `c` occurrences in their current order and delete the closest `c` to its right. That right occurrence is guaranteed to exist and to be the closest equal character in that direction. Thus the rule about “closest” never prevents progress.

After $r-1$ deletions, exactly one `c` remains. Performing this independently for every distinct character leaves exactly one occurrence of each kind, for total length $D$. Since $D$ is both a lower bound and achievable, it is the minimum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aaabc"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Frequency array:** Count the 26 lowercase lett:** - **Frequency array:** Count the 26 lowercase letters and return how many counts are positive; it has the same $O(n)$ time and fixed $O(1)$ space but is more verbose than a set.
- **Repeated deletion simulation:** Can reproduce a valid operation sequence, but mutable-string deletions and searches add unnecessary work because only distinctness affects the answer.
- **Sort and count changes:** Sorting the characters and counting new groups works in $O(n\log n)$ time, which is slower than hashing.
- **Single-character string:** Its only occurrence cannot be deleted, so the set size and answer are one.
- **All characters equal:** Every copy except one is removable, producing answer one.
- **All characters distinct:** No operation is possible because no selected character has an equal occurrence on either side; the answer remains $n$.
- **Separated duplicates:** Equal characters need not be adjacent. The closest-equal rule still permits deleting one copy because intervening different letters do not matter.
- **Changing indices:** Indices shift after conceptual deletions, but the set computation deliberately avoids depending on them.
- **Lowercase guarantee:** The fixed 26-letter alphabet is what turns $O(D)$ set storage into the manifest's $O(1)$ bound.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `s` and let $D$ be its number of distinct characters. Building `set(s)` examines all $n$ characters, so the expected running time is $O(n)$. Hash-table operations on individual one-character strings are expected $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
