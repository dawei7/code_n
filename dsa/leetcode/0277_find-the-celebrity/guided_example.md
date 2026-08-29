# Guided Example: Find the Celebrity

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 3, "knows_matrix": [[true, true, false], [false, true, false], [true, true, true]]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Suppose you are at a party with `n` people labeled from `0` to $n - 1$ and among them, there may exist one celebrity. The definition of a celebrity is that all the other $n - 1$ people know the celebrity, but the celebrity does not know any of them.

The objective is to compute `1` from `{"n": 3, "knows_matrix": [[true, true, false], [false, true, false], [true, true, true]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use each API answer to eliminate one person

A celebrity must satisfy two conditions relative to every other person:

- the celebrity knows nobody else; and
- everybody else knows the celebrity.

Testing both conditions for every possible person would make $O(n^2)$ calls to `knows`. The key observation is that one call `knows(a, b)` always proves that at least one of `a` and `b` is not the celebrity.

If `knows(a, b)` is true, `a` cannot be the celebrity because `a` knows another person. If it is false, `b` cannot be the celebrity because at least one other person, namely `a`, does not know `b`. Regardless of the answer, one participant in the comparison is conclusively eliminated.

This lets the source reduce $n$ possibilities to one survivor using only $n-1$ questions.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 3, "knows_matrix": [[true, true, false], [false, true, false], [true, true, true]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Maintain one surviving candidate

The solution begins with `ans = 0`. It then compares the current candidate with each person `i` from 1 through `n - 1`.

If `knows(ans, i)` returns true, the current candidate has been caught knowing someone and is disqualified. Person `i` has not been disqualified by this particular fact, so the source replaces `ans` with `i`.

If `knows(ans, i)` returns false, person `i` is disqualified because `ans` does not know them. The current candidate has not been disproved by this fact, so `ans` remains unchanged.

It is important not to read too much into the survivor. In the true branch, knowing that the old candidate knows `i` does not prove that `i` is a celebrity; it merely leaves `i` as the only member of this pair still possible. Likewise, a false result does not prove `ans` is a celebrity. This phase eliminates candidates but does not verify all required relationships.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why no real celebrity is ever discarded

After processing person `i`, `ans` is the only person among labels `0` through `i` who has not been ruled out by the questions asked so far.

The statement is true initially for person 0 alone. At the next comparison, exactly one of the old survivor and the new person is eliminated according to the API result, so one survivor remains for the enlarged prefix.

More strongly, if a real celebrity belongs to the processed prefix, that celebrity must be the survivor. Suppose the current candidate is the celebrity. They know nobody, so `knows(ans, i)` must be false and the algorithm keeps them. Suppose instead the newly considered person `i` is the celebrity. Everyone else knows them, so `knows(ans, i)` must be true and the algorithm changes the candidate to `i`. The update can never discard an actual celebrity.

After the loop, every person except `ans` has been disproved. Therefore, if a celebrity exists, it must be `ans`. This reduces verification to one person.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 3, "knows_matrix": [[true, true, false], [false, true, false], [true, true, true]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Verify every person independently:** Check both directions for each possible candidate. It is simple but makes $O(n^2)$ API calls in the worst case because the same relationships are queried repeatedly.
- **Stack elimination:** Put all people on a stack, pop two at a time, query one relationship, and push the only remaining possible candidate. This implements the same elimination proof with $O(n)$ calls but uses $O(n)$ stack space unnecessarily.
- **Cache API results:** Memoizing elimination calls can avoid repeating some questions during verification, at the cost of $O(n)$ stored results. The exact source already stays below `3n` calls with constant space.
- **Return the survivor without verification:** Incorrect when no celebrity exists. Elimination guarantees only that every other person was ruled out, not that the survivor satisfies all unqueried conditions.
- **Candidate knows someone:** One true outgoing query is enough to return `-1`; no incoming facts can repair that violation.
- **Someone does not know the candidate:** One false incoming query is likewise enough to return `-1`, even if the candidate knows nobody.
- **Self relationship:** The diagonal is skipped because knowing oneself neither qualifies nor disqualifies a celebrity under the definition.
- **Exactly one real celebrity:** The elimination pass is guaranteed to preserve that person, and complete verification returns their label.
- **No celebrity:** A survivor still emerges, but verification rejects it and returns `-1`.
- **Two people:** One elimination question leaves a candidate, and verification checks both required directions against the one other person.
- **API opacity:** The algorithm uses only `knows(a, b)` and never assumes direct access to `graph`. Reading or scanning the entire matrix would violate the interface contract.
- **Short-circuit order:** Querying the candidate's outgoing edge first allows immediate rejection without the incoming call. Reversing the checks remains correct but changes which failed cases save an API call.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. The elimination pass performs exactly $n-1$ calls to `knows`. Verification considers $n-1$ other people and makes at most two calls for each. The worst-case total is
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
