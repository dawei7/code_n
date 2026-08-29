# Guided Example: Maximum Substrings With Distinct Start

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abab"}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting of lowercase English letters.

The objective is to compute `2` from `{"s": "abab"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Every piece consumes one distinct starting character

Suppose a valid partition has `p` nonempty substrings. Each has one starting character, and all those starts must be distinct. Therefore `p` cannot exceed the number of distinct characters appearing anywhere in `s`.

If `D=len(set(s))`, then

$$
p\le D.
$$

This is an immediate upper bound. The important remaining step is proving that all `D` distinct characters can actually be used as starts in one complete consecutive partition.

The bound counts characters, not occurrences. If `a` appears one hundred times, at most one substring may start with `a`, because a second such substring would repeat a starting character. On the other hand, each different character can potentially contribute one start. This makes the number of distinct characters the natural candidate answer, but a candidate upper bound is not enough until a legal partition attaining it is shown.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abab"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Cut before each character's first occurrence

The character `s[0]` necessarily starts the first substring. For every other distinct character, consider its first occurrence in `s`. Place a cut immediately before that position.

These first-occurrence indices are distinct and appear in increasing order. They divide `s` into consecutive, nonempty pieces that cover the string exactly.

More explicitly, collect index zero and the first index of every character whose first occurrence is not zero. Sort those indices, although scanning the string would already discover them in sorted order. A substring begins at each collected index and ends immediately before the next collected index; the final substring ends at `n-1`. Because consecutive start indices are different, no piece is empty. Because the first index is zero and the last piece reaches the end, no character is omitted.

The first piece starts with `s[0]`. Every later piece starts at the first occurrence of a character not used as an earlier start, so all starting characters are distinct.

There is one piece for each distinct character, attaining `D`. Combined with the upper bound, the maximum is exactly `D`.

This is a tight-bound argument. The distinct-start rule proves that no solution can exceed `D`; the first-occurrence construction proves that one solution reaches `D`. When a lower construction and an upper limit meet at the same value, no search over other partitions can improve the answer.

For `"abab"`, distinct characters are `a` and `b`. Cut before the first `b` to obtain `"a"` and `"bab"`.

For `"abcd"`, every position is a first occurrence, so cutting before positions one, two, and three yields four single-character pieces.

For `"aaaa"`, only `a` is distinct. No valid second piece can start without repeating `a`, and the entire string as one piece attains one.

For `"cabcaab"`, the first occurrences are `c` at zero, `a` at one, and `b` at two. Cutting at one and two produces `"c"`, `"a"`, and `"bcaab"`. Later copies of all three characters remain inside the last piece, but the three starts are still `c`, `a`, and `b`, so the partition reaches the distinct-character bound.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why characters inside a piece do not matter

Only the first character of each substring is constrained. Repeated characters later in a piece do not consume or conflict with start characters. This is why cuts at first occurrences are enough even if earlier pieces contain future repetitions of already used letters.

For example, in `"abac"`, cuts at first `b` and first `c` produce `"a"`, `"ba"`, and `"c"`. The internal `a` in `"ba"` is harmless.

It would be incorrect to demand that every piece itself contain distinct characters or that characters be disjoint across pieces. Neither condition appears in the contract. The optimization concerns only the character at each selected starting position. Keeping that distinction in mind turns what looks like a partition dynamic-programming problem into a counting observation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abab"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Dynamic programming over cut positions:** The first-occurrence construction proves no optimization state is needed.
- **Greedily cut at every new character while scanning:** This explicitly realizes the proof and gives the same count, but storing substrings is unnecessary.
- **Count character runs:** A character may reappear after other letters, but it can start at most one piece. Runs can greatly exceed distinct characters.
- **Cut before every occurrence:** Repeated occurrences would create pieces with duplicate starting characters and violate the rule.
- **Require every character inside pieces to be unique:** The contract restricts only substring starts, not contents.
- **Single-character string:** One distinct character gives one piece.
- **All characters distinct:** Every character can be its own substring, so the answer is `n`.
- **All characters equal:** Only one start character is available.
- **Repeated first character later:** It may appear inside a later piece but cannot start another one.
- **Alphabet limit:** The answer can never exceed 26 even when `n` is much larger.
- **Complete partition requirement:** First-occurrence cuts cover every source position; no suffix is discarded.
- **Nonempty pieces:** Distinct cut positions ensure every piece has at least one character.
- **Construction versus return value:** The partition proves the count is attainable, but the source correctly returns only that count.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n=len(s)`. Building the set scans all characters once, taking expected $O(n)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
