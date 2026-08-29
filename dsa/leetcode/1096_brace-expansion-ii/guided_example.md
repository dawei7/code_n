# Guided Example: Brace Expansion II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"expression": "{a,b}{c,{d,e}}"}`
- **Required output:** `["ac", "ad", "ae", "bc", "bd", "be"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Under the grammar given below, strings can represent a set of lowercase words. Let `R(expr)` denote the set of words the expression represents.

The objective is to compute `["ac", "ad", "ae", "bc", "bd", "be"]` from `{"expression": "{a,b}{c,{d,e}}"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce one innermost union at a time

The expression combines two operations. Commas form a union of alternatives, while neighboring expressions concatenate through a Cartesian product. Nested braces make a direct left-to-right split difficult because a comma belongs only to its current brace depth.

This solution avoids building a formal parser. It repeatedly finds an innermost brace pair, substitutes each alternative into the surrounding expression, and recursively expands the resulting expressions. Once no braces remain, the expression is one complete word.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"expression": "{a,b}{c,{d,e}}"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the first closing brace identifies an innermost group

`j = exp.find('}')` chooses the first closing brace. No brace can close inside the group ending at `j`, because such an inner closing brace would have appeared earlier. The matching opening brace is therefore the last opening brace before it, found with `rfind`.

The code separates the current expression into prefix `a = exp[:i]`, group content `exp[i + 1:j]`, and suffix `c = exp[j + 1:]`. Because this group is innermost, its content contains no braces. Splitting it on commas yields its complete alternatives, which may be multi-letter strings such as `"ab"`.

For every alternative `b`, the recursive call receives `a + b + c`. This performs the group’s union by creating one branch per member. It also performs concatenation automatically: the chosen text remains adjacent to the unchanged prefix and suffix.

For example, in `"{a,b}{c,{d,e}}"`, the first closing brace reduces `"{a,b}"`, producing branches beginning with `a` and `b`. Later recursion reduces the innermost `"{d,e}"`, then its containing group. All combinations arise because every earlier branch is recursively paired with every later choice.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Terminate at complete words

Each recursive substitution removes one matched brace pair. The number of braces strictly decreases, so recursion must eventually reach an expression with no `'}'`. At that point, no union syntax remains and `exp` is one concrete lowercase word.

The word is inserted into set `s` rather than appended to a list. Set semantics are required because different grammar branches can represent the same word. For example, a union might contain `a` directly and also another expression that expands to `a`. Both recursive paths reach the same string, but the result must contain it once.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["ac", "ad", "ae", "bc", "bd", "be"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"expression": "{a,b}{c,{d,e}}"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["ac", "ad", "ae", "bc", "bd", "be"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recursive-descent parser:** Parse union and concatenation as separate grammar levels and return a set from each subexpression. This mirrors the formal grammar directly and can avoid repeatedly rescanning entire intermediate strings.
- **Stack-based set evaluation:** Maintain sets for the current concatenation and accumulated union at each brace depth. It avoids recursive string substitution but requires careful precedence handling.
- **Generate then deduplicate:** Using a list at leaves and converting to a set later is correct but can store many duplicate derivations unnecessarily.
- **No braces:** The first `find` returns `-1`, so the complete literal word is inserted immediately and returned as a one-element list.
- **Nested braces:** Selecting the first closing brace and last preceding opening brace guarantees the reduced group is innermost.
- **Multi-letter alternatives:** `split(',')` returns whole alternative strings, and substitution preserves them without treating each letter as a separate union choice.
- **Duplicate derivations:** The set collapses them, satisfying the rule that every word appears at most once.
- **Concatenated groups:** Recursive branching of one group remains in the prefix when later groups branch, producing the full Cartesian product.
- **Lexicographic order:** Sets are unordered, so the final `sorted` call is essential.
- **Valid grammar guarantee:** The algorithm assumes every closing brace has a matching opening brace and that innermost commas separate alternatives. Malformed syntax would require validation not present here.
- **Expression growth and shrinkage:** Replacing a group can change string length, but the next recursive call searches its newly formed expression from scratch, so stored indices never become stale.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(E + S)$. Let $E$ be the encoded expression length, $R$ the number of distinct returned words, $L$ a maximum returned word length, and $P$ the number of recursive leaf derivations before deduplication. $P$ can exceed $R$ because separate branches can produce the same word.
- **Auxiliary Space Complexity:** $O(E + S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
