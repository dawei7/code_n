# Guided Example: Jewels and Stones

We trace the step-by-step distinct jewel type set ingestion ($s = set(jewels)$), case-sensitive ASCII character comparison ($'a' \ne 'A'$), linear stone inventory stream traversal ($c \in stones$), constant-time indicator membership evaluation ($c \in s \implies 1$), and inventory jewel tally accumulation on representative stone collections:

- **Input:**
  - Jewel types: $jewels = \text{"aA"}$
  - Stone collection: $stones = \text{"aAAbbbb"}$
- **Required output:** `3`
  - Counting criteria & case sensitivity:
    - String $jewels$ contains all distinct character types considered jewels.
    - String $stones$ represents your collection of stones.
    - Each character represents a single stone.
    - Matching is **strictly case-sensitive**: `'a'` is completely distinct from `'A'`.
    - Objective: Count the total number of stones in $stones$ that are also in $jewels$.
    - For $jewels = \text{"aA"}$ and $stones = \text{"aAAbbbb"}$:
      - Stone 0: `'a'` $\to$ in $jewels$ (Jewel #1).
      - Stone 1: `'A'` $\to$ in $jewels$ (Jewel #2).
      - Stone 2: `'A'` $\to$ in $jewels$ (Jewel #3).
      - Stones 3, 4, 5, 6: `'b'` $\to$ not in $jewels$.
      - Total jewels owned: $1 + 1 + 1 + 0 + 0 + 0 + 0 = \mathbf{3}$.
- **Hash Set Ingestion & Indicator Summation Invariant:**
  - **The Jewel Universe ($\mathcal{J}$):**
    - Insert all characters of $jewels$ into a hash set:
      $$
      \mathcal{J} = \{ c \mid c \in jewels \}
      $$
    - Testing membership $c \in \mathcal{J}$ takes strictly $\mathcal{O}(1)$ average time.
  - **Inventory Streaming Aggregation:**
    - Stream each stone $c \in stones$:
      $$
      ans = \sum_{c \in stones} \mathbf{1}_{[c \in \mathcal{J}]}
      $$
    - Every stone is classified independently in constant time without sorting or nested rescanning.
- **Step-by-Step Worked Execution Trace on $stones = \text{"aAAbbbb"}$:**
  - **Phase 0: Build Set from $jewels = \text{"aA"}$:**
    - Insert `'a'`: $\mathcal{J} = \{\text{'a'}\}$.
    - Insert `'A'`: $\mathcal{J} = \{\text{'a'}, \; \text{'A'}\}$.
  - **Phase 1: Stream Stones ($stones = \text{"aAAbbbb"}$):**
    - Initialize counter: $ans = 0$.
    - **Position 0 ($c = \text{'a'}$):**
      - Membership: $\text{'a'} \in \mathcal{J} \implies \mathbf{True.}$
      - Increment: $ans \leftarrow 0 + 1 = \mathbf{1}$.
    - **Position 1 ($c = \text{'A'}$):**
      - Membership: $\text{'A'} \in \mathcal{J} \implies \mathbf{True.}$
      - Increment: $ans \leftarrow 1 + 1 = \mathbf{2}$.
    - **Position 2 ($c = \text{'A'}$):**
      - Membership: $\text{'A'} \in \mathcal{J} \implies \mathbf{True.}$
      - Increment: $ans \leftarrow 2 + 1 = \mathbf{3}$.
    - **Position 3 ($c = \text{'b'}$):**
      - Membership: $\text{'b'} \notin \mathcal{J} \implies \mathbf{False.}$
      - Counter unchanged: $ans = 3$.
    - **Position 4 ($c = \text{'b'}$):**
      - Membership: $\text{'b'} \notin \mathcal{J} \implies \mathbf{False.}$
      - Counter unchanged: $ans = 3$.
    - **Position 5 ($c = \text{'b'}$):**
      - Membership: $\text{'b'} \notin \mathcal{J} \implies \mathbf{False.}$
      - Counter unchanged: $ans = 3$.
    - **Position 6 ($c = \text{'b'}$):**
      - Membership: $\text{'b'} \notin \mathcal{J} \implies \mathbf{False.}$
      - Counter unchanged: $ans = 3$.
  - **Phase 2: Final Output:**
    $$
    ans = \mathbf{3}
    $$
- **Case-Sensitive Disjoint Trace ($jewels = \text{"z"}, stones = \text{"ZZ"}$):**
  - $\mathcal{J} = \{\text{'z'}\}$.
  - Stone 0: `'Z'` $\notin \mathcal{J}$ (ASCII 90 $\ne$ ASCII 122).
  - Stone 1: `'Z'` $\notin \mathcal{J}$.
  - Returns **`0`**.
- **All Stones Are Jewels Trace ($jewels = \text{"abc"}, stones = \text{"cba"}$):**
  - All 3 characters match $\implies ans = \mathbf{3}$.

This instance demonstrates linear filtering and hash set indicator aggregation, mathematically proves why characteristic set projection partitions multiset stone occurrences in constant time per element, and derives $O(|J| + |S|)$ runtime and $O(|J|)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a string $jewels$ and a string $stones$:
Count how many characters in $stones$ appear in $jewels$ (case-sensitive).

```text
jewels = "aA", stones = "aAAbbbb"

Jewels set: { 'a', 'A' }

Scan stones:
  'a' in set -> YES (count = 1)
  'A' in set -> YES (count = 2)
  'A' in set -> YES (count = 3)
  'b' in set -> NO
  'b' in set -> NO
  'b' in set -> NO
  'b' in set -> NO

Result: 3
```

### The Invariant of the Hash Set Lookup
- Pre-populating a hash set with $jewels$ allows checking if each stone is a jewel in strictly $O(1)$ time.
- Preserving case distinction is mandatory ('a' $\ne$ 'A').

---

## 2. Conceptual Foundation & Invariants

### 1. Set Construction:
$$
\mathcal{J} = \{ c \mid c \in jewels \}
$$

### 2. Stream Summation:
$$
ans = \sum_{c \in stones} [c \in \mathcal{J}]
$$

> **Characteristic Function Pullback.** Let $\chi_{\mathcal{J}}: \Sigma \to \{0, 1\}$ be the indicator function of the jewel subset. The total jewel count is the discrete integral $\int_{stones} \chi_{\mathcal{J}} \, d\mu_{stones}$ evaluated linearly in $O(|stones|)$.

---

## 3. Step-by-Step Worked Execution

We trace $jewels = \text{"aA"}, stones = \text{"aAAbbbb"}$:

---

### Step 1: Set Ingestion
- $\mathcal{J} = \{\text{'a'}, \text{'A'}\}$.

---

### Step 2: Stream Stones
- `'a'` $\in \mathcal{J} \implies$ +1
- `'A'` $\in \mathcal{J} \implies$ +1
- `'A'` $\in \mathcal{J} \implies$ +1
- `'b'`, `'b'`, `'b'`, `'b'` $\notin \mathcal{J} \implies$ +0

---

### Step 3: Output
$$
ans = \mathbf{3}
$$

---

## 4. Complete Execution Trace

| Stone Index $i$ | Character $c$ | In Jewel Set $\mathcal{J}$? | Indicator Value | Cumulative Count $ans$ |
|:---:|:---:|:---:|:---:|:---:|
| $0$ | `'a'` | Yes | $1$ | $1$ |
| $1$ | `'A'` | Yes | $1$ | $2$ |
| $2$ | `'A'` | Yes | $1$ | $3$ |
| $3$ | `'b'` | No | $0$ | $3$ |
| $4$ | `'b'` | No | $0$ | $3$ |
| $5$ | `'b'` | No | $0$ | $3$ |
| **$6$** | **`'b'`** | **No** | **$0$** | **`3`** |

---

## 5. Boundary Cases & Failure Modes

- **Case Mismatch ($"z"$ vs $"ZZ"$):** Lowercase and uppercase characters have distinct ASCII values $\implies$ returns 0.
- **Empty Stones ($""$):** Loop does not execute $\implies$ returns 0.
- **All Stones Match ($"abc"$ vs $"cba"$):** Returns $|stones|$.
- **Single Stone Match:** Returns 1.

---

## 6. Traps & Common Anti-Patterns

- **Searching in $jewels$ String Repeatedly ($O(|J| \cdot |S|)$):** Checking `c in jewels` where `jewels` is a string performs a linear substring scan each time. Converting `jewels` to a hash `set(jewels)` reduces lookup to $O(1)$.
- **Ignoring Case Sensitivity:** Normalizing to lowercase with `.lower()` combines `'a'` and `'A'`, corrupting the result.
- **Modifying the Input String:** Read-only pass over $stones$ is optimal and avoids object allocation.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Creating the jewel set: $\mathcal{O}(|jewels|)$.
  - Scanning all characters in $stones$: $\mathcal{O}(|stones|)$.
  - Total Time: strictly linear $\mathcal{O}(|jewels| + |stones|)$ where lengths $\le 50$. Completes in $< 0.01$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(|jewels|) \le 52$ memory for the hash set.
