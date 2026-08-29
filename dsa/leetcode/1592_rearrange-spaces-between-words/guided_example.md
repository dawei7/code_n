# Guided Example: Rearrange Spaces Between Words

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"text": "  this   is  a sentence "}`
- **Required output:** `"this   is   a   sentence"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `text` of words that are placed among some number of spaces. Each word consists of one or more lowercase English letters and are separated by at least one space. It's guaranteed that `text` **contains at least one word**.

The objective is to compute `"this   is   a   sentence"` from `{"text": "  this   is  a sentence "}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate content from spacing

The required output keeps every word in its original order and redistributes only the spaces. The solution first extracts the two pieces of information that fully determine the result:

- `spaces = text.count(" ")` counts the total number of space characters available;
- `words = text.split()` extracts the words and discards the original runs of whitespace.

Because the input uses ordinary space characters and guarantees at least one word, `split()` without an argument produces exactly the ordered word list. It ignores leading spaces, trailing spaces, and any number of spaces between words. No word letters are lost or reordered.

After this normalization, the original placement of spaces is irrelevant. Only their total count matters.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"text": "  this   is  a sentence "}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How many gaps receive equal spacing

If there are $W$ words, there are $W-1$ internal gaps between adjacent words. For example, four words have three places where equal separators can be inserted.

The problem asks to maximize the equal number of spaces in every internal gap. If $S$ spaces are available and $W>1$, integer division gives the largest equal separator size:

$$
\text{gap}=\left\lfloor\frac{S}{W-1}\right\rfloor.
$$

The remainder

$$
\text{extra}=S\bmod(W-1)
$$

is the number of spaces that cannot be distributed without making some gap larger than another. Those spaces must appear at the end.

The source computes both quantities at once with:

`cnt, mod = divmod(spaces, len(words) - 1)`.

Python’s `divmod(a, b)` returns the quotient and remainder satisfying `a = quotient * b + remainder` with `0 <= remainder < b`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Constructing the result

`" " * cnt` creates the common separator containing exactly `cnt` spaces. Calling `join(words)` with that separator places it between every adjacent pair of words and nowhere before the first or after the last.

The expression then appends `" " * mod`, placing every leftover space at the end as required:

`(" " * cnt).join(words) + " " * mod`.

This construction preserves the order of the words because `join` traverses `words` in order.

For `text = " practice makes perfect"`, there are seven spaces and three words. Two internal gaps receive `7 // 2 = 3` spaces each, consuming six spaces, and `7 % 2 = 1` space remains. The result is `"practice   makes   perfect "`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"this   is   a   sentence"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"text": "  this   is  a sentence "}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"this   is   a   sentence"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Manual character scan:** One can count spaces and build words with an explicit loop. It has the same $O(L)$ complexity but duplicates behavior already provided clearly by `count` and `split`.
- **Repeated string insertion:** Inserting spaces into an existing immutable Python string can repeatedly copy prefixes and become quadratic. Constructing once with `join` is linear.
- **Preserve original space runs:** Their positions do not matter; only the total space count is relevant. Keeping each run complicates redistribution without adding information.
- **Exactly one word:** There are no internal gaps, so all spaces are placed after the word and division by zero is avoided.
- **Exactly two words:** There is one gap, so every space divides evenly into that gap and no trailing remainder exists.
- **No spaces:** `cnt` and `mod` are zero. `join` places empty separators, which is valid only when the input’s word-separation guarantees allow the corresponding number of words; in practice, no spaces implies one word.
- **Spaces divide evenly:** `mod == 0`, so the result has no extra trailing spaces.
- **Nonzero remainder:** Every gap still has the equal maximum quotient, and only the remainder appears at the end.
- **Leading and trailing input spaces:** `split()` removes their original positions, while `count` preserves their quantity for redistribution.
- **Several spaces between words:** They are collapsed during extraction and reallocated through the quotient and remainder.
- **Maximum length preservation:** The quotient-remainder identity proves no space is lost or invented.
- **At-least-one-word guarantee:** The source assumes `words` is non-empty. An all-space string would need separate behavior but is outside the contract.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(L)$. Let $L$ be the length of `text`.
- **Auxiliary Space Complexity:** $O(L)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
