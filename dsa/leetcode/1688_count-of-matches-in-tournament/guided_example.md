# Guided Example: Count of Matches in Tournament

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 7}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `n`, the number of teams in a tournament that has strange rules:

The objective is to compute `6` from `{"n": 7}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count eliminations instead of simulating rounds

The round rules look different for even and odd team counts, but every actual match has one invariant outcome: exactly one team loses and is eliminated. The winning team remains in the tournament.

The tournament starts with `n` teams and ends when exactly one champion remains. Therefore exactly `n - 1` teams must be eliminated.

Since every match eliminates exactly one team, the number of matches is also exactly `n - 1`. The source returns that expression directly.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 7}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why a bye does not affect the count

In an odd-sized round, one team advances without playing. That bye eliminates no team and counts as no match. The other `n - 1` teams form pairs, and each match eliminates one of them.

The bye changes when eliminations occur, not how many eliminations are ultimately necessary. All nonchampion teams must still lose one match at some later or current round.

For seven teams, three first-round matches eliminate three teams and one team receives a bye, leaving four. Two more matches leave two teams, and one final match selects the champion. The distribution is `3 + 2 + 1`, but the total is simply six, or `7 - 1`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | In an odd-sized round, one team advances without playing.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A one-to-one correspondence

Every match can be paired with the unique team that loses that match. No team loses twice because its first loss removes it permanently. The champion never loses.

Thus the set of matches is in one-to-one correspondence with the set of nonchampion teams:

- each match contributes one distinct eliminated team;
- each of the `n - 1` nonchampions must be eliminated by some match.

This is stronger than merely observing examples. It proves that no legal arrangement of pairings or byes can change the total.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 7}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Round simulation:** Repeatedly add `floor(n/2):** - **Round simulation:** Repeatedly add `floor(n/2)` matches and replace `n` with `ceil(n/2)`. It is correct but takes $O(\log n)$ time and obscures the elimination invariant.
- **Recursive simulation:** It mirrors the tournament tree but adds unnecessary call-stack overhead.
- **One team:** No match is needed, and `n - 1` correctly returns zero.
- **Two teams:** One match eliminates one team and selects the winner; the formula returns one.
- **Odd team count:** A bye eliminates nobody and therefore adds nothing beyond the matches that actually occur.
- **Even team count:** Every team is paired, but only one member of each pair is eliminated, matching one elimination per match.
- **Random bye selection:** Which team advances freely can affect identities and bracket shape, never the total number of nonchampions.
- **Different winners:** Any possible champion leaves exactly the other `n - 1` teams to be eliminated.
- **No draws assumed:** The rules state that half of each matched pair advances, so every match has exactly one loser; the proof relies on this.
- **Closed-form insight:** The answer depends only on initial and final active counts, not the number of rounds.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The implementation performs one subtraction and one return, independent of `n`. Its time complexity is $O(1)$ and its auxiliary space complexity is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
