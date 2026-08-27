# Guided Example: Brace Expansion

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "{a,b}c{d,e}f"}`
- **Required output:** `["acdf", "acef", "bcdf", "bcef"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` representing a list of words. Each letter in the word has one or more options.

The objective is to compute `["acdf", "acef", "bcdf", "bcef"]` from `{"s": "{a,b}c{d,e}f"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: View the expression as independent output positions

After parsing, every literal letter outside braces is one fixed output position, while every brace group is one position with several possible letters. For `"{a,b}c{d,e}f"`, the position options are `["a", "b"]`, `["c"]`, `["d", "e"]`, and `["f"]`. A complete word chooses exactly one item from each list, in left-to-right order.

The groups do not nest, and every option is a distinct lowercase letter. Those guarantees let the parser look only for the next closing brace; it never needs a stack or a grammar for nested expressions.

The solution divides the work into two clean phases. `convert` turns the encoded string into the list of option lists named `items`. Then `dfs` enumerates the Cartesian product of those lists. Keeping parsing separate prevents the same substring from being reparsed on every backtracking branch.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "{a,b}c{d,e}f"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Parse a brace group

When the current substring begins with `'{'`, `convert` finds the next `'}'`. Validity and the no-nesting guarantee ensure that this is the matching closing brace. The slice `s[1:j]` removes the braces, and `split(',')` converts text such as `"a,b,c"` into `["a", "b", "c"]`. That list is appended as one output position.

Recursion continues on `s[j + 1:]`, the unparsed suffix after the closing brace. Nothing from the group is mistaken for a separate position: its commas are consumed by `split`, and all alternatives remain together in one nested list.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | When the current substring begins with `'{'`, `convert` find... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Parse consecutive literal letters

When the current substring does not begin with a brace, the parser searches for the next opening brace. If one exists at index `j`, then `s[:j]` is the maximal consecutive literal run before it. Calling `split(',')` on that run produces a one-element list because valid literal runs contain no commas. For example, `"abc".split(',')` is `["abc"]`.

Treating a whole literal run as one item rather than three single-character positions is safe. Every generated word must include all of `"abc"` unchanged and contiguously, so choosing the single string `"abc"` has exactly the same effect as choosing `"a"`, then `"b"`, then `"c"` from three singleton positions. Grouping the run merely shortens the recursion.

The parser then recurses starting at the brace with `s[j:]`. If no later brace exists, the remaining suffix is the final literal run and is appended once. The base case `if not s: return` stops after the entire input has been consumed.

As a result, concatenating one selected string from every list in `items` reconstructs one legal expansion, and every legal expansion corresponds to exactly one such sequence of choices.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["acdf", "acef", "bcdf", "bcef"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "{a,b}c{d,e}f"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["acdf", "acef", "bcdf", "bcef"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sort each option group before DFS:** If every :** - **Sort each option group before DFS:** If every position’s choices are lexicographically sorted, a left-to-right DFS can emit complete words in sorted order and avoid the final comparison sort. Care is needed because this parser stores whole literal runs as singleton strings, though singleton ordering is trivial.
- **Iterative Cartesian product:** Start with `[""]` and, for each option list, append every current option to every prefix built so far. This avoids DFS call-stack depth but may hold both the old and new prefix collections during each expansion step.
- **Index-based parser:** Walk the original string with one integer rather than recursively slicing suffixes. This makes the $O(n)$ parsing claim precise and avoids repeated string copies.
- **Generate while parsing:** Backtracking directly over the encoded string can work, but each recursive branch risks rediscovering brace boundaries. Precomputing `items` keeps syntax handling out of the exponential enumeration.
- **No braces:** Parsing stores the complete string as one singleton option list, DFS creates exactly that string, and sorting a one-element answer changes nothing.
- **Expression begins or ends with a group:** The brace branch consumes the group normally. Empty literal runs are never appended because parsing always recurses at an actual unconsumed token.
- **Adjacent brace groups:** After one closing brace, the recursive suffix begins with the next opening brace, so two separate option positions are appended with no literal separator required.
- **Consecutive literal letters:** They are stored as one fixed string piece. This reduces recursion depth without changing any produced word.
- **Unsorted group alternatives:** DFS initially follows source order, but the final `ans.sort()` guarantees lexicographic output regardless of that order.
- **Distinct alternatives:** The contract prevents duplicate characters inside a brace group, so separate paths do not create duplicate words. If duplicates were allowed, this code would preserve duplicate outputs rather than deduplicate them.
- **No nested braces:** Finding the first `'}'` is correct only because nesting is forbidden. Nested syntax would require matching-depth tracking and a different semantic model.
- **One represented word:** When every position has one option, $R=1$. DFS follows a single path and joins the fixed pieces once.
- **Large expansion count:** Even with a short encoded string, multiplying option counts can produce many words. This is inherent because the function must return every one of them; no algorithm can use sublinear output space while returning the full list.
- **Mutable path discipline:** Omitting `t.pop()` would leave a previous branch’s choice in the path and corrupt later words. The append, recursive call, and pop must remain a matched backtracking unit.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + RL)$. Let $n$ be the encoded input length, $L$ the length of each expanded word, and $R$ the number of generated words. If the option-list sizes are $a_0, a_1, \ldots, a_{k-1}$, then $R = \prod a_i$. Any solution must materialize $R$ words containing $RL$ output characters, so $\Omega(RL)$ time and output space are unavoidable.
- **Auxiliary Space Complexity:** $O(RL)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
