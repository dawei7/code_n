# Guided Example: High Five

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"items": [[1, 100], [1, 90], [1, 80], [1, 70], [1, 60]]}`
- **Required output:** `[[1, 80]]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a list of the scores of different students, `items`, where $\text{items}[i] = [\text{ID}_{i}, \text{score}_{i}]$ represents one score from a student with $\text{ID}_{i}$, calculate each student's **top five average**.

The objective is to compute `[[1, 80]]` from `{"items": [[1, 100], [1, 90], [1, 80], [1, 70], [1, 60]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate scores by student before choosing the best five

Every input row contains a student identifier and one score. Scores belonging to different students must never influence one another, so the first task is to partition the records by identifier. The `defaultdict(list)` named `d` performs that partition. When the loop reads `i, x`, it appends score `x` to the list stored under student `i`.

After all $N$ records have been processed, `d[i]` contains every score record for student `i`, including repeated score values. Repetition is intentional: two exams with the same score are two records and can both belong to the top five.

The same pass records the largest identifier in `m`. This solution does not later sort the dictionary keys. Instead, it visits every integer identifier from one through `m` and emits a row only when that identifier has scores. Since this scan is numerically increasing, the output rows are automatically ordered by student ID as the contract requires.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"items": [[1, 100], [1, 90], [1, 80], [1, 70], [1, 60]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why reading an absent identifier is safe

The loop `for i in range(1, m + 1)` may visit gaps. For example, the data could contain IDs one and seven but no IDs two through six. Because `d` is a `defaultdict(list)`, reading `d[i]` for a missing ID creates and returns an empty list rather than raising an error.

The assignment expression `if xs := d[i]` both names the list `xs` and checks whether it is nonempty. Empty lists are false, so missing IDs are skipped. Nonempty lists are true, so represented students proceed to the averaging step. The constraints guarantee at least five scores for each represented ID, meaning the later selection always has enough records.

Creating empty dictionary entries for gaps is a subtle implementation effect. It does not alter the answer, but it means the dictionary can contain identifiers that were absent from the input after the output scan. The bounded identifier range keeps this harmless.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Select exactly the five largest values

For a represented student, `nlargest(5, xs)` returns a list containing that student’s five greatest scores. Conceptually, it maintains a small min-heap of at most five candidates. A new score enters when there is room or when it is better than the smallest retained candidate. Once all scores have been considered, no discarded score can exceed a retained score, so the retained multiset is exactly the top five.

This selection respects duplicate values. If a student’s scores are `100, 100, 100, 100, 100, 90`, the five separate `100` records are all retained. The task ranks score records, not distinct numeric values.

The solution then computes `sum(nlargest(5, xs)) // 5`. The sum includes exactly five scores. Floor division by five implements the required integer division. Scores are nonnegative, so Python’s floor division is the same as truncating the ordinary average toward zero. An average such as `88.6` therefore becomes `88`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[[1, 80]]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"items": [[1, 100], [1, 90], [1, 80], [1, 70], [1, 60]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[[1, 80]]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Five-element min-heap per student:** Push each score into that student’s heap and pop the minimum whenever its size exceeds five. This truly keeps only $O(S)$ score storage because five is constant, and it is the strongest choice when students can have many records.
- **Sort all records:** Sort by ID ascending and score descending, then take the first five scores in each ID block. The logic is direct, but sorting all $N$ records costs $O(N\log N)$ time and may mutate the input if done in place.
- **Store all scores and sort each list:** Sorting every student’s complete list is simpler than heap selection, but it orders many low scores that are never used. Its total time can reach $O(N\log N)$.
- **Sort dictionary keys instead of scanning to `m`:** Iterating over `sorted(d)` costs $O(S\log S)$ and behaves well for sparse or very large IDs. The current range scan is attractive only because IDs are positive and capped at one thousand.
- **Exactly five scores:** `nlargest(5, xs)` returns all five, and the average is their integer quotient as usual.
- **More than five scores:** Only the greatest five affect the result; every lower score is correctly ignored after selection.
- **Duplicate top scores:** Equal scores are separate records. Several equal values may all appear among the selected five, and no deduplication should occur.
- **Average with a fractional part:** Integer division discards the fraction for these nonnegative scores, so `443 // 5` is `88` rather than a rounded `89`.
- **Score zero:** Zero is valid. It can belong to the top five when a student has sufficiently low scores, and the sum and division remain correct.
- **Gaps between identifiers:** Empty lists created for missing IDs are false and produce no result rows. The rows that are produced remain in increasing order.
- **No identifier zero:** The scan begins at one because the constraints make every valid ID at least one. Supporting zero or negative IDs would require iterating actual keys instead.
- **Empty input outside the contract:** The official input contains at least one record. With an empty list, `m` would remain zero and the function would return an empty answer, but represented-student guarantees would no longer be meaningful.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N + S\log S)$. Let $N$ be the number of score records, $S$ the number of distinct student IDs, and $U$ the largest identifier encountered. The package records a required time bound of $O(N + S\log S)$ and a required space bound of $O(S)$. That notation reflects the common optimal design that keeps only five scores per student and sorts the $S$ identifiers.
- **Auxiliary Space Complexity:** $O(S)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
