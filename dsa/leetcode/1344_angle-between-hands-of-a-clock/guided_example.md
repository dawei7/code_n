# Guided Example: Angle Between Hands of a Clock

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"hour": 12, "minutes": 30}`
- **Required output:** `165.0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two numbers, `hour` and `minutes`, return *the smaller angle (in degrees) formed between the *`hour`* and the *`minute`* hand*.

The objective is to compute `165.0` from `{"hour": 12, "minutes": 30}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Minute hand position

The minute hand completes one full rotation in sixty minutes. It therefore moves

$$
\frac{360}{60} = 6
$$

degrees per minute. At `minutes` minutes past the hour, its angle is `m = 6 * minutes`. For thirty minutes, this gives $180$ degrees; for fifteen minutes, it gives $90$ degrees.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"hour": 12, "minutes": 30}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Hour hand position

The hour hand completes one full rotation in twelve hours, so moving from one numbered hour mark to the next covers

$$
\frac{360}{12} = 30
$$

degrees. The integer-hour contribution is therefore `30 * hour`.

The hour hand does not wait at one hour mark and jump to the next when the hour changes. It moves continuously as minutes pass. During sixty minutes it travels another thirty degrees, which is $0.5$ degree per minute. The exact position is therefore `h = 30 * hour + 0.5 * minutes`.

For example, at 3:30 the hour hand is halfway between three and four. Its angle is `30 * 3 + 0.5 * 30 = 105` degrees, not merely ninety degrees. The minute hand is at $180$ degrees, so their direct difference is $75$ degrees.

The source does not reduce `hour` modulo twelve. At twelve o’clock it represents the hour hand at $360$ degrees rather than zero degrees. These are the same direction on a circle. For times after 12:00, it represents the hour hand just beyond $360$ degrees. The later circular-distance calculation still produces the correct smaller angle.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Choose the smaller circular separation

`diff = abs(h - m)` measures one angular separation between the two numerical positions. On a circle there are always two ways to travel from one hand to the other:

- One route has length `diff`.
- The complementary route has length `360 - diff`.

The required answer is the shorter route, so the method returns `min(diff, 360 - diff)`.

At 12:30, the source computes `h = 375` and `m = 180`. The direct difference is $195$ degrees, while the other route is `360 - 195 = 165` degrees. Returning $165$ is correct. At 12:00, the difference is $360$, whose complement is zero, also correct.

Under the input range, the representation never causes a problematic difference larger than $360$ degrees. For hour twelve, increasing minutes moves both hands clockwise, and the relevant difference stays within the full-circle range. For hours one through eleven, both positions are already within the ordinary range.

The formulas give exact physical positions for the idealized clock. The absolute difference gives one route, and subtracting from the full circle gives the only other route. Taking the minimum therefore exhausts the two possibilities and returns the requested smaller angle.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `165.0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"hour": 12, "minutes": 30}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `165.0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Normalize the hour first:** Use `hour % 12` before computing its angle. This keeps both positions in the range from zero up to but not including $360$ degrees and gives the same smaller result.
- **Integer half-degrees:** Multiply every angle by two, compute with integers, and divide the final minimum by two. This avoids floating-point arithmetic entirely.
- **Ignoring minute movement of the hour hand:** Using only `30 * hour` is incorrect except at minute zero. The extra `0.5 * minutes` term is essential.
- **Returning only the absolute difference:** A direct difference above $180$ degrees is the larger angle. The complementary `360 - diff` must also be considered.
- **Exactly twelve o’clock:** The source represents the hour position as $360$ degrees and returns the complementary angle zero.
- **Half past twelve:** The unnormalized hour position is $375$ degrees; the circular complement still yields the correct $165$ degrees.
- **Hands overlap:** When `h == m`, both the direct smaller angle and the returned minimum are zero.
- **Opposite hands:** When `diff == 180`, both circular routes have the same angle, so the method returns $180$.
- **Minute zero:** The hour hand lies exactly on an hour mark because the minute contribution is zero.
- **Minute fifty-nine:** Continuous hour-hand movement is still included, and the same formulas need no end-of-hour special case.
- **Why the result never exceeds $180$ degrees:** The two candidate routes sum to $360$ degrees, so at least one of them is no greater than half a circle. Taking their minimum enforces the conventional smaller-angle range.
- **Accepted numeric type:** Returning an integer-looking value as a Python float is valid because the contract accepts a numeric angle within the stated tolerance.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The method performs a fixed number of multiplications, additions, a subtraction, an absolute value, and a minimum. null of these operations depends on the magnitude of the input range in the standard arithmetic model. Time complexity is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
