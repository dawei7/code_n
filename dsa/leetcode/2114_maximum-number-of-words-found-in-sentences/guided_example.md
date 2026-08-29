# Guided Example: Maximum Number of Words Found in Sentences

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"sentences": ["please wait", "continue to fight", "continue to win"]}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A **sentence** is a list of **words** that are separated by a single space with no leading or trailing spaces.

The objective is to compute `3` from `{"sentences": ["please wait", "continue to fight", "continue to win"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use the sentence-format guarantee

Every sentence is nonempty, has no leading or trailing spaces, and separates consecutive words with exactly one space.

Under these guarantees, a sentence with $w$ words contains exactly $w-1$ spaces. Therefore,

$$
\text{word count}=1+\text{space count}.
$$

The source evaluates `s.count(' ')` for every sentence, takes the maximum space count, and adds one:

`1 + max(s.count(' ') for s in sentences)`.

This avoids splitting sentences into word lists because only the count is needed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"sentences": ["please wait", "continue to fight", "continue to win"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the formula works

Consider a sentence with words

`word1 word2 word3`.

There are three words and two separators. Each separator marks exactly one boundary between neighboring words. With no leading or trailing spaces, there are no separators that fail to represent a boundary. With single spacing, each boundary contributes exactly one space.

The first word accounts for the added one; every later word is preceded by one of the counted spaces.

A one-word sentence contains zero spaces, and the formula returns one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Find the maximum without storing all counts

The expression inside `max` is a generator. It computes one sentence's space count at a time rather than constructing a separate list of all counts.

`max` retains only the greatest count seen. Adding one after the maximum is equivalent to adding one to every individual count first because the same constant shifts all candidates equally:

$$
1+\max(c_i)=\max(1+c_i).
$$

The input guarantee `sentences.length >= 1` ensures `max` always receives at least one value and needs no default.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"sentences": ["please wait", "continue to fight", "continue to win"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **`len(s.split())`:** Correct under the contract and more general about whitespace, but allocates a list of word substrings for each sentence.
- **Manual character loop:** It can count spaces with the same time and constant space, but `str.count` expresses the operation directly.
- **One-word sentence:** Zero spaces plus one gives one word.
- **Multiple sentences tie:** Only the maximum count is returned, so no tie-breaking is needed.
- **Nonempty sentence array:** Guarantees `max` is safe without a default.
- **No leading or trailing spaces:** Essential to the separator formula.
- **Exactly one separator:** Essential because repeated spaces would be overcounted.
- **Lowercase-only content:** Letter identity is irrelevant; only separator positions matter.
- **Very short sentences:** A length-one sentence still contains one word.
- **Generator laziness:** Individual counts are not retained after `max` processes them.
- **Compact code versus work:** The implementation still scans all $S$ characters.
- **Input preservation:** Sentences remain unchanged.
- **Add after maximum:** A uniform plus one commutes with taking the maximum, so no per-sentence word-count list is needed.
- **Tie preservation:** Equal separator counts imply equal word counts under the format contract.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S)$. Let
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
