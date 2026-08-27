# Guided Example: Palindrome Permutation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "code"}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, return `true` *if a permutation of the string could form a ****palindrome**** and *`false`* otherwise*.

The objective is to compute `false` from `{"s": "code"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reframe the question around character counts

The task does not ask whether `s` itself is a palindrome. It asks whether the characters of `s` can be rearranged into one. Rearranging can change every position, but it cannot change how many copies of each character exist. Therefore, the useful information is not the current order of the characters; it is the frequency of each distinct character.

For example, `"aab"` is not a palindrome in its given order, yet its counts are two `a` characters and one `b`. Those characters can be rearranged as `"aba"`, so the answer is `true`. Conversely, `"code"` has four different characters, each appearing once. Moving those four characters around cannot create the matching pairs that a palindrome needs, so the answer is `false`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "code"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why parity is the decisive property

In a palindrome, every position away from the center has a mirror position on the other side. If a character is placed at one of those positions, the same character must be placed at its mirror. Characters used outside the center are consequently consumed two at a time. That is why an even frequency is always easy to place: split its copies into pairs, place one copy of each pair on the left, and put the other copy in the corresponding position on the right.

There can be at most one position without a different mirror partner: the center position of an odd-length palindrome. One character with an odd frequency can use one copy in that center and distribute all of its remaining copies in mirrored pairs. Two different odd-frequency characters cannot both do this, because there is only one center position.

This gives one rule that works for both possible length parities:

$$
\text{a palindromic permutation exists}
\quad\Longleftrightarrow\quad
\text{the number of odd frequencies is at most }1.
$$

For an even-length string, the total length is even, so odd frequencies must occur in an even number. The condition “at most one” therefore forces the number of odd frequencies to be zero. For an odd-length string, the total length is odd, so there must be an odd number of odd frequencies; “at most one” forces exactly one. The same test handles both cases without explicitly checking whether the length is even or odd.

The rule is necessary because a palindrome has only mirrored pairs and possibly one center. It is also sufficient, not merely a warning sign. If every count is even, put half of every character's copies in the left half and mirror them into the right half. If exactly one count is odd, reserve one copy of that character for the center, then perform the same pairing process with all remaining copies. This construction always produces a palindrome, so no positional search is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | In a palindrome, every position away from the center has a m... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build all frequencies with `Counter`

The exact solution begins conceptually with `Counter(s)`. A counter is a hash-based mapping from each distinct character to the number of times it occurs. Scanning `s` once produces entries such as the following for `s = "carerac"`:

| Character | Frequency | Parity contribution |
|---|---:|---:|
| `c` | 2 | 0 |
| `a` | 2 | 0 |
| `r` | 2 | 0 |
| `e` | 1 | 1 |

Only values are needed after the map is built. The identities of the odd characters no longer matter because the requested result is only a Boolean. The solution therefore iterates over `Counter(s).values()` instead of iterating over key-value pairs.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "code"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Odd-character toggle set:** Instead of storing:** - **Odd-character toggle set:** Instead of storing full counts, scan the string and add a character when it is absent from a set or remove it when it is present. At the end, the set contains exactly the characters with odd frequencies. This also gives expected $O(n)$ time and $O(k)$ space, and it matches the parity idea directly, but it is not the exact protected solution explained here.
- **Fixed array of 26 counts:** Because every legal character is lowercase English, an array indexed by `ord(ch) - ord('a')` can replace the hash map. It has $O(n)$ time and $O(1)$ space relative to $n$, with smaller and more predictable storage, but it is tied to the fixed alphabet and is less general than `Counter`.
- **Sort before counting runs:** Sorting brings equal characters together, after which run lengths can be checked for oddness. This needs $O(n \log n)$ time in general and may allocate storage or modify a mutable representation, so it is unnecessary when direct frequency counting is linear.
- **Generate permutations:** Trying rearrangements and testing each one attacks the surface wording instead of the count invariant. There can be $n!$ position permutations before accounting for duplicates, making this approach vastly more expensive than the parity test.
- **Single-character input:** Its only frequency is one, so the odd-frequency sum is one and the method returns `true`. The character itself is already a palindrome and occupies the center.
- **All characters identical:** Whether the common frequency is even or odd, there are at most one odd counts. Every permutation is the same repeated-character string, which is a palindrome.
- **Exactly two odd frequencies:** This is the smallest impossible case. Both odd groups would need a center after all possible pairs were removed, but only one center can exist, so `< 2` correctly rejects it.
- **Many temporary odd counts in a prefix:** A prefix such as `"abc"` has three odd counts, but later matching copies could make all three even. That is why rejecting during the initial scan solely from prefix parity would be invalid unless the complete input had already been processed.
- **Empty string outside the stated contract:** The legal input is nonempty. If an empty string were nevertheless passed to this implementation, the counter would have no values, `sum(...)` would be zero, and the method would return `true`, consistent with treating the empty string as a palindrome.
- **Character identity and case sensitivity:** The legal domain contains lowercase letters only. `Counter` nevertheless treats every distinct Python character as a separate key, so an out-of-contract uppercase `A` would not match lowercase `a`; spaces and punctuation would also count as characters rather than being ignored.
- **Counter iteration order:** No particular order is required. Addition is independent of order, and the final decision uses only the sum of parity bits, so any valid mapping iteration order produces the same result.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `s`, and let $k$ be the number of distinct characters in it.
- **Auxiliary Space Complexity:** $O(k)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
