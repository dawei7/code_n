# Guided Example: Similar RGB Color

We trace the step-by-step hexadecimal color channel decomposition ($R, G, B \in [0, 255]$), 3-character shorthand duplicate digit representation ($d \cdot 16 + d = 17 \cdot d$), channel independence orthogonalization, nearest multiple of 17 quotient rounding ($divmod(V, 17)$ with midpoint threshold $8$), and closest shorthand hexadecimal color formatting on representative color strings:

- **Input:**
  $$
  color = \text{"\#09f166"}
  $$
- **Required output:**
  $$
  \text{"\#11ee66"}
  $$
  - RGB color definitions & similarity metric:
    - A 7-character RGB color string has format `"#RRGGBB"`, where each two-character channel represents an integer in $[0, 255]$ in base 16.
    - A color has a **shorthand representation** if each channel consists of two identical hex digits:
      $$
      \text{"\#AABBCC"} \equiv \text{"\#ABC"}
      $$
    - The similarity metric between color $c_1 = (r_1, g_1, b_1)$ and color $c_2 = (r_2, g_2, b_2)$ is defined as:
      $$
      \text{Similarity}(c_1, c_2) = -(r_1 - r_2)^2 - (g_1 - g_2)^2 - (b_1 - b_2)^2
      $$
    - Maximizing similarity is mathematically identical to **minimizing Euclidean squared distance**:
      $$
      \min \left( (r_1 - r_2)^2 + (g_1 - g_2)^2 + (b_1 - b_2)^2 \right)
      $$
    - Because each channel $r_2, g_2, b_2$ can be chosen independently, the 3D minimization problem factors into **three independent 1D nearest-neighbor problems**!
- **Shorthand Multiples of 17 & Rounding Invariant:**
  - **The Multiple of 17 Property:**
    - Any two-digit hexadecimal number with identical digits `$dd$` represents the integer:
      $$
      \text{val}(dd) = d \times 16^1 + d \times 16^0 = d \times (16 + 1) = 17 \times d
      $$
      where $d \in \{0, 1, 2, \dots, 15\}$ (corresponding to hex characters `'0'` through `'f'`).
    - The 16 possible shorthand channel values in decimal are precisely the multiples of 17:
      $$
      \{ 0, 17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255 \}
      $$
  - **The Midpoint Division Rule ($r > 8$):**
    - For any target channel value $V \in [0, 255]$:
      - Compute quotient and remainder upon division by 17:
        $$
        q = \lfloor V / 17 \rfloor, \quad r = V \bmod 17
        $$
      - The distance to the lower multiple $17q$ is $r$.
      - The distance to the upper multiple $17(q + 1)$ is $17 - r$.
      - Compare distances:
        $$
        17 - r < r \iff 2r > 17 \iff r \ge 9
        $$
      - Therefore:
        - If remainder $r > 8$: round up to multiple $q + 1$.
        - If remainder $r \le 8$: round down to multiple $q$.
    - The optimal shorthand channel value is $17 \times (q + [r > 8])$, formatted as a 2-digit hex string.
- **Step-by-Step Worked Execution Trace on $color =$ `"#09f166"`:**
  - Segment channels:
    - Red channel: `"09"`
    - Green channel: `"f1"`
    - Blue channel: `"66"`
  - **Channel 1: Red (`"09"`):**
    - Convert from hexadecimal:
      $$
      V_{\text{red}} = 0 \times 16 + 9 = \mathbf{9}
      $$
    - Divide by 17:
      $$
      q, r = \text{divmod}(9, 17) \implies q = 0, \quad r = 9
      $$
    - Midpoint check:
      $$
      r > 8 \iff 9 > 8 \implies \mathbf{Round\ Up!}
      $$
    - Adjusted quotient: $q \leftarrow 0 + 1 = \mathbf{1}$.
    - Best multiple: $17 \times 1 = \mathbf{17}$.
    - Convert to hexadecimal: $17 = (11)_{16} \implies \mathbf{\text{"11"}}$.
    - Squared error: $(9 - 17)^2 = (-8)^2 = 64$ (versus $(9 - 0)^2 = 81$).
  - **Channel 2: Green (`"f1"`):**
    - Convert from hexadecimal:
      $$
      V_{\text{green}} = 15 \times 16 + 1 = 240 + 1 = \mathbf{241}
      $$
    - Divide by 17:
      $$
      q, r = \text{divmod}(241, 17) \implies q = 14, \quad r = 3
      $$
      *(Because $14 \times 17 = 238$, and $241 - 238 = 3$)*.
    - Midpoint check:
      $$
      r \le 8 \iff 3 \le 8 \implies \mathbf{Round\ Down!}
      $$
    - Adjusted quotient: $q = \mathbf{14}$.
    - Best multiple: $17 \times 14 = \mathbf{238}$.
    - Convert to hexadecimal: $238 = (\text{ee})_{16} \implies \mathbf{\text{"ee"}}$.
    - Squared error: $(241 - 238)^2 = 3^2 = 9$ (versus $(255 - 241)^2 = 14^2 = 196$).
  - **Channel 3: Blue (`"66"`):**
    - Channel already has identical digits `'6'` and `'6'`.
    - $V_{\text{blue}} = 6 \times 17 = 102 \implies r = 0 \implies \mathbf{\text{"66"}}$.
    - Squared error: $(102 - 102)^2 = 0$.
  - **Assembly of Optimal Shorthand Color:**
    $$
    ans = \text{"\#"} + \text{"11"} + \text{"ee"} + \text{"66"} = \mathbf{\text{"\#11ee66"}}
    $$
- **Boundary Rounding Threshold Trace ($color =$ `"#080808"` vs `"#090909"`):**
  - For `"#080808"`: each channel has $V = 8$. Remainder $8 \le 8 \implies$ rounds down to `"#000000"`.
  - For `"#090909"`: each channel has $V = 9$. Remainder $9 > 8 \implies$ rounds up to `"#111111"`.
- **Pure Black & White Identical Shorthand Trace:**
  - `"#000000"` remains `"#000000"`.
  - `"#ffffff"` remains `"#ffffff"`.

This instance demonstrates 3D metric projection onto regular integer sub-lattices and orthogonal 1D coordinate quantization, mathematically proves why identical hex digit constraints restrict target values to the ideal $(17\mathbb{Z}) \cap [0, 255]$, and derives $O(1)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a 7-character hex color string `"#RRGGBB"`:
Find the most similar shorthand color `"#AABBCC"` (identical digits per channel) minimizing $(r_1 - r_2)^2 + (g_1 - g_2)^2 + (b_1 - b_2)^2$.

```text
color = "#09f166"

Channels are independent:
  Red "09" = 9:
    9 / 17 = 0 remainder 9.
    Since remainder 9 > 8, round up to 1 -> 17 -> "11".

  Green "f1" = 241:
    241 / 17 = 14 remainder 3.
    Since remainder 3 <= 8, round down to 14 -> 238 -> "ee".

  Blue "66" = 102:
    Already a duplicate "66".

Result: "#11ee66"
```

### The Invariant of the Multiples of 17
- Any shorthand channel has identical hex digits $dd$, equal to $16d + d = 17d$.
- The 16 possible values are the multiples of 17 ($17 \times 0 \dots 17 \times 15$).
- Each channel rounds to the nearest multiple of 17 (round up if remainder $> 8$).

---

## 2. Conceptual Foundation & Invariants

### 1. Hexadecimal Decimalization:
$$
V = 16 \cdot \text{hex}(c_0) + \text{hex}(c_1)
$$

### 2. Nearest Multiple Rounding:
$$
q = \lfloor V / 17 \rfloor, \quad r = V \bmod 17
$$
$$
d^* = \begin{cases} q + 1 & r > 8 \\ q & r \le 8 \end{cases}
$$
$$
\text{channel}^* = \text{hex}(17 \cdot d^*)
$$

> **Lattice Quantization Invariant.** The shorthand RGB manifold is the discrete cubic sub-lattice $(17\mathbb{Z})^3 \subseteq \mathbb{Z}^3$. Because the metric is isotropic Euclidean, the nearest lattice point projection decomposes into 1D Voronoi cells of length 17 with decision boundary at offset 8.5.

---

## 3. Step-by-Step Worked Execution

We trace $color =$ `"#09f166"`:

---

### Step 1: Red `"09"`
- $V = 9$. $9 / 17 = 0$, remainder 9.
- $9 > 8 \implies q = 1 \implies 17 \implies \mathbf{\text{"11"}}$.

---

### Step 2: Green `"f1"`
- $V = 15 \times 16 + 1 = 241$.
- $241 / 17 = 14$, remainder 3.
- $3 \le 8 \implies q = 14 \implies 14 \times 17 = 238 \implies \mathbf{\text{"ee"}}$.

---

### Step 3: Blue `"66"`
- $V = 6 \times 17 = 102$.
- Remainder 0 $\implies \mathbf{\text{"66"}}$.

---

### Step 4: Output
$$
\mathbf{\text{"\#11ee66"}}
$$

---

## 4. Complete Execution Trace

| Channel | Hex Pair | Decimal Value $V$ | Quotient $q = V // 17$ | Remainder $r = V \% 17$ | Rounding Action ($r > 8$) | Nearest Multiplier | Output Hex |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Red | `"09"` | $9$ | $0$ | $9$ | Round Up ($9 > 8$) | $1$ | `"11"` |
| Green | `"f1"` | $241$ | $14$ | $3$ | Round Down ($3 \le 8$) | $14$ | `"ee"` |
| **Blue** | **`"66"`** | **$102$** | **$6$** | **$0$** | **Exact ($0 \le 8$)** | **$6$** | **`"66"`** |
| **Final** | — | — | — | — | — | — | **`"#11ee66"`** |

---

## 5. Boundary Cases & Failure Modes

- **Boundary 8 ($V = 8$):** $8 / 17 = 0$ rem 8. $8 \le 8 \implies$ rounds down to 0 (`"00"`).
- **Boundary 9 ($V = 9$):** $9 / 17 = 0$ rem 9. $9 > 8 \implies$ rounds up to 17 (`"11"`).
- **Upper Limit ($V = 255$):** $255 / 17 = 15$ rem 0 $\implies$ rounds to 255 (`"ff"`).
- **Already Shorthand (`"#88aa44"`):** All remainders 0 $\implies$ returns identical string `"#88aa44"`.

---

## 6. Traps & Common Anti-Patterns

- **Searching Over All $16^3 = 4096$ Colors:** There is no need to loop through all 4096 shorthand combinations; the channels are completely independent, allowing each channel to be solved in $O(1)$ arithmetic.
- **Forgetting Leading Zero in Hex Formatting:** If the nearest multiple is 0, format as `"00"`, not `"0"`. Use `{:02x}`.
- **Case Sensitivity:** Hex digits must be lowercase as specified in problem contract.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - 3 channels evaluated using constant-time arithmetic (`divmod` by 17): $\mathcal{O}(1)$.
  - Total Time: strictly $\mathcal{O}(1)$. Completes in $< 0.01$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space.
