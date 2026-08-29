# Guided Example: Nim Game

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 9999}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are playing the following Nim Game with your friend:

The objective is to compute `true` from `{"n": 9999}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Winning and losing positions

A position is *winning* when the current player has at least one legal move that leaves the opponent in a losing position. A position is *losing* when every legal move leaves the opponent in a winning position. This distinction is about the player whose turn it is; it does not permanently label one person as the winner or loser.

Start with the smallest heap sizes:

- With one stone, the current player removes one stone and wins immediately.
- With two stones, the current player removes both stones and wins immediately.
- With three stones, the current player removes all three stones and wins immediately.
- With four stones, no immediate win is possible. Removing one, two, or three stones leaves respectively three, two, or one stone. The opponent can remove everything that remains and win.

Thus, sizes one through three are winning, while size four is losing. The next few positions reveal the pattern. From five stones, remove one and leave four. From six, remove two and leave four. From seven, remove three and leave four. Each of those moves hands the opponent the losing four-stone position. With eight stones, however, every legal move leaves five, six, or seven stones, all of which are winning for the next player.

So the classifications repeat in blocks of four:

| Stones modulo 4 | Status for the current player | Useful move |
| --- | --- | --- |
| $0$ | Losing | No legal move reaches another multiple of four |
| $1$ | Winning | Remove 1 |
| $2$ | Winning | Remove 2 |
| $3$ | Winning | Remove 3 |

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 9999}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why every nonmultiple of four is winning

Suppose the heap contains

$$
n = 4q + r,
$$

where the remainder $r$ is one of $1$, $2$, or $3$. Removing exactly $r$ stones is legal, because the game permits removing any amount from one through three. That move leaves

$$
n-r = 4q,
$$

which is a multiple of four. Therefore, from any positive heap size that is not divisible by four, the current player can deliberately move to a multiple of four.

This is not merely a locally convenient move. It establishes control over every later round. If the opponent removes $x$ stones, where $x\in\{1,2,3\}$, the controlling player removes $4-x$ stones. The response is also in the legal range, and the two moves together remove exactly four stones. Consequently, after each such pair of turns, the opponent again receives a multiple of four.

For example, begin with ten stones. The first player removes two, leaving eight. If the opponent then removes one, the first player removes three; if the opponent removes two, the first player removes two; and if the opponent removes three, the first player removes one. In every case the combined removal is four. Repeating this response eventually makes the opponent face four stones. Whatever that opponent removes, the first player removes the remaining stones and wins.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why every positive multiple of four is losing

Now suppose the current heap has $4q$ stones. Any legal move removes a number $x$ in $\{1,2,3\}$, leaving $4q-x$. Its remainder modulo four is respectively three, two, or one, so it is not a multiple of four. The opponent can then use the strategy above: remove $4-x$ stones and restore a multiple-of-four heap for the original player.

This proves both necessary directions. A nonmultiple has a move into the losing class, whereas a multiple has no move that stays in the losing class. The two classifications therefore support one another all the way down to the base position of four stones. There is no unexplored type of position, because every positive integer has exactly one remainder in $\{0,1,2,3\}$ when divided by four.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 9999}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Dynamic programming over every heap size:** Mark sizes one through `n` as winning or losing according to whether they can reach a losing predecessor. This can rediscover the four-position pattern, but it requires $O(n)$ time and $O(n)$ space if the whole table is stored, which is unnecessary for a value as large as $2^{31}-1$.
- **Constant-space iterative classification:** Track only a few recent winning and losing states while advancing from one to `n`. This reduces auxiliary space to $O(1)$ but still spends $O(n)$ time reproducing a pattern that the modulo invariant expresses directly.
- **Recursive game search:** Try each removal and ask recursively whether the opponent loses. Without memoization it repeats many states; with memoization it becomes a slower form of dynamic programming. Neither version is suitable when the mathematical structure already gives a constant-time answer.
- **Always removing three stones:** This does not preserve the winning invariant. The correct first removal depends on the current remainder, and later responses must complement the opponent's removal so that each pair totals four.
- **Confusing this game with general Nim:** Classical multi-heap Nim uses the bitwise XOR of heap sizes. This problem has exactly one heap and permits removing only one to three stones, so the relevant invariant is divisibility by four, not a multi-heap XOR calculation.
- **`n = 1`, `n = 2`, or `n = 3`:** The first player removes the entire heap in one legal move. Their nonzero remainders correctly produce `true`.
- **`n = 4`:** This is the first losing position. Every legal first move gives the opponent a heap small enough to take completely, so the zero remainder correctly produces `false`.
- **A larger multiple of four:** Values such as 8, 12, and 16 remain losing under optimal play. The opponent can complement every removal to make the two turns remove four stones in total.
- **A value immediately after a multiple of four:** For values such as 5 or 9, removing one stone leaves a losing multiple of four. The modulo test correctly returns `true`.
- **The maximum allowed input:** The method neither allocates memory proportional to `n` nor loops `n` times. It handles $2^{31}-1$ with the same constant amount of work as a small input.
- **Positive-input guarantee:** The constraints begin at one, so the implementation does not need to define a game with an initially empty heap. If zero were introduced under the usual rules, it would be losing for the player to move and would also have remainder zero, but that case is outside the stated contract.
- **Optimal-play assumption:** A winning position guarantees that a winning strategy exists. A player can still lose by choosing a poor move, but the requested Boolean assumes that the player follows the force-win strategy.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The solution performs one remainder operation and one comparison, independent of the numeric value of $n$. Under the problem's fixed-width integer model, both operations take constant time, so the time complexity is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
