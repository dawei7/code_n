# Guided Example: Lexicographically Smallest String After Deleting Duplicate Characters

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "aaccb"}`
- **Required output:** `"aacb"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `s` that consists of lowercase English letters.

The objective is to compute `"aacb"` from `{"s": "aaccb"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: The final string need not contain each letter exactly once

An occurrence may be deleted only while another copy of the same letter remains. Therefore every distinct letter in the original string must survive at least once. Any subsequence retaining at least one occurrence of each original letter is reachable: delete the unwanted occurrences one by one, always leaving a chosen survivor.

However, deleting every duplicate is not automatically best. Lexicographic order compares the first differing character; only when one string is a complete prefix of the other does the shorter string win. In `"aaccb"`, the one-copy result `"acb"` is larger than `"aacb"` because their first characters agree and then `a < c` at the second position. Keeping an extra small letter near the front can be beneficial.

The real task is to delete an occurrence only when its removal makes the earliest possible part of the string smaller, while never removing the last copy of any letter.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "aaccb"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Track how many undeleted copies still exist

`cnt = Counter(s)` starts with the total frequency of every letter. The source decrements a count only when an occurrence is popped and permanently deleted. It does not decrement merely because the scan passes a character.

Consequently, `cnt[x]` always means the number of copies of `x` that have not been deleted: copies already stored in `stk` plus copies not processed yet. This is different from the common “remaining suffix frequency” interpretation.

The test `cnt[stk[-1]] > 1` therefore answers exactly the safety question: if the top stack occurrence is deleted, does at least one copy of that letter remain somewhere among the other kept or future occurrences? If yes, popping respects the operation rule. If the count is 1, that top occurrence is the last surviving copy and cannot be removed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Use the stack to repair a harmful adjacent order

The stack holds the current subsequence after chosen deletions. Every new character `c` is compared with the most recent kept character.

While all three conditions hold—

- the stack is nonempty;
- `stk[-1] > c`, so the previous character is lexicographically larger;
- `cnt[stk[-1]] > 1`, so deleting it preserves another copy—

the source pops the stack top and decrements that letter's surviving count.

Why is this deletion beneficial? At the position occupied by the larger top character, keeping it would expose that character before the smaller current `c`. Removing it lets `c`, or another no-larger character uncovered by further pops, appear earlier. The first difference between the improved subsequence and one retaining the harmful top favors the improved subsequence.

After one pop, a still-earlier stack character may also be larger than `c` and safely duplicated. The `while` loop continues so that `c` moves left across the entire removable decreasing suffix, not just one character.

The current `c` is then always appended. Unlike the classic “remove duplicate letters” problem, there is no `in_stack` set and no rule skipping an already-kept letter. Extra copies can improve lexicographic order, so every occurrence remains unless a concrete greedy pop deletes it.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"aacb"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "aaccb"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"aacb"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Force one copy per distinct letter:** The classic monotonic-stack algorithm with a kept set solves a different problem. It would return `"acb"` for `"aaccb"` and miss the smaller legal answer `"aacb"`.
- **Enumerate reachable subsequences:** Every subsequence retaining all distinct letters is a candidate, giving exponentially many possibilities and making brute force infeasible for $N=10^5$.
- **Dynamic programming over positions and counts:** The state needed to compare arbitrary future suffixes is large; the exchange property captured by the stack eliminates that complexity.
- **All characters distinct:** Every count is 1, so no pop is legal. The original string is the only reachable result and is returned unchanged.
- **All characters equal:** The scan keeps every copy, then the final loop removes trailing copies until exactly one remains.
- **A decreasing string with no duplicates:** Larger leading letters cannot be removed because each is the last copy of its letter, so the result remains the original string.
- **A larger letter duplicated later:** An earlier copy can be popped when a smaller current letter arrives because `cnt` confirms another copy survives, allowing the smaller letter to move forward.
- **Another copy already lies earlier in the stack:** The safety count includes kept occurrences as well as future ones. A duplicated top may be deleted even when no copy remains in the unread suffix.
- **Trailing duplicates:** They require the second loop; no future character exists to trigger the main comparison, but shortening an equal-prefix result is still lexicographically beneficial.
- **Counter interpretation:** Counts are decremented only for deletions. Treating them as unread-suffix frequencies and decrementing every scanned character would change the safety condition and no longer match the exact source.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=\lvert\texttt{s}\rvert$. Building `Counter(s)` takes $O(N)$ time. Every character is pushed onto `stk` exactly once. An occurrence can be popped at most once, either during the scan or during final trimming. Although a `while` loop is nested inside the `for` loop, all its iterations across the entire run total at most $N$. The total running time is $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
