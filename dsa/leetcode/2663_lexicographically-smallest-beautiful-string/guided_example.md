# Guided Example: Lexicographically Smallest Beautiful String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abcz", "k": 26}`
- **Required output:** `"abda"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A string is **beautiful** if:

The objective is to compute `"abda"` from `{"s": "abcz", "k": 26}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Beautiful means avoiding equality one or two positions back

A palindrome of length two has equal adjacent characters: `aa`.

A palindrome of length three has equal first and last characters: `aba`.

Every palindrome of length at least four contains a smaller palindrome of length two or three at its center. Therefore, a string contains no palindrome of length at least two exactly when each character differs from:

- the immediately preceding character;
- the character two positions earlier.

The solution only needs these two local checks while constructing a candidate.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abcz", "k": 26}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Find the rightmost position that can be increased

To obtain the smallest lexicographically larger string, preserve the longest possible prefix of `s`.

The code scans position `i` from right to left. At one position, it tries letters strictly larger than the current `cs[i]`, starting with the next letter.

If a valid increase is possible far to the right, it changes a less significant lexicographic position and is smaller than every candidate whose first change occurs farther left.

This is analogous to carrying in a numeral system, except some digits are forbidden by the palindrome rule.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Try larger letters in increasing order

Current zero-based alphabet index is:

`p = ord(cs[i]) - ord('a') + 1`.

Starting at `p` means the first tried character is exactly one greater than the current one. Loop ends before `k`, so only the first $k$ lowercase letters are used.

For candidate `c`, the code rejects it when it equals `cs[i-1]` or `cs[i-2]`, when those positions exist.

The unchanged prefix was already beautiful, so these are the only new palindromes that can end at position $i$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"abda"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abcz", "k": 26}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"abda"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Generate strings in lexicographic order:** Exponential and unnecessary.
- **Backtracking from scratch:** Ignores that the input is already beautiful and that only the next lexicographic string is needed.
- **Check every substring for palindromes:** Local distance-one and distance-two checks are sufficient.
- **Increase last position:** Preferred whenever a legal larger character exists.
- **Character already at alphabet limit:** Carry moves left.
- **Two forbidden predecessors equal:** At most one distinct letter is excluded, making completion even easier.
- **Length one:** Only alphabet bound matters; return next letter or empty.
- **No successor:** Exhausted carry search returns empty string.
- **`k >= 4`:** Guarantees greedy suffix completion after excluding at most two letters.
- **Input preservation:** The original string is immutable; changes occur in list `cs`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(nk)$. There are $n$ positions and at most $k$ candidate letters tested at each during carry search. Suffix construction also tests at most $k$ letters per suffix position once. Total time is $O(nk)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
