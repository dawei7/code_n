# Guided Example: Restore IP Addresses

We trace the step-by-step 4-segment backtracking search with leading zero checks and remaining-length pruning on a representative digit string:

- **Input:** $s = \text{"25525511135"}$
- **Required output:** `["255.255.11.135", "255.255.111.35"]`
- **Single-Zero Address:** $s = \text{"0000"} \implies \text{["0.0.0.0"]}$

This instance demonstrates recursive backtracking to partition a string into exactly 4 valid octets, checking numerical bounds ($0 \le \text{val} \le 255$), enforcing leading zero prohibitions ($s[i] == \text{'0'} \implies \text{len} = 1$), remaining-length feasibility pruning ($4 - k \le \text{rem} \le 3(4 - k)$), and state rollback in $O(1)$ constant time.

---

## 1. Instance & Teaching Goal

A valid IPv4 address consists of exactly 4 integers (called octets) separated by single dots.
Each octet must satisfy:
1. **Numerical range:** Integer value between $0$ and $255$ inclusive.
2. **No leading zeroes:** An octet cannot start with `'0'` unless it is the single character `"0"` (e.g. `"0"` is valid, but `"01"`, `"00"`, `"025"` are forbidden).

Given $s = \text{"25525511135"}$ ($|s| = 11$):
- Valid IPv4 addresses must use all 11 digits across exactly 4 octets.
- Because each octet has length between $1$ and $3$, the partition sizes must sum to 11. The only valid 4-integer partitions of 11 using integers $\in \{1, 2, 3\}$ are:
  - $(3, 3, 2, 3) \implies \text{"255.255.11.135"}$
  - $(3, 3, 3, 2) \implies \text{"255.255.111.35"}$

A brute-force loop without length pruning explores invalid partitions.
By tracking the number of remaining segments $4 - k$ and comparing against remaining character count, candidate branches outside the range $[4 - k, \, 3(4 - k)]$ are pruned instantly.

---

## 2. Conceptual Foundation & Invariants

### 4-Part Backtracking Protocol
We define $\text{backtrack}(\text{start}, \text{octets})$:
- $\text{start}$: The starting character index in $s$.
- $\text{octets}$: List of confirmed octet strings (length $k \in [0, 4]$).

1. **Terminal Condition ($|\text{octets}| == 4$):**
   - If $\text{start} == |s|$:
     Valid address found! Add $\text{".".join}(\text{octets})$ to results.
   - Return.
2. **Remaining Length Feasibility Check:**
   Let $\text{rem} = |s| - \text{start}$, and $\text{needed} = 4 - |\text{octets}|$.
   - If $\text{rem} < \text{needed}$ (not enough digits left for each remaining octet to have at least 1 digit): **Prune**.
   - If $\text{rem} > 3 \times \text{needed}$ (too many digits left; even with 3 digits per remaining octet, digits will remain): **Prune**.
3. **Octet Exploration (Length $L \in \{1, 2, 3\}$):**
   For $L = 1, 2, 3$ where $\text{start} + L \le |s|$:
   - Candidate substring: $\text{part} = s[\text{start} : \text{start} + L]$.
   - **Leading Zero Check:** If $L > 1$ and $\text{part}[0] == \text{'0'}$:
     Break (adding more digits to a leading zero will still produce an invalid leading zero).
   - **Numerical Range Check:** If $\text{int}(\text{part}) > 255$:
     Break (adding more digits will only increase the value).
   - **Recurse & Rollback:**
     - $\text{octets.append}(\text{part})$
     - $\text{backtrack}(\text{start} + L, \text{octets})$
     - $\text{octets.pop()}$

> **Invariant.** At recursion depth $k$, $\text{octets}$ contains $k$ strictly valid IPv4 segments that exactly concatenate to $s[0 \dots \text{start}-1]$.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"25525511135"}$ ($|s| = 11$):

### Top-Level Call ($k = 0, \text{start} = 0, \text{rem} = 11$)
- Needed octets: $4$. Required digits: $[4, 12]$. Since $11 \in [4, 12]$, valid.
- Testing candidate lengths $L$ for Octet 1:
  - $L = 1$ (`"2"`): remaining $10 > 3 \times 3 = 9$. **Pruned by length check!**
  - $L = 2$ (`"25"`): remaining $9 \le 3 \times 3 = 9$. Valid!
    - Subtree explores: no partition can form 3 valid octets with remaining digits.
  - $L = 3$ (`"255"`): value $255 \le 255$. Remaining $8 \in [3, 9]$. **Accepted!**
  - Append `"255"`. Recurse to Octet 2.

---

### Octet 2 ($k = 1, \text{start} = 3, \text{rem} = 8$)
- Needed octets: $3$. Permitted remaining length: $[3, 9]$. $8 \in [3, 9]$.
- Candidate lengths:
  - $L = 1$ (`"2"`): remaining $7 > 2 \times 3 = 6$. **Pruned!**
  - $L = 2$ (`"25"`): remaining $6 \in [2, 6]$.
    - Fails deeper downstream checks.
  - $L = 3$ (`"255"`): value $255 \le 255$. Remaining $5 \in [2, 6]$. **Accepted!**
  - Append `"255"`. Recurse to Octet 3.

---

### Octet 3 ($k = 2, \text{start} = 6, \text{rem} = 5$, Suffix `"11135"`)
- Needed octets: $2$. Permitted remaining length: $[2, 6]$. $5 \in [2, 6]$.
- Candidate lengths:
  - **Branch $L = 2$ (`"11"`):**
    - Value $11 \le 255$.
    - Remaining digits: $5 - 2 = 3$ (Suffix `"135"`).
    - Octet 4 evaluation:
      - Needed: 1 octet. Length of `"135"` is $3$.
      - Numerical check: $135 \le 255$. No leading zero. **Valid!**
      - **Emit Result 1:** `"255.255.11.135"`.
  - **Branch $L = 3$ (`"111"`):**
    - Value $111 \le 255$.
    - Remaining digits: $5 - 3 = 2$ (Suffix `"35"`).
    - Octet 4 evaluation:
      - Needed: 1 octet. Length of `"35"` is $2$.
      - Numerical check: $35 \le 255$. No leading zero. **Valid!**
      - **Emit Result 2:** `"255.255.111.35"`.
  - **Branch $L = 1$ (`"1"`):**
    - Remaining digits: $4 > 1 \times 3 = 3$. **Pruned by length check!**

---

### All branches concluded.
Output: `["255.255.11.135", "255.255.111.35"]`.

---

## 4. Complete Execution Trace

```text
                                  Root ""
                                     |
                                  "255" (Octet 1)
                                     |
                                  "255" (Octet 2)
                                  /            \
                       "11" (Octet 3)       "111" (Octet 3)
                             |                     |
                      "135" (Octet 4)        "35" (Octet 4)
                             |                     |
                     255.255.11.135         255.255.111.35
```

| Depth $k$ | Start Index | Candidate String | Length $L$ | Leading Zero? | Numerical Value | Feasibility Check | Decision |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 0 | 0 | `"2"` | 1 | No | 2 | $\text{rem} = 10 > 9$ | **Pruned (too long)** |
| 0 | 0 | `"25"` | 2 | No | 25 | $\text{rem} = 9 \le 9$ | Explored (dead end) |
| 0 | 0 | `"255"` | 3 | No | 255 | $\text{rem} = 8 \le 9$ | **Accepted (Branch 1)** |
| 1 | 3 | `"255"` | 3 | No | 255 | $\text{rem} = 5 \le 6$ | **Accepted (Branch 2)** |
| 2 | 6 | `"11"` | 2 | No | 11 | $\text{rem} = 3 \le 3$ | **Accepted $\implies$ "255.255.11.135"** |
| 2 | 6 | `"111"` | 3 | No | 111 | $\text{rem} = 2 \le 3$ | **Accepted $\implies$ "255.255.111.35"** |

---

## 5. Algorithmic Correctness

**Soundness.** Every generated candidate consists of exactly four octets whose string lengths sum to $|s|$. Each octet passes the non-leading zero test and is verified to fall within $[0, 255]$. Thus, every emitted IP address is strictly valid.

**Completeness.** Backtracking evaluates all possible segment lengths $1, 2, 3$ at each step. Pruning is applied only when the remaining length is mathematically insufficient ($\text{rem} < \text{needed}$) or exceeds maximal capacity ($\text{rem} > 3 \times \text{needed}$), so no valid 4-part partition can be skipped.

---

## 6. Traps This Instance Exposes

- **Global String Length Filtering:** If $|s| < 4$ or $|s| > 12$, an IPv4 address is mathematically impossible. Returning `[]` before initiating backtracking saves execution overhead.
- **Leading Zero Rejection:** `"01"` is numerically $1$, but as an IP octet it is illegal. The rule must be: if $\text{len} > 1$ and $\text{part}[0] == \text{'0'}$, reject!
- **Single Zero Acceptance:** A single digit `"0"` is fully legal (e.g. `"0.0.0.0"`). Rejection must not trigger when $\text{len} == 1$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$ constant upper bound! Because an IPv4 address has strictly 4 octets and each octet has at most 3 choices ($1, 2, 3$ digits), the search tree has at most $3^4 = 81$ leaf paths.
- **Auxiliary Space Complexity:** $O(1)$ bounded auxiliary space for the recursion stack (maximum depth 4) and path storage.
