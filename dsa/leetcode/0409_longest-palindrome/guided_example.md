# Guided Example: Longest Palindrome

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abccccdd"}`
- **Required output:** `7`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s` which consists of lowercase or uppercase letters, return the length of the **longest palindrome** that can be built with those letters.

The objective is to compute `7` from `{"s": "abccccdd"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What a palindrome requires

A palindrome reads the same from left to right and from right to left. That symmetry forces almost every character used in it to have a partner. If a character is placed three positions from the left end, the same character must be placed three positions from the right end. Consequently, all characters outside the center are consumed in pairs.

An odd-length palindrome has one exceptional position: its single center. That position mirrors itself, so it does not need a matching copy. An even-length palindrome has no such position. This gives the complete frequency rule:

- from every character frequency, use as many complete pairs as possible; and
- after all pairs have been chosen, use at most one leftover character as the center.

Case sensitivity matters here. The characters `A` and `a` have separate frequencies and cannot form a pair with one another.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abccccdd"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count the available copies

The solution begins with `cnt = Counter(s)`. The counter maps each distinct character to the number of times it occurs. The order of the original string is irrelevant because the problem permits rearranging its letters. Only the multiset of available characters determines what can be built.

For a character whose frequency is `v`, the expression `v // 2` counts its complete pairs. Multiplying by two converts that pair count back into the number of usable character copies:

`v // 2 * 2`

For example, a frequency of `6` contributes all `6` copies. A frequency of `5` contains two pairs and contributes `4` copies. A frequency of `1` contributes no paired copies. This expression is also the largest even integer no greater than `v`.

The generator inside

`sum(v // 2 * 2 for v in cnt.values())`

computes this contribution for every distinct character. Call the sum `ans`. At this moment, `ans` is the length of the longest even-length palindrome that can be assembled. A concrete arrangement need not be built: for each selected pair, one copy can go on the left and its mate on the matching position on the right.

Consider `s = "abccccdd"`. Its frequencies are `a:1`, `b:1`, `c:4`, and `d:2`. The paired contribution is therefore `0 + 0 + 4 + 2 = 6`. Those six characters can form symmetric halves such as `dcc` and `ccd`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The solution begins with `cnt = Counter(s)`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Detect whether a center is available

The line `ans += int(ans < len(s))` deserves careful attention. In Python, the comparison `ans < len(s)` is a Boolean. Converting it with `int(...)` produces `1` when true and `0` when false.

Why does comparing these two lengths detect a valid center? `ans` contains every copy belonging to every available pair. If `ans` is smaller than the total number of input characters, at least one occurrence was not paired. Such an occurrence exists exactly when at least one character has odd frequency. Any one of those leftovers can occupy the center, so the answer increases by one. It does not matter if several characters have odd frequencies: a palindrome has only one center, and every other unpaired occurrence must remain unused.

If `ans == len(s)`, every occurrence was already consumed in pairs. There is no unused character to place in a center, and adding one would invent a character that the input does not contain. The Boolean conversion therefore adds exactly the permitted amount.

For the running example, `ans` is `6` while `len(s)` is `8`, so one leftover becomes the center and the result is `7`. For `s = "aabb"`, the paired sum is already `4`; the comparison is false and the answer remains `4`. For `s = "a"`, the paired sum is `0`, one center is available, and the result is `1`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `7` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abccccdd"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `7` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Set of currently unmatched characters:** Scan :** - **Set of currently unmatched characters:** Scan `s`; add a character when it is unmatched, and remove it while adding two to the answer when its mate appears. One remaining set member may become the center. This is also $O(n)$ time and constant space for this alphabet, but the frequency formula in the chosen solution states the pair count more directly.
- **Odd-frequency counter maintained during counting:** Track how many frequencies are currently odd, then compute `len(s) - odd_count + 1` when at least one odd frequency exists. It has the same bounds, although updating parity after every occurrence is somewhat less immediate than summing complete pairs after counting.
- **Sort all characters:** Equal characters become adjacent after sorting, making pairs easy to count. Sorting costs $O(n \log n)$ time and is unnecessary when the alphabet can be counted directly.
- **Try to build candidate palindromes:** Generating arrangements solves a much harder problem than requested and can create an enormous search space. The answer depends only on frequencies, not on which valid arrangement is selected.
- **Several odd frequencies:** Only one leftover can be the center. The solution deliberately adds one, rather than one per odd-frequency character.
- **All frequencies even:** `ans == len(s)`, so no center is added and every input character is used.
- **A one-character string:** There are no pairs, but the sole character becomes the center, producing length `1`.
- **Case-sensitive letters:** `Counter` naturally keeps `A` and `a` as different keys, exactly matching the contract.
- **Repeated use of a high-frequency character:** A frequency such as `7` contributes `6` paired copies and may also provide the center. The integer-division expression handles this without a special branch.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `s`, and let $u$ be the number of distinct characters in it. Constructing `Counter(s)` examines all $n$ characters, so it takes $O(n)$ time. Summing over `cnt.values()` visits $u$ frequencies, which takes $O(u)$ time. Because $u \le n$, the total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(u)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
