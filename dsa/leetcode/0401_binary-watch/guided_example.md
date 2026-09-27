# Guided Example: Binary Watch

We trace the step-by-step exhaustive domain filtering ($12 \times 60 = 720$ state grid), binary population count evaluation ($\text{popcount}(h) + \text{popcount}(m) == turnedOn$), clock formatting rules (`'{:d}:{:02d}'`), and pruning on representative LED counts:

- **Input:** $turnedOn = 1$
- **Required output:** `["0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"]`
  - Total valid times checked: $12 \text{ hours } \times 60 \text{ minutes } = 720$ combinations
  - Filtering for $\text{popcount}(h) + \text{popcount}(m) == 1$:
    - Case A ($h = 0$, $\text{popcount}(h) = 0$):
      - Minutes with 1 bit on: $m \in \{1, 2, 4, 8, 16, 32\}$
      - Formatted times: `"0:01", "0:02", "0:04", "0:08", "0:16", "0:32"`
    - Case B ($m = 0$, $\text{popcount}(m) = 0$):
      - Hours with 1 bit on: $h \in \{1, 2, 4, 8\}$ (since $8 < 12$)
      - Formatted times: `"1:00", "2:00", "4:00", "8:00"`
    - Case C ($h > 0$ and $m > 0$):
      - Sum of bits is at least $1 + 1 = 2 > 1$ (None qualify)
  - Exactly 10 valid times match
- **Zero LEDs Lit:** $turnedOn = 0 \implies ["0:00"]$ (Only $h = 0, m = 0$)
- **Impossible High LED Count:** $turnedOn = 9 \implies []$
  - Max bits for hour: $11 = 1011_2 \implies 3$ bits
  - Max bits for minute: $59 = 111011_2 \implies 5$ bits
  - Max possible lit LEDs $= 3 + 5 = 8 < 9$

This instance demonstrates exploiting small, strictly bounded problem spaces ($720$ fixed states), mathematically proves why checking all valid clock readings in $O(1)$ time is simpler and safer than complex backtracking, and analyzes $O(1)$ time and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

A binary watch has 4 LEDs on the top for hours ($0 \dots 11$) and 6 LEDs on the bottom for minutes ($0 \dots 59$):
Given an integer $turnedOn = 1$, return all possible times the watch could represent:

```text
Hour LEDs:   [ 8, 4, 2, 1 ]       (Values 0 to 11)
Minute LEDs: [ 32, 16, 8, 4, 2, 1 ] (Values 0 to 59)

Target: turnedOn = 1 lit LED in total

Either 1 hour LED is ON and 0 minute LEDs are ON:
  Hour in {1, 2, 4, 8}, Minute = 0 -> "1:00", "2:00", "4:00", "8:00"

Or 0 hour LEDs are ON and 1 minute LED is ON:
  Hour = 0, Minute in {1, 2, 4, 8, 16, 32} -> "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"

Total Valid Times: 10
```

---

## 2. Conceptual Foundation & Invariants

### 1. The Bounded Domain Principle:
A physical digital clock can display only:
$$
h \in [0, 11], \quad m \in [0, 59]
$$
There are exactly $12 \times 60 = \mathbf{720}$ total valid time combinations in existence.
Rather than generating subsets of 10 LEDs and filtering invalid hour/minute values, iterating directly over all 720 legal times is trivial, bug-free, and runs in constant time!

### 2. Selection Condition:
For any time pair $(h, m)$:
- The number of lit LEDs is the sum of bits set to 1:
  $$
  \text{lit}(h, m) = \text{popcount}(h) + \text{popcount}(m)
  $$
- The time is valid if and only if $\text{lit}(h, m) == turnedOn$.

### 3. Formatting Rule:
- Hour: no leading zero (e.g. `"1"`, `"11"`).
- Minute: exactly 2 digits, zero-padded (e.g. `"01"`, `"00"`, `"59"`).
- Pattern: `'{:d}:{:02d}'.format(h, m)`.

> **Invariant.** Iterating $h \in [0, 11]$ and $m \in [0, 59]$ checks every legal time display exactly once, guaranteeing no duplicates and zero out-of-range times.

---

## 3. Step-by-Step Worked Execution

We trace $turnedOn = 1$ across the 720 time pairs:

---

### Step 1: Scan Hour $h = 0$ ($0_2$, popcount $= 0$)
- Required minute popcount: $1 - 0 = 1$.
- Scan $m \in [0, 59]$ with popcount 1 (powers of 2):
  - $m = 1 = 2^0 \implies \text{"0:01"}$
  - $m = 2 = 2^1 \implies \text{"0:02"}$
  - $m = 4 = 2^2 \implies \text{"0:04"}$
  - $m = 8 = 2^3 \implies \text{"0:08"}$
  - $m = 16 = 2^4 \implies \text{"0:16"}$
  - $m = 32 = 2^5 \implies \text{"0:32"}$
- Subtotal collected: 6 times.

---

### Step 2: Scan Hour $h = 1$ ($0001_2$, popcount $= 1$)
- Required minute popcount: $1 - 1 = 0$.
- Minute with popcount 0: only $m = 0$.
- Collected: `'{:d}:{:02d}'.format(1, 0) \implies \mathbf{\text{"1:00"}}`.

---

### Step 3: Scan Hour $h = 2$ ($0010_2$, popcount $= 1$)
- Required minute popcount: 0.
- Collected: `'{:d}:{:02d}'.format(2, 0) \implies \mathbf{\text{"2:00"}}`.

---

### Step 4: Scan Hour $h = 3$ ($0011_2$, popcount $= 2$)
- Popcount $2 > turnedOn = 1$.
- No valid minutes possible ($2 + \text{popcount}(m) \ge 2$). Skip entirely.

---

### Step 5: Scan Hour $h = 4$ ($0100_2$, popcount $= 1$)
- Required minute popcount: 0.
- Collected: $\mathbf{\text{"4:00"}}$.

---

### Step 6: Scan Hour $h = 5, 6, 7$
- $h = 5 (0101_2, 2 \text{ bits}), 6 (0110_2, 2 \text{ bits}), 7 (0111_2, 3 \text{ bits}) > 1$.
- All skipped.

---

### Step 7: Scan Hour $h = 8$ ($1000_2$, popcount $= 1$)
- Required minute popcount: 0.
- Collected: $\mathbf{\text{"8:00"}}$.

---

### Step 8: Scan Hour $h = 9, 10, 11$
- All have popcount $\ge 2$. All skipped.

---

### Step 9: Final Assembly
All 720 pairs inspected. Aggregate collection:
$$
[\text{"0:01"}, \; \text{"0:02"}, \; \text{"0:04"}, \; \text{"0:08"}, \; \text{"0:16"}, \; \text{"0:32"}, \; \text{"1:00"}, \; \text{"2:00"}, \; \text{"4:00"}, \; \text{"8:00"}]
$$

---

## 4. Complete Execution Trace

```text
turnedOn = 1
Searching all 720 pairs (h in 0..11, m in 0..59):

h = 0 (0 bits):
  m in {1, 2, 4, 8, 16, 32} -> "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"
h = 1 (1 bit):
  m = 0 (0 bits) -> "1:00"
h = 2 (1 bit):
  m = 0 (0 bits) -> "2:00"
h = 4 (1 bit):
  m = 0 (0 bits) -> "4:00"
h = 8 (1 bit):
  m = 0 (0 bits) -> "8:00"

All other h, m pairs have total bits != 1.
Total Results: 10 times.
```

| Hour $h$ | Binary $h$ | Popcount $h$ | Matching Minutes $m$ | Minute Binary | Popcount $m$ | Total Bits | Formatted Time Output |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | $0000_2$ | 0 | $1, 2, 4, 8, 16, 32$ | Powers of 2 | 1 | 1 | `"0:01", "0:02", ..., "0:32"` |
| 1 | $0001_2$ | 1 | 0 | $000000_2$ | 0 | 1 | `"1:00"` |
| 2 | $0010_2$ | 1 | 0 | $000000_2$ | 0 | 1 | `"2:00"` |
| 4 | $0100_2$ | 1 | 0 | $000000_2$ | 0 | 1 | `"4:00"` |
| 8 | $1000_2$ | 1 | 0 | $000000_2$ | 0 | 1 | `"8:00"` |
| Others | - | $\ge 2$ | None | - | $\ge 0$ | $\ge 2$ | Skipped |

---

## 5. Algorithmic Correctness

**Soundness.** The loop boundaries $h \in [0, 11]$ and $m \in [0, 59]$ ensure that every generated time is valid according to a 12-hour clock format. Formatting with `{:02d}` for minutes guarantees proper zero-padding (e.g. `"0:03"` instead of `"0:3"`).

**Completeness.** Since every possible hour and minute is enumerated, no valid time can be missed. For any $turnedOn > 8$, the loop finishes with an empty list, which is correct because the maximum possible sum of bits is $\text{popcount}(11) + \text{popcount}(59) = 3 + 5 = 8$.

---

## 6. Traps This Instance Exposes

- **Formatting Flaws:** Formatting minutes as single digits (e.g. `"1:2"` instead of `"1:02"`) or padding hours (e.g. `"01:00"` instead of `"1:00"`) violates the specification.
- **Impossible LED Counts:** If $turnedOn \ge 9$, backtracking or subset generation might waste effort before filtering. The 720-iteration loop naturally yields an empty list with zero special branching.
- **Bit Counting Performance:** `(bin(i) + bin(j)).count('1')` or `i.bit_count() + j.bit_count()` operates instantaneously for small integers.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$ constant time.
  - The loops execute exactly $12 \times 60 = 720$ iterations regardless of $turnedOn$.
  - Each iteration performs a few bit-count operations and string formatting.
  - 720 operations execute in $< 0.1$ ms.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary space, bounded by the maximum number of valid formatted strings returned (at most 720 strings).
