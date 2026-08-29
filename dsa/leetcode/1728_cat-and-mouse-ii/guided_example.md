# Guided Example: Cat and Mouse II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"grid": ["####F", "#C...", "M...."], "catJump": 1, "mouseJump": 2}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A game is played by a cat and a mouse named Cat and Mouse.

The objective is to compute `true` from `{"grid": ["####F", "#C...", "M...."], "catJump": 1, "mouseJump": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Model the game by positions and whose turn it is

A complete game state is `(mouse_position, cat_position, turn)`. Turn zero means Mouse moves next; turn one means Cat moves next.

The board contains at most 64 cells, so although play can last many turns, the number of distinct position-turn states is finite: at most $2V^2$, where $V$ is the number of flattened grid positions.

The source classifies each state as:

- zero: outcome not yet proven,
- one: Mouse can force a win,
- two: Cat can force a win.

Rather than exploring forward recursively and struggling with cycles, it starts from known terminal outcomes and propagates their consequences backward.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"grid": ["####F", "#C...", "M...."], "catJump": 1, "mouseJump": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Flatten cells and precompute legal moves

Cell `(i,j)` becomes vertex `i*n+j`. While scanning non-wall cells, the source records Cat, Mouse, and food positions.

For each of the four directions, it tries jump lengths from zero through the player's maximum. A jump stops as soon as it leaves the grid or encounters a wall; this correctly prevents jumping over walls.

The legal destinations are stored in `g_mouse[v]` and `g_cat[v]`. Jump length zero represents staying still.

Because zero is considered separately for all four directions, the exact adjacency lists contain four duplicate stay destinations. These duplicates do not add a new strategic choice. The later degree counts and predecessor enumeration both retain the same multiplicity, so their eliminations remain consistent; they only add a constant amount of redundant processing.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the same move lists can find predecessors

A legal straight jump between two open cells is reversible: if a player can move from `u` to `v` without crossing a wall and within its jump limit, the reverse direction from `v` to `u` is also legal.

Therefore, when retrograde processing asks which previous player positions could move into a current position, it can iterate that current position's ordinary move list.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"grid": ["####F", "#C...", "M...."], "catJump": 1, "mouseJump": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Memoized forward minimax with a turn counter:** It can encode the 1000-turn limit directly but creates a much larger time dimension and delicate cycle handling.
- **Value iteration:** Repeatedly classify states until convergence. Retrograde degree processing reaches the same fixed point more directly.
- **No stay move:** That would change the game; jump length zero must be legal for both players.
- **Duplicate stay destinations:** They are strategy-equivalent but counted consistently in degrees and predecessor lists.
- **Wall blocking:** Directional generation stops at the first wall, so no longer jump may cross it.
- **Board boundary:** Generation also stops when coordinates leave the grid.
- **Mouse reaches food:** Outcome one is terminal before Cat's next move.
- **Cat reaches food:** Outcome two is terminal.
- **Same position:** Cat wins, including overlap at food.
- **Disconnected regions:** Unreachable terminal states may leave cycles unresolved, which returns false for Mouse.
- **Multiple legal winning moves:** Finding the first is enough to classify the predecessor.
- **All moves losing:** Degree reaches zero only after every listed option has been refuted.
- **Turn encoding:** Zero is Mouse and one is Cat; the arithmetic `t-1` relies on outcomes one and two.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(V^2D)$. Let $V$ be the number of flattened board positions and $D$ the maximum number of destinations considered per position, proportional to the jump bounds and four directions.
- **Auxiliary Space Complexity:** $O(V^2+VD)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
