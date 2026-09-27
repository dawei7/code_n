# Guided Example: Student Attendance Record I

We trace the step-by-step total absence frequency evaluation ($count(\text{'A'}) < 2$), consecutive late streak substring detection ($\text{'LLL'} \notin s$), conjunctive award eligibility criteria validation, and linear single-pass verification on representative attendance strings:

- **Input:** $s = \text{"PPALLP"}$
- **Required output:** `true`
  - Character alphabet:
    - `'A'`: Absent
    - `'L'`: Late
    - `'P'`: Present
  - Attendance award dual eligibility rules:
    1. **Absence Rule:** Total absences throughout the record must be **strictly fewer than 2** ($count(\text{'A'}) \le 1$).
    2. **Late Streak Rule:** The student was **never late for 3 or more consecutive days** (substring `"LLL"` must not appear).
- **Rule-by-rule evaluation trace on `"PPALLP"`:**
  - **Rule 1: Count Absences (`'A'`):**
    - Day 0: `'P'`
    - Day 1: `'P'`
    - Day 2: `'A'` $\implies$ Absence count $= 1$
    - Day 3: `'L'`
    - Day 4: `'L'`
    - Day 5: `'P'`
    - Total absences:
      $$
      cnt_A = \mathbf{1}
      $$
    - Check condition: $cnt_A < 2 \iff 1 < 2 \implies \mathbf{True}$ (Eligible under Rule 1!).
  - **Rule 2: Consecutive Late Streak (`'L'`):**
    - Track consecutive run of `'L'` characters:
      - Days 0–1: `'P'`, `'P'` $\to$ streak $= 0$
      - Day 2: `'A'` $\to$ streak $= 0$
      - Day 3: `'L'` $\to$ streak $= 1$
      - Day 4: `'L'` $\to$ streak $= 2$
      - Day 5: `'P'` $\to$ streak resets to $0$
    - Maximum consecutive late days: $\mathbf{2}$.
    - Substring test:
      $$
      \text{"LLL"} \notin \text{"PPALLP"} \implies \mathbf{True}
      $$
    - Eligible under Rule 2!
  - **Conjunctive Eligibility:**
    $$
    \text{Eligible} = \text{Rule 1} \land \text{Rule 2} = \text{True} \land \text{True} = \mathbf{true}
    $$
- **Late Streak Disqualification Instance ($s = \text{"PPALLL"}$):**
  - Days 3, 4, 5 contain `"LLL"` (3 consecutive late days).
  - Rule 2 fails $\implies \mathbf{false}$.
- **Absence Disqualification Instance ($s = \text{"AA"}$):**
  - $cnt_A = 2 \nless 2 \implies$ Rule 1 fails $\implies \mathbf{false}$.
- **Scattered Absences Disqualification ($s = \text{"APALP"}$):**
  - Two absences on Day 0 and Day 2 $\implies cnt_A = 2 \nless 2 \implies \mathbf{false}$.

This instance demonstrates dual-constraint invariant checking across global frequency and local contiguous subsegment windows, mathematically proves why predicate conjunction completely determines award eligibility, and derives $O(N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an attendance string $s$ consisting of `'P'`, `'A'`, and `'L'`:
A student qualifies for an award **if and only if**:
1. The student has strictly fewer than 2 absences (`'A'`).
2. The student does not have 3 or more consecutive late days (`"LLL"`).
Return `true` if eligible, and `false` otherwise.

```text
Evaluating "PPALLP":
  Absence count: 1 ('A' at index 2) -> 1 < 2 (Passes Rule 1)
  Consecutive 'L's:
    Indices 3..4: "LL" (streak of 2) -> No "LLL" (Passes Rule 2)

Result: true
```

### Decoupled Dual Invariants
- The two conditions are independent:
  - **Global Accumulation:** Total count of `'A'` anywhere in the string.
  - **Local Window:** Presence of a contiguous run of 3 `'L'`s (`"LLL"`).
- We can verify both in a single linear pass or via two standard string operations:
  $$
  count(\text{'A'}) < 2 \quad \land \quad \text{"LLL"} \notin s
  $$

---

## 2. Conceptual Foundation & Invariants

### 1. The Global Absence Condition:
Let $cnt_A = \sum_{c \in s} \mathbf{1}[c == \text{'A'}]$:
$$
\text{Condition 1: } cnt_A \le 1
$$

### 2. The Local Streak Condition:
$$
\text{Condition 2: } \forall i \in [0, n - 3], \quad s[i \dots i+2] \ne \text{"LLL"}
$$

### 3. Boolean Conjunction:
$$
\text{Award} = (cnt_A < 2) \land (\text{"LLL"} \notin s)
$$

> **Conjunctive Filtering Invariant.** Failing either the global count threshold or the local sliding window test immediately disqualifies the student.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"PPALLP"}$ ($n = 6$):

---

### Step 1: Count Absences
- Index 0: `'P'`
- Index 1: `'P'`
- Index 2: `'A'` ($cnt_A = 1$)
- Index 3: `'L'`
- Index 4: `'L'`
- Index 5: `'P'`
Total absences: $cnt_A = 1 < 2 \implies \mathbf{True}$.

---

### Step 2: Check Consecutive Late Days
- Sliding window of length 3:
  - $s[0 \dots 2] = \text{"PPA"} \ne \text{"LLL"}$
  - $s[1 \dots 3] = \text{"PAL"} \ne \text{"LLL"}$
  - $s[2 \dots 4] = \text{"ALL"} \ne \text{"LLL"}$
  - $s[3 \dots 5] = \text{"LLP"} \ne \text{"LLL"}$
Substring `"LLL"` is not found $\implies \mathbf{True}$.

---

### Step 3: Conjunction
$$
\mathbf{True} \land \mathbf{True} = \mathbf{true}
$$

---

## 4. Complete Execution Trace

| Record $s$ | Absence Count $cnt_A$ | $cnt_A < 2$? | Contains `"LLL"`? | Eligible for Award? |
|:---:|:---:|:---:|:---:|:---:|
| **`"PPALLP"`** | $1$ | **True** | No (**True**) | **`true`** |
| `"PPALLL"` | $1$ | **True** | **Yes** (False) | **`false`** |
| `"AA"` | $2$ | **False** | No (True) | **`false`** |
| `"APALP"` | $2$ | **False** | No (True) | **`false`** |
| `"LALL"` | $1$ | **True** | No (**True**) | **`true`** |

---

## 5. Boundary Cases & Failure Modes

- **Three Consecutive L's at Start (`"LLLPP"`):** Fails Rule 2 immediately $\implies \mathbf{false}$.
- **Three Consecutive L's at End (`"PPLLLL"`):** Fails Rule 2 immediately $\implies \mathbf{false}$.
- **Two L's Repeated Separately (`"LLPLL"`):** Neither streak reaches 3 $\implies \mathbf{true}$.
- **Record Length $< 3$:** `"LLL"` can never appear; qualification depends solely on $cnt_A < 2$.

---

## 6. Traps & Common Anti-Patterns

- **Resetting Absence Counter on Other Letters:** Absences are **cumulative**, not consecutive. Counting consecutive absences instead of total absences allows `"APAPA"` to pass erroneously.
- **Requiring Late Days to be Dispersed:** A student can have two consecutive late days (`"LL"`) and still receive the award. Only streaks of **3 or more** (`"LLL"`) disqualify.
- **Complex Regex State Machines:** Using complex regular expressions is overkill; a simple count and substring search runs faster and with zero regex parsing overhead.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Counting occurrences of `'A'` takes a single linear pass: $O(N)$.
  - Substring search for `"LLL"` takes linear time: $O(N)$.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^5$, completes in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space.
