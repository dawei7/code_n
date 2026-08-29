# Guided Example: Assign Cookies

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"g": [1, 2, 3], "s": [1, 1]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

The objective is to compute `1` from `{"g": [1, 2, 3], "s": [1, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why sorting creates a safe decision order

After sorting, `g[0]` is the easiest child to satisfy, and `s[0]` is the least useful cookie. At any moment, `g[i]` is the smallest greed among all children not yet matched, while `s[j]` is the smallest cookie not already assigned or discarded.

This order makes two greedy decisions safe:

1. If `s[j] < g[i]`, this cookie cannot satisfy the current child. Since every later child has greed at least `g[i]`, the cookie cannot satisfy any remaining child either. Advancing `j` discards something that no future assignment could use.
2. Once `s[j] >= g[i]`, assign that cookie to the current child. It is the smallest remaining cookie that works, so using it preserves every larger cookie for children whose requirements may be larger.

The inner `while` loop implements the first rule by skipping undersized cookies. After the loop, either a suitable cookie has been found or the cookie list is exhausted.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"g": [1, 2, 3], "s": [1, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why assigning the first suitable cookie is optimal

Consider the least-greedy remaining child `i` and the first remaining cookie `s[j]` that can satisfy that child. Take any maximum-cardinality assignment for the remaining problem.

If that assignment already pairs this child with `s[j]`, it agrees with the greedy choice. If the child receives a larger cookie instead, replace that larger cookie with `s[j]`; the child remains content, and the larger cookie becomes available.

If `s[j]` was assigned to another remaining child while child `i` received a larger cookie, swap the two cookies. The current child accepts `s[j]`. The other child accepted `s[j]`, so its greed is at most `s[j]`; it also accepts the larger cookie. The number of content children does not change.

If the current child was unmatched but `s[j]` was used for a later child, reassign `s[j]` to the current child. This preserves the number of matched children. Thus there is always an optimal assignment that contains the greedy match. Removing that child and cookie leaves a smaller problem of exactly the same form, so repeating the argument proves all greedy matches can belong to an optimal solution.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How the exact loop counts matches

The loop is `for i, x in enumerate(g)`. The variable `x` receives the current greed value but is not used; the code reads the equivalent `g[i]` directly.

At the start of iteration `i`, all children at indices `0` through `i - 1` have been matched, so exactly `i` children are content. Pointer `j` is the first cookie not yet assigned or ruled out.

The inner loop advances over every cookie smaller than `g[i]`. If `j >= len(s)` afterward, no cookies remain. Because children are sorted and all later children are at least as greedy, no later child can be satisfied either. Returning `i` is therefore correct: exactly the preceding `i` children were matched.

If a cookie remains, the first non-skipped cookie satisfies `g[i]`. Incrementing `j` consumes it, and the next outer iteration handles the next child. If all child iterations finish, every child was matched, so the method returns `len(g)`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"g": [1, 2, 3], "s": [1, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Try every child-cookie pairing:** This becomes a bipartite matching problem and is far more expensive than necessary because acceptability is ordered by size.
- **Process largest values first:** Matching the greediest child with the largest fitting cookie can also be made correct, but the smallest-first scan makes useless cookies easy to discard and matches the exact source.
- **Use a multiset without sorting children:** For each child, find the smallest adequate cookie in a balanced tree. It costs roughly $O((G+S)\log S)$ and needs more machinery.
- **Empty cookie list:** The first child finds `j >= len(s)` and the method returns zero.
- **More cookies than children:** Once every child is matched, leftover cookies do not matter and `len(g)` is returned.
- **More children than cookies:** Exhaustion returns the number already matched; no cookie is reused.
- **Exact-size cookie:** The skip condition is `<`, so equality is accepted as required.
- **Many duplicate sizes or greed factors:** Sorting keeps equal values adjacent, and each pointer advance still represents one distinct child or cookie occurrence.
- **Huge cookie for a small child:** It is used only if every smaller remaining cookie is inadequate; the greedy proof shows this cannot reduce the maximum match count.
- **Input mutation:** Both input lists are reordered. A caller needing their original order would have to sort copies instead.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(S\log S)$. Let $G$ be the number of children and $S$ the number of cookies. Sorting `g` takes $O(G\log G)$ time, and sorting `s` takes $O(S\log S)$ time. The outer loop visits each child at most once. Pointer `j` only moves forward and passes each cookie at most once, so all inner-loop iterations together cost $O(S)$, not $O(GS)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
