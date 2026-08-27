# Guided Example: Remove All Adjacent Duplicates In String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abbaca"}`
- **Required output:** `"ca"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting of lowercase English letters. A **duplicate removal** consists of choosing two **adjacent** and **equal** letters and removing them.

The objective is to compute `"ca"` from `{"s": "abbaca"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Keep the fully reduced result of the processed prefix

The stack `stk` represents what remains after performing all possible adjacent-equal removals on the part of `s` processed so far.

When a new character `c` arrives, it is appended conceptually at the right end of that reduced prefix. The only pair it can immediately form is with the current last surviving character, `stk[-1]`. No earlier position can be adjacent to `c` while that top character remains between them.

This leads to two cases:

- If the stack is nonempty and its top equals `c`, the adjacent equal pair is removed by popping the top and not storing `c`.
- Otherwise, no removal involving `c` is currently possible, so `c` is pushed.

The stack is both working memory and the eventual output character sequence.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abbaca"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why checking only the top is sufficient

Before processing `c`, the stack has no adjacent duplicate pair by the invariant. Appending `c` changes adjacency only at one boundary: between the old stack top and `c`.

If those characters differ, every old adjacency remains valid and the new boundary is also valid. Pushing preserves a fully reduced stack.

If they match, removing both restores the stack to exactly its earlier state before that top was pushed. That remaining stack was already fully reduced, so no additional immediate pair exists inside it.

Thus one top comparison completely handles the new character. There is no need to scan backward after each update.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Before processing `c`, the stack has no adjacent duplicate p... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How chain reactions appear naturally

Consider `"abbaca"`.

- Read `a` and push it: `[a]`.
- Read the first `b` and push: `[a,b]`.
- Read the second `b`. It matches the top, so pop: `[a]`.
- Read the next `a`. The earlier `bb` removal has made this `a` adjacent to the surviving first `a`. It matches the top, so pop: `[]`.
- Read `c` and push, then read `a` and push.

Joining the final stack gives `"ca"`.

The second cancellation is not found by repeatedly rescanning a modified string. It emerges when the later `a` is processed against the current reduced prefix.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"ca"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abbaca"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"ca"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Repeated string replacement:** Remove `aa` thr:** - **Repeated string replacement:** Remove `aa` through `zz` until the length stops changing. It is simple but repeatedly scans and allocates strings, leading to quadratic worst-case work.
- **Repeated full rescans:** Find one adjacent pair, remove it, and restart. Each removal can shift or rebuild most of the string, again becoming quadratic.
- **Use a mutable character array with a write pointer:** Treat the array prefix as a stack and overwrite positions in place. This implements the same invariant and can reduce object overhead.
- **Recursive removal:** Recursion complicates newly formed boundaries and risks deep call stacks; the explicit stack captures them directly.
- **One character:** The stack receives it and returns it unchanged.
- **Two equal characters:** The second pops the first, producing the empty string.
- **Two different characters:** Both remain in order.
- **All equal characters:** Pairs cancel successively; an even count leaves empty, while an odd count leaves one character.
- **No duplicates anywhere:** Every character is pushed, and the original string is returned.
- **Nested chain reaction:** Patterns such as `abbaca` are handled because later characters compare against the already reduced prefix.
- **Empty final result:** `''.join([])` returns `""` without a special case.
- **Lowercase alphabet:** The stack algorithm actually works for any comparable characters, but the source restricts input to lowercase English letters.
- **Removal order:** Different manual orders lead to the same final answer by the source guarantee; the stack realizes one deterministic left-to-right order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N = len(s)`. Each character is processed once, pushed at most once, and popped at most once. All stack operations are constant time, so the scan takes `O(N)` time.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
