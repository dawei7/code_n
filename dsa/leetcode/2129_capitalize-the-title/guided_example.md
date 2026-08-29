# Guided Example: Capitalize the Title

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"title": "capiTalIze tHe titLe"}`
- **Required output:** `"Capitalize The Title"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `title` consisting of one or more words separated by a single space, where each word consists of English letters. **Capitalize** the string by changing the capitalization of each word such that:

The objective is to compute `"Capitalize The Title"` from `{"title": "capiTalIze tHe titLe"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate the title into exactly the units governed by the rule

The expression `title.split()` produces the sequence of words. Because it is called without an explicit separator, Python treats whitespace as the separator and omits empty pieces. The problem guarantees one space between words and no leading or trailing spaces, so this behavior gives precisely the stated words. The implementation does not need indexes for the spaces because it reconstructs the separators after transforming the words.

The list comprehension visits each word `w` once:

`[w.lower() if len(w) < 3 else w.capitalize() for w in title.split()]`

The condition `len(w) < 3` is exactly another way to say that the word contains one or two letters. There is no overlap or missing case: positive word lengths below three use the short-word rule, and lengths of at least three use the other rule.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"title": "capiTalIze tHe titLe"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Normalize short words completely

For a word of length one or two, `w.lower()` converts every uppercase English letter to its lowercase form and leaves an already lowercase letter unchanged. This directly implements the requirement that every letter of a short word be lowercase.

It is important to normalize the entire word rather than merely lowercasing its first character. An input such as `"OF"` must become `"of"`, not `"oF"`. Calling `lower()` expresses this complete transformation in one operation.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Normalize longer words in both directions

For a word of at least three letters, `w.capitalize()` makes its first character uppercase and the remaining characters lowercase. Both parts matter. Merely uppercasing the first letter would mishandle mixed-case input such as `"capiTalIze"` because the internal uppercase `T` and `I` would remain. `capitalize()` first establishes the requested leading capital and normalizes the rest, producing `"Capitalize"`.

The input contains only English letters, so there are no punctuation marks, digits, or unusual word-boundary cases to reinterpret. Each source word is non-empty, which also guarantees that there is always a first letter when the long-word branch is selected.

The transformed results are stored in `words`. At this point, an invariant holds for every element already produced: if its original length was below three, all its letters are lowercase; otherwise, its first letter is uppercase and every later letter is lowercase. Since the transformation does not change a word’s length, the branch choice remains valid after capitalization.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"Capitalize The Title"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"title": "capiTalIze tHe titLe"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"Capitalize The Title"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Manual character scan:** One can locate each word boundary, measure the word, and append transformed characters to a buffer. This is also $O(n)$ time and $O(n)$ output space, but requires more indexing logic and creates more opportunities for off-by-one errors.
- **Lowercase the entire title first:** After `title.lower()`, the first character of every word of length at least three could be uppercased. This is correct with careful boundary and length tracking, but it still needs a second pass and does not simplify the exact split-and-transform solution.
- **Using `title.title()`:** This capitalizes every word regardless of length, so it incorrectly turns short words such as `"of"` and `"i"` into `"Of"` and `"I"`.
- **Uppercasing only the first character:** This fails to lowercase the remaining letters of a long mixed-case word. The `"capiTalIze"` example demonstrates why full normalization is required.
- **One-letter word:** Its length is below three, so `lower()` is selected. An uppercase `"I"` becomes `"i"` as required.
- **Two-letter word:** The strict comparison `len(w) < 3` includes length two. Both letters become lowercase, even when both were originally uppercase.
- **Exactly three letters:** Length three enters the `capitalize()` branch. This boundary is important because the short-word rule applies only to lengths one and two.
- **Already normalized title:** Applying `lower()` or `capitalize()` again leaves every word in the same required form, so the method is idempotent.
- **Mixed original casing:** Each selected string method rewrites all relevant letters, making the result independent of the input’s prior capitalization.
- **One-word title:** `split()` returns a one-element list and `join()` returns that transformed element without adding spaces.
- **Maximum-length title:** The same linear passes apply when the title has length 100; there is no combinatorial behavior or nested scan over all words.
- **Whitespace semantics:** Python’s no-argument `split()` would also collapse repeated whitespace, but the contract guarantees exactly one space and no leading or trailing spaces. The implementation’s output therefore preserves the required separator format for every legal input.
- **Input immutability:** Neither string methods nor `join()` modify `title`; each creates a new string, which matches Python’s immutable string model.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of characters in `title`, including its spaces. Splitting scans the title and creates word strings whose combined number of letters is at most $n$. For each word, `lower()` or `capitalize()` scans and creates a result proportional to that word’s length. Joining scans the transformed words and writes the final $n$-character result. These are consecutive linear passes, so their costs add rather than multiply. The total time is $O(n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
