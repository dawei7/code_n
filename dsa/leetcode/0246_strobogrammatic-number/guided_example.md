# Guided Example: Strobogrammatic Number

We trace the step-by-step 180-degree glyph rotation mapping, two-pointer inward mirror matching, and center self-symmetry validation on representative numeric strings:

- **Input:** $\text{num} = \text{"69"}$
- **Required output:** `true` (Rotated 180 degrees: the first digit `'6'` turns into `'9'` at the end, and the second digit `'9'` turns into `'6'` at the start $\implies \text{"69"}$)
- **Self-Symmetric Instance:** $\text{num} = \text{"88"} \implies \text{true}$ (Both `'8'`s rotate into themselves)
- **Invalid Digit Instance:** $\text{num} = \text{"962"} \implies \text{false}$ (Digit `'2'` is unreadable when inverted 180 degrees)
- **Odd Length Valid Instance:** $\text{num} = \text{"818"} \implies \text{true}$ (Center element `'1'` is self-symmetric)
- **Odd Length Mirror Mismatch:** $\text{num} = \text{"696"} \implies \text{false}$ (The outer pair compares `'6'` with `'6'`, and $\rho(\text{'6'}) = \text{'9'} \ne \text{'6'}$, so the rejection happens before the center is reached)

This instance demonstrates 180-degree rotational symmetry on decimal glyphs, identifies the five valid invertible digits ($\{0, 1, 6, 8, 9\}$) and the three self-symmetric center digits ($\{0, 1, 8\}$), details the two-pointer inward check ($L \le R$), and operates in $O(N)$ time with $O(1)$ auxiliary space.

---

## 1. Instance & Teaching Goal

Given a string `num = "69"`, determine whether it is a **strobogrammatic number** (a number that appears identical after a 180-degree plane rotation):
```text
Original:   6 9
Rotated:    6 9   (Matches original!)
```

### The 180-Degree Inversion Function
Physical 180-degree rotation of a string produces two transformations:
1. **Reversal of Position:** The $i^{\text{th}}$ character from the left moves to the $i^{\text{th}}$ position from the right ($N - 1 - i$).
2. **Inversion of Glyph:** The character itself rotates upside-down:
   - `'0'` rotates to `'0'` (Self-symmetric)
   - `'1'` rotates to `'1'` (Self-symmetric)
   - `'8'` rotates to `'8'` (Self-symmetric)
   - `'6'` rotates to `'9'` (Reciprocal pair)
   - `'9'` rotates to `'6'` (Reciprocal pair)
   - All other digits (`'2', '3', '4', '5', '7'`) are invalid.

To verify strobogrammatic symmetry without constructing a full reversed string in memory ($O(N)$ extra space), two pointers move inward from the boundaries, checking whether each left character rotates into the corresponding right character.

---

## 2. Conceptual Foundation & Invariants

### Rotational Mapping Table
Define involution $\rho$:
$$
\rho(\text{'0'}) = \text{'0'}, \quad \rho(\text{'1'}) = \text{'1'}, \quad \rho(\text{'8'}) = \text{'8'}, \quad \rho(\text{'6'}) = \text{'9'}, \quad \rho(\text{'9'}) = \text{'6'}
$$
For any other character $c$, $\rho(c) = \text{invalid}$.

The complete alphabet, with the position each glyph is allowed to occupy:

| Digit $c$ | Image $\rho(c)$ | Class | Positions it may occupy in a strobogrammatic numeral |
|:---:|:---:|:---|:---|
| `'0'` | `'0'` | Self-symmetric | Anywhere, including the center of an odd-length numeral; as the leading character only for the single-digit numeral `"0"` allowed by the contract |
| `'1'` | `'1'` | Self-symmetric | Anywhere, including the center |
| `'8'` | `'8'` | Self-symmetric | Anywhere, including the center |
| `'6'` | `'9'` | Reciprocal pair | Only as the left member of a mirror pair whose right member is `'9'`; never alone at the center of an odd-length numeral |
| `'9'` | `'6'` | Reciprocal pair | Only as the left member of a mirror pair whose right member is `'6'`; never alone at the center |
| `'2'`, `'3'`, `'4'`, `'5'`, `'7'` | invalid | Not rotatable | Nowhere: one occurrence at any index forces the answer `false` |

### Two-Pointer Inward Matching Protocol:
Initialize $L = 0, \quad R = \text{len}(\text{num}) - 1$:
While $L \le R$:
1. Check if $\text{num}[L]$ is a valid rotatable character:
   If $\text{num}[L] \notin \rho$:
   $$
   \text{return false}
   $$
2. Check if the rotated image of $\text{num}[L]$ matches $\text{num}[R]$:
   If $\rho(\text{num}[L]) \ne \text{num}[R]$:
   $$
   \text{return false}
   $$
3. Advance pointers inward:
   $$
   L \leftarrow L + 1, \quad R \leftarrow R - 1
   $$
Return `true`.

*(Crucial Invariant: The loop condition is $L \le R$, inclusive of $L == R$. This ensures the center digit of an odd-length string is tested: $\rho(c) == c$, which is satisfied only by $\{'0', '1', '8'\}$)*.

> **Invariant.** After checking pair $(L, R)$, the prefix $\text{num}[0 \dots L]$ and suffix $\text{num}[R \dots N-1]$ are guaranteed to form an exact 180-degree mirror reflection of each other.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{num} = \text{"69"}$ ($N = 2$):

### Step 1: Initialization
- String: $\text{num}[0] = \text{'6'}, \quad \text{num}[1] = \text{'9'}$.
- Pointers: $L = 0, \quad R = 1$.

---

### Step 2: Evaluate Outer Pair $(L = 0, R = 1)$
- Left character: $\text{num}[L] = \text{'6'}$.
- Right character: $\text{num}[R] = \text{'9'}$.
- Apply rotation map to left character:
  $$
  \rho(\text{'6'}) = \text{'9'}
  $$
- Compare with right character:
  $$
  \rho(\text{'6'}) == \text{num}[R] \implies \text{'9'} == \text{'9'} \quad (\mathbf{\text{Match!}})
  $$
- Advance pointers:
  $$
  L \leftarrow 0 + 1 = 1, \quad R \leftarrow 1 - 1 = 0
  $$

---

### Step 3: Termination Check
- Check loop condition: $L \le R \implies 1 \le 0$ (False).
- Loop terminates cleanly.
- **Return `true`!**

---

## 4. Complete Execution Trace

```text
num = "69"
L = 0, R = 1: num[0] = '6', num[1] = '9'
rotate('6') = '9' == num[1] -> MATCH!
L advances to 1, R to 0 -> L > R -> Return True
```

| Iteration | Left Index $L$ | Right Index $R$ | Left Char $\text{num}[L]$ | Right Char $\text{num}[R]$ | Rotated $\rho(\text{num}[L])$ | Equality Match? | Action |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| **1** | **0** | **1** | `'6'` | `'9'` | `'9'` | **Yes ('9' == '9')** | $L \leftarrow 1, R \leftarrow 0$ |
| **Finish** | 1 | 0 | - | - | - | - | **`true`** |

### Contrast: Odd-Length Self-Symmetry Failure ($\text{num} = \text{"696"}$)
- $L = 0, R = 2$: $\text{num}[0] = \text{'6'}, \text{num}[2] = \text{'6'}$.
  - $\rho(\text{'6'}) = \text{'9'} \ne \text{'6'}$.
  - Fails on step 1! Returns **`false`**.

### Contrast: Invalid Digit Rejection ($\text{num} = \text{"962"}$)
- $L = 0, R = 2$: $\text{num}[0] = \text{'9'}, \text{num}[2] = \text{'2'}$.
  - $\rho(\text{'9'}) = \text{'6'} \ne \text{'2'}$.
  - Fails on step 1! Returns **`false`**.

### Position-Pair Comparison Across Four Numerals

Reading one row per pointer step shows that the same check explains four different outcomes, and that the center step is the only place where a lone digit is compared with itself:

| Numeral | Pair $(L, R)$ | `num[L]` | `num[R]` | $\rho(\text{num}[L])$ | Decision |
|:---|:---:|:---:|:---:|:---:|:---|
| `"818"` | $(0, 2)$ | `'8'` | `'8'` | `'8'` | Images agree; pointers advance |
| `"818"` | $(1, 1)$ | `'1'` | `'1'` | `'1'` | Lone center digit maps to itself, so the whole numeral is `true` |
| `"629"` | $(0, 2)$ | `'6'` | `'9'` | `'9'` | Images agree; pointers advance to the center |
| `"629"` | $(1, 1)$ | `'2'` | `'2'` | invalid | `'2'` has no 180-degree image at all, so the center alone forces `false` |
| `"696"` | $(0, 2)$ | `'6'` | `'6'` | `'9'` | `'9' \ne '6'`; rejected before the center is ever examined |
| `"9006"` | $(0, 3)$ | `'9'` | `'6'` | `'6'` | Reciprocal pair matches; pointers advance |
| `"9006"` | $(1, 2)$ | `'0'` | `'0'` | `'0'` | Interior zero maps to itself; all pairs consumed, so `true` |

The `"629"` rows are the instructive ones: its outer pair `'6'` and `'9'` is perfectly legal, and only the inclusive loop condition $L \le R$ exposes the unrotatable `'2'` sitting at the center.

---

## 5. Algorithmic Correctness

**Soundness.** Rotation by 180 degrees sends character at index $i$ to index $N - 1 - i$, inverting its orientation. Testing $\rho(\text{num}[i]) == \text{num}[N - 1 - i]$ for all $0 \le i \le \lfloor N/2 \rfloor$ verifies the exact mathematical definition of 180-degree rotational invariance. Because $\rho$ is an involution on valid pairs ($\rho(\rho(c)) = c$), checking from left to right simultaneously proves the reverse transformation.

**Completeness.** Every character index in the string is evaluated. Because $L \le R$, odd-length center characters are evaluated against themselves, ensuring non-self-symmetric digits like `'6'` or `'9'` cannot falsely pass when placed in the center.

---

## 6. Traps This Instance Exposes

- **Skipping Center Digit ($L < R$ vs $L \le R$):** Using $L < R$ skips the center digit of odd-length strings! For example, $\text{"898"}$ has center digit `'9'`. When rotated, $\text{"898"}$ becomes $\text{"868"} \ne \text{"898"}$. Using $L \le R$ tests $\rho(\text{'9'}) == \text{'9'}$ (which evaluates to $\text{'6'} == \text{'9'} \implies \text{false}$), catching the error.
- **Symmetric Pairs Trap:** `'6'` must pair with `'9'`, never with another `'6'`. $\text{"66"}$ rotated is $\text{"99"} \ne \text{"66"}$.
- **Unnecessary String Allocations:** Reversing the string and mapping characters requires allocating a new string of length $N$. The two-pointer check uses $O(1)$ auxiliary space.

### Boundary Behaviour of the Mirror Check

| Boundary scenario | Concrete input | Required result | Why the check decides correctly |
|:---|:---|:---:|:---|
| Single self-symmetric digit | $\text{num} = \text{"0"}$ | `true` | The step $L = R = 0$ compares `'0'` with $\rho(\text{'0'}) = \text{'0'}$; this is also the only numeral the contract permits to begin with a zero |
| Single reciprocal digit | $\text{num} = \text{"6"}$ | `false` | At the center the same glyph occupies both sides, so $\rho(\text{'6'}) = \text{'9'} \ne \text{'6'}$; a reciprocal digit needs a partner, not a reflection of itself |
| Unrotatable digit at the center only | $\text{num} = \text{"629"}$ | `false` | The outer pair `'6'` and `'9'` matches, so only the inclusive condition $L \le R$ reaches the `'2'`, which has no image |
| Rotatable digits paired with the wrong partner | $\text{num} = \text{"89"}$ | `false` | Both glyphs rotate, but $\rho(\text{'8'}) = \text{'8'} \ne \text{'9'}$; rotatability of each digit is necessary and nowhere near sufficient |
| Interior zeros | $\text{num} = \text{"9006"}$ | `true` | The reverse pair `'9'` and `'6'` matches, and the interior `'0'` maps to itself, so the whole numeral is its own rotation |
| Trailing zero | $\text{num} = \text{"10"}$ | `false` | A final `'0'` would have to be the image of an initial `'0'`, which the contract forbids except for `"0"` itself; here $\rho(\text{'1'}) = \text{'1'} \ne \text{'0'}$ |
| Maximum length | $50$ copies of `'1'` | `true` | Even length means no center step is needed: the pointers execute exactly $25$ matching pairs and stop when they cross |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the number of characters in `num`. The two pointers advance toward each other, executing $\lceil N/2 \rceil$ iterations. Each step performs an $O(1)$ dictionary lookup and character comparison.
- **Auxiliary Space Complexity:** $O(1)$ auxiliary memory. The rotation mapping $\rho$ is a fixed 5-entry dictionary.
