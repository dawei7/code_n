# Guided Example: Minimum Cost to Set Cooking Time

We analyze and execute the dual-representation minute-second decomposition algorithm on a representative microwave input instance, establishing how trade-offs between finger movements and digit counts determine the optimal typing sequence.

- **Input:** `startAt = 1`, `moveCost = 2`, `pushCost = 1`, `targetSeconds = 600`
- **Output:** `6`

This instance illustrates time partitioning into minutes and seconds, the single minute-to-second borrow trade-off, stripping leading zeros, and evaluating physical button cost.

---

## 1. Problem Overview & Representative Instance

A microwave takes an input of up to four pressed digits. The machine pads the typed sequence with leading zeros to four digits:
$$\text{Digits} = [d_1, d_2, d_3, d_4]$$
The first two digits represent minutes ($m = 10 d_1 + d_2$), and the last two represent seconds ($s = 10 d_3 + d_4$). The resulting cooking time in seconds is:
$$\text{Total Time} = m \cdot 60 + s$$

Unlike standard clock notation, the seconds field $s$ is allowed to exceed $59$, taking any value up to $99$.

Typing costs are governed by:
- **Move Cost (`moveCost`):** Paid whenever the finger moves from its current digit to a different digit.
- **Push Cost (`pushCost`):** Paid every time any button is pressed. Repeating the same button incurs no move cost.
- The finger begins positioned over digit `startAt`.
- The user does **not** need to press leading zeros.

We must find the minimum cost to input an entry yielding exactly `targetSeconds`.

In our representative instance:
- `startAt = 1`, `moveCost = 2`, `pushCost = 1`.
- `targetSeconds = 600`.

There are two distinct ways to express $600$ seconds under the microwave constraints:
1. $10$ minutes and $0$ seconds ($10 \times 60 + 0 = 600$).
2. $9$ minutes and $60$ seconds ($9 \times 60 + 60 = 600$).

We must compare the total mechanical typing cost of each valid representation.

---

## 2. Mathematical & Algorithmic Principles

### Dual Feasible Partition Space

Any integer $\text{targetSeconds} \in [1, 6039]$ can be represented in at most two valid pairs $(m, s)$ satisfying $0 \le m \le 99$ and $0 \le s \le 99$:
1. **Primary Representation (Standard Quotient):**
   $$m_1 = \left\lfloor \frac{\text{targetSeconds}}{60} \right\rfloor, \quad s_1 = \text{targetSeconds} \bmod 60$$
   This representation is valid if $m_1 \le 99$.
2. **Alternative Borrowed Representation (Minute Transfer):**
   $$m_2 = m_1 - 1, \quad s_2 = s_1 + 60$$
   This representation is valid if $m_2 \ge 0$ and $s_2 \le 99$.

Borrowing a second minute would yield $s \ge 120 > 99$, which is impossible. Hence, $|\mathcal{C}| \in \{1, 2\}$.

### Sequence Formatting & Leading Zero Suppression

For each valid pair $(m, s)$:
- The 4-digit code is:
  $$\text{code} = [\lfloor m / 10 \rfloor, \, m \bmod 10, \, \lfloor s / 10 \rfloor, \, s \bmod 10]$$
- Strip all leading zeros until the first non-zero digit is reached (e.g., $[0, 9, 6, 0] \to [9, 6, 0]$).
- Because $\text{targetSeconds} \ge 1$, the stripped sequence $D = [d_0, d_1, \dots, d_{L-1}]$ contains between $1$ and $4$ digits.

### Deterministic Cost Evaluation

For digit sequence $D$, initialize $\text{curr} = \text{startAt}$ and $\text{cost} = 0$:
- For each digit $d \in D$:
  - If $d \ne \text{curr}$:
    $$\text{cost} \leftarrow \text{cost} + \text{moveCost}, \quad \text{curr} \leftarrow d$$
  - Press the button:
    $$\text{cost} \leftarrow \text{cost} + \text{pushCost}$$

The optimal answer is the minimum cost among all valid representations:
$$\text{MinCost} = \min_{(m, s) \in \mathcal{C}} \text{EvaluateCost}(m, s)$$

| Candidate Option | Mathematical Split | 4-Digit Code | Stripped Keystrokes | Move / Press Trade-Off |
|---|---|---|---|---|
| Option 1 (Standard) | $10 \text{ min}, 0 \text{ sec}$ | `1000` | `['1', '0', '0', '0']` (4 presses) | $4$ presses, but benefits from repeated `'0'` presses |
| Option 2 (Borrowed) | $9 \text{ min}, 60 \text{ sec}$ | `0960` | `['9', '6', '0']` (3 presses) | $3$ presses, but requires $3$ separate finger movements |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We evaluate `startAt = 1, moveCost = 2, pushCost = 1, targetSeconds = 600`.

```
Target = 600 seconds. Start finger at 1.

Option 1: m = 10, s = 0   => code "1000" (4 digits)
Option 2: m = 9,  s = 60  => code "0960" -> "960" (3 digits)
```

### Step 1: Evaluate Option 1 (`"1000"`)
- Minute-second pair: $m = 10, s = 0$.
- Formatted string: `"1000"`. No leading zero.
- Keystrokes: `['1', '0', '0', '0']`.
- Trace from $\text{curr} = 1$:
  - **Digit 1 (`'1'`):**
    - Already at $1$ ($\text{curr} == 1$): $0$ move cost.
    - Press `'1'`: $+1$ push cost.
    - Cost so far: $1$. Finger at $1$.
  - **Digit 2 (`'0'`):**
    - Move from $1$ to $0$: $+2$ move cost.
    - Press `'0'`: $+1$ push cost.
    - Cost so far: $1 + 2 + 1 = 4$. Finger at $0$.
  - **Digit 3 (`'0'`):**
    - Already at $0$ ($\text{curr} == 0$): $0$ move cost.
    - Press `'0'`: $+1$ push cost.
    - Cost so far: $4 + 1 = 5$. Finger at $0$.
  - **Digit 4 (`'0'`):**
    - Already at $0$ ($\text{curr} == 0$): $0$ move cost.
    - Press `'0'`: $+1$ push cost.
    - Cost so far: $5 + 1 = 6$. Finger at $0$.
- Total cost for Option 1: **6**.

### Step 2: Evaluate Option 2 (`"960"`)
- Minute-second pair: $m = 9, s = 60$.
- Formatted 4 digits: `"0960"`.
- Strip leading zero: `"960"`.
- Keystrokes: `['9', '6', '0']`.
- Trace from $\text{curr} = 1$:
  - **Digit 1 (`'9'`):**
    - Move from $1$ to $9$: $+2$ move cost.
    - Press `'9'`: $+1$ push cost.
    - Cost so far: $3$. Finger at $9$.
  - **Digit 2 (`'6'`):**
    - Move from $9$ to $6$: $+2$ move cost.
    - Press `'6'`: $+1$ push cost.
    - Cost so far: $3 + 2 + 1 = 6$. Finger at $6$.
  - **Digit 3 (`'0'`):**
    - Move from $6$ to $0$: $+2$ move cost.
    - Press `'0'`: $+1$ push cost.
    - Cost so far: $6 + 2 + 1 = 9$. Finger at $0$.
- Total cost for Option 2: **9**.

### Step 3: Selection
- Option 1 cost: $6$.
- Option 2 cost: $9$.
- Optimal choice: $\min(6, 9) = 6$.

Even though Option 2 has one fewer digit ($3$ vs $4$), Option 1 avoids two costly finger movements because the finger starts on `'1'` and presses `'0'` three times in place.

---

## 4. Comprehensive State Trace

The table below catalogs every button press and finger transition for both options:

| Option | Digit Index | Target Digit | Previous Finger Location | Movement Required? | Move Cost | Push Cost | Step Cost | Running Cost |
|---|---|---|---|---|---|---|---|---|
| **Option 1 (`"1000"`)** | $0$ | `'1'` | $1$ (`startAt`) | No ($1 == 1$) | $0$ | $1$ | $1$ | $1$ |
| | $1$ | `'0'` | $1$ | Yes ($1 \to 0$) | $2$ | $1$ | $3$ | $4$ |
| | $2$ | `'0'` | $0$ | No ($0 == 0$) | $0$ | $1$ | $1$ | $5$ |
| | $3$ | `'0'` | $0$ | No ($0 == 0$) | $0$ | $1$ | $1$ | **6 (Optimum)** |
| **Option 2 (`"960"`)** | $0$ | `'9'` | $1$ (`startAt`) | Yes ($1 \to 9$) | $2$ | $1$ | $3$ | $3$ |
| | $1$ | `'6'` | $9$ | Yes ($9 \to 6$) | $2$ | $1$ | $3$ | $6$ |
| | $2$ | `'0'` | $6$ | Yes ($6 \to 0$) | $2$ | $1$ | $3$ | **9** |

Option 1 achieves the global minimum cost of $6$.

---

## 5. Algorithmic Correctness & Soundness

### Exhaustive Representation Bound
Any entry evaluates to:
$$\text{Seconds} = 60m + s \quad \text{with } 0 \le m \le 99 \text{ and } 0 \le s \le 99$$
By Euclidean division, there is a unique representation $60q + r$ with $0 \le r < 60$. Any other representation with integer $m$ must satisfy $m = q - k$ and $s = r + 60k$.
- If $k \ge 2$, $s \ge 120 > 99$ (Violates maximum two-digit second bound).
- If $k \le -1$, $s = r - 60 < 0$ (Violates non-negative second bound).
- Therefore, $k \in \{0, 1\}$ are the only possible integer solutions.
Testing both $k = 0$ and $k = 1$ when within $[0, 99]$ explores $100\%$ of feasible representations, ensuring completeness and optimality.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Target Less Than 60 Seconds:** E.g., `targetSeconds = 45`.
   - $m_1 = 0, s_1 = 45 \implies \text{"45"}$.
   - $m_2 = -1 < 0$ (Borrowing impossible).
   - Only one valid representation exists.
2. **Borrowed Seconds Exceed 99:** E.g., `targetSeconds = 100`.
   - $m_1 = 1, s_1 = 40 \implies \text{"140"}$.
   - $m_2 = 0, s_2 = 40 + 60 = 100 > 99$ (Invalid).
   - Only standard representation is valid.
3. **Move Cost is Zero:** If `moveCost = 0`, cost depends strictly on the number of button presses. The shorter representation always wins.
4. **Push Cost Dominates:** If `pushCost = 100000` and `moveCost = 1`, minimizing the number of digits is paramount.

### Common Anti-Patterns
- **Greedy Shorter Sequence Assumption:** Assuming fewer digits is always better fails whenever finger movements cost more than button presses, as seen in the representative instance.
- **Forgetting to Strip Leading Zeros:** Typing `"0076"` instead of `"76"` adds two redundant zero presses and potential movements.
- **Missing the Borrowed Minute Option:** Restricting seconds to $s < 60$ misses valid alternative microwave entries like `960` for $10$ minutes.

---

## 7. Complexity Analysis

### Time Complexity
- Generating candidate minute-second pairs requires $2$ division/modulo operations: $O(1)$.
- Formatting and stripping strings has length at most $4$: $O(1)$.
- Cost evaluation iterates through at most $4$ characters: $O(1)$.
- Total time complexity is strictly $O(1)$, executing in under $1$ microsecond.

### Auxiliary Space Complexity
- Stores strings of length at most $4$ characters.
- Total auxiliary space complexity is strictly $O(1)$.
