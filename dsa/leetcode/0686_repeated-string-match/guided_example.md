# Guided Example: Repeated String Match

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"a": "abcd", "b": "cdabcdab"}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two strings `a` and `b`, return *the minimum number of times you should repeat string *`a`* so that string* `b` *is a substring of it*. If it is impossible for `b`​​​​​​ to be a substring of `a` after repeating it, return `-1`.

The objective is to compute `3` from `{"a": "abcd", "b": "cdabcdab"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The unavoidable lower bound on the repeat count

A string made from `r` copies of `a` has length `r m`. It cannot contain `b` unless its total length is at least `n`. Thus any answer must satisfy

$$
r m \ge n.
$$

The smallest integer that satisfies this condition is

$$
q=\left\lceil\frac{n}{m}\right\rceil.
$$

The code stores this lower bound in `ans`. It also constructs `t = [a] * ans`, a list containing `ans` references to `a`. Joining that list produces the repeated candidate string.

Starting at this lower bound matters for minimality. Every smaller repeat count is too short even before character content is considered, so there is no reason to test it.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"a": "abcd", "b": "cdabcdab"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why only one extra copy is theoretically necessary

The infinitely repeated string

`aaaa...`

is periodic with period `m`. If `b` occurs anywhere in it, an equivalent starting alignment occurs at some offset from `0` through `m - 1` within a copy of `a`. There are only `m` distinct alignments modulo the period.

The lower-bound string of `q` copies already has length at least `n`. It can contain every occurrence that starts at offset zero and ends early enough. An occurrence beginning at a positive offset may extend beyond its right boundary. Adding one more full copy supplies `m` additional characters, enough for any start offset smaller than `m`:

$$
\text{offset}+n \le (m-1)+n \le (q+1)m.
$$

Therefore, if `b` is a substring of any number of repetitions, it must already be a substring of either `a` repeated `q` times or `a` repeated `q+1` times.

The exact code loops three times, so it checks repeat counts `q`, `q+1`, and `q+2`. The third check is redundant under the proof above, but harmless. It cannot produce a nonminimal answer: if `b` could first appear at `q+2`, periodicity says it would already have appeared by `q+1`. In a correct substring implementation, the third attempt can only repeat the conclusion that no occurrence exists.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The infinitely repeated string

`aaaa...`

is periodic with ... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: What happens in each loop iteration

At the start of an iteration, `t` contains exactly `ans` copies of `a`.

The expression `''.join(t)` materializes the current repeated string. The membership test

`b in ''.join(t)`

asks whether `b` occurs contiguously anywhere in it.

If the answer is true, the method immediately returns `ans`. Because the tested counts increase one at a time from the length lower bound, this is the minimum possible repeat count.

If the membership test fails, `ans` is increased and one more copy of `a` is appended to `t`. The next iteration tests the next repeat count. After all three attempts fail, the method returns `-1`.

The final increment and append after the third failed test are never examined. They do not affect the return value; they are simply a consequence of placing the update at the bottom of every loop iteration.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"a": "abcd", "b": "cdabcdab"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **KMP over a virtual repeated string:** Build th:** - **KMP over a virtual repeated string:** Build the prefix table for `b` and scan characters of repeated `a` by modular indexing. This gives an explicit deterministic `O(m+n)` search guarantee and avoids materializing every candidate, but its prefix-function logic is longer.
- **- **Rabin–Karp rolling hash:** Rolling hashes can :** - **Rabin–Karp rolling hash:** Rolling hashes can test all periodic alignments efficiently. A direct character verification is needed after a hash match to eliminate collision risk.
- **- **Only two attempts:** Testing `q` and `q+1` is :** - **Only two attempts:** Testing `q` and `q+1` is sufficient by periodicity. The exact three-iteration loop performs one unnecessary final test without changing correctness.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m+n)$. Let `m = len(a)` and `n = len(b)`. The largest relevant repeated string has length at most `n + 2m`, which is `O(m+n)`. The exact loop performs only three iterations, a constant independent of input sizes.
- **Auxiliary Space Complexity:** $O(m+n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
