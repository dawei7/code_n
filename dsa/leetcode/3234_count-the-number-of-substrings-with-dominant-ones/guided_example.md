# Guided Example: Count the Number of Substrings With Dominant Ones

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "00011"}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a binary string `s`.

The objective is to compute `5` from `{"s": "00011"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

A substring is valid when its number of ones is at least the square of its number of zeros. If a substring contains $z$ zeros and $o$ ones, the condition is

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "00011"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 3

Checking all $O(n^2)$ substrings is too slow for $n$ up to $4\cdot10^4$. The square in the condition supplies the useful restriction: a valid substring containing $z$ zeros needs length at least $z+z^2$. Since its length cannot exceed $n$, only $z=O(\sqrt n)$ can be relevant. The solution fixes each starting index and visits groups of endings according to how many zeros they contain, jumping directly from one zero to the next.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Checking all $O(n^2)$ substrings is too slow for $n$ up to $... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 4

**Precompute the next zero.** The array `nxt` has length `n + 1` and is initially filled with `n`, a sentinel meaning “there is no zero at or after this position.” Scanning from right to left, `nxt[i]` first inherits `nxt[i + 1]`. If `s[i] == "0"`, it is overwritten with `i`. Therefore, after preprocessing, `nxt[i]` is the smallest zero index greater than or equal to `i`, or `n` if none exists.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "00011"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate all substrings with prefix sums:** P:** - **Enumerate all substrings with prefix sums:** Prefix zero and one counts make checking one substring $O(1)$, but there are still $O(n^2)$ substrings. This is useful as a brute-force verifier for small strings, not for the full constraint.
- **Editorial's reversed orientation:** One can fix a right endpoint and jump left through previous-zero positions. It uses the same grouping and arithmetic idea. The source solution fixes the left endpoint and uses next-zero positions; mixing the two orientations would make the endpoint formula incorrect.
- **Count zero-free substrings separately:** Runs of ones contribute $L(L+1)/2$ valid substrings and could be counted in a separate pass. The exact solution includes them naturally as the `cnt0 = 0` group, avoiding a separate case.
- **Use a list of zero indices:** Storing only zero positions with sentinels can support similar enumeration. The `nxt` array consumes $O(n)$ space but gives direct constant-time jumps from any starting position.
- **All ones:** Every substring has zero zeros, and $o\ge0$ always holds. For each start, the first iteration counts all remaining endings, after which `j` becomes `n`. The result is $n(n+1)/2$.
- **All zeros:** A substring containing any zero has no ones and cannot satisfy $0\ge z^2$ for positive $z$. Each group fails the `cnt1` test, so the answer is zero.
- **One zero followed by ones:** Endings become valid only after at least one following one is included. The surplus formula excludes the too-short prefix and then counts every longer ending.
- **Sentinel access:** Because `nxt` has length `n + 1`, reading `nxt[j + 1]` is safe whenever `j < n`, including `j = n - 1`. The sentinel value `n` also makes the final run of ones behave like an ordinary gap before a next zero.
- **Nonempty substrings only:** In the zero-free group, the cap `nxt[j + 1] - j` prevents the extra “plus one” in the surplus expression from accidentally counting an empty substring.
- **Large answer:** The number of valid substrings can be quadratic even though the algorithm is subquadratic. A fixed-width implementation should use a 64-bit result; Python integers expand automatically.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `s`. Building `nxt` takes $O(n)$ time and $O(n)$ space. There are $n$ choices for `i`. For each one, `cnt0` increases once per inner iteration and never exceeds $\lfloor\sqrt n\rfloor+1$ while the loop continues. Every iteration performs constant-time indexing and arithmetic, so the nested loops take $O(n\sqrt n)$ time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
