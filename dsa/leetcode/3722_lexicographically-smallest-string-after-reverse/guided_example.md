# Guided Example: Lexicographically Smallest String After Reverse

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "dcab"}`
- **Required output:** `"acdb"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` of length `n` consisting of lowercase English letters.

The objective is to compute `"acdb"` from `{"s": "dcab"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The allowed operation creates only a linear number of candidates

The operation must reverse either a prefix or a suffix, and its length `k` can be any integer from one through `n`. For each `k` there are at most two results:

- Reverse the first `k` characters.
- Reverse the last `k` characters.

That gives only `2n` described operations. Some operations can produce the same string—for example, both choices are identical when `n = 1`, and reversing the whole string as a prefix is the same as reversing it as a suffix—but duplicates do not affect a minimum.

Because `n <= 1000`, the Optimal source constructs the result of every legal operation and compares them lexicographically. This exhaustive approach is simple, complete, and fast enough. It does not enumerate arbitrary substrings or arbitrary permutations; it enumerates exactly the endpoint-touching reversals allowed by the contract.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "dcab"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Construct a prefix-reversal candidate

For a fixed `k`, the first candidate is

`t1 = s[:k][::-1] + s[k:]`.

Python's slice `s[:k]` contains indices zero through `k - 1`, exactly the first `k` characters. The slice step `[::-1]` reverses that prefix. The suffix `s[k:]` begins at index `k` and remains in its original order. Concatenating them performs precisely one prefix reversal and leaves every character outside the chosen segment unchanged.

For example, if `s = "dcab"` and `k = 3`:

- `s[:3]` is `"dca"`.
- Reversing it gives `"acd"`.
- `s[3:]` is `"b"`.
- The candidate is `"acdb"`.

Every character appears once because the two source slices partition `s`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Construct a suffix-reversal candidate

The second candidate is

`t2 = s[:-k] + s[-k:][::-1]`.

The slice `s[-k:]` is the final `k` characters, and `s[:-k]` is everything before them. Reversing only the final slice and appending it to the unchanged prefix performs the required suffix reversal.

For `s = "abba"` and `k = 3`:

- `s[:-3]` is `"a"`.
- `s[-3:]` is `"bba"`.
- Its reverse is `"abb"`.
- The candidate is `"aabb"`.

Negative slicing also behaves correctly at `k = n`. In that case, `s[:-n]` is empty and `s[-n:]` is the entire string, so `t2` is the full reversal. The prefix formula `t1` also becomes the full reversal.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"acdb"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "dcab"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"acdb"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Enumerate every substring reversal:** There are $\Theta(n^2)$ substrings and $O(n)$ work per constructed result, producing $O(n^3)$ time while considering many operations the problem forbids. Only segments touching an endpoint are legal.
- **Store all `2n` candidates and sort them:** This yields the same answer but uses $O(n^2)$ character storage and $O(n\log n)$ candidate comparisons. A running minimum needs only the current candidates.
- **Search for a greedy first character:** The smallest reachable first character can help analyze prefix reversals, but suffix reversals leave a prefix unchanged and ties require comparing long arrangements. With `n <= 1000`, exact enumeration avoids complicated tie logic.
- **Use a specialized string data structure:** Rolling hashes, suffix structures, or longest-common-prefix comparisons could reduce repeated comparison work, but they add substantial complexity beyond what the constraints require. The shown $O(n^2)$ method is the intended clear optimum for this bound.
- **Exactly one operation:** Initializing `ans = s` remains valid because choosing `k = 1` reverses a one-character prefix or suffix and leaves `s` unchanged. The algorithm is not relying on a forbidden zero-operation choice.
- **`k = 1`:** Both `t1` and `t2` equal `s`. Their duplication is harmless and establishes the unchanged string as a legal candidate.
- **`k = n`:** Prefix and suffix reversal both reverse the entire string. Python's positive and negative slices produce the correct empty unchanged portion.
- **Single-character string:** The only legal reversal has length one and returns the same string. The loop constructs it safely and returns it.
- **Palindrome:** Some or all reversals may reproduce the original string. The running minimum handles equal candidates without special cases.
- **Repeated letters:** Different values of `k` can create identical strings, but lexicographic minimum is unaffected by duplicates. Slicing also preserves every copy exactly.
- **Already lexicographically smallest among candidates:** Since `s` is a legal `k = 1` result, no reversal is required to improve it. `ans` remains `s` when all constructed candidates are equal or larger.
- **Improvement from a suffix reversal:** The loop treats suffix and prefix candidates symmetrically at every length, so cases such as `"abba"` are not biased toward front reversals.
- **Long common prefixes between candidates:** String comparison may scan many characters, which is already accounted for in the $O(n^2)$ time bound.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Let `n` be the length of `s`. The loop runs exactly `n` times. For each `k`, slicing, reversing, and concatenating `t1` creates a total of $O(n)$ characters. Constructing `t2` also costs $O(n)$. Comparing strings with `min` can inspect up to $O(n)$ characters in the worst case when candidates share long prefixes.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
