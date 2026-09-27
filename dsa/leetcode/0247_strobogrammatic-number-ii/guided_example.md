# Guided Example: Strobogrammatic Number II

We trace the step-by-step center-outward recursive expansion, valid rotational pair wrapping, and leading-zero boundary suppression on representative integer length requests:

- **Input:** $n = 2$
- **Required output:** `["11", "69", "88", "96"]` (All four 2-digit strobogrammatic numbers; `"00"` is suppressed to prevent leading zero)
- **Odd Length Instance:** $n = 1 \implies \text{["0", "1", "8"]}$ (All three self-symmetric single digits)
- **Three-Digit Instance:** $n = 3 \implies 12$ numbers (Wraps centers `["0", "1", "8"]` with 4 outer pairs $\implies 4 \times 3 = 12$)
- **Four-Digit Instance:** $n = 4 \implies 20$ numbers (Outer layer has 4 choices; inner layer has 5 choices including `"00"` $\implies 4 \times 5 = 20$)

This instance demonstrates recursive divide-and-conquer string synthesis, explains why generating strings inside-out ($m - 2 \to m$) cleanly separates inner zeroes from forbidden leading zeroes, derives the exact combinatorial cardinality ($4 \times 5^{\lfloor n/2 \rfloor - 1}$), and operates in $O(N \cdot 5^{N/2})$ optimal time.

---

## 1. Instance & Teaching Goal

Given an integer $n = 2$, construct and return **all strobogrammatic numbers of length $n$**.
A strobogrammatic number looks identical when rotated 180 degrees upside down.
For $n = 2$:
- Valid pairs: `"11"`, `"69"`, `"88"`, `"96"`.
- What about `"00"`? Rotating `"00"` produces `"00"`, but standard multi-digit decimal numbers cannot have leading zeroes (`"00"` is not a valid 2-digit number!).
Therefore, `"00"` is forbidden on the outermost layer.
Output: `["11", "69", "88", "96"]`.

### Inside-Out vs Outside-In Construction
If we try to construct candidate numbers digit-by-digit from left to right, we must maintain mirroring constraints with the right half.
Instead, **expanding from the center outward** ($m - 2 \to m$) naturally mirrors the string symmetrically:
- Base center for even $n$: empty string `""` (length 0).
- Base centers for odd $n$: single digits `["0", "1", "8"]` (length 1).
- Each recursive step wraps the existing inner string $s$ with the 5 valid rotational pairs:
  $$
  (\text{"1"}, \text{"1"}), \quad (\text{"6"}, \text{"9"}), \quad (\text{"8"}, \text{"8"}), \quad (\text{"9"}, \text{"6"}), \quad (\text{"0"}, \text{"0"})
  $$
- The pair $(\text{"0"}, \text{"0"})$ is permitted at all internal layers, but suppressed at the outermost layer ($m == n$)!

---

## 2. Conceptual Foundation & Invariants

### Recursive Expansion Contract `helper(m, n)`
`helper(m, n)` returns all valid strobogrammatic sub-strings of length $m$ intended for a final number of length $n$:
1. **Base Cases:**
   - If $m == 0$: return `[""]`.
   - If $m == 1$: return `["0", "1", "8"]`.
2. **Recursive Step ($m > 1$):**
   Obtain smaller centered sub-strings:
   $$
   \text{inner\_list} = \text{helper}(m - 2, n)
   $$
   Initialize $\text{results} = []$.
   For each inner string $s \in \text{inner\_list}$:
   - Always append non-zero rotational wrappers:
     $$
     \text{"1"} + s + \text{"1"}
     $$
     $$
     \text{"6"} + s + \text{"9"}
     $$
     $$
     \text{"8"} + s + \text{"8"}
     $$
     $$
     \text{"9"} + s + \text{"6"}
     $$
   - **Leading Zero Guard:**
     Append $(\text{"0"}, \text{"0"})$ **only if $m \ne n$**:
     $$
     \text{if } m \ne n: \quad \text{results}.\text{append}(\text{"0"} + s + \text{"0"})
     $$
3. Return `results`.

### Combinatorial Cardinality Formula
Let $h = \lfloor n / 2 \rfloor$:
- If $n$ is even ($n = 2h, h \ge 1$):
  $$
  \text{Count} = 4 \times 5^{h - 1}
  $$
- If $n$ is odd ($n = 2h + 1, h \ge 1$):
  $$
  \text{Count} = 4 \times 5^{h - 1} \times 3
  $$
*(For $n = 1$, count is 3)*.

The same formula read as a table, with the authored cases as evidence:

| $n$ | Layer structure | Count formula | Exact count | Where the value is confirmed |
|:---:|:---|:---|:---:|:---|
| 1 | center only, no wrapper | $3$ self-symmetric centers | 3 | authored single-digit case `["0", "1", "8"]` |
| 2 | one wrapper layer | $4 \times 5^{0}$ | 4 | authored case listing `"11", "69", "88", "96"` |
| 3 | one wrapper plus a center | $4 \times 3$ | 12 | authored three-digit case |
| 4 | two wrapper layers | $4 \times 5$ | 20 | authored four-digit case |
| 5 | two wrappers plus a center | $4 \times 3 \times 5$ | 60 | formula only; no authored case |
| 6 | three wrapper layers | $4 \times 5^{2}$ | 100 | formula only; no authored case |
| 14 | seven wrapper layers, the maximum in contract | $4 \times 5^{6}$ | 62500 | authored maximum-length case, which lists all of them |

> **Invariant.** Every string generated at level $m$ is symmetrically strobogrammatic. At the terminal level $m = n$, no generated string begins with `'0'`.

---

## 3. Step-by-Step Worked Execution

We trace the execution for $n = 2$:
Target length $n = 2$.
Top-level call: `helper(m = 2, n = 2)`.

### Step 1: Recurse to Base Case
- Top-level needs `helper(2 - 2, 2) = helper(0, 2)`.
- $m = 0 \implies$ Base case triggered!
- Returns `inner_list = [""]`.

---

### Step 2: Wrap Base Center at $m = 2$
Inner string to wrap: $s = \text{""}$.
Available rotational pairs:
1. Wrap with $(1, 1)$: $\text{"1"} + \text{""} + \text{"1"} = \mathbf{\text{"11"}}$.
2. Wrap with $(6, 9)$: $\text{"6"} + \text{""} + \text{"9"} = \mathbf{\text{"69"}}$.
3. Wrap with $(8, 8)$: $\text{"8"} + \text{""} + \text{"8"} = \mathbf{\text{"88"}}$.
4. Wrap with $(9, 6)$: $\text{"9"} + \text{""} + \text{"6"} = \mathbf{\text{"96"}}$.
5. Wrap with $(0, 0)$?
   - Check condition: $m \ne n \implies 2 \ne 2$ (**False**).
   - Because $m == n$, this is the outermost boundary!
   - Wrapper $(\text{"0"}, \text{"0"})$ is **suppressed** to avoid leading zero `"00"`.

---

### Step 3: Emit Final Collection
Aggregated results for $n = 2$:
$$
\text{["11", "69", "88", "96"]}
$$

---

## 4. Complete Execution Trace

```text
n = 2:
helper(2, 2):
  helper(0, 2) -> [""]
  Wrap "" with non-zero pairs:
    "1" + "" + "1" -> "11"
    "6" + "" + "9" -> "69"
    "8" + "" + "8" -> "88"
    "9" + "" + "6" -> "96"
  (Pair "0" + "" + "0" skipped because m == n)
Result: ["11", "69", "88", "96"]
```

| Recursion Depth | Layer Length $m$ | Target Length $n$ | Base / Inner Sub-strings | Active Wrappers Applied | Generated Strings |
|:---:|:---:|:---:|:---:|:---|:---|
| **Base** | 0 | 2 | None | Base identity | `[""]` |
| **Outermost** | 2 | 2 | `[""]` | `(1,1), (6,9), (8,8), (9,6)` (`00` skipped) | **`["11", "69", "88", "96"]`** |

### Contrast: Odd Length Execution ($n = 3$)
- `helper(1, 3)` returns `["0", "1", "8"]` (Base case $m = 1$).
- `helper(3, 3)` wraps each center with the 4 outer pairs ($m == 3 == n \implies 00$ skipped):
  - Around `"0"`: `"101", "609", "808", "906"`
  - Around `"1"`: `"111", "619", "818", "916"`
  - Around `"8"`: `"181", "689", "888", "986"`
- Total: $4 \times 3 = 12$ valid numbers.

### Layer-by-Layer Expansion for $n = 4$

The guard depends on the layer index, not on the digit, and this table is the clearest place to see why:

| Layer length $m$ | Inner layer already computed | Wrappers available at this layer | Is `"0" + s + "0"` allowed? | Strings emerging from this layer |
|:---:|:---|:---|:---|:---|
| 0 | none, this is the base | base identity | not applicable | `[""]` |
| 2 | `[""]` | `11`, `88`, `69`, `96`, `00` | Yes, because $m = 2 \ne 4 = n$ | `["00", "11", "69", "88", "96"]`, five strings |
| 4, the outermost | the five strings above | `11`, `88`, `69`, `96` | No, because $m = 4 = n$; a leading `'0'` would be produced | the $20$ four-digit numerals, from `"1001"` through `"9966"` |

The interior layer is exactly what licenses zeros inside a numeral: wrapping the inner string `"00"` with `"1"` on both sides yields `"1001"`, and the guard never even inspects that inner string, because the decision belongs to the layer currently being wrapped. Reading outward, $5 \times 4 = 20$, which is the count the case data confirms.

---

## 5. Algorithmic Correctness

**Soundness.** By mathematical induction:
1. Base cases $m = 0$ (empty) and $m = 1$ (`0, 1, 8`) are palindromic under 180-degree rotation.
2. If string $s$ is strobogrammatic, prepending $a$ and appending $b$ where $\rho(a) = b$ produces a new string $a s b$ that is also strobogrammatic.
3. Suppressing $(0, 0)$ when $m == n$ guarantees the first character is non-zero, satisfying decimal integer formatting rules.

**Completeness.** Any strobogrammatic string of length $n$ must end in a valid pair $(a, b)$ with $\rho(a) = b$ and contain a valid strobogrammatic string of length $n - 2$ in its interior. The algorithm systematically recurses through all combinations without omission.

---

## 6. Traps This Instance Exposes

- **Prematurely Banning Zeroes:** Internal zeroes are completely valid (e.g. `"1001"` for $n = 4$ or `"101"` for $n = 3$). The check must be `if m != n:`, allowing `"0" + s + "0"` at internal depths and only banning it at the outer perimeter.
- **Center Digits in Odd Numbers:** Only `'0'`, `'1'`, and `'8'` can serve as single-character centers. Digits `'6'` and `'9'` rotate into each other, not themselves, so they can never be placed in the center.
- **Stack Overflow on Large $n$:** The recursion performs $\lfloor n/2 \rfloor$ expansions, hence $\lfloor n/2 \rfloor + 1$ nested calls once the base case is counted. For LeetCode constraints ($n \le 14$) that is at most $8$ frames, well within call-stack safety.

### Boundary Behaviour of the Generator

| Boundary scenario | Concrete input | Required result | Why the recursion produces it |
|:---|:---|:---|:---|
| Minimum length | $n = 1$ | `["0", "1", "8"]` | The base case returns the three self-symmetric digits and no wrapper layer exists, so the single digit `'0'` is legal; the leading-zero guard never fires because there is no outer wrap to suppress |
| Smallest even length | $n = 2$ | $4$ numerals | `"00"` is strobogrammatic as a glyph sequence but would be a leading zero, so the outermost layer drops it and keeps only `"11", "69", "88", "96"` |
| Interior zeros | $n = 4$ | $20$ numerals including `"1001"` | The inner string `"00"` is produced at layer $2$, where $m \ne n$; the guard is a property of the layer being wrapped and never of the digit itself |
| Lone center digit | $n = 3$ | $12$ numerals | Only `'0'`, `'1'` and `'8'` are offered as centers: `'6'` and `'9'` rotate into each other, so a single one of them cannot be its own image |
| Every result is self-mirroring at the ends | any even $n$, e.g. the last $n = 4$ result `"9966"` | the final digit is the image of the first | Each wrapper appends exactly $\rho$ of the digit it prepends, so the property holds by construction rather than by a later filter |
| Maximum length | $n = 14$ | $62500 = 4 \times 5^{6}$ numerals, from `"10000000000001"` to `"99999996666666"` | Seven wrapper layers, each contributing five choices except the outermost four; the recursion nests $8$ calls including the base case |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N \cdot 5^{N/2})$, where $N = n$. The algorithm generates exactly $4 \times 5^{\lfloor N/2 \rfloor - 1}$ strings for even $N$ (and $12 \times 5^{\lfloor N/2 \rfloor - 1}$ for odd $N$). Each string has length $N$, requiring $O(N)$ string concatenation time. The runtime is asymptotically optimal since it is proportional to the size of the output.
- **Auxiliary Space Complexity:** $O(N \cdot 5^{N/2})$ to store all generated strings in memory (call stack depth is only $O(N)$).
