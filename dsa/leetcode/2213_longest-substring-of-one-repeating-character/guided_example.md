# Guided Example: Longest Substring of One Repeating Character

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "babacc", "queryCharacters": "bcb", "queryIndices": [1, 3, 3]}`
- **Required output:** `[3, 3, 4]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** string `s`. You are also given a **0-indexed** string `queryCharacters` of length `k` and a **0-indexed** array of integer **indices** `queryIndices` of length `k`, both of which are used to describe `k` queries.

The objective is to compute `[3, 3, 4]` from `{"s": "babacc", "queryCharacters": "bcb", "queryIndices": [1, 3, 3]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What must be maintained after every character replacement

After each query, the answer is the length of the longest contiguous run containing one repeated character. Recomputing that answer by scanning the entire string after every replacement would be easy to understand, but with a long string and many queries it repeats almost all of the same work. A point replacement changes only one position. The useful goal is therefore to store summaries of string intervals and repair only the summaries whose intervals contain the changed position.

The solution uses a segment tree. Every tree node represents an inclusive, one-based interval `[l, r]` of the string. It records three measurements:

- `lmx` is the length of the longest same-character run that starts exactly at `l`, so it is the interval's uniform prefix length.
- `rmx` is the length of the longest same-character run that ends exactly at `r`, so it is the interval's uniform suffix length.
- `mx` is the length of the longest same-character run anywhere inside the interval.

These three values are enough because a run in a parent interval has only three possible locations: entirely inside the left child, entirely inside the right child, or crossing the single boundary between the children. The children's `mx` values handle the first two cases. Their boundary-facing suffix and prefix handle the crossing case.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "babacc", "queryCharacters": "bcb", "queryIndices": [1, 3, 3]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build leaves first, then combine upward

The `SegmentTree` constructor converts the immutable input string into `s = list(s)` because individual characters must later be replaced. It allocates `tr` with `4 * n` slots, a conventional safe capacity for a binary segment tree over `n` elements, and calls `build(1, 1, n)`. Tree node index `1` is the root.

At a leaf, `l == r`, so the represented interval contains exactly one character. Its longest prefix, suffix, and internal run all have length one. The `Node` constructor initializes `lmx`, `rmx`, and `mx` to `1`, which means leaf construction needs no additional assignments. For a non-leaf interval, `build` recursively creates the two children and then calls `pushup` to derive the parent summary.

The implementation uses one-based interval positions but stores characters in a zero-based Python list. Thus, character at tree position `p` is `s[p - 1]`. The boundary comparison in `pushup` follows this conversion exactly: `s[left.r - 1]` is the last character of the left interval, and `s[right.l - 1]` is the first character of the right interval.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The `SegmentTree` constructor converts the immutable input s... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How two child summaries become one parent summary

Suppose the left child covers `[l, mid]` and the right child covers `[mid + 1, r]`. The merge first assumes no run crosses their boundary:

- the parent's prefix length begins as `left.lmx`;
- its suffix length begins as `right.rmx`; and
- its best internal run begins as `max(left.mx, right.mx)`.

If the last left character and first right character differ, that assumption is final. A same-character substring cannot cross a boundary whose two adjacent characters are different.

If the boundary characters match, a crossing run exists. It consists of the left interval's longest uniform suffix followed immediately by the right interval's longest uniform prefix, so its length is `left.rmx + right.lmx`. The parent updates `mx` with the larger of its current value and this crossing length.

The parent's prefix cannot always be extended into the right child merely because the boundary matches. It reaches the boundary only when the entire left interval is one uniform run. The code computes the left interval length as `a = left.r - left.l + 1` and checks `left.lmx == a`. Only then does it add `right.lmx` to the parent's prefix. Symmetrically, the parent suffix extends into the left child only if the entire right interval is uniform, tested by `right.rmx == b`.

These conditions prevent a subtle overcount. For example, if the left interval begins with `a` characters but ends with `b` characters, a matching `b` at the right boundary may create a crossing run, yet it cannot extend the parent's prefix because the different character inside the left interval breaks continuity.

The merge accounts for every possible longest run. Runs contained in one child are represented by the child maxima; every run using positions from both children must cross their common boundary and is exactly captured by the left suffix plus right prefix when the boundary characters agree. Therefore, once both children hold accurate summaries, `pushup` produces an accurate summary for the parent. Leaves are accurate by definition, so building upward makes the root's `mx` the answer for the whole initial string.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 3, 4]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "babacc", "queryCharacters": "bcb", "queryIndices": [1, 3, 3]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 3, 4]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Rescan after every query:** Replace the charac:** - **Rescan after every query:** Replace the character and scan the string while counting consecutive equal characters. This is simple and uses little auxiliary space, but it costs `O(nq)` time in the worst case because every query revisits the entire string.
- **Store only one maximum per segment-tree node:** Child maxima alone cannot describe a run that crosses the midpoint. The prefix and suffix lengths are necessary connection information; omitting either makes an exact constant-time merge impossible.
- **Balanced ordered set of run boundaries:** One can maintain maximal equal-character intervals in an ordered structure, splitting and merging near an update while separately tracking run lengths. This can also be efficient, but it requires more intricate bookkeeping than the three-field segment-tree summary.
- **A Fenwick tree:** Fenwick trees are excellent when an aggregate has an invertible prefix operation such as addition. Longest equal-character runs need boundary-aware merging and cannot be recovered from a single scalar prefix aggregate, so a standard Fenwick tree is not a natural match.
- **Single-character string:** The tree consists of one leaf. Every replacement writes that leaf, the root `mx` remains one, and every answer is `1`.
- **All characters initially equal:** The root prefix, suffix, and maximum all equal `n`. Replacing a middle position with a different character breaks the run, and the ancestor merges correctly choose the longer remaining side.
- **An update joins two runs:** When the new character matches both neighbors, the relevant merge eventually uses a left suffix plus a right prefix, allowing one update to combine the two neighboring runs and the updated position into a larger run.
- **An update breaks a run:** Replacing a character inside a uniform interval causes affected leaves and ancestors to stop extending prefixes or suffixes through mismatching boundaries. Unaffected subtrees retain their summaries.
- **Repeated replacement with the same value:** There is no early-return optimization. The work remains `O(\log n)`, but the reconstructed summaries and answer are unchanged.
- **Index conversion:** Query indices are zero-based while tree positions are one-based. The exact `x + 1` on entry and `x - 1` when accessing `s` are both required; dropping either conversion would update the wrong character.
- **Whole-range query only:** The provided `query` is sufficient for this method's exact call `query(1, 1, len(s))`. It should not be reused as a general arbitrary-range longest-run query without adding a richer return summary and explicit cross-boundary merge.
- **Output order:** One result is appended immediately after each update. Even when multiple queries target the same index, the list records the state after each operation in the original order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + q log n)$. Let `n` be the string length and `q` be the number of replacement queries. Building the segment tree creates `O(n)` nodes. Although the backing array reserves `4n` references, the recursive build visits only a linear number of actual intervals, and each `pushup` performs constant work. Initial construction therefore takes `O(n)` time.
- **Auxiliary Space Complexity:** $O(n + q)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
