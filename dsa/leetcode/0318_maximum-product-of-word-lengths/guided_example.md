# Guided Example: Maximum Product of Word Lengths

We trace the step-by-step bitmask integer encoding for alphabet character sets, $O(1)$ bitwise disjointness testing (`mask[i] & mask[j] == 0`), word length product accumulation, and global maximum product extraction on representative word array instances:

- **Input:** $\text{words} = [\text{"abcw"}, \text{"baz"}, \text{"foo"}, \text{"bar"}, \text{"xtfn"}, \text{"abcdef"}]$
- **Required output:** $16$
  - Disjoint pair: `"abcw"` ($\text{length} = 4$) and `"xtfn"` ($\text{length} = 4$)
  - Bitwise check: $\text{mask}(\text{"abcw"}) \ \& \ \text{mask}(\text{"xtfn"}) == 0$ (no shared letters)
  - Length product: $4 \times 4 = \mathbf{16}$
- **Multiple Disjoint Words:** `"ab"` ($\text{length} = 2$) and `"cd"` ($\text{length} = 2$) yield product $2 \times 2 = 4$
- **All Pairs Sharing Letters:** $\text{words} = [\text{"a"}, \text{"aa"}, \text{"aaa"}] \implies 0$ (all words share letter `'a'`)
- **Single Letter Disjoint Words:** $[\text{"a"}, \text{"b"}] \implies 1 \times 1 = 1$

This instance demonstrates 26-bit bitmask compression for English lowercase alphabets, proves why `(mask[i] & mask[j]) == 0` tests set disjointness in a single CPU instruction, contrasts $O(1)$ bitwise comparisons against $O(L)$ character set scans, and analyzes time and auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a list of words:
$$
\text{words} = [\text{"abcw"}, \text{"baz"}, \text{"foo"}, \text{"bar"}, \text{"xtfn"}, \text{"abcdef"}] \quad (N = 6)
$$
Find the maximum value of $\text{len}(\text{words}[i]) \times \text{len}(\text{words}[j])$ such that the two words share **zero** common letters:

```text
Pair Comparisons:
- "abcw" (len 4) and "baz" (len 3):    Share 'a', 'b' -> Incompatible
- "abcw" (len 4) and "foo" (len 3):    Disjoint! Product = 4 * 3 = 12
- "abcw" (len 4) and "bar" (len 3):    Share 'a', 'b' -> Incompatible
- "abcw" (len 4) and "xtfn" (len 4):   Disjoint! Product = 4 * 4 = 16 (MAXIMUM!)
- "abcdef" (len 6) shares letters with all other words.

Output: 16
```

### The Power of Bitwise Representation
- Checking character overlap using strings or sets for every pair of words takes $O(L)$ per pair, leading to $O(N^2 \cdot L)$ overall time.
- Because the alphabet contains only 26 lowercase English letters ($a$ through $z$), each word's distinct character set can be represented as a **single 26-bit integer**:
  $$
  \text{mask} = \sum_{c \in \text{word}} (1 \ll (\operatorname{ord}(c) - \operatorname{ord}('a')))
  $$
- Two words share no letters if and only if their bitwise AND is zero:
  $$
  \text{mask}[i] \ \& \ \text{mask}[j] == 0
  $$
  This reduces the disjointness check to a single constant-time bitwise instruction!

---

## 2. Conceptual Foundation & Invariants

### 26-Bit Integer Mapping
For each character $c \in [\text{'a'}, \dots, \text{'z'}]$:
- Bit position $b = \operatorname{ord}(c) - \operatorname{ord}('a') \in [0, 25]$.
- `mask[i] |= 1 << b`.
Duplicate characters in the same word simply set the same bit multiple times, naturally deduplicating character presence.

### Pairwise Comparison Protocol:
Iterate index $i$ from $0$ to $N - 1$:
1. Compute $\text{mask}[i]$ from the characters of $\text{words}[i]$.
2. For every prior word $j \in [0, i - 1]$:
   - If $(\text{mask}[i] \ \& \ \text{mask}[j]) == 0$:
     $$
     \text{ans} = \max(\text{ans}, \; \text{len}(\text{words}[i]) \times \text{len}(\text{words}[j]))
     $$

> **Invariant.** For any pair $(i, j)$, $(\text{mask}[i] \ \& \ \text{mask}[j]) == 0$ if and only if the set intersection of characters in $\text{words}[i]$ and $\text{words}[j]$ is empty.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on the 6 words:

---

### Step 1: $i = 0, \text{word} = \text{"abcw"}$ ($\text{len} = 4$)
- Characters: $\{a, b, c, w\} \to$ Bits: $0, 1, 2, 22$.
- $\text{mask}[0] = 2^0 + 2^1 + 2^2 + 2^{22} = 1 + 2 + 4 + 4194304 = 4194311$.
- Prior words: None. $\text{ans} = 0$.

---

### Step 2: $i = 1, \text{word} = \text{"baz"}$ ($\text{len} = 3$)
- Characters: $\{a, b, z\} \to$ Bits: $0, 1, 25$.
- $\text{mask}[1] = 2^0 + 2^1 + 2^{25} = 1 + 2 + 33554432 = 33554435$.
- Check $j = 0$ ("abcw"):
  - $\text{mask}[1] \ \& \ \text{mask}[0]$: shared bits $0, 1$ ('a', 'b').
  - Result $\ne 0$ (Incompatible).
- $\text{ans} = 0$.

---

### Step 3: $i = 2, \text{word} = \text{"foo"}$ ($\text{len} = 3$)
- Characters: $\{f, o\} \to$ Bits: $5, 14$.
- $\text{mask}[2] = 2^5 + 2^{14} = 32 + 16384 = 16416$.
- Check $j = 0$ ("abcw"):
  - $\text{mask}[2] \ \& \ \text{mask}[0] == 0$ (**Disjoint!**).
  - Product: $3 \times 4 = 12 \implies \text{ans} = \max(0, 12) = \mathbf{12}$.
- Check $j = 1$ ("baz"):
  - $\text{mask}[2] \ \& \ \text{mask}[1] == 0$ (**Disjoint!**).
  - Product: $3 \times 3 = 9 \implies \text{ans} = \max(12, 9) = 12$.

---

### Step 4: $i = 3, \text{word} = \text{"bar"}$ ($\text{len} = 3$)
- Characters: $\{a, b, r\} \to$ Bits: $0, 1, 17$.
- Check $j = 0$ ("abcw"): shares 'a', 'b'.
- Check $j = 1$ ("baz"): shares 'a', 'b'.
- Check $j = 2$ ("foo"):
  - Disjoint! Product $= 3 \times 3 = 9 \le 12$.

---

### Step 5: $i = 4, \text{word} = \text{"xtfn"}$ ($\text{len} = 4$)
- Characters: $\{f, n, t, x\} \to$ Bits: $5, 13, 19, 23$.
- Check $j = 0$ ("abcw"):
  - Characters of "abcw": $\{a, b, c, w\}$.
  - $\text{mask}[4] \ \& \ \text{mask}[0] == 0$ (**Disjoint!**).
  - Product: $4 \times 4 = \mathbf{16}$!
  - Update $\text{ans} = \max(12, 16) = \mathbf{16}$.
- Check $j = 1$ ("baz"):
  - Disjoint! Product $= 4 \times 3 = 12 \le 16$.
- Check $j = 2$ ("foo"):
  - Shares 'f' ($\text{mask} \ \& \ \text{mask} \ne 0$).
- Check $j = 3$ ("bar"):
  - Disjoint! Product $= 4 \times 3 = 12 \le 16$.

---

### Step 6: $i = 5, \text{word} = \text{"abcdef"}$ ($\text{len} = 6$)
- Characters: $\{a, b, c, d, e, f\}$.
- Tests against all earlier words:
  - vs "abcw": shares 'a', 'b', 'c'.
  - vs "baz": shares 'a', 'b'.
  - vs "foo": shares 'f'.
  - vs "bar": shares 'a', 'b'.
  - vs "xtfn": shares 'f'.
- Every pair overlaps; no product evaluated.

Final maximum product:
$$
\text{ans} = \mathbf{16}
$$

---

## 4. Complete Execution Trace

```text
words: ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]

i=0, "abcw" (len=4): mask constructed
i=1, "baz"  (len=3): vs "abcw" -> overlap ('a', 'b')
i=2, "foo"  (len=3): vs "abcw" -> disjoint -> 3 * 4 = 12
                     vs "baz"  -> disjoint -> 3 * 3 = 9
i=3, "bar"  (len=3): vs "foo"  -> disjoint -> 3 * 3 = 9
i=4, "xtfn" (len=4): vs "abcw" -> disjoint -> 4 * 4 = 16 (NEW MAX)
                     vs "baz"  -> disjoint -> 4 * 3 = 12
                     vs "bar"  -> disjoint -> 4 * 3 = 12
i=5, "abcdef":       overlaps with all prior words

Maximum Product: 16
```

| Word $i$ | Word $s$ | Length | Word $j$ | Word $t$ | Length | Bitwise AND $(\text{mask}_i \ \& \ \text{mask}_j)$ | Compatible? | Product | Global Max `ans` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | "baz" | 3 | 0 | "abcw" | 4 | $> 0$ ('a', 'b') | No | - | 0 |
| 2 | "foo" | 3 | 0 | "abcw" | 4 | $0$ | Yes | $3 \times 4 = 12$ | 12 |
| 2 | "foo" | 3 | 1 | "baz" | 3 | $0$ | Yes | $3 \times 3 = 9$ | 12 |
| 3 | "bar" | 3 | 2 | "foo" | 3 | $0$ | Yes | $3 \times 3 = 9$ | 12 |
| **4** | **"xtfn"** | **4** | **0** | **"abcw"** | **4** | **$0$** | **Yes** | **$4 \times 4 = 16$** | **$\mathbf{16}$** |
| 4 | "xtfn" | 4 | 1 | "baz" | 3 | $0$ | Yes | $4 \times 3 = 12$ | 16 |
| 4 | "xtfn" | 4 | 3 | "bar" | 3 | $0$ | Yes | $4 \times 3 = 12$ | 16 |
| 5 | "abcdef" | 6 | All | - | - | $> 0$ (all) | No | - | 16 |

---

## 5. Algorithmic Correctness

**Soundness.** Bit $k$ in $\text{mask}[i]$ is set if and only if character $\text{chr}(\operatorname{ord}('a') + k)$ occurs in $\text{words}[i]$. The bitwise AND between two masks is zero if and only if no bit is set in both masks, which precisely guarantees that the two words share no characters. Thus, any product calculated comes from a valid disjoint pair.

**Completeness.** The nested loops evaluate all pairs $0 \le j < i < N$. Since every pair of distinct words is compared, the maximum product over all mutually disjoint word pairs is guaranteed to be identified.

---

## 6. Traps This Instance Exposes

- **Repeated Characters:** Words with repeated characters (e.g. `"foo"`, `"aaaa"`) still set each unique letter bit exactly once. String length (`len(s)`) must reflect the full original word length, not the number of set bits.
- **Operator Precedence in Python:** In Python, comparison operators like `==` have higher precedence than bitwise operators like `&`. Writing `mask[i] & mask[j] == 0` evaluates as `mask[i] & (mask[j] == 0)`, which causes severe logic errors! Parentheses are strictly required: `(mask[i] & mask[j]) == 0`.
- **Zero Product Default:** If no two words are disjoint, the algorithm must return $0$. Initializing `ans = 0` guarantees this behavior.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(C + N^2)$, where $C = \sum \text{len}(\text{words}[i])$ is the total number of characters across all words, and $N$ is the number of words.
  - Constructing bitmasks takes $O(C)$ time.
  - The nested loops compare all $\frac{N(N - 1)}{2}$ pairs using $O(1)$ bitwise operations, taking $O(N^2)$ time.
- **Auxiliary Space Complexity:** $O(N)$ auxiliary memory to store the `mask` array of length $N$.
