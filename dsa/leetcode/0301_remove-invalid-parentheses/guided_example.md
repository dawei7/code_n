# Guided Example: Remove Invalid Parentheses

We trace the step-by-step two-phase search: greedy prefix pre-scan to compute exact minimal deletion quotas ($l$ and $r$), prefix validity pruning ($lcnt \ge rcnt$), remaining-capacity bounding ($N - i \ge l + r$), and pruned DFS backtracking on representative parenthesis strings:

- **Input:** $s = \text{"()())()"}$
- **Required output:** `["(())()", "()()()"]` (Two unique strings formed by deleting exactly one invalid `')'`)
- **Letters with Parentheses:** $s = \text{"(a)())()"} \implies \text{["(a())()", "(a)()()"]}$ (Non-parenthesis characters are always preserved)
- **Opposite Inverted Order:** $s = \text{")("} \implies \text{[""]}$ (Requires removing $1$ `')'` and $1$ `'('`, yielding the empty string)
- **Already Valid String:** $s = \text{"()()"} \implies \text{["()()"]}$ ($l = 0, r = 0$; zero deletions needed)

This instance demonstrates constrained combinatorial pruning, proves why precalculating the exact number of misplaced left and right parentheses reduces the search space from $O(2^N)$ to only valid minimal paths, details prefix balance invariants, and executes within $O(N \cdot 2^P)$ time and $O(N)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given a string of parentheses:
$$
s = \text{"()())()"} \quad (N = 7)
$$
Remove the **minimum number of invalid parentheses** so that the remaining string is valid. Return **all unique** valid configurations.

```text
Input:  (  )  (  )  )  (  )
Index:  0  1  2  3  4  5  6

Valid pairs:
(0, 1) and (2, 3) match.
Index 4 is an extra ')' with no opening counterpart.
Index (5, 6) matches.

The extra ')' must go, and the pre-scan finds l = 0, so no '(' may be removed.
Every minimal candidate therefore deletes exactly one of indices 1, 3, 4, 6:

Deleting index 1: "(())()" -> VALID!
Deleting index 3: "()()()" -> VALID!
Deleting index 4: "()()()" -> VALID! (the same text as deleting index 3)
Deleting index 6: "()())(" -> INVALID (a prefix goes negative and index 5's '(' is left unclosed)

All unique minimal valid outputs: ["(())()", "()()()"]
```

### Which Single Deletions Are Even Candidates
Because the quota is $l = 0, r = 1$, a candidate answer is any string obtained by deleting exactly one `')'`. Checking all seven single deletions makes the surviving set and the reason each other index fails completely explicit:

| Deleted index | Character | Resulting string | Running balance ever negative? | Valid? | Why it is admitted or rejected |
|:---:|:---:|:---|:---:|:---:|:---|
| 0 | `'('` | `")())()"` | yes, immediately | no | An opening parenthesis may not be deleted at all: the quota is $l = 0$ |
| 1 | `')'` | `"(())()"` | no | **yes** | The extra `')'` leaves the two pairs nested |
| 2 | `'('` | `"()))()"` | yes, at index 2 | no | Deleting a matched `'('` orphans its partner and exhausts the quota |
| 3 | `')'` | `"()()()"` | no | **yes** | Removing the first `')'` of the adjacent pair flattens the string |
| 4 | `')'` | `"()()()"` | no | **yes** | Removing the second `')'` of that same pair yields identical text, so the set deduplicates it |
| 5 | `'('` | `"()()))"` | yes, at index 4 | no | A `'('` deletion, forbidden by $l = 0$, and it also unbalances the tail |
| 6 | `')'` | `"()())("` | yes, at index 4 | no | The prefix fails before the end, and the search never reaches this branch either |

The two admissions in the middle are why the answer is a **set** of strings rather than a set of decisions: indices 3 and 4 are distinct branch choices that produce the same text.

### The Search Space Challenge
A string of length $N$ has $2^N$ possible subsequences. Generating and testing all subsequences is infeasible.
We solve this with a two-phase strategy:
1. **Pre-scan ($O(N)$):** Determine the exact number of excess `'('` ($l$) and excess `')'` ($r$) that *must* be deleted.
2. **Constrained DFS:** Backtrack while enforcing two pruning invariants:
   - **Prefix Balance:** At no point can kept `')'` exceed kept `'('` ($lcnt \ge rcnt$).
   - **Removal Budget:** Remaining characters must be sufficient to fulfill deletion quotas ($N - i \ge l + r$).

---

## 2. Conceptual Foundation & Invariants

### Phase 1: Calculating Minimum Removals ($l$ and $r$)
Scan $s$ from left to right:
- Maintain `l` (unmatched `'('` available) and `r` (unmatched `')'` that cannot be paired):
  - On `'('`: $l \leftarrow l + 1$.
  - On `')'`:
    - If $l > 0$: Match with an available `'('` $\implies l \leftarrow l - 1$.
    - Else ($l == 0$): Unmatched right parenthesis $\implies r \leftarrow r + 1$.
  - Letters do not affect counts.

For $s = \text{"()())()"}$:
- Step 0: `'('` $\to l = 1, r = 0$
- Step 1: `')'` $\to l = 0, r = 0$
- Step 2: `'('` $\to l = 1, r = 0$
- Step 3: `')'` $\to l = 0, r = 0$
- Step 4: `')'` $\to l = 0, r = \mathbf{1}$ (Excess `')'`)
- Step 5: `'('` $\to l = 1, r = 1$
- Step 6: `')'` $\to l = \mathbf{0}, r = \mathbf{1}$
Exact minimum deletions required: $l = 0$ (no left removals), $r = 1$ (exactly one right removal).

### Phase 2: Backtracking State `dfs(i, l, r, lcnt, rcnt, t)`
- $i$: Current character index in $s$.
- $l, r$: Remaining deletions budget for `'('` and `')'`.
- $lcnt, rcnt$: Count of kept `'('` and `')'` in prefix $t$.
- $t$: Reconstructed string accumulator.

### Pruning Conditions:
1. **Budget Exhaustion Check:** If $N - i < l + r$, remaining characters cannot fulfill required deletions $\implies$ Prune.
2. **Prefix Invariant Violation:** If $lcnt < rcnt$, more closing parentheses were kept than opening ones $\implies$ Prune.

### Branch Transitions at Index $i$:
1. **Delete Branch (if budget remains):**
   - If $s[i] == \text{'('}$ and $l > 0$: $\text{dfs}(i + 1, \; l - 1, \; r, \; lcnt, \; rcnt, \; t)$.
   - If $s[i] == \text{')'}$ and $r > 0$: $\text{dfs}(i + 1, \; l, \; r - 1, \; lcnt, \; rcnt, \; t)$.
2. **Keep Branch:**
   $$
   \text{dfs}(i + 1, \; l, \; r, \; lcnt + [s[i] == \text{'('}], \; rcnt + [s[i] == \text{')'}], \; t + s[i])
   $$

> **Invariant.** Any completed path reaching $i = N$ with $l = 0$ and $r = 0$ is guaranteed to have minimal deletions and valid parenthesis balancing.

---

## 3. Step-by-Step Worked Execution

We trace the DFS on $s = \text{"()())()"}$ with target quotas $l = 0, r = 1$:

---

### Step 1: Processing Indices $0$ to $2$
- $i = 0$ (`'('`): $l = 0$, so `'('` cannot be deleted. Must keep: $t = \text{"("}, lcnt = 1, rcnt = 0$.
- $i = 1$ (`')'`): $r = 1$.
  - *Branch A (Delete index 1):* $r \leftarrow 0$. State: $t = \text{"("}, lcnt = 1, rcnt = 0$.
    - Next char $i = 2$ is `'('`: kept $\implies t = \text{"(("}, lcnt = 2$.
    - Next char $i = 3$ is `')'`: kept $\implies t = \text{"(()"}, lcnt = 2, rcnt = 1$.
    - Next char $i = 4$ is `')'`: kept $\implies t = \text{"(())"}, lcnt = 2, rcnt = 2$.
    - Next chars $5, 6$ are `"()"` $\implies$ result: $\mathbf{\text{"(())()"}}$!
  - *Branch B (Keep index 1):* $t = \text{"()"}, lcnt = 1, rcnt = 1, r = 1$.

---

### Step 2: Exploring Branch B ($t = \text{"()"}, r = 1$)
- $i = 2$ (`'('`): Must keep ($l = 0$). $t = \text{"()("}, lcnt = 2, rcnt = 1$.
- $i = 3$ (`')'`):
  - *Branch B1 (Delete index 3):* $r \leftarrow 0$. $t = \text{"()("}, lcnt = 2, rcnt = 1$.
    - $i = 4$ (`')'`): Must keep ($r = 0$). $t = \text{"()()"}, lcnt = 2, rcnt = 2$.
    - $i = 5, 6$ (`"()"`): Must keep. $t = \mathbf{\text{"()()()"}}$!
  - *Branch B2 (Keep index 3):* $t = \text{"()()"}, lcnt = 2, rcnt = 2, r = 1$.

---

### Step 3: Exploring Branch B2 ($t = \text{"()()"}, r = 1$)
- $i = 4$ (`')'`):
  - *Branch B2a (Delete index 4):* $r \leftarrow 0$. $t = \text{"()()"}, lcnt = 2, rcnt = 2$.
    - $i = 5, 6$ (`"()"`): Must keep. Result: $\mathbf{\text{"()()()"}}$ (duplicate handled by set).
  - *Branch B2b (Keep index 4):* $t = \text{"()())"}, lcnt = 2, rcnt = 3$.
    - Check invariant: $lcnt < rcnt$ ($2 < 3$).
    - **Violates prefix balance!** Pruned immediately.

---

### Step 4: Why the Budget Never Reaches Index 6
Spending the single deletion on index 6 would require arriving there with $r = 1$ still unspent, which means indices 1, 3 and 4 were all kept. Keeping index 4 already produces $t = \text{"()())"}$ with $lcnt = 2$ and $rcnt = 3$, so the prefix invariant $lcnt \ge rcnt$ fails on entry to index 5 and that whole subtree is discarded before index 6 is ever considered. The enumeration below confirms it: the only pruned state in the entire search is $\text{"()())"}$, and the delete-at-6 branch is never generated. (The string $\text{"()())("}$ that this branch would build is invalid anyway, because its running balance dips to $-1$ at index 4.)

Final collected unique valid strings:
$$
\mathbf{[\text{"(())()"}, \text{"()()()"}]}
$$

---

## 4. Complete Execution Trace

```text
Initial quotas: l = 0, r = 1 (must remove exactly 1 ')')

Path 1: Delete index 1 -> "(())()" (Valid)
Path 2: Keep 1, delete index 3 -> "()()()" (Duplicate in set)
Path 3: Keep 1, 3, delete index 4 -> "()()()" (Valid)
Path 4: Keep 1, 3, 4 -> lcnt < rcnt (2 < 3) -> PRUNED!

Unique Results: ["(())()", "()()()"]
```

| Decision Path | Removals Made | Kept String $t$ | $lcnt$ | $rcnt$ | Validity Status | Final Status |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Delete $s[1]$ (`')'`) | Index 1 | `"(())()"` | 3 | 3 | $lcnt == rcnt$ | **Valid Output** |
| Delete $s[3]$ (`')'`) | Index 3 | `"()()()"` | 3 | 3 | $lcnt == rcnt$ | **Duplicate (Set merges)** |
| Delete $s[4]$ (`')'`) | Index 4 | `"()()()"` | 3 | 3 | $lcnt == rcnt$ | **Valid Output** |
| Keep all $s[0..4]$ | None yet | `"()())"` | 2 | 3 | $lcnt < rcnt$ | **Pruned (Invalid Prefix)** |
| Delete $s[6]$ (`')'`) | Never reached | `"()())("` would require indices $1, 3, 4$ kept | 2 | 3 | $lcnt < rcnt$ at index 5 | **Pruned earlier** |

Which mechanism actually does the work on this input is worth separating, since the two guards are not equally active:

| Mechanism | When it is evaluated | State in this instance | Arithmetic | Effect here |
|:---|:---|:---|:---|:---|
| Deletion-budget guard | On entry to every call: prune when $N - i < l + r$ | $i = 1$ with $l = 0, r = 1$ | $7 - 1 = 6 \ge 1$ | Dormant: a single pending deletion always fits in the characters that remain |
| Prefix-balance guard | On entry to every call: prune when $lcnt < rcnt$ | $i = 5$ with $t = \text{"()())"}$, $lcnt = 2$, $rcnt = 3$ | $2 < 3$ | Fires exactly once, discarding the whole subtree that keeps index 4 |
| Delete-branch availability | Before offering a delete branch | $i = 0, 2, 5$ all hold `'('` while $l = 0$ | $l = 0$ | No opening parenthesis is ever deletable, halving the branching at those indices |
| Leaf acceptance | At $i = N$ | $i = 7$ with $l = 0, r = 0$ | $l = 0$ and $r = 0$ | Reached three times, yielding two distinct strings because indices 3 and 4 coincide textually |

The budget guard matters on other inputs: for `"((((("` the pre-scan leaves $l = 5$, and the keep-everything branch at $i = 1$ is discarded because $4 < 5$ remaining characters cannot supply five deletions. On this instance, though, the prefix guard is the only pruning that fires, and the deduplication at the leaf is what turns three accepted paths into two answers.

---

## 5. Algorithmic Correctness

**Soundness.** Every string accepted at a leaf node $i = N$ has exactly $l = 0$ and $r = 0$, meaning the exact number of excess parentheses calculated in Phase 1 was removed. The prefix check $lcnt \ge rcnt$ ensures that no closing parenthesis ever appears without a preceding opening match, guaranteeing structural validity.

**Completeness.** Phase 1 computes the theoretical minimum number of deletions. Because the backtracking search explores all combinations of removals that match these exact counts and prunes only provably invalid prefixes, no valid string with the minimal deletion count can be missed.

---

## 6. Traps This Instance Exposes

- **Duplicate Outputs:** When multiple identical adjacent parentheses exist (e.g. `"))"`), deleting either character yields the identical string. Using a `set` for `ans` cleanly deduplicates these equivalent paths.
- **Prefix Pruning Necessity:** Without `lcnt < rcnt` pruning, the search explores every placement of the quota deletions — and, because the leaf test only checks that the quotas are exhausted, it would also collect unbalanced strings: on this input it additionally emits `"()())("`, the result of spending the single `')'` deletion on index 6. The guard is therefore part of correctness, not only of speed.
- **Preserving Letters:** Letters (e.g. `'a'`) must never be deleted; they have only a "keep" branch in the DFS and bypass parenthesis counter modifications.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot 2^P)$ in the worst case, where $N$ is string length and $P$ is the number of parentheses ($P \le 20$). With precomputed quotas $l$ and $r$, branching is restricted to $\binom{P}{l + r}$, and prefix pruning further curtails the state space.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory for recursion stack depth and substring accumulators.

### Alternatives and Their Costs
| Approach | Time | Space | Tradeoff |
|:---|:---|:---|:---|
| **Quota-guided DFS with prefix pruning (the method traced here)** | $O(N \cdot 2^P)$, and in practice far below it | $O(N)$ stack plus the output set | The pre-scan fixes how many deletions are legal, so the search never spends time on non-minimal removals; the prefix guard then cancels whole subtrees |
| **Same DFS without the prefix guard** | Same worst-case bound, with more branches explored | $O(N)$ | Not interchangeable: the leaf test only verifies the quotas ($l = 0$ and $r = 0$), so the prefix guard is what guarantees balance. On this input the unguarded search also emits `"()())("` by deleting index 6 |
| **Breadth-first removal by level** | $O(N \cdot 2^P)$ | $O(2^P)$ for a whole frontier | Removes the pre-scan: delete one character at a time, stop at the first level that produces a valid string. Minimality comes for free, but levels are stored and re-tested repeatedly |
| **Enumerate every subsequence, filter valid, keep the longest** | $O(2^N \cdot N)$ where $N$ counts letters too | $O(2^N)$ | The most direct statement of the problem and therefore the easiest to get right on tiny inputs, but letters inflate $N$ far beyond the twenty parentheses the constraints permit |
| **Counting DP for the number of deletions only** | $O(N^2)$ | $O(N)$ | Computes the same minimum the pre-scan finds, but returns no strings, so it cannot produce the required output |
