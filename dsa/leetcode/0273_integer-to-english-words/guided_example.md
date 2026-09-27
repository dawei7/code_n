# Guided Example: Integer to English Words

We trace the step-by-step 3-digit triad chunking (Billions, Millions, Thousands, Units), irregular teen lookup table dispatch, and whitespace-normalized concatenation on representative integer instances:

- **Input:** $\text{num} = 123$
- **Required output:** `"One Hundred Twenty Three"`
- **Seven-Figure Multi-Triad Instance:** $\text{num} = 1234567 \implies \text{"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"}$
- **Zero Base Case:** $\text{num} = 0 \implies \text{"Zero"}$ (The only instance where "Zero" is pronounced)
- **Zero-Padded Internal Triad:** $\text{num} = 1000010 \implies \text{"One Million Ten"}$ (Empty thousands group is completely omitted; no "Zero Thousand")
- **Maximum 32-Bit Signed Integer:** $\text{num} = 2147483647 \implies \text{"Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven"}$

This instance demonstrates recursive base-1000 decomposition, explains why values under 20 require a dedicated irregular lookup table, formalizes the suppression of zero-valued triads, and operates in strictly $O(1)$ constant time (at most 4 triads for any 32-bit integer) and $O(1)$ space.

---

## 1. Instance & Teaching Goal

Given an integer $\text{num} = 123$, generate its canonical English words representation:
```text
Value: 123
Breakdown:
100 -> "One Hundred"
 20 -> "Twenty"
  3 -> "Three"
Combined: "One Hundred Twenty Three"
```

### The Base-1000 Triad Architecture
English numerals partition decimal numbers into groups of three digits (powers of $1,000$):
$$
\text{num} = b \times 10^9 + m \times 10^6 + t \times 10^3 + u
$$
where each coefficient $b, m, t, u \in [0, 999]$.
- $b$: Scaled by `"Billion"`
- $m$: Scaled by `"Million"`
- $t$: Scaled by `"Thousand"`
- $u$: Unscaled (Units)

Because the pronunciation of any 3-digit number $X \in [1, 999]$ follows the identical rules regardless of its scale, we delegate the conversion to a sub-function `convert_triad(X)` and attach the appropriate scale word.

---

## 2. Conceptual Foundation & Invariants

### 1. Lookup Dictionaries for Irregularities
English contains phonetic irregularities that cannot be derived by regular arithmetic rules:
- **Numbers under 20 (`UNDER_20`):**
  $0 \dots 19$: `["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]`.
- **Tens (`TENS`):**
  Multiples of 10 from $20 \dots 90$: `["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]`.

### 2. Triad Converter `convert_triad(n)` for $n \in [1, 999]$:
1. **Hundreds Digit:**
   If $n \ge 100$:
   Append `UNDER_20[n // 100] + " Hundred"`.
   $n \leftarrow n \pmod{100}$.
2. **Tens and Units Digits:**
   - If $n \ge 20$:
     Append `TENS[n // 10]`.
     If $n \pmod{10} > 0$: Append `UNDER_20[n % 10]`.
   - Else if $n > 0$:
     Append `UNDER_20[n]` (covers $1 \dots 19$).
3. Return list of words.

### 3. Triad Scaling Driver:
- If $\text{num} == 0$: Return `"Zero"`.
- Scales: $[(10^9, \text{"Billion"}), (10^6, \text{"Million"}), (10^3, \text{"Thousand"}), (1, \text{""})]$.
- For each $(\text{unit}, \text{label})$:
  If $\text{num} \ge \text{unit}$:
    $\text{chunk} = \text{num} // \text{unit}$
    $\text{words}.\text{extend}(\text{convert\_triad}(\text{chunk}))$
    If $\text{label} \ne \text{""}$: $\text{words}.\text{append}(\text{label})$
    $\text{num} \leftarrow \text{num} \pmod{\text{unit}}$
- Return `" ".join(words)`.

> **Invariant.** A scale word (`"Billion"`, `"Million"`, `"Thousand"`) is appended if and only if its corresponding 3-digit triad is strictly positive ($> 0$). Empty triads ($000$) are completely silent.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{num} = 1234567$:
$\text{num} = 1{,}234{,}567$.

---

### Step 1: Scale $10^9$ (Billions)
- $\text{unit} = 10^9 = 1{,}000{,}000{,}000$.
- $\text{num} < 10^9 \implies$ Triad is $0$. Skipped.

---

### Step 2: Scale $10^6$ (Millions)
- $\text{unit} = 10^6 = 1{,}000{,}000$.
- Chunk: $\text{chunk} = 1{,}234{,}567 // 1{,}000{,}000 = \mathbf{1}$.
- Remainder: $\text{num} \leftarrow 1{,}234{,}567 \pmod{1{,}000{,}000} = 234{,}567$.
- Convert chunk $1$:
  - $\text{convert\_triad}(1) \implies \text{["One"]}$.
- Append scale word: `"Million"`.
- Collected words: `["One", "Million"]`.

---

### Step 3: Scale $10^3$ (Thousands)
- $\text{unit} = 10^3 = 1{,}000$.
- Chunk: $\text{chunk} = 234{,}567 // 1{,}000 = \mathbf{234}$.
- Remainder: $\text{num} \leftarrow 234{,}567 \pmod{1{,}000} = 567$.
- Convert chunk $234$:
  - Hundreds: $234 // 100 = 2 \implies \text{"Two Hundred"}$.
  - Sub-remainder: $234 \pmod{100} = 34$.
  - Tens: $34 \ge 20 \implies \text{TENS}[3] = \text{"Thirty"}$.
  - Units: $34 \pmod{10} = 4 \implies \text{UNDER\_20}[4] = \text{"Four"}$.
  - Chunk words: `["Two", "Hundred", "Thirty", "Four"]`.
- Append scale word: `"Thousand"`.
- Collected words: `["One", "Million", "Two", "Hundred", "Thirty", "Four", "Thousand"]`.

---

### Step 4: Scale $1$ (Units)
- $\text{unit} = 1$.
- Chunk: $\text{chunk} = 567 // 1 = \mathbf{567}$.
- Remainder: $\text{num} \leftarrow 0$.
- Convert chunk $567$:
  - Hundreds: $567 // 100 = 5 \implies \text{"Five Hundred"}$.
  - Sub-remainder: $567 \pmod{100} = 67$.
  - Tens: $67 \ge 20 \implies \text{TENS}[6] = \text{"Sixty"}$.
  - Units: $67 \pmod{10} = 7 \implies \text{UNDER\_20}[7] = \text{"Seven"}$.
  - Chunk words: `["Five", "Hundred", "Sixty", "Seven"]`.
- Scale word: None.
- Collected words: `[..., "Five", "Hundred", "Sixty", "Seven"]`.

---

### Step 5: String Synthesis
Join all accumulated words with a single space:
$$
\mathbf{\text{"One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"}}
$$

---

## 4. Complete Execution Trace

```text
num = 1234567

Scale 1,000,000 (Million):
  chunk = 1234567 // 1000000 = 1 -> "One"
  scale = "Million" -> ["One", "Million"]
  rem = 234567

Scale 1,000 (Thousand):
  chunk = 234567 // 1000 = 234
    200 -> "Two Hundred"
     34 -> "Thirty Four"
  scale = "Thousand" -> ["Two", "Hundred", "Thirty", "Four", "Thousand"]
  rem = 567

Scale 1 (Units):
  chunk = 567 // 1 = 567
    500 -> "Five Hundred"
     67 -> "Sixty Seven"
  scale = "" -> ["Five", "Hundred", "Sixty", "Seven"]
  rem = 0

Combined Result: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
```

| Triad Level | Divisor ($\text{unit}$) | Triad Value | Triad English Pronunciation | Scale Word Appended | Cumulative Word Count |
|:---:|:---:|:---:|:---|:---:|:---:|
| Billions | $10^9$ | 0 | (Silent) | (None) | 0 |
| **Millions** | $10^6$ | 1 | `"One"` | `"Million"` | 2 |
| **Thousands** | $10^3$ | 234 | `"Two Hundred Thirty Four"` | `"Thousand"` | 7 |
| **Units** | 1 | 567 | `"Five Hundred Sixty Seven"` | (None) | 11 |
| **End** | - | - | - | - | **11 Words Joined** |

---

## 5. Algorithmic Correctness

**Soundness.** Every numeric value in $[0, 2^{31} - 1]$ has a unique representation in base 1000 with at most 4 digits. The conversion for numbers under 1000 accurately mirrors English grammar rules: irregular teens ($10 \dots 19$) take priority over composite tens-and-ones, and exact tens omit the trailing zero.

**Completeness.** Handling $\text{num} = 0$ as an upfront special case guarantees that zero returns `"Zero"` without creating spurious `"Zero Thousand"` outputs in composite numbers like $1{,}000{,}005$.

---

## 6. Traps This Instance Exposes

- **Spurious "Zero" in Composite Numbers:** In $1{,}000{,}005$, the thousands group is $0$. If zero is converted to `"Zero"`, it would print `"One Million Zero Thousand Five"`. Skipping groups with value $0$ ensures proper English silence.
- **Teens Handling ($10 \dots 19$):** Treating $15$ as $10 + 5$ would output `"Ten Five"`. English uses `"Fifteen"`. The `UNDER_20` table up to index 19 prevents decomposition of irregular numbers.
- **Extra Whitespace:** Concatenating with `+ " "` often introduces leading, trailing, or double internal spaces. Accumulating words into a Python list and executing `" ".join(words)` guarantees single space separation.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$ constant time. Any 32-bit signed integer is bounded by $2^{31} - 1 \approx 2.14 \times 10^9$, requiring at most 4 triad iterations. Each triad performs at most 3 table lookups and divisions.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space. The lookup tables contain fewer than 30 short strings, and the output word list contains at most 30 tokens.
