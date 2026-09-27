# Guided Example: String to Integer (atoi)

We trace the step-by-step deterministic finite state machine execution on a representative input string:

- **Input:** $s = \text{"   -042 with words"}$
- **Required output:** $-42$

This instance is selected because it exercises all five sequential phases of the conversion specification: skipping leading whitespace, resolving an optional sign, consuming leading zeroes and consecutive digits, stopping immediately at the first non-digit delimiter, and clamping the signed value within 32-bit limits.

---

## 1. Instance & Teaching Goal

The `atoi` specification converts a string $s$ into a 32-bit signed integer through a strictly ordered sequence of parsing phases:
1. **Whitespace:** Discard any leading whitespace characters (`' '`).
2. **Sign:** Read an optional sign (`'+'` or `'-'`), defaulting to positive if absent.
3. **Digits:** Read contiguous decimal digits until the next non-digit or end-of-string.
4. **Delimitation:** Stop immediately upon encountering any non-digit character. Subsequent digits or characters are disregarded.
5. **Rounding (Clamping):** Clamp the resulting integer to the 32-bit signed range $[-2^{31}, 2^{31}-1] = [-2147483648, 2147483647]$.

For $s = \text{"   -042 with words"}$:
- The three leading spaces are skipped.
- The negative sign `'-'` sets $\text{sign} = -1$.
- The digit `'0'` is processed ($\text{num} = 0$).
- The digits `'4'` and `'2'` form $42$.
- The subsequent space `' '` before $\text{"with"}$ is a non-digit, immediately terminating parsing.
- The final signed value is $-42$, which falls comfortably within $[-2^{31}, 2^{31}-1]$.

---

## 2. Conceptual Foundation & Invariants

### Deterministic State Machine (DFA)

The parser operates as a 5-phase deterministic transition system:

```text
[START: Spaces] ---> [SIGN: '+' / '-'] ---> [DIGITS: '0'-'9'] ---> [STOP]
       |                      |                     ^
       |                      v                     |
       +--------------------------------------------+
```

1. **State `LEAD_SPACE`:** Cursor $i$ advances while $s[i] = \text{' '}$.
2. **State `SIGN`:** If $s[i] = \text{'-'}$, set $\text{sign} = -1, i \leftarrow i + 1$; else if $s[i] = \text{'+'}$, set $\text{sign} = +1, i \leftarrow i + 1$.
3. **State `DIGITS`:** While $i < |s|$ and $s[i] \in [\text{'0'}, \text{'9'}]$:
   - Extract numerical value $d = s[i] - \text{'0'}$.
   - Guard against 32-bit overflow before multiplying.
   - Update $\text{magnitude} \leftarrow \text{magnitude} \cdot 10 + d$.
4. **State `TERMINAL`:** Return $\text{sign} \cdot \text{magnitude}$ clamped to $[-2^{31}, 2^{31}-1]$.

### Overflow Clamping Invariant
At each digit $d$, before computing $\text{magnitude} \cdot 10 + d$, we evaluate the 32-bit limits:
- If $\text{sign} = +1$ and $\text{magnitude} > \lfloor (2^{31}-1)/10 \rfloor = 214748364$ (or equals $214748364$ and $d \ge 7$), return $2^{31}-1 = 2147483647$.
- If $\text{sign} = -1$ and $\text{magnitude} > \lfloor 2^{31}/10 \rfloor = 214748364$ (or equals $214748364$ and $d \ge 8$), return $-2^{31} = -2147483648$.

> **Invariant.** The transition order is irreversible. Once the parser enters `DIGITS`, spaces or signs are treated as terminal delimiters rather than phase triggers.

---

## 3. Step-by-Step Worked Execution

We parse $s = \text{"   -042 with words"}$ index by index:

### Phase 1: Leading Whitespace
- **Index 0 ($s[0] = \text{' '}$):** Whitespace detected. Advance cursor to $i = 1$.
- **Index 1 ($s[1] = \text{' '}$):** Whitespace detected. Advance cursor to $i = 2$.
- **Index 2 ($s[2] = \text{' '}$):** Whitespace detected. Advance cursor to $i = 3$.

### Phase 2: Sign Determination
- **Index 3 ($s[3] = \text{'-'}$):** Negative sign encountered. Set $\text{sign} = -1$. Transition permanently to digit-reading phase. Advance to $i = 4$.

### Phase 3: Digit Accumulation
- **Index 4 ($s[4] = \text{'0'}$):** Valid digit $d = 0$.
  - Magnitude update: $0 \cdot 10 + 0 = 0$.
  - Advance to $i = 5$.
- **Index 5 ($s[5] = \text{'4'}$):** Valid digit $d = 4$.
  - Magnitude update: $0 \cdot 10 + 4 = 4$.
  - Advance to $i = 6$.
- **Index 6 ($s[6] = \text{'2'}$):** Valid digit $d = 2$.
  - Magnitude update: $4 \cdot 10 + 2 = 42$.
  - Advance to $i = 7$.

### Phase 4: Non-Digit Termination
- **Index 7 ($s[7] = \text{' '}$):** Space character encountered. Because the parser is already in the `DIGITS` state, this space is an invalid character, not a skippable leading space. Parsing halts immediately.

### Phase 5: Range Clamping
- Resulting value: $\text{sign} \cdot \text{magnitude} = -1 \cdot 42 = -42$.
- Bounds verification: $-2147483648 \le -42 \le 2147483647$.
- Output: $-42$.

---

## 4. Complete Execution Trace

| Cursor $i$ | Character $s[i]$ | Parser State | Action Taken | Current Sign | Magnitude So Far | Effective Value |
|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| 0 | `' '` | `LEAD_SPACE` | Skip whitespace; advance | $+1$ | 0 | 0 |
| 1 | `' '` | `LEAD_SPACE` | Skip whitespace; advance | $+1$ | 0 | 0 |
| 2 | `' '` | `LEAD_SPACE` | Skip whitespace; advance | $+1$ | 0 | 0 |
| 3 | `'-'` | `SIGN` | Record negative sign; advance | $-1$ | 0 | 0 |
| 4 | `'0'` | `DIGITS` | Append digit: $0 \cdot 10 + 0$ | $-1$ | 0 | 0 |
| 5 | `'4'` | `DIGITS` | Append digit: $0 \cdot 10 + 4$ | $-1$ | 4 | -4 |
| 6 | `'2'` | `DIGITS` | Append digit: $4 \cdot 10 + 2$ | $-1$ | 42 | -42 |
| 7 | `' '` | `TERMINAL` | Non-digit encountered; halt | $-1$ | 42 | **-42** |

### Boundary Behavior Demonstration

| Input Variant | Delimiting Reason | Final Parsed Result |
|:---|:---|:---:|
| `"-91283472332"` | Exceeds $-2^{31} = -2147483648$ | Clamped to **$-2147483648$** |
| `"4193 with words"` | Non-digit `' '` after `'3'` | **$4193$** |
| `"words and 987"` | Non-digit `'w'` before any digits | **$0$** |
| `"+-12"` | Second sign `'-'` after `'+'` | **$0$** |

---

## 5. Algorithmic Correctness

**Soundness.** The linear parser models a formal DFA with irreversible transitions. By construction:
- No character preceding the first non-whitespace can affect the sign.
- At most one sign character is consumed.
- The numeric value is built using exact positional decimal arithmetic ($v \leftarrow 10v + d$).
- Checking against 32-bit limits before multiplication guarantees arithmetic safety and prevents integer overflow.

**Completeness.** Every character in the input string is inspected at most once. The algorithm either terminates upon examining all characters or upon meeting the first invalid character, ensuring deterministic termination in at most $N$ steps.

---

## 6. Traps This Instance Exposes

- **Irreversible Whitespace Skipping:** Spaces after digits or signs are delimiters, not skippable leading spaces. For example, `" 1 2"` yields $1$, not $12$.
- **Multiple Signs:** An input like `"+-12"` must not evaluate to $-12$. Consuming `'+'` advances the phase; the immediately following `'-'` is a non-digit that terminates conversion with magnitude $0$.
- **Pre-Overflow Clamping:** Relying on language-level 64-bit integers or unbounded Python integers obscures the algorithmic requirement of 32-bit clamping. Checking whether $v > 214748364$ before multiplication preserves platform-independent correctness.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = |s|$. The cursor $i$ advances monotonically from $0$ to at most $N$. Each character evaluation involves $O(1)$ comparisons and arithmetic updates.
- **Auxiliary Space Complexity:** $O(1)$. Parsing is performed in place using a fixed set of scalar variables (index, sign, magnitude).
