# Guided Example: Decode the Message

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"key": "the quick brown fox jumps over the lazy dog", "message": "vkbs bs t suepuv"}`
- **Required output:** `"this is a secret"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given the strings `key` and `message`, which represent a cipher key and a secret message, respectively. The steps to decode `message` are as follows:

The objective is to compute `"this is a secret"` from `{"key": "the quick brown fox jumps over the lazy dog", "message": "vkbs bs t suepuv"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The key's first distinct letters define a decoding dictionary

The cipher table is determined by the order in which distinct lowercase letters first appear in `key`. The first distinct key letter maps to plain `a`, the second maps to `b`, and so on through the twenty-sixth mapping to `z`.

The solution stores these substitutions in dictionary `d`. It begins with `{" ": " "}` because spaces must survive unchanged. Preloading the space also ensures that spaces encountered while scanning `key` do not consume a position in the alphabet.

The integer `i` counts how many distinct lowercase key letters have been mapped. It starts at zero, so the first new letter maps to `ascii_lowercase[0]`, which is `a`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"key": "the quick brown fox jumps over the lazy dog", "message": "vkbs bs t suepuv"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Ignore every repeated appearance after the first

The loop visits key characters from left to right. For each character `c`, it checks `if c not in d`. If `c` is a new lowercase letter, the method assigns

`d[c] = ascii_lowercase[i]`

and increments `i`. If it is a repeated letter, its existing mapping remains unchanged and `i` does not move.

This precisely implements “use the first appearance.” Once a key character has been assigned its alphabet position, later copies cannot overwrite it.

For a partial key beginning `"happy boy"`, the first new characters are `h`, `a`, `p`, `y`, `b`, and `o`. They receive `a`, `b`, `c`, `d`, `e`, and `f`. The second `p` and the spaces are already in `d` and are skipped.

The source guarantees that every lowercase English letter appears in the key at least once. At the end of the scan, `d` therefore contains mappings for all 26 letters plus space, and `i` has advanced exactly 26 times.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The loop visits key characters from left to right.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Translate the message in its original order

The return expression

`"".join(d[c] for c in message)`

looks up each message character and yields its decoded replacement. `join` concatenates those replacements in the same order, producing the final plaintext string.

A lowercase cipher character uses the mapping established by its first key appearance. A space uses the preinstalled mapping to another space. The message constraints guarantee no other character type, so every lookup succeeds.

Repeated message letters are translated repeatedly to the same plaintext letter because the dictionary is fixed after key processing. The procedure is substitution, not stateful decoding; one message character never changes the meaning of a later one.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"this is a secret"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"key": "the quick brown fox jumps over the lazy dog", "message": "vkbs bs t suepuv"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"this is a secret"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **A 26-entry array indexed by character code:** :** - **A 26-entry array indexed by character code:** Record each cipher letter's plaintext character at `ord(c) - ord('a')`. This has the same asymptotic bounds but needs a separate branch for spaces and explicit index arithmetic.
- **Build an ordered distinct-key string first:** Remove spaces and duplicates, then zip with the alphabet. This can be readable but may create extra strings or sets; the one-pass dictionary builds the mapping directly.
- **Use the last appearance of each key letter:** Overwriting mappings would violate the first-appearance order and could assign several alphabet positions incorrectly.
- **Advance `i` for spaces:** Spaces are not one of the 26 substitution letters. Preloading them in `d` ensures they never consume an alphabet position.
- **Advance `i` for repeated letters:** Only newly discovered characters advance the substitution order. Repeats must be ignored.
- **Map plaintext to cipher instead of cipher to plaintext:** Decoding needs to look up each encrypted message character and retrieve its regular alphabet replacement. Reversing the dictionary would require another inversion step.
- **Key begins with spaces:** They are already mapped and skipped; the first lowercase letter still receives `a`.
- **Many repeated letters before a new one:** Repetition leaves both the existing mapping and `i` unchanged, preserving first-distinct order.
- **Message contains only spaces:** Every character maps to itself, so the returned string is identical.
- **Message repeats one cipher letter:** Each occurrence receives the same decoded character, as a substitution cipher requires.
- **All 26 letters guaranteed:** No message lowercase lookup can fail because every letter has a key mapping by the end of the first pass.
- **Missing-letter invalid input:** The contract excludes it. If a missing key letter appeared in the message, direct dictionary lookup would raise an error rather than invent a mapping.
- **Non-lowercase characters:** The source excludes them. The mapping covers only lowercase English letters and space.
- **Input preservation:** Both strings are read only, and the result is newly constructed.
- **Output length:** Substitution replaces each input character with exactly one character, so decoded length equals message length.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(k + m)$. Let `k` be the key length and `m` the message length. The first loop examines each key character once, with expected constant-time dictionary membership and insertion. Decoding examines each message character once, and joining writes an output of length `m`. Total expected time is `O(k + m)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
