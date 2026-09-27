# Guided Example: Monotonic Array

We trace the step-by-step evaluation of directional monotonicity invariants, adjacent pairwise difference signs ($\Delta_i = nums[i+1] - nums[i]$), simultaneous tracking of non-decreasing and non-increasing properties, and definitive boolean classification on representative integer sequences:

- **Primary Input:** $nums = [1, 2, 2, 3]$
- **Required Output:** `true`
  - Monotonicity definition:
    - An array $nums$ is **monotone increasing** (more precisely, non-decreasing) if for all $i \le j$, $nums[i] \le nums[j]$. Equivalently, for every adjacent pair $(nums[i], nums[i+1])$, $nums[i] \le nums[i+1]$ (i.e. $\Delta_i \ge 0$).
    - An array $nums$ is **monotone decreasing** (more precisely, non-increasing) if for all $i \le j$, $nums[i] \ge nums[j]$. Equivalently, for every adjacent pair $(nums[i], nums[i+1])$, $nums[i] \ge nums[i+1]$ (i.e. $\Delta_i \le 0$).
    - An array is **monotonic** if it is either monotone increasing or monotone decreasing.
  - Evaluation on $[1, 2, 2, 3]$:
    - Pair 0: $(1, 2) \implies 1 \le 2$ (valid for non-decreasing), but $1 \not\ge 2$ (violates non-increasing). Non-increasing is eliminated!
    - Pair 1: $(2, 2) \implies 2 \le 2$ (valid for non-decreasing). Equality preserves non-decreasing.
    - Pair 2: $(2, 3) \implies 2 \le 3$ (valid for non-decreasing).
    - Since every adjacent pair satisfies $nums[i] \le nums[i+1]$, the entire array is non-decreasing $\implies$ return **`true`**.
- **Counterexample Instance:** $nums = [1, 3, 2]$
  - Pair 0: $(1, 3) \implies 1 \le 3$ (rules out decreasing).
  - Pair 1: $(3, 2) \implies 3 \ge 2$ (rules out increasing).
  - Both directions eliminated $\implies$ return **`false`**.

---

## 1. Instance & Teaching Goal

Given the sequence $nums = [1, 2, 2, 3]$ of length $n = 4$:

Determine whether the values are ordered monotonically in at least one direction.

```text
Sequence Visualization:
Index:      0       1       2       3
Value:     [1] ---> [2] === [2] ---> [3]
Step:          +1       0       +1
Trend:       Rising   Plateau  Rising   ==> Monotone Non-Decreasing
```

The core teaching goal is to demonstrate that testing monotonicity does not require multiple passes or sorting. By initializing two concurrent hypotheses—`is_increasing = true` and `is_decreasing = true`—any strictly positive step falsifies the decreasing hypothesis, while any strictly negative step falsifies the increasing hypothesis. Plateau steps (where $nums[i] = nums[i+1]$) satisfy both hypotheses simultaneously.

---

## 2. Conceptual Foundation & Invariants

We maintain two boolean directional flags across the traversal:

| State Variable | Role & Meaning | Initial State |
|---|---|---|
| `is_increasing` | Remains `true` as long as no step strictly decreases ($nums[i] \le nums[i+1]$) | `true` |
| `is_decreasing` | Remains `true` as long as no step strictly increases ($nums[i] \ge nums[i+1]$) | `true` |

### Transition Rules for Adjacent Pair $(a, b)$

1. If $a < b$:
   - The sequence strictly climbs.
   - `is_decreasing` becomes permanently `false`.
   - `is_increasing` remains unchanged.
2. If $a > b$:
   - The sequence strictly drops.
   - `is_increasing` becomes permanently `false`.
   - `is_decreasing` remains unchanged.
3. If $a = b$:
   - Both relations $a \le b$ and $a \ge b$ hold simultaneously.
   - Neither hypothesis is falsified; both flags retain their current values.

> **Directional Invariant.** After processing prefix $nums[0 \dots k]$, `is_increasing` is `true` if and only if the prefix is non-decreasing, and `is_decreasing` is `true` if and only if the prefix is non-increasing. If at any index both flags become `false`, monotonicity is permanently broken.

---

## 3. Step-by-Step Worked Execution

We trace the representative instance $nums = [1, 2, 2, 3]$ across all adjacent pairs.

| Step | Pair $(nums[i], nums[i+1])$ | Difference $\Delta$ | Increasing Test ($a \le b$) | Decreasing Test ($a \ge b$) | `is_increasing` | `is_decreasing` | Status & Deduction |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Init | — | — | — | — | `true` | `true` | Both hypotheses active. |
| 1 | $(nums[0], nums[1]) = (1, 2)$ | $+1$ | $1 \le 2$ (Pass) | $1 \ge 2$ (Fail) | `true` | `false` | First step rises: decreasing hypothesis eliminated. |
| 2 | $(nums[1], nums[2]) = (2, 2)$ | $0$ | $2 \le 2$ (Pass) | $2 \ge 2$ (Pass) | `true` | `false` | Plateau: equality satisfies non-decreasing invariant. |
| 3 | $(nums[2], nums[3]) = (2, 3)$ | $+1$ | $2 \le 3$ (Pass) | $2 \ge 3$ (Fail) | `true` | `false` | Final step rises: non-decreasing property holds globally. |

### Final Classification

- `is_increasing` = `true`
- `is_decreasing` = `false`
- Combined result: $\text{is\_increasing} \lor \text{is\_decreasing} = \text{true} \lor \text{false} = \mathbf{true}$.

---

## 4. Counterexample Execution: Non-Monotonic Array

To contrast, consider the non-monotonic instance $nums = [1, 3, 2]$.

| Step | Pair $(a, b)$ | $\Delta$ | Non-Decreasing Check | Non-Increasing Check | `is_increasing` | `is_decreasing` | State Summary |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Init | — | — | — | — | `true` | `true` | Both hypotheses active. |
| 1 | $(1, 3)$ | $+2$ | $1 \le 3$ (Pass) | $1 \ge 3$ (Fail) | `true` | `false` | Rising step invalidates decreasing hypothesis. |
| 2 | $(3, 2)$ | $-1$ | $3 \le 2$ (Fail) | $3 \ge 2$ (Pass) | `false` | `false` | Falling step invalidates increasing hypothesis. |

At step 2, both flags have become `false`. An early exit may terminate immediately, returning `false`.

---

## 5. Algorithmic Correctness

### Directional Decoupling Principle

The mathematical condition for monotonicity is a logical disjunction:
$$
\text{Monotonic}(nums) \iff \left( \forall i \in [0, n-2]: nums[i] \le nums[i+1] \right) \lor \left( \forall i \in [0, n-2]: nums[i] \ge nums[i+1] \right)
$$

Because universal quantification distributes over conjunction but not disjunction, evaluating both properties simultaneously in a single pass is correct:
1. If an array contains both an ascending step ($nums[i] < nums[i+1]$) and a descending step ($nums[j] > nums[j+1]$), then neither universal condition can hold.
2. If an array contains only non-decreasing steps and plateaus, the first condition holds.
3. If an array contains only non-increasing steps and plateaus, the second condition holds.
4. If an array consists entirely of identical elements, all steps are plateaus, and both conditions hold simultaneously.

---

## 6. Edge Cases & Traps

| Edge Condition | Instance | Behavior & Invariant Handling | Result |
|---|---|---|:---:|
| Single Element | $nums = [7]$ | $0$ adjacent pairs exist. Loop body executes zero times; both flags remain `true`. | `true` |
| Two Elements | $nums = [4, 9]$ | Exactly one pair $(4, 9)$. $\Delta = +5 > 0$. `is_decreasing` becomes `false`, `is_increasing` stays `true`. | `true` |
| All Identical | $nums = [5, 5, 5, 5]$ | Every step has $\Delta = 0$. Both tests pass at every step; both flags remain `true`. | `true` |
| Plateau at Peak | $nums = [1, 2, 2, 1]$ | Step 1: rises ($is\_desc \to false$). Step 2: plateau. Step 3: drops ($is\_asc \to false$). Both false. | `false` |

---

## 7. Complexity Derivation

- **Time Complexity:** $\mathcal{O}(n)$, where $n$ is the number of elements in $nums$. The algorithm examines each of the $n-1$ adjacent pairs exactly once. An optional early return halts as soon as both flags become `false`, achieving $\mathcal{O}(1)$ best-case time.
- **Auxiliary Space:** $\mathcal{O}(1)$. Only two boolean flags or difference sign trackers are maintained in memory during the traversal.
