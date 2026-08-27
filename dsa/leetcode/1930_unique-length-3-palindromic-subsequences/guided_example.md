# Guided Example: Unique Length-3 Palindromic Subsequences

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aabca"}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, return *the number of **unique palindromes of length three** that are a **subsequence** of *`s`.

The objective is to compute `3` from `{"s": "aabca"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Every length-three palindrome has only two choices to identify

A palindrome of length three must have the form $cxc$: the first and last characters are the same outer character $c$, and the middle character $x$ may be any lowercase letter, including $c$ itself. Therefore a unique answer is completely identified by the ordered pair “outer character, middle character.”

The solution considers each possible outer character `c` from `ascii_lowercase`. For that character it finds `l = s.find(c)`, the first occurrence, and `r = s.rfind(c)`, the last occurrence. If at least one index lies strictly between them, every distinct character in `s[l + 1 : r]` can serve as the middle of a palindrome whose outer character is `c`.

The expression `len(set(s[l + 1 : r]))` counts those distinct middle characters. A set deliberately discards repeated occurrences. For example, if several `b` characters lie between the chosen outer `a` characters, they may give many index triples spelling `"aba"`, but the problem counts that subsequence value only once.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aabca"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the first and last occurrences capture every possibility

Suppose some palindrome $cxc$ can be formed using occurrences of $c$ at indices $i$ and $j$, with an $x$ between them. The first occurrence `l` of $c$ cannot be later than $i$, and the last occurrence `r` cannot be earlier than $j$. Thus the same middle occurrence of $x$ also lies strictly between `l` and `r`. Every feasible middle character for any pair of outer `c` occurrences is therefore present inside the widest interval between the first and last `c`.

The reverse is immediate: if a character $x$ occurs between `l` and `r`, choosing those two outer occurrences and that middle occurrence produces the subsequence $cxc$. So the set of characters in this widest interval is exactly the set of unique palindromes with outer character $c$.

Choosing the widest pair is what lets the algorithm avoid examining all pairs of equal outer-character occurrences. An interior pair can never expose a middle character that is absent from the first-to-last interval.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Suppose some palindrome $cxc$ can be formed using occurrence... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why different loop iterations cannot double-count

Within one outer-character iteration, the set ensures each middle character is counted once. Across iterations, the outer character differs. Even if the middle character is the same, palindromes such as `"aba"` and `"cbc"` are different strings, so both should count. Consequently, summing the set sizes over all 26 possible outer characters counts each unique length-three palindrome exactly once.

The guard `r - l > 1` requires at least one position strictly between the outer copies. If a letter is absent, both `find` and `rfind` return `-1`, so the difference is zero and the iteration contributes nothing. If it appears once, the indices are equal. If it appears twice consecutively, their difference is one. All three cases correctly fail the guard.

For `s = "aabca"`, the first `a` is at index zero and the last at index four. The substring between them is `"abc"`, whose set is `{"a", "b", "c"}`. These characters produce `"aaa"`, `"aba"`, and `"aca"`. Considering other outer letters adds nothing, so the answer is three.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aabca"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Precomputed first and last arrays:** One pass :** - **Precomputed first and last arrays:** One pass can store both indices for all 26 letters, avoiding repeated `find` scans. Scanning each interior interval still gives linear time because the alphabet size is constant.
- **Prefix character counts:** A 26-by-position prefix table can test which middle letters occur between two endpoints in constant time per letter, but uses $O(26N)$ space and is unnecessary.
- **Enumerate index triples:** Testing all $O(N^3)$ triples repeats enormous amounts of work and requires extra deduplication.
- **Scan without slicing:** Iterate indices from `l + 1` to `r - 1` and add characters directly to a set. This keeps the same logic and achieves constant auxiliary space under the fixed alphabet.
- **Outer letter absent:** Both searches return `-1` and the guard prevents a contribution.
- **Outer letter appears once:** No palindrome can use it at both ends, and `r - l` is zero.
- **Two adjacent copies:** There is no position available for a middle character, so the difference-one interval contributes nothing.
- **Middle equals outer:** A third copy of $c$ between the endpoints adds $c$ to the set and correctly counts `ccc`.
- **Many ways to form one string:** Repeated middle occurrences and alternative outer pairs still produce one string value; the set and widest interval count it once.
- **Different outer letters:** Palindromes with the same middle but different ends are different and are counted in separate iterations.
- **Lowercase-only dependency:** Iterating `ascii_lowercase` is complete only because the contract restricts `s` to lowercase English letters.
- **Imported alphabet symbol:** The exact method assumes `ascii_lowercase` is available in its execution environment.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the length of `s`. The loop has exactly 26 iterations because the alphabet is fixed. For each character, `find` may scan $O(N)$ positions, `rfind` may scan $O(N)$ positions, and constructing the slice and its set may inspect another $O(N)$ characters. Therefore the explicit bound is $O(26N)$, which simplifies to $O(N)$ because 26 is constant.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
