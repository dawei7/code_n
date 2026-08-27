# Guided Example: Substrings That Begin and End With the Same Letter

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abcba"}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** string `s` consisting of only lowercase English letters. Return *the number of **substrings** in *`s` *that begin and end with the **same** character.*

The objective is to compute `7` from `{"s": "abcba"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A substring is determined by its two endpoint positions

For a substring to be valid, its first and last characters must match. The characters between them can be anything. Therefore, when the scan reaches a position that will serve as the substring's right endpoint, the only useful historical information is how many times the same character has appeared up to that point.

The solution processes `s` from left to right. `cnt` maps each character to the number of occurrences seen in the current prefix, and `ans` stores the total number of valid substrings counted so far.

For each current character `c`, it performs:

`cnt[c] += 1`

followed by

`ans += cnt[c]`.

The order is important. Incrementing first includes the current occurrence itself, which represents the one-character substring beginning and ending at the current position.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abcba"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the current frequency equals the number of new substrings

Suppose the current character `c` is its $t$th occurrence in the string. After incrementing, `cnt[c] = t`.

There are exactly $t$ valid choices for the starting position of a substring that ends here:

- each of the previous $t-1$ occurrences of `c` can be the left endpoint;
- the current occurrence itself can be the left endpoint, producing a substring of length one.

Each starting occurrence determines one unique contiguous substring from that position through the current position. All those substrings begin and end with `c`, so they are valid. No other starting position works with this right endpoint because its character would differ from `c`.

Therefore, adding `cnt[c]` counts exactly all new valid substrings whose right endpoint is the current character.

For `s = "abcba"`, the running additions are:

- first `a`: its frequency becomes 1, adding the substring `"a"`;
- first `b`: its frequency becomes 1, adding `"b"`;
- `c`: its frequency becomes 1, adding `"c"`;
- second `b`: its frequency becomes 2, adding the one-character `"b"` and `"bcb"`;
- second `a`: its frequency becomes 2, adding the one-character `"a"` and `"abcba"`.

The total is $1+1+1+2+2=7$.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Suppose the current character `c` is its $t$th occurrence in... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Count occurrences by position, not distinct substring text

The problem asks for substrings, which are defined by their positions in the original string. Two substrings with the same textual content but different positions are separate occurrences and must both be counted.

For example, in `"aaa"` there are three length-one substrings `"a"` at different positions, two length-two substrings `"aa"`, and one length-three substring `"aaa"`. The running frequencies are 1, 2, and 3, whose sum is 6. Using a set of substring strings would incorrectly collapse duplicates and return only three distinct texts.

The counter approach naturally respects positions because every right endpoint is processed separately and every earlier matching occurrence supplies a separate left endpoint.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abcba"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerating all substrings:** There are $O(n^2:** - **Enumerating all substrings:** There are $O(n^2)$ endpoint pairs, and materializing their text can cost even more. The prefix count groups all matching starts for one right endpoint into one addition.
- **Final frequency formula:** Count every character first, then sum $m(m+1)/2$ over frequencies. This is also $O(n)$ and correct; the exact source accumulates the same triangular numbers during the first pass.
- **Set of substring strings:** This answers how many distinct textual values exist, not how many positional substrings satisfy the endpoint rule. Duplicate occurrences must remain separate.
- **Checking only adjacent equal characters:** Valid endpoints can be arbitrarily far apart, and the middle characters are unrestricted.
- **Incrementing after adding:** If `ans += cnt[c]` occurred before `cnt[c] += 1`, every one-character substring would be omitted. Incrementing first includes the current position as both endpoints.
- **Single-character string:** The first frequency becomes one, so the method returns one.
- **All characters different:** Every frequency is one when encountered, and only the $n$ one-character substrings are counted.
- **All characters equal:** The additions are $1,2,\ldots,n$, producing $n(n+1)/2$, which counts every possible substring.
- **Repeated textual substrings:** Different start or end positions remain separate choices and are counted independently.
- **Large answer:** The maximum can exceed 32-bit range. Python handles it directly; fixed-width implementations should use a 64-bit integer.
- **Fixed lowercase alphabet:** This guarantee makes the counter's storage constant. A more general character domain would change only the space analysis, not the counting logic.
- **No input mutation:** The string is read once from left to right, and all state resides in `cnt` and `ans`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `s`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
