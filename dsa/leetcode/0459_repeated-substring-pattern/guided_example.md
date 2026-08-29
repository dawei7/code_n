# Guided Example: Repeated Substring Pattern

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abab"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

The objective is to compute `true` from `{"s": "abab"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why `s + s` contains rotations

Let `n = len(s)`. Start at offset `d` inside the doubled string, where $0\le d<n$, and take the next `n` characters. The slice first takes the suffix `s[d:]`, then wraps into the second copy for the prefix `s[:d]`. It is therefore the left rotation

`s[d:] + s[:d]`.

As `d` ranges from zero through `n - 1`, the length-`n` windows in `s + s` represent every cyclic rotation of `s`.

The call `(s + s).index(s, 1)` asks for the first occurrence of `s` whose starting position is at least one. Starting at one deliberately ignores the trivial original occurrence at position zero.

There is always at least one later occurrence: the second literal copy begins at index `n`. Therefore `.index` cannot fail for a nonempty `s`; no exception handling is needed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abab"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why an occurrence before `n` proves repetition

Suppose the search returns an offset `d` with $1\le d<n$. Then the rotation of `s` by `d` positions equals `s` itself. Character equality around that rotation means positions repeat with period determined by `d`; more precisely, indices connected by repeatedly adding `d` modulo `n` carry equal characters. The string is therefore made from a block whose length is $\gcd(n,d)$.

Because `d` is strictly between zero and `n`, $\gcd(n,d)<n$. The block is a proper nonempty prefix, and it repeats exactly $n/\gcd(n,d)$ times, which is at least two. Thus a match beginning before `n` proves the required repeated-substring structure.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why every repeated string creates an early occurrence

Conversely, suppose `s` consists of `k >= 2` copies of a block `p` of length `d`. Rotating `s` left by exactly `d` positions removes the first copy of `p` and appends an identical copy at the end, so the string does not change. The doubled string therefore contains `s` starting at offset `d`.

Since at least two copies exist, $1\le d<n$. The search begins at one and will find this occurrence or an even earlier nontrivial occurrence. Its index is consequently less than `len(s)`, and the method returns `true`.

These two directions show the exact equivalence:

$$
\text{proper repeated block exists}
\quad\Longleftrightarrow\quad
1\le\text{next occurrence index}<n.
$$

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abab"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Try every prefix length that divides `n`:** Repeat each candidate prefix and compare with `s`. It is easy to derive but can perform repeated full-string construction and comparison.
- **KMP prefix function:** Let `L` be the longest proper prefix of `s` that is also a suffix. The string repeats exactly when `L > 0` and `n % (n - L) == 0`. This guarantees $O(n)$ time and $O(n)$ space without depending on library substring search.
- **Rolling hash:** Hashes can test candidate periods efficiently, but collisions require verification or multiple hashes and add needless risk here.
- **One-character string:** The only later match starts at index one, equal to `n`, so it correctly returns false; a proper nonempty substring cannot exist.
- **All one character:** For length greater than one, the search finds `s` starting at index one, proving repetition of the one-character block.
- **Prime length:** A repeated pattern is possible only with block length one; the rotation test handles this without explicitly factoring `n`.
- **Overlapping occurrence:** `.index` considers overlapping matches, which is necessary for strings such as `"aaaa"` whose next occurrence starts at one.
- **Guaranteed nonempty input:** The proof assumes `n > 0`. The source contract supplies that guarantee.
- **Strict properness:** A match at exactly `n` represents merely the second copy and is intentionally rejected.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the string length. Constructing `s + s` creates a string of length `2n`, taking $O(n)$ time and $O(n)$ space.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
