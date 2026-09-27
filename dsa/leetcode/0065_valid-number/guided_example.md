# Guided Example: Valid Number

We trace the step-by-step state machine / grammar verification on representative valid and invalid numerical strings:

- **Valid Scientific Notation:** $s = \text{"-90E3"} \implies \text{True}$
- **Valid Decimal Without Trailing Digit:** $s = \text{"3."} \implies \text{True}$
- **Invalid Malformed Instances:** $s = \text{"."}$, $s = \text{"e3"}$, $s = \text{"1e"} \implies \text{False}$

This instance demonstrates modeling numeric syntax as a deterministic state machine, validating sign placements ($i = 0$ or after `e`), enforcing dot exclusivity before exponents, and requiring digit presence after exponent markers in $O(N)$ time and $O(1)$ space.

---

## 1. Instance & Teaching Goal

A **valid number** can be split into:
1. A **decimal number** or an **integer**.
2. (Optional) An **exponent** consisting of `'e'` or `'E'` followed by an integer.

- An **integer** consists of an optional sign (`'+'` or `'-'`) followed by one or more digits.
- A **decimal number** consists of an optional sign followed by:
  - At least one digit followed by a dot `.` (e.g. `"3."`).
  - At least one digit followed by a dot followed by digits (e.g. `"3.14"`).
  - A dot followed by at least one digit (e.g. `".1"`).
  *(A dot alone `"."` with no digits is invalid).*
- An **exponent** cannot contain dots, and must be followed by an integer with at least one digit.

A naive regular expression can be slow and prone to catastrophic backtracking on crafted strings. The optimal approach processes characters linearly using three boolean flags: `seen_digit`, `seen_dot`, and `seen_exponent`.

---

## 2. Conceptual Foundation & Invariants

### 3-Flag State Tracking Rules
We iterate through characters $s[i]$ from $i = 0$ to $N - 1$:

1. **Digit ($0 \dots 9$):**
   - Set $\text{seen\_digit} \leftarrow \text{True}$.
2. **Sign (`'+'` or `'-'`):**
   - A sign is legally valid **only** if:
     - It is the very first character ($i == 0$), OR
     - It immediately follows an exponent character ($s[i - 1] \in \{\text{'e'}, \text{'E'}\}$).
   - If a sign appears anywhere else, return $\text{False}$.
3. **Decimal Point (`'.'`):**
   - A dot is legally valid **only** if:
     - No dot has appeared yet ($\neg \text{seen\_dot}$), AND
     - No exponent has appeared yet ($\neg \text{seen\_exponent}$).
   - If valid, set $\text{seen\_dot} \leftarrow \text{True}$. Otherwise, return $\text{False}$.
4. **Exponent Marker (`'e'` or `'E'`):**
   - An exponent is legally valid **only** if:
     - No exponent has appeared yet ($\neg \text{seen\_exponent}$), AND
     - At least one digit has appeared in the mantissa ($\text{seen\_digit} == \text{True}$).
   - If valid:
     - Set $\text{seen\_exponent} \leftarrow \text{True}$.
     - Reset $\text{seen\_digit} \leftarrow \text{False}$ *(because an exponent must be followed by at least one new integer digit!)*.
   - Otherwise, return $\text{False}$.
5. **Any Other Character:**
   - Return $\text{False}$ immediately.

### Final Acceptance Condition
After scanning all characters, the string is valid if and only if:
$$
\text{seen\_digit} == \text{True}
$$
*(Guarantees that trailing exponents like `"1e"` or bare dots `"."` are rejected).*

---

## 3. Step-by-Step Worked Execution

### Case 1: Valid Exponent $s = \text{"-90E3"}$
Initialize $\text{seen\_digit} = \text{False}, \text{seen\_dot} = \text{False}, \text{seen\_exponent} = \text{False}$.

- **Character 0 ($i = 0, c = \text{'-'}$):**
  - Sign at index 0: Allowed!
- **Character 1 ($i = 1, c = \text{'9'}$):**
  - Digit: $\text{seen\_digit} \leftarrow \text{True}$.
- **Character 2 ($i = 2, c = \text{'0'}$):**
  - Digit: $\text{seen\_digit} \leftarrow \text{True}$.
- **Character 3 ($i = 3, c = \text{'E'}$):**
  - Exponent check: $\text{seen\_digit}$ is True, $\text{seen\_exponent}$ is False. Allowed!
  - State update: $\text{seen\_exponent} \leftarrow \text{True}, \text{seen\_digit} \leftarrow \text{False}$.
- **Character 4 ($i = 4, c = \text{'3'}$):**
  - Digit: $\text{seen\_digit} \leftarrow \text{True}$.
- **End of String:**
  - Check acceptance: $\text{seen\_digit} == \text{True}$.
  - Result: $\text{True}$.

---

### Case 2: Trap Breakdown Analysis

| Input String | Failure Point / Rule Violation | Accepted? |
|:---:|:---|:---:|
| `"."` | $\text{seen\_digit}$ is False upon termination | **False** |
| `"e3"` | Exponent encountered when $\text{seen\_digit}$ is False | **False** |
| `"1e"` | After `'e'`, $\text{seen\_digit}$ reset to False and string ended | **False** |
| `"1a"` | Letter `'a'` is not a digit, sign, dot, or exponent | **False** |
| `"+-5"` | Sign `'-'` at index 1 does not follow `'e'` | **False** |
| `"99e2.5"` | Dot `'.'` encountered when $\text{seen\_exponent}$ is True | **False** |
| `"3."` | Dot is valid, $\text{seen\_digit}$ was set by `'3'`, terminates True | **True** |
| `".1"` | Dot valid, $\text{seen\_digit}$ set by `'1'`, terminates True | **True** |

---

## 4. Complete Execution Trace

### Trace for $s = \text{"-90E3"}$

| Index $i$ | Token $c$ | Validation Rule Applied | Flag: `seen_digit` | Flag: `seen_dot` | Flag: `seen_exponent` | Outcome |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| 0 | `'-'` | Leading sign at index 0 | False | False | False | Valid |
| 1 | `'9'` | First mantissa digit | **True** | False | False | Valid |
| 2 | `'0'` | Subsequent digit | **True** | False | False | Valid |
| 3 | `'E'` | Exponent preceded by digit | **False (Reset)** | False | **True** | Valid |
| 4 | `'3'` | Exponent integer digit | **True** | False | True | Valid |
| Exit | - | Terminal test: `seen_digit == True` | **True** | False | True | **Emit True** |

---

## 5. Algorithmic Correctness

**Soundness.** Every character transition enforces the context-free numeric grammar defined by the problem. Any illegal combination—such as misplaced signs, duplicate dots, dots inside exponents, or unknown characters—triggers an immediate `False` verdict.

**Completeness.** Every character in $s$ is examined once in order. Resetting $\text{seen\_digit} = \text{False}$ upon reading an exponent ensures that no incomplete number like `"12e"` or `"12e+"` can terminate in an accepting state without at least one subsequent digit.

---

## 6. Traps This Instance Exposes

- **Lone Signs or Lone Dots:** A string containing only `"+"` or `"."` passes local character validation but fails the terminal $\text{seen\_digit} == \text{True}$ test.
- **Signs After Exponent:** A sign is valid after `'e'` (e.g. `"1e-5"` or `"2e+3"`). Restricting signs to only index 0 would wrongly reject valid signed exponents.
- **No Dots in Exponent:** Numbers like `"1e2.5"` are invalid in standard scientific notation. The condition `not seen_exponent` during dot handling prevents this.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the string length. The loop executes $N$ iterations, doing $O(1)$ operations per character.
- **Auxiliary Space Complexity:** $O(1)$. Memory consumption is strictly constant using three boolean flags.
