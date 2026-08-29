# Guided Example: Read N Characters Given Read4

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"content": "abc", "n": 4}`
- **Required output:** `"abc"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a `file` and assume that you can only read the file using a given method `read4`, implement a method to read `n` characters.

The objective is to compute `"abc"` from `{"content": "abc", "n": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Bridge a four-character API to an arbitrary request

The solution cannot inspect the file directly. Its only way to advance the
file pointer is `read4(buf4)`, which writes up to four consecutive characters
into a supplied temporary buffer and returns how many positions it filled.

The requested method has a different interface: place at most `n` characters
in `buf` and report how many were actually copied. The file may end before
`n`, and `n` may not be divisible by four. Therefore the method needs two
counts:

- `v`, the number returned by the most recent `read4`;
- `i`, the number of characters already copied into the destination.

The selected source allocates `buf4 = [0] * 4`. Its initial numeric values are
only placeholders; every position below the count returned by `read4` is
replaced with a real character before being read.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"content": "abc", "n": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use a short block as the end-of-file signal

The loop continues while `v >= 4`. Before the first call, `v` is set to five
only to enter the loop. It is not a claim that five characters were read.

After calling `read4(buf4)`, there are three possible results:

- four means a complete block was available, so the file may still contain
  more characters;
- one, two, or three means those characters are the final partial block;
- zero means the file pointer was already at end of file.

The contract of `read4` makes a return smaller than four an end-of-file signal.
After copying that partial result, the next loop check fails, so another API
call is unnecessary.

The loop does not use `i < n` as its outer condition. Instead, the inner copy
returns immediately when `i` reaches `n`. Either organization can work; here
the early return is the protection against placing too many characters in the
destination.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Copy only the positions reported as valid

For each API result `v`, the source iterates `j` from zero through `v - 1`.
Only those positions in `buf4` were written by the current call. Reading all
four positions after a short call would copy stale data left from an earlier
block, so the returned count must control the copy loop.

Each valid temporary character is assigned to `buf[i]`, then `i` is
incremented. If `i >= n`, the method returns `n` immediately. Since `i`
increases by exactly one after each successful assignment and begins at zero,
the first such event is exactly `i == n`; no destination position at index
`n` is written.

If the loop ends because `read4` returned fewer than four, then every remaining
file character has been copied unless the early limit return occurred. The
method returns `i`, the actual number copied.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"abc"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"content": "abc", "n": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"abc"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Direct block writes in pointer-based languages:** Full groups of four can be written directly into the correct destination offset, avoiding a second character-by-character copy; Python's given API still expects a separate list buffer.
- **Preserve leftover characters:** Required by the follow-up where `read` may be called repeatedly, but unnecessary under the single-call guarantee.
- **Read one character at a time conceptually:** Impossible because the only permitted file interface advances in blocks of up to four.
- **File shorter than `n`:** A short return is copied completely, then its size stops the loop.
- **File length divisible by four:** If more characters are requested, a final zero-length API call is needed to discover EOF.
- **`n` smaller than four:** One block may be fetched, but the early return prevents more than `n` destination writes.
- **Stale temporary positions:** Only indices below `v` are valid after a call; the loop correctly ignores all others.
- **Destination capacity:** The contract guarantees room for `n`, and the source never writes beyond index `n - 1`.
- **Single-call dependency:** Fetched but uncopied characters are discarded; this solution must not be reused unchanged for multiple `read` calls.
- **Platform API:** `read4` and its file pointer are harness-provided; the solution should not attempt to manipulate the file directly.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(k)$. Let $k$ be the number of characters actually copied, where
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
