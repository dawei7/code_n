# Guided Example: Letter Case Permutation

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "a1b2"}`
- **Required output:** `["a1b2", "a1B2", "A1b2", "A1B2"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, you can transform every letter individually to be lowercase or uppercase to create another string.

The objective is to compute `["a1b2", "a1B2", "A1b2", "A1B2"]` from `{"s": "a1b2"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: See the result as a sequence of independent choices

Every digit has exactly one allowed form: it must remain unchanged. Every letter has exactly two allowed forms: lowercase and uppercase.

If the string contains $\ell$ letters, choosing one of two cases independently for each letter creates $2^\ell$ distinct output strings. The algorithm must produce all of them, so exponential output size is unavoidable. The goal is to generate that complete set systematically without doing unrelated work.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "a1b2"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Use depth-first search over string positions

The mutable list `t = list(s)` holds the characters of the current candidate. Function `dfs(i)` is responsible for generating every valid completion of positions `i` through the end, while positions before `i` already represent choices made on the current recursion path.

At every position, the function first calls `dfs(i + 1)` without changing `t[i]`. This branch keeps the character in its current case.

If `t[i].isalpha()` is true, there is a second valid choice. The algorithm toggles the character's case and calls `dfs(i + 1)` again. For a digit, there is no second call because changing a digit is not permitted.

Thus a letter creates two branches and a digit creates one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The mutable list `t = list(s)` holds the characters of the c... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Understand the base case

When `i >= len(t)`, every input position has been assigned a valid character. The method joins the list into a string and appends that completed candidate to `ans`.

Joining is important. If the algorithm appended the mutable list `t` itself, later toggles would change the already stored results because every entry would refer to the same list object. `"".join(t)` creates an independent immutable string snapshot.

The index advances by one in every recursive call, so every path eventually reaches this base case.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["a1b2", "a1B2", "A1b2", "A1B2"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "a1b2"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["a1b2", "a1B2", "A1b2", "A1B2"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Iterative answer doubling:** Start with one pr:** - **Iterative answer doubling:** Start with one prefix and duplicate all existing prefixes for every letter. It has the same output-sensitive complexity but may allocate more intermediate strings.
- **- **Bit-mask enumeration:** Number the $\ell$ lett:** - **Bit-mask enumeration:** Number the $\ell$ letters and let each mask choose their cases. It is direct but scans or maps positions for every one of the $2^\ell$ masks.
- **- **Cartesian product:** Build a one-choice collec:** - **Cartesian product:** Build a one-choice collection for each digit and a two-choice collection for each letter, then join every product tuple. This is concise when a suitable library is available.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \cdot 2^l)$. Let $n$ be the string length and $\ell$ the number of letters. There are exactly $2^\ell$ leaves. Creating each result with `"".join(t)` writes $n$ characters, so output construction takes $\Theta(n \cdot 2^\ell)$ time. This is also an unavoidable lower bound because the returned data itself contains that many characters.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
