# Guided Example: Read N Characters Given read4 II - Call Multiple Times

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"content": "abc", "requests": [1, 2, 1]}`
- **Required output:** `["a", "bc", ""]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a `file` and assume that you can only read the file using a given method `read4`, implement a method `read` to read `n` characters. Your method `read` may be **called multiple times**.

The objective is to compute `["a", "bc", ""]` from `{"content": "abc", "requests": [1, 2, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Preserve characters fetched for a later call

`read4` may advance the file pointer by more characters than the current
`read` call requests. If the file begins `"abcd"` and the caller asks for one
character, `read4` still fetches four. Returning `"a"` while discarding
`"bcd"` would make the next call start at the wrong logical position.

The solution therefore keeps a four-slot staging buffer as object state:

- `buf4` stores the most recently fetched block;
- `size` is the number of valid characters in that block;
- `i` is the index of the next valid character that has not yet been
  returned to a caller.

The unread portion is `buf4[i:size]`. These fields are created
in `__init__`, so they survive between calls to `read` on the same solution
object. At construction both counts are zero, meaning no buffered character is
available.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"content": "abc", "requests": [1, 2, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Consume buffered data before touching the file

Each `read(buf, n)` uses a local counter `j`, the number of characters written
for this particular call. The outer loop continues while `j < n`.

At its start, the method checks `i == size`. Equality means every
valid character from the previous block has been consumed. Only then does it
call `read4(buf4)`, save the returned count in `size`, and reset
`i` to zero.

This order is essential. Calling `read4` while `i < size` would
overwrite unread characters in the staging buffer. Since the file pointer has
already moved past them, those characters could never be recovered.

If a refill returns zero, the file is exhausted. The method breaks and returns
however many characters it supplied during this call. A return of one through
four creates a new valid interval `[0, size)`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Copy until either side reaches its limit

The inner loop has two conditions: `j < n` and `i < size`.
For each iteration, it copies the next staged character into `buf[j]`, then
increments both indices.

The loop can stop for two distinct reasons:

- `j == n`: the caller has received its requested number. Any staged
  characters from `i` through `size - 1` remain untouched for the
  next call.
- `i == size`: the current staging block is exhausted. If the caller
  still needs more, control returns to the outer loop, which refills it.

Separating the requested count from the staging-buffer count prevents mixing
positions from different coordinate systems. `j` always starts at zero for a
new destination request, whereas `i` deliberately retains its old value
across requests.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["a", "bc", ""]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"content": "abc", "requests": [1, 2, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["a", "bc", ""]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Queue of leftovers:** A deque can express pending characters naturally, but its size never exceeds three here, so an indexed four-slot array is simpler and has the same $O(1)$ bound.
- **Single-call strategy:** Discarding the unused part of a fetched block works for ID 157 but is incorrect when this method may be called again.
- **Read one character per loop:** The competitive variant does this with the same persistent state; chunking through an inner loop reduces repeated branch checks.
- **Request smaller than remaining buffer:** No API call occurs, and the unused suffix remains for the next request.
- **Request spans several blocks:** The inner loop exhausts a block, and the outer loop refills until the request or file ends.
- **Short final block:** Its valid count prevents stale positions from being copied; leftovers can still survive to the next call.
- **Repeated calls after EOF:** They return zero; an optional persistent EOF flag could avoid repeated zero-result API calls.
- **Same destination object:** Each call writes from `buf[0]` as specified; persistent reader state is independent of the destination's earlier contents.
- **New test case:** Construct a new solution instance so old buffer indices do not persist across files.
- **Platform contract:** `read4` owns the file pointer and is supplied by the harness; only its returned prefix is valid.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. For one call requesting `n` characters, let $k \le n$ be the number returned.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
