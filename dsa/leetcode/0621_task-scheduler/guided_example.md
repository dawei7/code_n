# Guided Example: Task Scheduler

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tasks": ["A", "A", "A", "B", "B", "B"], "n": 2}`
- **Required output:** `8`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of CPU `tasks`, each labeled with a letter from A to Z, and a number `n`. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of **at least** `n` intervals between two tasks with the same label.

The objective is to compute `8` from `{"tasks": ["A", "A", "A", "B", "B", "B"], "n": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Reduce the schedule to the labels that create the tightest spacing requirement.** Every task takes exactly one interval. If cooldowns never force an idle interval, the answer is simply the number of tasks. Idles are needed only when repeated copies of a frequent label cannot be separated by enough other work.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tasks": ["A", "A", "A", "B", "B", "B"], "n": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

The exact solution first builds `Counter(tasks)`. Let:

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The exact solution first builds `Counter(tasks)`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

- $T$ be the total number of tasks;
- $x$ be the largest frequency of any label;
- $s$ be the number of labels whose frequency equals $x$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `8` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tasks": ["A", "A", "A", "B", "B", "B"], "n": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `8` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Max-heap simulation:** Repeatedly choose the m:** - **Max-heap simulation:** Repeatedly choose the most frequent available labels in cycles of length $n+1$. This can construct the timing explicitly and generalizes well, but it is more machinery than the closed formula needs.
- **Sort 26 frequencies and count idle slots:** Use one maximum label to create gaps, then fill them with other frequencies. This is also constant-alphabet linear time but has more bookkeeping around tied maxima.
- **Cooldown queue simulation:** Track time, a max heap of available labels, and a queue of cooling labels. It is useful when an actual schedule is needed, but unnecessary for returning only the length.
- **`n = 0`:** The skeleton cannot force a gap, and the maximum returns exactly $T$.
- **Every task label is unique:** Then $x=1$ and $s=T$; the skeleton equals $T$, so no idle is introduced.
- **Only one distinct label:** Here $s=1$; the answer is $(x-1)(n+1)+1$, representing one task followed by $n$ idles between repetitions.
- **Several maximum-frequency labels:** The final `+ s` term is essential. Omitting it undercounts the last round.
- **Enough filler tasks:** When $T$ exceeds the skeleton, the result is $T$ because useful work fills all cooldown gaps.
- **Nonempty input guarantee:** It makes `max(cnt.values())` safe. An empty task array would require a separate return of 0.
- **Fixed alphabet assumption:** Constant space depends on A through Z. With arbitrary labels, describe counter storage as $O(U)$.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(T)$. Counting all tasks takes $O(T)$ time. Scanning the frequency values to find $x$ and then count $s$ takes $O(U)$ time, where $U$ is the number of distinct labels. Because labels are restricted to the 26 uppercase English letters, $U\le26$ is a fixed constant. Total time is therefore $O(T)$.
- **Auxiliary Space Complexity:** $O(26)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
