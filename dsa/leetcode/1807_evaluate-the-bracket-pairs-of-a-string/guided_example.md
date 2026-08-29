# Guided Example: Evaluate the Bracket Pairs of a String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "(name)is(age)yearsold", "knowledge": [["name", "bob"], ["age", "two"]]}`
- **Required output:** `"bobistwoyearsold"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` that contains some bracket pairs, with each pair containing a **non-empty** key.

The objective is to compute `"bobistwoyearsold"` from `{"s": "(name)is(age)yearsold", "knowledge": [["name", "bob"], ["age", "two"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Prepare constant-time key lookup

The knowledge list contains unique keys. The solution first builds dictionary `d` mapping every key to its value. A bracket pair can then be evaluated with expected constant-time lookup rather than scanning the knowledge list repeatedly.

If a key is missing, `d.get(key, '?')` returns the required question mark.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "(name)is(age)yearsold", "knowledge": [["name", "bob"], ["age", "two"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Scan ordinary text and bracket pairs differently

Index `i` moves from left to right through `s`. List `ans` collects output pieces.

When `s[i]` is an ordinary lowercase letter, the solution appends that one character unchanged and increments `i`.

When `s[i] == '('`, the solution uses `s.find(')', i + 1)` to locate the matching close bracket at index `j`. The constraints guarantee that it exists and that brackets are not nested, so the next close bracket is the correct partner.

Slice `s[i + 1:j]` is the nonempty key. The dictionary value or `"?"` is appended as one output piece. The solution assigns `i = j`, and the common increment at the loop bottom moves past the close bracket. Neither parenthesis nor the key text itself is copied into the output.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why `find` does not make the total scan quadratic here

Each call to `find` scans only from an opening bracket to its corresponding closing bracket. After replacement, `i` jumps beyond that entire bracket region. Because bracket pairs are non-nested and disjoint, these searched regions do not overlap.

Consequently, the total number of characters examined across all `find` calls is linear in the input length. Ordinary text outside brackets is also visited once by the outer scan.

This argument depends on the source guarantees. Arbitrary nested or malformed parentheses would need a different parser.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"bobistwoyearsold"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "(name)is(age)yearsold", "knowledge": [["name", "bob"], ["age", "two"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"bobistwoyearsold"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Repeatedly concatenate strings:** It is easy to write but can copy an ever-growing result and become quadratic.
- **Scan knowledge per bracket:** It costs up to $O(N\cdot|\texttt{knowledge}|)$; a dictionary makes lookup expected $O(1)$.
- **Regular-expression replacement:** It can work but still needs a callback and dictionary, while the direct parser follows the simple grammar clearly.
- **Stack parser:** Useful for nested brackets, but nesting is explicitly absent here.
- **Unknown key:** Append exactly one question mark and omit the bracket syntax.
- **Known key:** Append its entire mapped value as one piece.
- **Repeated bracket key:** Each occurrence is replaced; dictionary construction happens only once.
- **Known letters outside brackets:** They remain literal and are never treated as keys.
- **Empty knowledge:** Every bracket pair becomes `"?"`.
- **No bracket pairs:** Every character is copied and the result equals `s`.
- **Bracket at the beginning or end:** Index jumps and the common increment handle both boundaries.
- **Nonempty-key guarantee:** The slice never represents an intentionally empty key.
- **Matched-bracket guarantee:** `find` never returns -1 on valid input.
- **No nesting:** The first following close bracket always matches the current open bracket.
- **Unique knowledge keys:** Dictionary construction never faces conflicting values.
- **Output length:** Replacements may change length, so complexity should include produced characters.
- **Input preservation:** The method creates a dictionary and result string without modifying `s` or `knowledge`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N+K+R)$. Let $N$ be the length of `s`, let $K$ be the total number of characters stored across the knowledge keys and values, and let $R$ be the output length.
- **Auxiliary Space Complexity:** $O(K+R)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
