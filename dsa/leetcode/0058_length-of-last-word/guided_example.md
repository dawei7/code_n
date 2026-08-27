# Guided Example: Length of Last Word

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "Hello World"}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s` consisting of words and spaces, return *the length of the **last** word in the string.*

The objective is to compute `5` from `{"s": "Hello World"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Search from the end because only the final word matters

Scanning from the beginning would require remembering the most recent completed word and continuing through the entire string. Starting at the end goes directly toward the answer. The only complication is that the string may end with spaces, which are not part of any word.

The source uses two backward scans. The first finds the final non-space character. The second finds the space immediately before that word, or moves past index 0 if the word begins the string.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "Hello World"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: First pointer: remove the trailing-space region conceptually

`i` starts at `len(s) - 1`, the final character index. While `s[i]` is a space, it decreases. No string is actually trimmed or copied; the pointer simply moves over the irrelevant suffix.

When this loop stops, `i` is the index of the final word's last character. The contract guarantees at least one word, so `i` cannot remain negative after all valid trailing spaces have been skipped.

For `"fly me   "`, `i` moves past the three trailing spaces and stops on `e`. For `"World"`, the final character is already non-space, so the loop performs no decrement.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `i` starts at `len(s) - 1`, the final character index.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Second pointer: locate the word's left boundary

`j` begins at `i` and moves left while characters are not spaces. Because a word is a maximal substring of non-space characters, this loop traverses exactly the last word.

It stops in one of two ways:

- `j` points to the separating space immediately before the word; or
- `j == -1`, meaning the word begins at index 0.

It is important that `j` stops *before* the first character of the word rather than on it. This makes one length formula handle both cases uniformly.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "Hello World"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **One backward loop with a counter:** Ignore spa:** - **One backward loop with a counter:** Ignore spaces until a word character is found, then count until the next space. This combines the two phases but encodes the phase in the counter.
- **Forward scan:** Reset a current length after spaces and save completed word lengths. It is linear and constant-space but necessarily inspects the whole prefix.
- **`strip` and `split`:** `len(s.strip().split()[-1])` is concise but allocates new strings and a token list, using $O(n)$ extra memory.
- **No trailing spaces:** The first loop does nothing; the second begins at the final word immediately.
- **Many trailing spaces:** They are skipped without affecting the count.
- **One word occupying the whole string:** `j` reaches `-1`, and `i-j` returns the full length.
- **Single-letter last word:** The second loop moves left once, producing length 1.
- **Leading spaces:** They are irrelevant once the left boundary of the last word is found.
- **All spaces outside the contract:** The first loop would make `i = -1`, and the method would return zero; valid inputs always contain a word.
- **Literal-space definition:** The source intentionally checks `' '` rather than all Unicode whitespace because the contract names only English letters and spaces.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. If there are $t$ trailing spaces and the final word has length $w$, the method examines $t+w$ characters. This is at most the full string length $n$, so worst-case time is $O(n)$. It may stop much earlier when the last word is near the end.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
