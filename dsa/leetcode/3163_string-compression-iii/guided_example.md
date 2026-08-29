# Guided Example: String Compression III

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"word": "abcde"}`
- **Required output:** `"1a1b1c1d1e"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `word`, compress it using the following algorithm:

The objective is to compute `"1a1b1c1d1e"` from `{"word": "abcde"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: First identify maximal equal-character runs

The compression operation repeatedly removes the longest prefix consisting of one repeated character, but no chunk may be longer than 9.

`groupby(word)` partitions the string into maximal consecutive runs of the same character. For example,

`"aaabbcccc"`

becomes runs `("a",3)`, `("b",2)`, and `("c",4)`.

Run boundaries are forced: a chunk can never contain two different characters. Therefore, each maximal run can be compressed independently.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"word": "abcde"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Split a long run into maximum legal chunks

For one group, `c` is its character and iterator `v` yields the repeated occurrences. The code computes run length with

`k = len(list(v))`.

While characters remain, it chooses

`x = min(9, k)`.

This is the longest prefix allowed by the rule. It appends decimal count followed by the character, `str(x) + c`, then removes that many conceptually by `k -= x`.

For a run of length 14, chunks are 9 and 5, producing `"9a5a"`. For a run length at most 9, one iteration encodes the whole run.

Because $x$ is between 1 and 9, the count is always one digit and decoding boundaries remain clear: count, then character, repeatedly.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why group-first processing matches prefix removal

At any point in the original algorithm, the remaining word begins inside one maximal run. The maximum single-character prefix has length equal to the remaining portion of that run, capped at 9. Choosing `min(9,k)` makes exactly that operation.

After consuming a chunk shorter than the whole run only because of the cap, the next prefix has the same character and is processed again. Once the run is exhausted, the next `groupby` group is exactly the next prefix character.

Thus the grouped implementation produces the identical chunk sequence as literal repeated slicing from the front, without modifying the string.


Consider a maximal run of character $c$ and length $r$. The loop emits chunks whose sizes are 9 until the remaining length is at most 9, then emits that remainder. Every size is legal, their sum is $r$, and each is the largest legal prefix at its step.

Runs cover every input position exactly once and do not overlap. Concatenating their encodings therefore accounts for every character in order and applies the specified operation at every step. `"".join(ans)` returns exactly `comp`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"1a1b1c1d1e"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"word": "abcde"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"1a1b1c1d1e"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Two-pointer scan:** Measure each run with indices and emit chunks as its length is known. It avoids materializing group characters and can use $O(1)$ working space excluding output.
- **Streaming counter:** Track current character and count, flushing a chunk whenever count reaches 9 or the character changes.
- **Repeated front slicing:** It mirrors the statement but can copy string suffixes repeatedly and approach quadratic time.
- **Run length exactly nine:** It emits one `9c` chunk.
- **Run length ten:** It must emit `9c1c`, not a two-digit count.
- **Single character:** It becomes count 1 followed by that character.
- **Alternating characters:** Every run length is one, so compressed output is twice the input length.
- **Very long run:** The while loop emits as many 9-sized chunks as needed and one optional remainder.
- **Same character in separated runs:** Other characters between them prevent merging; `groupby` keeps them distinct.
- **Lowercase alphabet:** Counts and characters are unambiguous because each count is one digit and each symbol one character.
- **Group iterator consumption:** `list(v)` fully consumes each shared iterator before the outer `groupby` advances.
- **Output construction:** Accumulating parts and joining avoids repeated immutable-string concatenation costs.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the word length.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
