# Guided Example: Largest Substring Between Two Equal Characters

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aa"}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, return *the length of the longest substring between two equal characters, excluding the two characters.* If there is no such substring return `-1`.

The objective is to compute `0` from `{"s": "aa"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Describe a candidate by its two equal boundary characters

If equal characters occur at indices $L$ and $R$, with $L<R$, the substring strictly between them begins at $L+1$ and ends at $R-1$. Its length is

$$
R-L-1.
$$

The subtraction by one is easy to get wrong. The inclusive span from $L$ through $R$ has length $R-L+1$, but both boundary characters must be excluded, so two positions are removed: $(R-L+1)-2=R-L-1$.

The task is therefore to find two equal characters whose indices are as far apart as possible. It is not necessary to construct or slice the substring itself; only its length is requested.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aa"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Scan once while remembering the earliest occurrence

The dictionary `d` maps each character already seen to its first index. The answer `ans` starts at `-1`, which is the required result when no character appears twice.

The loop `for i, c in enumerate(s)` reads the string from left to right. At every index there are two cases.

If `c` is absent from `d`, this is the first occurrence of that character, so the source records `d[c] = i`.

If `c` is already present, then `d[c]` is the earliest possible left boundary for a substring ending at `i`. The candidate interior length is `i - d[c] - 1`. The source compares it with the best length found so far and retains the larger one.

Crucially, the dictionary entry is not updated after a repeated occurrence. Suppose a character occurs at indices 2, 5, and 9. When index 9 is the right boundary, pairing it with index 2 produces length $9-2-1=6$, while pairing it with index 5 produces only $9-5-1=3$. For a fixed right boundary, the smallest left index always creates the greatest distance. Replacing 2 with 5 would discard the only occurrence that can produce the best future answer for that character.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The dictionary `d` maps each character already seen to its f... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why skipped pairs cannot improve the answer

There can be many pairs of equal occurrences, but the source examines only pairs made from each occurrence and the character's first occurrence. This pruning is safe.

Fix any right endpoint $R$ containing character $c$. Let $F$ be the first index at which $c$ appears. Any other eligible left endpoint $L$ satisfies $F\le L<R$. Therefore,

$$
R-F-1 \ge R-L-1.
$$

The pair $(F,R)$ is at least as long as every pair $(L,R)$ ending at the same position. Thus, none of the omitted later-left-boundary pairs can be the unique optimum. As the scan eventually treats every occurrence as a possible right endpoint, it considers a candidate at least as good as every valid pair in the string.

Another equivalent perspective is to focus on one character. Its longest possible interior is always between its first and last occurrences. The dictionary permanently retains the first, while the scan eventually reaches the last, so that maximum is considered. Taking `max` across all repeated characters then yields the global maximum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aa"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Brute-force all index pairs:** Test every $L<R:** - **Brute-force all index pairs:** Test every $L<R$ and update the answer when `s[L] == s[R]`. This is direct and correct, but it performs $O(n^2)$ comparisons instead of using the earliest-occurrence observation.
- **First and last occurrence arrays:** With 26 lowercase letters, two fixed arrays can record each letter's first and last indices. A second pass computes every distance. This is also $O(n)$ time and $O(1)$ space, but the one-pass dictionary updates the answer immediately.
- **Use `str.find` and `str.rfind` for each letter:** Calling both for every one of 26 fixed letters is still $O(n)$ under the fixed alphabet. It is concise but scans the same string repeatedly and is less adaptable to a larger alphabet.
- **Store every occurrence index:** This uses unnecessary $O(n)$ space. Only the first occurrence is needed because it dominates all later left boundaries for every future right endpoint.
- **Adjacent equal characters:** Their interior length is zero. The formula produces zero, which is a valid answer rather than `-1`.
- **No repeated character:** No candidate is evaluated and the sentinel `-1` is returned.
- **A character appears many times:** The first dictionary index must remain unchanged. Updating it would make later candidates shorter and could lose the optimum.
- **A one-character string:** It contains no pair, so the initialized `-1` is correct.
- **Do not include the boundary characters:** Using `i - d[c] + 1` would measure the whole bounded substring; using `i - d[c]` would still be one too large. The required interior is `i - d[c] - 1`.
- **Lexicographic concerns are irrelevant here:** The result asks only for maximum length. If several pairs have the same length, there is no need to retain their positions or choose among their contents.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `s`. The loop visits every character once. Dictionary membership, lookup, and insertion take expected $O(1)$ time, so the total expected time complexity is $O(n)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
