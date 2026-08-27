# Guided Example: Longest Palindrome by Concatenating Two Letter Words

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"words": ["lc", "cl", "gg"]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of strings `words`. Each element of `words` consists of **two** lowercase English letters.

The objective is to compute `6` from `{"words": ["lc", "cl", "gg"]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count first because order is chosen freely

The code begins with `cnt = Counter(words)`. Since words may be concatenated in any order, their original positions do not affect feasibility. Only the number of available copies of each two-letter string matters. The counter converts the problem from arranging individual array entries into deciding how many copies of each type can participate.

The variables are initialized together as `ans = x = 0`. Here, `ans` accumulates the answer in characters, not in words. The variable `x` records how many equal-letter word types have an odd count. Only whether `x` is zero matters at the end, but adding the odd indicators is a compact way to remember that fact.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"words": ["lc", "cl", "gg"]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Pair a non-palindromic word with its reverse

For a key `k` whose two letters differ, `k[::-1]` is a different two-letter word. If `k` occurs $v$ times and its reverse occurs $u$ times, no palindrome can use more than $\min(v,u)$ copies of either type. Each left-side copy needs one reverse on the right, and the less frequent type is exhausted first.

One matched pair contributes two words, hence four characters. The exact code may initially look surprising:

`ans += min(v, cnt[k[::-1]]) * 2`

This line adds only two characters per match, but the loop later processes the reverse key separately. When processing `"ab"`, it adds $2\min(\text{count}(\text{"ab"}),\text{count}(\text{"ba"}))$. When processing `"ba"`, it adds the same amount again. Together the two iterations add four characters per matched pair, exactly the full contribution.

This deliberate double visit is correct because the contribution in each visit is half of a complete pair. If a reverse does not occur, `Counter` returns zero for the missing key, so the contribution is zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For a key `k` whose two letters differ, `k[::-1]` is a diffe... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Handle self-reversing words in pairs

When `k[0] == k[1]`, the word is already a two-character palindrome, such as `"aa"`. Two copies can be placed symmetrically, one on each side. The number of complete pairs is `v // 2`.

The expression

`v // 2 * 2 * 2`

means complete pairs times two words per pair times two characters per word. Equivalently, it contributes $4\lfloor v/2\rfloor$ characters. This uses every copy when $v$ is even and all but one when $v$ is odd.

The expression `v & 1` is `1` exactly when $v$ is odd and `0` when it is even. Therefore `x += v & 1` counts the equal-letter types that leave one unmatched copy after all possible symmetric pairs are used.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"words": ["lc", "cl", "gg"]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **A 26 by 26 frequency table:** Map each letter :** - **A 26 by 26 frequency table:** Map each letter to an index and store counts in a fixed matrix. This gives the same $O(n)$ time and explicit $O(26^2)$ space, avoiding hashing at the cost of more indexing code.
- **Match online while scanning:** Keep unmatched counts and immediately consume a reverse when it is available. This can also be linear, but center handling for equal-letter words is easier to reason about after complete counts are known.
- **Generate concatenation orders:** Trying permutations and subsets is exponential and ignores the central symmetry rule that reduces the problem to independent frequency matches.
- **Process each reverse pair only once:** One may impose an ordering such as `k < k[::-1]` and add four characters per match. The exact code instead visits both keys and adds two per visit; both accounting styles reach the same total.
- **Only non-palindromic words:** The answer consists entirely of reverse pairs. If no word has its reverse, every contribution is zero and the method returns `0`.
- **Only equal-letter words:** Every count contributes its largest even part, and at most one odd leftover contributes the center.
- **Several odd equal-letter counts:** Each type contributes all possible pairs, but only one of their leftover words is added centrally. The condition `if x` correctly ignores how many choices beyond one exist.
- **One word:** If it has equal letters, it becomes the two-character center. If its letters differ, no palindrome can be formed and the answer is zero.
- **Unequal reverse frequencies:** With seven `"ab"` words and four `"ba"` words, exactly four matches are usable. The `min` operation prevents the three surplus `"ab"` copies from being counted.
- **Missing reverse key:** `cnt[k[::-1]]` evaluates to zero, so the unmatched word type adds nothing.
- **Even equal-letter count:** It leaves no center candidate from that type because `v & 1` is zero, but every copy is used in symmetric pairs.
- **Odd equal-letter count:** The largest even portion is paired, and exactly one copy remains eligible for the shared center.
- **Intentional double accounting:** For differing letters, each complete reverse pair is encountered under both keys. The factor `2` per encounter is therefore correct; changing it to `4` without also restricting the loop would double the answer incorrectly.
- **Character length versus word count:** `ans` is already measured in characters. The method must not multiply the final result by two again.
- **Original order:** The counter discards positions safely because the problem explicitly permits concatenating selected words in any order.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+d)$. Let $n$ be the number of input words and let $d$ be the number of distinct two-letter words. Building `Counter(words)` takes $O(n)$ expected time. Iterating through its entries takes $O(d)$ time. Reversing a two-character key, comparing its letters, and performing counter lookups are all $O(1)$ because every word has fixed length two. Total time is $O(n+d)$, which simplifies to $O(n)$ because $d \le n$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
