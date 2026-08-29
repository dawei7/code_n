# Guided Example: Report Spam Message

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"message": ["hello", "world", "leetcode"], "bannedWords": ["world", "hello"]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of strings `message` and an array of strings `bannedWords`.

The objective is to compute `true` from `{"message": ["hello", "world", "leetcode"], "bannedWords": ["world", "hello"]}` while avoiding redundant calculations and unnecessary overhead.

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

**Count matching message positions, not distinct banned values.** A message is spam when at least two words in the message exactly match any banned word. If the same banned word appears twice in `message`, those are two matching positions and are enough. Conversely, one matching word is not enough even if it appears multiple times in `bannedWords`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"message": ["hello", "world", "leetcode"], "bannedWords": ["world", "hello"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The source first constructs `s = set(bannedWords)`. A set answers membership questions directly and removes duplicate banned entries because multiplicity in the banned list has no meaning. For every word `w` in `message`, the expression `w in s` produces the Boolean value `true` if that entire string is a banned word and `false` otherwise.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

Python treats `true` as the integer one and `false` as zero when summing. Therefore `sum(w in s for w in message)` is exactly the number of message positions whose words belong to the banned set. Comparing that count with two implements the definition:

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"message": ["hello", "world", "leetcode"], "bannedWords": ["world", "hello"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Early-return loop:** Increment a counter for each banned message word and return `true` immediately when it reaches two. This has the same worst-case $O(B+M)$ time and $O(B)$ space but can do less work; it is what the manifest summary describes, not what the exact source executes.
- **Nested scanning of banned words:** Testing each message word against every list entry costs $O(MB)$ comparisons and is unnecessary at sizes up to $10^5$.
- **Counter for banned words:** Frequencies in `bannedWords` are irrelevant, so a full counter stores more information than the membership-only set requires.
- **Sorting both lists:** Sorting and merging can identify matches but complicates the positional multiplicity semantics and costs $O(B\log B+M\log M)$ time.
- **Same banned word twice in the message:** Both positions count, so the method returns `true` even if the banned set contains only one distinct word.
- **Duplicate entries in `bannedWords`:** They collapse in the set and do not inflate the match count, which is required.
- **Exactly one match:** The sum equals one, and `1 >= 2` is `false`.
- **No matches:** Every generated Boolean is false, the sum is zero, and the result is `false`.
- **More than two matches:** The method returns `true`, but because it uses `sum` it still scans all remaining message words.
- **Partial string overlap:** Only complete equality counts. Prefixes, suffixes, and substrings do not match.
- **Case sensitivity:** Inputs are guaranteed lowercase. Outside that contract, `"Spam"` and `"spam"` would be different strings.
- **Maximum input sizes:** The set prevents the $10^5$-by-$10^5$ comparison explosion; the full generator scan remains comfortably linear.
- **Empty arrays:** The stated constraints require both arrays to be nonempty. Even outside the contract, an empty message would sum to zero, while an empty banned list would create an empty set and also return false.
- **Manifest discrepancy:** The stated asymptotic bounds are correct, but the claimed second-match short-circuit is absent from this implementation.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(B+M)$. Let $B$ be the number of entries in `bannedWords` and $M$ the number of words in `message`. Because each word has length at most 15, hashing and equality take bounded constant time under the problem constraints. Constructing the set takes expected $O(B)$ time, and consuming the generator performs $M$ expected constant-time membership checks, so total expected time is $O(B+M)$.
- **Auxiliary Space Complexity:** $O(b)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
