# Guided Example: Longest Palindrome by Concatenating Two Letter Words

We trace the step-by-step execution of the optimal frequency-matching and central-pivot greedy approach on a representative problem instance:

- **Input Words (`words`):** `["lc", "cl", "gg"]`
- **Expected Output:** `6`

This instance illustrates the structural distinction between asymmetric two-letter word pairs and self-palindromic symmetric words, demonstrating how bilateral pairing and a single central pivot maximize the overall palindrome length.

---

## 1. Problem Overview & Representative Instance

We are given an array of strings `words`, where each string consists of exactly two lowercase English letters. We may select a subset of these words and concatenate them in any order to form a palindrome. Each word in the input may be selected at most once. We must determine the maximum length of such a palindrome.

Consider our representative instance `words = ["lc", "cl", "gg"]`:
- Word `"lc"` has reverse `"cl"`. Placing `"lc"` on the left and `"cl"` on the right forms the symmetric frame `"lc...cl"` (contributing $4$ characters).
- Word `"gg"` has identical letters ($g = g$). It is inherently self-palindromic and can be placed in the dead center between `"lc"` and `"cl"`, yielding `"lcggcl"` (contributing $2$ characters).
- The total length is $4 + 2 = 6$.

---

## 2. Mathematical & Algorithmic Principles

### Bipartite Symmetry Classification
Let each word $w = c_1 c_2$ be classified by its symmetry:
1. **Asymmetric Words ($c_1 \ne c_2$):**
   - The reversed word $w^R = c_2 c_1$ is distinct from $w$.
   - Neither $w$ nor $w^R$ can sit at the exact center of a palindrome because neither is individually palindromic.
   - They can only appear as matching pairs $(w, w^R)$ on opposite sides of the palindrome:

$$\text{Pairs}(w, w^R) = \min(\text{count}(w), \text{count}(w^R))$$

   - Each pair contributes $2 \times 2 = 4$ characters.
2. **Symmetric Words ($c_1 = c_2$):**
   - The word is self-palindromic ($w = w^R$, such as `"gg"`, `"aa"`).
   - If $\text{count}(w) = k$, we can form $\lfloor k / 2 \rfloor$ symmetric pairs placed on opposite sides, contributing $4 \lfloor k / 2 \rfloor$ characters.
   - If $k$ is odd ($k \bmod 2 = 1$), one instance of $w$ remains unmatched. At most **one** such leftover symmetric word across the entire vocabulary can be placed in the exact center of the palindrome, contributing $+2$ characters.

### Greedy Length Synthesis
The maximal palindrome length is expressed in closed form:

$$\text{Length} = 4 \sum_{\{u, v\}, u < v, u = v^R} \min(C_u, C_v) + 4 \sum_{w = w^R} \left\lfloor \frac{C_w}{2} \right\rfloor + 2 \cdot \mathbb{I}\left(\exists w = w^R \text{ s.t. } C_w \equiv 1 \pmod 2\right)$$

where $C_w$ denotes the occurrence count of word $w$.

| Word Type | Internal Symmetry | Contribution Rule | Length Contribution per Unit |
|---|---|---|---|
| Asymmetric Pair | $c_1 \ne c_2$ and $w^R \ne w$ | Bilateral placement $(w \dots w^R)$ | $4$ characters per matched pair |
| Symmetric Even | $c_1 = c_2$ | Bilateral placement $(w \dots w)$ | $4$ characters per pair ($2$ words) |
| Symmetric Center | $c_1 = c_2$ | Central placement $(\dots w \dots)$ | $2$ characters (at most one word) |

---

## 3. Step-by-Step Walkthrough with Intermediate State

Input words: `["lc", "cl", "gg"]`.

### Phase 1: Frequency Histogram Construction
We construct the frequency table:
- $\text{count}["lc"] = 1$
- $\text{count}["cl"] = 1$
- $\text{count}["gg"] = 1$

Initialize cumulative length $L = 0$, central odd pivot available $\text{has\_center} = \text{false}$.

### Phase 2: Processing Asymmetric Pair `("lc", "cl")`
- Word $w = \text{"lc"}$ has reverse $w^R = \text{"cl"}$.
- Check: letters differ ($'l' \ne 'c'$).
- Calculate matched pairs:

$$\min(\text{count}["lc"], \text{count}["cl"]) = \min(1, 1) = 1$$

- Characters contributed: $1 \times 4 = 4$.
- Running length: $L \leftarrow 0 + 4 = 4$.

### Phase 3: Processing Symmetric Word `"gg"`
- Letters agree ($'g' = 'g'$).
- Occurrence count: $k = 1$.
- Bilateral pairs: $\lfloor 1 / 2 \rfloor = 0$.
- Remainder check: $1 \bmod 2 = 1$.
- Because an unused symmetric word is available, we set $\text{has\_center} = \text{true}$.

### Phase 4: Assembly of Final Length
- Cumulative bilateral length: $L = 4$.
- Central pivot bonus: since $\text{has\_center} = \text{true}$, we add $2$ characters.
- Final maximum length: $4 + 2 = 6$.
- Constructed example palindrome: `"lc"` $+$ `"gg"` $+$ `"cl"` $=$ `"lcggcl"`.

---

## 4. Comprehensive State Trace

The evaluation metrics across all unique word tokens are detailed below:

| Word $w$ | Reverse $w^R$ | Symmetry Type | Count $C_w$ | Count $C_{w^R}$ | Bilateral Pairs Formed | Characters Added | Center Eligible? |
|---|---|---|---|---|---|---|---|
| `"lc"` | `"cl"` | Asymmetric | $1$ | $1$ | $1$ | $4$ | No |
| `"gg"` | `"gg"` | Symmetric | $1$ | $1$ | $0$ | $0$ | Yes (Odd remainder) |

### Center Resolution
| Central Candidate Available? | Center Character Bonus Added | Final Concatenated Length |
|---|---|---|
| Yes (`"gg"`) | $+2$ | $4 + 2 = 6$ |

Maximum length achieved: $6$.

---

## 5. Algorithmic Correctness & Soundness

**Soundness.** Any valid palindrome reads identically forwards and backwards. Characters at index $j$ and index $N - 1 - j$ must match. For 2-letter words, this implies that words at symmetrical positions from the ends must be mutual reverses. Asymmetric words must appear in equal numbers on both sides, yielding $\min(C_w, C_{w^R})$ pairs. Symmetric words can be paired with themselves across the center. If an unmatched symmetric word exists, placing it at the exact center creates a 2-character middle whose internal reflection is self-consistent ($c_1 c_2 = c_1 c_1$). Because only one 2-character middle can exist in any string, at most one odd symmetric word can contribute $+2$.

**Completeness.** No palindrome can include more copies of an asymmetric pair than $\min(C_w, C_{w^R})$, nor more than $\lfloor C_w / 2 \rfloor$ pairs of a symmetric word, nor more than one central pivot. Because each upper bound is saturated and all components are arranged into a valid palindrome, the resulting length is provably maximal.

---

## 6. Edge Cases & Anti-Patterns

- **Multiple Odd Symmetric Words:** If words contains `"aa"`, `"bb"`, `"cc"`, each with count 1, all bilateral pair counts are 0. Exactly one of them can serve as the center, yielding length $2$ (not $6$).
- **No Symmetric Words:** If all words are asymmetric, the central pivot bonus is $0$, and the length is solely the sum of matched asymmetric pairs.
- **Unbalanced Asymmetric Frequencies:** If `"ab"` appears 5 times and `"ba"` appears 2 times, exactly 2 pairs can be formed, yielding $2 \times 4 = 8$ characters; the remaining 3 copies of `"ab"` cannot be used.
- **Anti-Pattern — Exponential Permutation Search:** Generating subsets and testing palindromic property takes exponential time $\mathcal{O}(2^N \cdot N!)$. The frequency table reduces the problem to an $\mathcal{O}(N)$ counting pass.

---

## 7. Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$, where $N$ is the number of words in `words`. Counting frequencies takes $\mathcal{O}(N)$ time. Because the lowercase English alphabet contains 26 letters, there are at most $26^2 = 676$ distinct two-letter combinations. Processing the hash table takes at most $\mathcal{O}(26^2) = \mathcal{O}(1)$ time. Overall time is strictly linear $\mathcal{O}(N)$.
- **Auxiliary Space Complexity:** $\mathcal{O}(1)$ auxiliary space, bounded by the maximum possible 676 entries in the frequency map.
