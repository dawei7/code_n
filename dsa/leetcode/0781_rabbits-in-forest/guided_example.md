# Guided Example: Rabbits in Forest

We trace the step-by-step color group size derivation ($group = x + 1$), answer frequency binning ($v = cnt[x]$), ceiling division group capacity packing ($\lceil v / (x + 1) \rceil$), monochromatic cohort allocation, and minimum total forest population summation on representative rabbit response sets:

- **Input:** $answers = [1, 1, 2]$
- **Required output:** `5`
  - Rabbit reporting mechanics:
    - Each rabbit reports how many **other rabbits** share its exact same coat color.
    - If a rabbit answers $x$, its color group has total size:
      $$
      group\_size = x + 1
      $$
      (The rabbit itself plus the $x$ other rabbits).
    - Multiple rabbits that answer $x$ can belong to the **same color group**, up to a maximum capacity of $x + 1$ rabbits.
    - If more than $x + 1$ rabbits answer $x$, they cannot all share the same color; they must belong to different color groups of size $x + 1$.
    - Objective: Find the **minimum possible number of rabbits** in the forest consistent with all answers.
    - For $answers = [1, 1, 2]$:
      - Two rabbits answer `1`:
        - Group size is $1 + 1 = 2$.
        - Both rabbits can be the two members of the same color group (e.g. both blue).
        - Forest has at least 2 blue rabbits.
      - One rabbit answers `2`:
        - Group size is $2 + 1 = 3$.
        - This rabbit is one member of a 3-rabbit color group (e.g. red).
        - The other 2 red rabbits were not questioned, but they must exist in the forest.
        - Forest has at least 3 red rabbits.
      - Total minimum rabbits: $2 + 3 = \mathbf{5}$.
- **Ceiling Division & Capacity Packing Invariant:**
  - **Group Size Formula:**
    - For an answer $x$, the unique cohort capacity is:
      $$
      C_x = x + 1
      $$
  - **Color Group Multiplicity:**
    - Let $v$ be the number of rabbits that answered $x$ ($v = cnt[x]$).
    - Each color group can accommodate at most $C_x$ respondents.
    - Therefore, the minimum number of distinct color groups required to cover all $v$ respondents is given by integer ceiling division:
      $$
      \text{groups}(x) = \left\lceil \frac{v}{x + 1} \right\rceil = \left\lfloor \frac{v + x}{x + 1} \right\rfloor
      $$
  - **Population Contribution:**
    - Each complete color group must contain exactly $x + 1$ rabbits (even if some did not answer):
      $$
      \text{population}(x) = \text{groups}(x) \times (x + 1) = \left\lceil \frac{v}{x + 1} \right\rceil \times (x + 1)
      $$
  - **Global Summation:**
    - Because rabbits answering different numbers $x \ne y$ cannot share the same color group (their claimed group sizes conflict), the total minimum population is simply:
      $$
      ans = \sum_{x \in \text{distinct answers}} \left\lceil \frac{cnt[x]}{x + 1} \right\rceil \times (x + 1)
      $$
- **Step-by-Step Worked Execution Trace on $answers = [1, 1, 2]$:**
  - **Phase 0: Count Answer Frequencies:**
    - $cnt = \{ 1: 2, \; 2: 1 \}$
  - **Phase 1: Process Answer $x = 1$ ($v = 2$):**
    - Group size:
      $$
      C_1 = x + 1 = 1 + 1 = \mathbf{2}
      $$
    - Number of distinct groups required for 2 respondents:
      $$
      \text{groups}(1) = \left\lceil \frac{2}{2} \right\rceil = \mathbf{1} \text{ group}
      $$
    - Total rabbits in this color:
      $$
      \text{population}(1) = 1 \times 2 = \mathbf{2}
      $$
  - **Phase 2: Process Answer $x = 2$ ($v = 1$):**
    - Group size:
      $$
      C_2 = x + 1 = 2 + 1 = \mathbf{3}
      $$
    - Number of distinct groups required for 1 respondent:
      $$
      \text{groups}(2) = \left\lceil \frac{1}{3} \right\rceil = \mathbf{1} \text{ group}
      $$
    - Total rabbits in this color:
      $$
      \text{population}(2) = 1 \times 3 = \mathbf{3}
      $$
  - **Phase 3: Aggregate Minimum Population:**
    $$
    ans = \text{population}(1) + \text{population}(2) = 2 + 3 = \mathbf{5}
    $$
- **Partial Group Overflow Trace ($answers = [10, 10, 10]$):**
  - Answer $x = 10$, respondents $v = 3$.
  - Group size is $10 + 1 = 11$.
  - Number of groups: $\lceil 3 / 11 \rceil = 1$.
  - Total rabbits: $1 \times 11 = \mathbf{11}$.
- **Multiple Groups for Same Answer Trace ($answers = [1, 1, 1]$):**
  - Answer $x = 1$, respondents $v = 3$. Group size is 2.
  - 3 rabbits cannot fit into a single group of size 2!
  - Groups needed: $\lceil 3 / 2 \rceil = 2$ groups.
  - Total rabbits: $2 \times 2 = \mathbf{4}$.
- **Zero Answers Trace ($answers = [0, 0, 0]$):**
  - Each rabbit says "0 other rabbits share my color" $\implies$ unique colors!
  - Group size: $0 + 1 = 1$.
  - 3 groups of size 1 $\implies \mathbf{3}$ rabbits.

This instance demonstrates equivalence class partitioning and greedy bin-packing with fixed capacities, mathematically proves why ceiling division over uniform cohort sizes minimizes total fiber cardinality, and derives $O(N)$ execution time and $O(U)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an array $answers$ where each rabbit reports how many *other* rabbits have its color:
Find the **minimum number of rabbits** in the forest.

```text
answers = [ 1, 1, 2 ]

- Two rabbits say "1 other rabbit has my color":
    Group size = 1 + 1 = 2 rabbits.
    Both rabbits fit in 1 group of 2 -> 2 rabbits.

- One rabbit says "2 other rabbits have my color":
    Group size = 2 + 1 = 3 rabbits.
    Fits in 1 group of 3 -> 3 rabbits.

Total = 2 + 3 = 5 rabbits.
Result: 5
```

### The Invariant of Ceiling Bin-Packing
- A rabbit answering $x$ belongs to a color group of size $x + 1$.
- If $v$ rabbits answer $x$, they require $\lceil v / (x + 1) \rceil$ separate color groups.
- Each group contains $x + 1$ rabbits, contributing $\lceil v / (x + 1) \rceil \times (x + 1)$ to the total.

---

## 2. Conceptual Foundation & Invariants

### 1. Cohort Size & Ceiling Formula:
$$
group\_size = x + 1
$$
$$
num\_groups = \left\lceil \frac{v}{x + 1} \right\rceil = \frac{v + x}{x + 1}
$$

### 2. Total Population Accumulation:
$$
ans = \sum_{x} \left( \left\lfloor \frac{v + x}{x + 1} \right\rfloor \times (x + 1) \right)
$$

> **Equivalence Relation Quotient Invariant.** The color partition on the forest population forms an equivalence relation where each equivalence class $[r]$ containing respondents answering $x$ has cardinality $x + 1$. Minimizing total cardinality corresponds to maximizing class occupancy under the capacity constraint $|[r]| = x + 1$.

---

## 3. Step-by-Step Worked Execution

We trace $answers = [1, 1, 2]$:

---

### Step 1: Count
- `'1'` appears 2 times ($v = 2$).
- `'2'` appears 1 time ($v = 1$).

---

### Step 2: Answer 1
- Group size: $1 + 1 = 2$.
- Groups: $\lceil 2 / 2 \rceil = 1$.
- Rabbits: $1 \times 2 = 2$.

---

### Step 3: Answer 2
- Group size: $2 + 1 = 3$.
- Groups: $\lceil 1 / 3 \rceil = 1$.
- Rabbits: $1 \times 3 = 3$.

---

### Step 4: Output
- $2 + 3 = \mathbf{5}$.

---

## 4. Complete Execution Trace

| Answer $x$ | Frequency $v$ | Group Capacity $x + 1$ | Color Groups Needed $\lceil v / (x+1) \rceil$ | Rabbits in Color |
|:---:|:---:|:---:|:---:|:---:|
| $1$ | $2$ | $2$ | $1$ | $2$ |
| $2$ | $1$ | $3$ | $1$ | $3$ |
| **Total** | — | — | — | **`5`** |

---

## 5. Boundary Cases & Failure Modes

- **All Answer 0 ($[0, 0, 0]$):** Each rabbit has a unique color $\implies$ returns $N$.
- **More Respondents Than Capacity ($[1, 1, 1]$):** 3 rabbits answering 1 need $\lceil 3 / 2 \rceil = 2$ groups of size 2 $\implies 4$ rabbits.
- **Single Rabbit ($[5]$):** Group of size 6 $\implies 6$ rabbits.
- **Empty Array:** Returns 0.

---

## 6. Traps & Common Anti-Patterns

- **Assuming All Rabbits Answering Same Number Belong to Same Group:** If 5 rabbits answer 1, they cannot all be the same color because a color group for answer 1 has size exactly 2. They require $\lceil 5 / 2 \rceil = 3$ groups of size 2 (6 rabbits).
- **Floating Point Division Inaccuracies:** Avoid floating point ceiling `math.ceil(v / group) * group`; integer division `(v + group - 1) // group * group` is exact, fast, and immune to precision error.
- **Counting Only Questioned Rabbits:** A rabbit answering 10 implies 10 other rabbits exist of that color, even if none of the other 10 were interviewed.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Counting frequencies with `Counter`: $\mathcal{O}(N)$.
  - Iterating through unique answers $U \le N$: $\mathcal{O}(U)$.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 1000$. Completes in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(U) \le 1000$ space for the frequency counter dictionary.
