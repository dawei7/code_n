# Guided Example: Mirror Frequency Distance

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "ab1z9"}`
- **Required output:** `3`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` consisting of lowercase English letters and digits.

The objective is to compute `3` from `{"s": "ab1z9"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The mirror mapping is two independent reversals

Letters and digits belong to different character sets. A letter is mirrored within the 26 lowercase letters, while a digit is mirrored within the ten decimal digits.

For a lowercase letter `c`, its zero-based alphabet position is

$$
p=\operatorname{ord}(c)-\operatorname{ord}(\texttt{'a'}).
$$

Reversing positions $0$ through $25$ changes $p$ into $25-p$. The source reconstructs the corresponding character as

$$
\operatorname{chr}\!\left(
\operatorname{ord}(\texttt{'a'})+25-p
\right).
$$

Thus `a` maps to `z`, `b` maps to `y`, and `m` maps to `n`. Applying the formula twice returns to the original letter.

For a digit, the same reversal is simpler. After converting `c` to its integer value $d$, its mirror is $9-d$, converted back to a string. Consequently `0` pairs with `9`, `1` with `8`, and `4` with `5`.

Both domains have even size, so no valid character is its own mirror. The 36 possible characters form exactly 18 disjoint unordered pairs: 13 letter pairs and 5 digit pairs.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "ab1z9"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why frequency counting is sufficient

For one pair $\{c,m\}$, the required contribution is

$$
\left|\operatorname{freq}(c)-\operatorname{freq}(m)\right|.
$$

No index, adjacency, or ordering information appears in this expression. Once `freq = Counter(s)` has been built, every needed value is available in constant time.

The source iterates over `freq.items()` rather than over all 36 allowed characters. That is enough because a pair for which neither character appears contributes $|0-0|=0$. If exactly one member appears, that present member is encountered and `freq[m]` evaluates to zero. Python's `Counter` returns zero for a missing key, which is precisely the frequency required by the definition.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For one pair $\{c,m\}$, the required contribution is

$$
\le... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How one unordered pair is counted once

The subtle part is avoiding both orientations. If `b` and `y` both occur, iterating over distinct characters eventually sees both `b` and `y`, but the pair's absolute difference must be added only once.

The set `vis` records the character that represented each pair when that pair was first processed. Suppose `c` is the first encountered member:

1. The source computes its mirror `m`.
2. Because the pair has not yet been handled, `m` is not in `vis`.
3. The source adds `c` to `vis` and adds $|\texttt{freq[c]}-\texttt{freq[m]}|$ to `ans`.
4. If `m` also occurs, its later iteration computes mirror `c`.
5. Now `c in vis` is true, so that reverse orientation is skipped.

At first glance, adding only `c` rather than both `c` and `m` may look incomplete. It is nevertheless sufficient. The later member tests whether its mirror—the earlier member—is present in the set. If the mirror character never appears in the string, no later iteration exists and no duplicate can occur.

This also shows that the result does not depend on which member happens to be encountered first. Reversing the representative changes

$$
|\operatorname{freq}(c)-\operatorname{freq}(m)|
$$

into

$$
|\operatorname{freq}(m)-\operatorname{freq}(c)|,
$$

which is identical.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `3` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "ab1z9"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `3` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Iterate over 18 predetermined pairs:** A fixed:** - **Iterate over 18 predetermined pairs:** A fixed table such as `(a,z)` through `(m,n)` and `(0,9)` through `(4,5)` removes the need for `vis`. It has the same $O(n)$ time and $O(1)$ space, but the source instead derives mirrors arithmetically.
- **Iterate over all 36 characters:** Comparing a character only when it is the lexicographically smaller member of its pair also prevents duplication. This remains constant work after frequency counting.
- **Mirror absent from the string:** Its frequency is zero, so a present character with count $v$ contributes $|v-0|=v$. `Counter` provides that zero without a special branch.
- **Both mirror counts equal:** The pair is still processed, but its contribution is zero, as with `b` and `y` in `"byby"`.
- **Only one distinct character:** The answer equals the string length because the character's mirror has frequency zero.
- **Pairs absent on both sides:** They need not be visited because their contribution is zero; this is why looping only through `freq.items()` is complete.
- **No self-mirror case:** Lowercase letters and digits both have even-sized domains, so the formulas never map a valid character to itself.
- **Letter and digit boundaries stay separate:** `a` cannot mirror a digit, and `0` cannot mirror a letter. The source chooses one formula before computing the opposite character.
- **Input contract matters for `isalpha`:** Other Unicode alphabetic characters would pass `isalpha()` but would not fit the lowercase-English arithmetic. The stated constraints exclude them.
- **Missing imports:** Standalone execution needs `Counter` from `collections`. This is an integration requirement, not a change to the counting logic.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(36)$. Let $n=\lvert\texttt{s}\rvert$. Constructing `Counter(s)` reads all $n$ characters, so it costs $O(n)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
