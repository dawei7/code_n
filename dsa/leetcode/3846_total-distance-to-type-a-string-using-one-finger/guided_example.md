# Guided Example: Total Distance to Type a String Using One Finger

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "hello"}`
- **Required output:** `17`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a special keyboard where keys are arranged in a rectangular grid as follows.
<table style="border: 1px solid black;">
	<tbody>
		<tr>
			<td style="border: 1px solid black;">q</td>
			<td style="border: 1px solid black;">w</td>
			<td style="border: 1px solid black;">e</td>
			<td style="border: 1px solid black;">r</td>
			<td style="border: 1px solid black;">t</td>
			<td style="border: 1px solid black;">y</td>
			<td style="border: 1px solid black;">u</td>
			<td style="border: 1px solid black;">i</td>
			<td style="border: 1px solid black;">o</td>
			<td style="border: 1px solid black;">p</td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">a</td>
			<td style="border: 1px solid black;">s</td>
			<td style="border: 1px solid black;">d</td>
			<td style="border: 1px solid black;">f</td>
			<td style="border: 1px solid black;">g</td>
			<td style="border: 1px solid black;">h</td>
			<td style="border: 1px solid black;">j</td>
			<td style="border: 1px solid black;">k</td>
			<td style="border: 1px solid black;">l</td>
			<td style="border: 1px solid black;"> </td>
		</tr>
		<tr>
			<td style="border: 1px solid black;">z</td>
			<td style="border: 1px solid black;">x</td>
			<td style="border: 1px solid black;">c</td>
			<td style="border: 1px solid black;">v</td>
			<td style="border: 1px solid black;">b</td>
			<td style="border: 1px solid black;">n</td>
			<td style="border: 1px solid black;">m</td>
			<td style="border: 1px solid black;"> </td>
			<td style="border: 1px solid black;"> </td>
			<td style="border: 1px solid black;"> </td>
		</tr>
	</tbody>
</table>

The objective is to compute `17` from `{"s": "hello"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Precompute one coordinate for every letter

The keyboard rows are stored as:

- `"qwertyuiop"` at row 0;
- `"asdfghjkl"` at row 1;
- `"zxcvbnm"` at row 2.

The nested module-level loops use `enumerate` to assign each character:

`pos[key] = (row_index, column_index)`.

The shorter second and third strings naturally omit the blank table cells. Every lowercase English letter appears exactly once, so `pos` ends with 26 unambiguous coordinates.

This precomputation keeps the typing loop simple and avoids searching the keyboard rows for every character.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "hello"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The finger position is completely determined

Only one finger is used, and characters must be typed in string order. There is no choice about which key to visit next.

Before the first character, the finger is on `'a'`, so the source initializes:

`pre = 'a'`.

For each current character `cur`, `pos[pre]` is the starting coordinate and `pos[cur]` is the destination.

After paying the distance, `pre = cur` records that the finger remains on the newly typed key. This becomes the starting position for the next character.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Compute one Manhattan distance

If the previous key is at $(x_1,y_1)$ and the current key at $(x_2,y_2)$, the required movement is:

$$
\lvert x_1-x_2\rvert+\lvert y_1-y_2\rvert.
$$

The source calculates exactly this and adds it to `ans`.

Manhattan distance corresponds to moving vertically and horizontally through the grid. No diagonal shortcut is allowed.

The layout rows need not have equal numbers of real keys for this formula. Every actual letter still has the coordinate assigned by its table cell.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `17` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "hello"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `17` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Search row strings per character:** Find each letter's row and column on demand. It remains bounded by 26 but repeats avoidable work; the coordinate map is clearer.
- **Hard-code 26 coordinates:** This removes initialization loops but is more error-prone and harder to compare with the shown keyboard.
- **Breadth-first search:** It is unnecessary because the statement defines distance directly as Manhattan distance.
- **First character a:** The finger already starts there, so the first contribution is zero.
- **Repeated consecutive letter:** The two coordinates match and movement costs zero.
- **One-character string:** The answer is simply the distance from `a` to that key.
- **Letters on different rows:** Both vertical and horizontal differences contribute.
- **Blank table cells:** They are not included in the row strings and never appear in valid input.
- **Finger persistence:** Every transition starts from the previously typed character, not from `a` again.
- **All lowercase letters covered:** The coordinate dictionary contains every permitted input character.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=\lvert\texttt{s}\rvert$. Building `pos` processes 26 fixed letters once at module load, which is $O(1)$ with respect to $N$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
