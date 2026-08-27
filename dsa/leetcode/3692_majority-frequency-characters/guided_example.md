# Guided Example: Majority Frequency Characters

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aaabbbccdddde"}`
- **Required output:** `"ab"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting of lowercase English letters.

The objective is to compute `"ab"` from `{"s": "aaabbbccdddde"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Counting each character

The statement restricts `s` to lowercase English letters. The source uses:

`cnt = Counter(s)`

For every distinct character `c`, `cnt[c]` is its total number of occurrences in the entire string.

If `s = "aaabbbccdddde"`, the resulting character frequencies are:

- `a -> 3`;
- `b -> 3`;
- `c -> 2`;
- `d -> 4`;
- `e -> 1`.

These counts identify which group each character belongs to, but the mapping is in the opposite direction from the desired group representation.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aaabbbccdddde"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reversing frequencies into groups

The source creates:

`f = defaultdict(list)`

and visits every `(character, frequency)` pair from `cnt`:

`f[v].append(c)`

Now each key `v` is a frequency value, and `f[v]` is the list of distinct characters that appear exactly `v` times.

For the example above, the groups are conceptually:

- frequency $1$: `[e]`;
- frequency $2$: `[c]`;
- frequency $3$: `[a, b]`;
- frequency $4$: `[d]`.

Each character appears in exactly one list because it has exactly one total frequency. A character is appended once, even if it occurs many times in `s`, because the loop iterates over `cnt.items()` rather than over the original string.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The source creates:

`f = defaultdict(list)`

and visits eve... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Comparing groups using both required priorities

The variables have these meanings:

- `mx` is the largest group size selected so far;
- `mv` is that selected group's frequency value;
- `ans` refers to the selected list of characters.

For a candidate frequency `v` with character list `cs`, the source updates the answer if:

`mx < len(cs)`

or if:

`mx == len(cs) and mv < v`.

The first comparison implements the primary rule: more distinct characters always wins.

The second comparison is evaluated only when group sizes tie. It implements the secondary rule: among equally large groups, choose the larger frequency.

This is equivalent to maximizing the ordered pair:

$$
(\text{group size},\text{frequency})
$$

lexicographically. Frequency does not influence the choice unless the group-size components are equal.

Whenever a candidate wins, all three pieces of selected state are updated together:

`mx = len(cs)`

`mv = v`

`ans = cs`

Assigning `ans = cs` does not copy the list, but no more characters are appended to `f` after the selection loop begins. The referenced list is stable for the remainder of the method.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"ab"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aaabbbccdddde"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"ab"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Choose characters with maximum individual freq:** - **Choose characters with maximum individual frequency:** This solves a different problem. A lower frequency can win when more distinct characters share it.
- **Sort all groups:** Sorting by `(len(group), frequency)` would identify the winner but costs extra $O(U\log U)$ work. A running maximum is enough.
- **Use fixed arrays:** Since there are only 26 lowercase letters, one could count with a 26-element array and group counts manually. `Counter` and `defaultdict` express the same logic more directly.
- **Tie in group size:** The larger frequency must win. The condition `mv < v` implements this only after confirming equal sizes.
- **One distinct character:** There is one group of size one, and that character is returned regardless of its frequency.
- **Every character appears once:** All distinct characters belong to frequency group one, so the result contains all of them.
- **Every distinct character has a different frequency:** Every group has size one. The tie rule selects the character whose frequency is largest.
- **Several characters share the winning frequency:** Each is appended once from `cnt.items()`, so the result contains distinct characters with no duplicates.
- **Output order:** The method uses first-occurrence order within the winning list, but the contract accepts any order.
- **Nonempty guarantee:** At least one group exists, so `ans` cannot remain empty for a valid input.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be `len(s)` and let $U$ be the number of distinct characters.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
