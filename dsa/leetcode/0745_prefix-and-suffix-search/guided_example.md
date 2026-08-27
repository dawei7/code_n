# Guided Example: Prefix and Suffix Search

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["WordFilter", "f"], "arguments": [[["apple"]], ["a", "e"]]}`
- **Required output:** `[null, 0]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Design a special dictionary that searches the words in it by a prefix and a suffix.

The objective is to compute `[null, 0]` from `{"operations": ["WordFilter", "f"], "arguments": [[["apple"]], ["a", "e"]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Move work from queries into construction

The class may receive many prefix-and-suffix queries. Because every word has very small bounded length, the exact solution precomputes the answer for every possible prefix and suffix combination of every dictionary word.

The dictionary `d` maps a tuple

`(prefix, suffix)`

to the largest word index seen that has both properties. A query then becomes one hash-table lookup instead of scanning words or traversing data structures.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["WordFilter", "f"], "arguments": [[["apple"]], ["a", "e"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Enumerate every prefix

For a word `w` of length `n`, the loop `i in range(n + 1)` creates `w[:i]`:

- `i = 0` gives the empty prefix.
- `i = 1` gives the first character.
- `i = n` gives the complete word.

Although the stated queries have nonempty prefixes, including the empty prefix makes the table conceptually complete and would support a broader query contract.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For a word `w` of length `n`, the loop `i in range(n + 1)` c... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Enumerate every suffix

For every chosen prefix, the inner loop `j in range(n + 1)` creates `w[j:]`:

- `j = 0` gives the complete word.
- `j = n` gives the empty suffix.
- Intermediate values give every proper suffix.

The Cartesian product of `n + 1` prefixes and `n + 1` suffixes covers every pair a query could ask about for this word. Prefix and suffix may overlap inside the word; that is allowed and requires no special case.

For `"apple"`, the table includes keys such as `("a", "e")`, `("app", "ple")`, and `("apple", "apple")`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, 0]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["WordFilter", "f"], "arguments": [[["apple"]], ["a", "e"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, 0]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Combined prefix-suffix trie:** Insert forms su:** - **Combined prefix-suffix trie:** Insert forms such as suffix plus separator plus word and search prefix/suffix jointly. This can avoid enumerating all string-pair keys but is more complex and still stores substantial trie data.
- **- **Two tries with index lists:** One trie indexes:** - **Two tries with index lists:** One trie indexes prefixes and another suffixes; a query intersects their descending index lists. This can save some preprocessing but makes queries more expensive.
- **- **Scan words backward per query:** The first mat:** - **Scan words backward per query:** The first match found is the largest index. It uses little extra memory but can cost `O(wL)` per query and becomes expensive for many calls.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(wL^2)$. Let `w` be the number of dictionary words and `L` the maximum word length. Each word generates `(length + 1)^2 = O(L^2)` prefix-suffix pairs. Under the usual bounded-string operation model, construction takes `O(wL^2)` time and stores `O(wL^2)` keys in the worst case. Each query is expected `O(1)` hash lookup, so `q` queries add expected `O(q)` time.
- **Auxiliary Space Complexity:** $O(wL^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
