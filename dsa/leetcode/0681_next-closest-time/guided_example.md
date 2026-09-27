# Guided Example: Next Closest Time

We trace the step-by-step distinct digit alphabet extraction ($S = \{c \mid c \ne \text{':'}\}$), exhaustive 4-digit permutation generation ($|S|^4 \le 256$ candidates), 24-hour clock validity verification ($0 \le H < 24 \land 0 \le M < 60$), elapsed minute delta calculation ($p = 60H + M$), same-day forward chronometry filtering ($t < p$), and midnight wraparound fallback ($mi = \min(S) \implies mi\,mi:mi\,mi$) on representative digital clock strings:

- **Input:** $time = \text{"19:34"}$
- **Required output:** `"19:39"`
  - Clock rules:
    - Time format: `"HH:MM"` where $00 \le HH \le 23$ and $00 \le MM \le 59$.
    - Digit reuse rule: Any digit appearing in the original time may be reused an arbitrary number of times.
    - Objective: Find the next chronologically closest valid time that can be constructed using **only** the digits in the input.
    - If no valid time can be formed later today, the clock wraps past midnight into tomorrow.
- **Digit Alphabet & Chronological Distance Invariant:**
  - **The Digit Alphabet ($S$):**
    - For `"19:34"`, the available digits are:
      $$
      S = \{\text{'1'}, \; \text{'9'}, \; \text{'3'}, \; \text{'4'}\} \quad (|S| = 4)
      $$
    - Because each of the 4 clock positions can choose any digit from $S$, there are at most $4^4 = \mathbf{256}$ conceivable time strings.
  - **Clock Validity Predicate:**
    - A 4-digit string $c_1 c_2 c_3 c_4$ forms a valid time if and only if:
      $$
      \text{Hours } H = 10c_1 + c_2 \in [0, 23] \quad \land \quad \text{Minutes } M = 10c_3 + c_4 \in [0, 59]
      $$
  - **Chronological Distance Comparison:**
    - Convert current time to absolute elapsed minutes from midnight:
      $$
      t = 60 \times 19 + 34 = 1140 + 34 = \mathbf{1174}
      $$
    - For any valid candidate time $p = 60H + M$:
      - **Same-Day Candidates ($p > t$):**
        - Elapsed distance: $d = p - t$.
        - We seek to minimize $d$.
      - **Midnight Wrap Fallback:**
        - If no valid candidate satisfies $p > t$, the next time must occur after midnight on the following day.
        - To minimize the time elapsed into tomorrow, we greedily pick the **smallest available digit** $mi = \min(S)$ for all 4 positions:
          $$
          ans = \text{f"}\{mi\}\{mi\}:\{mi\}\{mi\}\text{"}
          $$
- **Step-by-Step Worked Execution Trace on $time = \text{"19:34"}$ ($t = 1174$):**
  - Digits available: $S = \{1, 3, 4, 9\}$.
  - Initial state: current minutes $t = 1174$, minimum forward distance $d = \infty, \; ans = \text{null}$.
  - **Candidate Generation and Pruning:**
    - Generate combinations $c_1 c_2 : c_3 c_4$:
    - **Testing hour 19 ($c_1 = 1, c_2 = 9$):**
      - Valid hour: $19 \in [0, 23]$.
      - Now vary minutes $c_3 c_4 \in \{1, 3, 4, 9\} \times \{1, 3, 4, 9\}$:
      - Candidate `"19:31"`: $M = 31 < 34 \implies p = 1171 < 1174$ (in the past, skip).
      - Candidate `"19:33"`: $M = 33 < 34 \implies p = 1173 < 1174$ (in the past, skip).
      - Candidate `"19:34"`: $M = 34 == 34 \implies p = 1174 == t$ (same time, skip).
      - Candidate `"19:39"`:
        - Valid minute: $39 < 60 \implies \mathbf{Valid\ Time!}$
        - Total minutes:
          $$
          p = 19 \times 60 + 39 = 1140 + 39 = \mathbf{1179}
          $$
        - Forward distance check:
          $$
          p = 1179 > t = 1174 \implies \mathbf{Later\ Today!}
          $$
          $$
          d = 1179 - 1174 = \mathbf{5\ minutes}
          $$
        - Record best candidate:
          $$
          ans \leftarrow \text{"19:39"}, \quad d \leftarrow 5
          $$
      - Candidate `"19:41"`: $p = 1181 \implies d = 7 > 5$.
      - Candidate `"19:43"`: $p = 1183 \implies d = 9 > 5$.
      - Candidate `"19:44"`: $p = 1184 \implies d = 10 > 5$.
      - Candidate `"19:49"`: $p = 1189 \implies d = 15 > 5$.
      - Candidate `"19:9x"`: $M = 91, 93, 94, 99 \ge 60 \implies$ Invalid minute, pruned!
    - **Testing other hours:**
      - Hours starting with $3, 4, 9$ (e.g. $3x, 4x, 9x$) are $\ge 24 \implies$ Invalid hours, pruned!
      - Hours like $11, 13, 14$ are $< 19 \implies$ Occurred earlier in the day.
  - **Step 4: Output:**
    - Smallest positive time delta found is $5$ minutes at `"19:39"`.
    - Return **`"19:39"`**.
- **Midnight Wraparound Trace ($time = \text{"23:59"}$):**
  - Digits available: $S = \{2, 3, 5, 9\}$. Current time: $t = 23 \times 60 + 59 = 1439$.
  - Any valid time on the same day must be strictly greater than $1439$.
  - But the maximum possible time on a clock is $23:59$ (1439 minutes).
  - No candidate satisfies $p > 1439$.
  - Therefore, $ans$ remains `null`.
  - **Trigger Wraparound Fallback:**
    - Smallest available digit:
      $$
      mi = \min(2, 3, 5, 9) = \mathbf{2}
      $$
    - The earliest time that can be displayed tomorrow is:
      $$
      \text{"22:22"}
      $$
    - Output is **`"22:22"`**.
- **All Identical Digits ($time = \text{"11:11"}$):**
  - Only one digit available: $S = \{1\}$.
  - The only constructible time is `"11:11"`, which wraps a full 24 hours back to itself $\implies$ returns **`"11:11"`**.

This instance demonstrates constrained combinatorial configuration search and modulo-1440 circular time projection, mathematically proves why uniform minimal digit replication uniquely minimizes post-midnight arrival times, and derives $O(1)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a time `"HH:MM"`:
Find the **next closest valid time** that can be constructed using only the digits from the input.
Digits can be reused any number of times.

```text
time = "19:34"
Digits: { 1, 9, 3, 4 }

Current: 19:34 (1174 minutes from midnight)

Next available time today:
  Keep 19:xx
  Try increasing minute 34:
  34 -> 39  (9 is in the digit set!)

19:39 is valid (39 < 60) and is 5 minutes away.
Result: "19:39"
```

### The Invariant of Circular Chronometry
- A valid time must satisfy $H \in [0, 23]$ and $M \in [0, 59]$.
- If a valid time exists with $p > t$, choose the one that minimizes $p - t$.
- If no valid time exists today ($p > t$), wrap to tomorrow: the earliest valid time is formed by repeating the smallest available digit: $mi\,mi:mi\,mi$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Minute Projection Metric:
$$
t = 60 \times \text{int}(time[:2]) + \text{int}(time[3:])
$$
$$
p = 60 \times \text{int}(curr[:2]) + \text{int}(curr[2:])
$$

### 2. The Decision Boundary:
For all valid 4-digit permutations of digits in $S$:
$$
\text{If } t < p < t + d \implies d \leftarrow p - t, \quad ans \leftarrow curr
$$
$$
\text{If } ans \text{ is null} \implies ans = f"{mi}{mi}:{mi}{mi}" \quad \text{where } mi = \min(S)
$$

> **Circular Metric Minimization Invariant.** The chronological distance on the 24-hour torus $\mathbb{Z}_{1440}$ partitions candidate configurations into a same-day interval $(t, 1440)$ and an overflow interval $[0, t]$, where the latter is uniquely minimized by the lexicographically smallest admissible digit tuple $(mi, mi, mi, mi)$.

---

## 3. Step-by-Step Worked Execution

We trace $time = \text{"19:34"}$:

---

### Step 1: Available Digits & Current Minute
- $S = \{1, 3, 4, 9\}$.
- $t = 19 \times 60 + 34 = 1174$.

---

### Step 2: Test Minutes for Hour 19
- $19:31 \implies 1171 < 1174$ (past).
- $19:34 \implies 1174 = 1174$ (same).
- $19:39 \implies 1179 > 1174$ (distance = $5$).

---

### Step 3: Best Delta
- $d = 5$ at `"19:39"`.
- All other valid same-day candidates (e.g. $19:41$) have larger deltas ($d \ge 7$).

---

### Step 4: Output
$$
\mathbf{\text{"19:39"}}
$$

---

## 4. Complete Execution Trace

| Candidate Generated | Valid 24h Clock? | Minutes from Midnight $p$ | Condition $p > 1174$? | Delta $p - t$ | Best Answer So Far |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `"19:31"` | Yes ($31 < 60$) | $1171$ | No (Past) | — | None |
| `"19:34"` | Yes | $1174$ | No (Identical) | — | None |
| **`"19:39"`** | **Yes ($39 < 60$)** | **$1179$** | **Yes** | **$\mathbf{5}$ minutes** | **`"19:39"`** |
| `"19:41"` | Yes | $1181$ | Yes | $7$ minutes | `"19:39"` (Kept) |
| `"19:91"` | No ($91 \ge 60$) | — | Invalid | — | `"19:39"` |
| **Final** | — | — | — | — | **`"19:39"`** |

---

## 5. Boundary Cases & Failure Modes

- **Latest Time in Day ($23:59$):** No time later today exists $\implies$ wraps to `"22:22"`.
- **Single Unique Digit ($11:11$):** Only one digit $\implies$ wraps 24 hours back to `"11:11"`.
- **Midnight ($00:00$):** Digit set $\{0\} \implies$ wraps to `"00:00"`.
- **Digit Exceeding Clock Limits ($S = \{7, 8, 9\}$):** Combinations like $77:77$ are invalid; only combinations with $H < 24$ and $M < 60$ survive validation.

---

## 6. Traps & Common Anti-Patterns

- **Incrementing Minute-by-Minute ($1440$ steps):** Simulating minute-by-minute with string conversions is unnecessary when only $\le 256$ candidate strings exist.
- **Forgetting the Colon Formatter:** Output must format as `"HH:MM"`.
- **Overlooking 24-Hour Limits:** The first two digits must form a number $< 24$ and the last two must form a number $< 60$. Candidates like `"29:11"` or `"19:94"` must be rejected.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Number of distinct digits is at most $4$.
  - Total 4-digit permutations: at most $4^4 = 256$.
  - Each candidate checks validity in $\mathcal{O}(1)$ time.
  - Total Time: strictly constant $\mathcal{O}(1)$ time. Completes in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - Maximum recursion depth is $4 \implies \mathcal{O}(1)$ auxiliary space.
