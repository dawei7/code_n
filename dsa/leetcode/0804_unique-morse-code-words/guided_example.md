# Guided Example: Unique Morse Code Words

We trace the step-by-step International Morse Code mapping ($c \mapsto \text{morse}(c)$), concatenated transformation word generation ($T(w) = \prod \text{morse}(w[i])$), boundary concatenation collisions (e.g. `"gin"` vs `"zen"`), hash set deduplication ($S = \{ T(w) \mid w \in words \}$), and distinct transformation cardinality extraction on representative word vocabularies:

- **Input:**
  $$
  words = [\text{"gin"}, \; \text{"zen"}, \; \text{"gig"}, \; \text{"msg"}]
  $$
- **Required output:** `2`
  - Morse code transformation specifications:
    - The 26 lowercase English letters are mapped to Morse sequences of dots (`.`) and dashes (`-`):
      - `'a' \to \text{".-"}`
      - `'e' \to \text{"."}`
      - `'g' \to \text{"--."}`
      - `'i' \to \text{".."}`
      - `'m' \to \text{"--"}`
      - `'n' \to \text{"-."}`
      - `'s' \to \text{"..."}`
      - `'z' \to \text{"--.."}`
    - The transformation of a word is the concatenation of the Morse codes of its letters in order:
      $$
      T(w) = \text{morse}(w_0) \cdot \text{morse}(w_1) \cdots \text{morse}(w_{k-1})
      $$
    - Because letters are concatenated without spaces or delimiters, different words can produce **identical** Morse sequences (collisions).
    - Objective: Count the number of **unique** Morse transformations across all words.
    - For the input array:
      - `"gin"` $\implies \text{"--."} + \text{".."} + \text{"-."} = \mathbf{\text{"--...-."}}$
      - `"zen"` $\implies \text{"--.."} + \text{"."} + \text{"-."} = \mathbf{\text{"--...-."}}$ (Identical!)
      - `"gig"` $\implies \text{"--."} + \text{".."} + \text{"--."} = \mathbf{\text{"--...--."}}$
      - `"msg"` $\implies \text{"--"} + \text{"..."} + \text{"--."} = \mathbf{\text{"--...--."}}$ (Identical!)
      - Unique representations: $\{\text{"--...-."}, \; \text{"--...--."}\}$.
      - Distinct count is **2**.
- **Morphism Concatenation & Set Cardinality Invariant:**
  - **The Free Monoid Homomorphism:**
    - Let $\Sigma = \{a, b, \dots, z\}$ and $\Delta = \{., -\}$.
    - The Morse map is a monoid homomorphism $h: \Sigma^* \to \Delta^*$:
      $$
      h(uv) = h(u) \cdot h(v)
      $$
    - Because the Morse code is **not prefix-free** and contains no inter-character spaces, $h$ is **not injective**.
    - Distinct words can collide under $h$:
      $$
      h(\text{"gin"}) = h(\text{"zen"})
      $$
  - **Deduplication via Hash Set:**
    - Construct the image set:
      $$
      S = \{ h(w) \mid w \in words \}
      $$
    - Cardinality $|S|$ gives the exact number of distinct transformations in $\mathcal{O}(\sum |w_i|)$ time.
- **Step-by-Step Worked Execution Trace on the 4-Word Vocabulary:**
  - Initialize empty hash set: $S = \emptyset$.
  - **Word 1: `"gin"`:**
    - Letters: `'g'`, `'i'`, `'n'`.
      - `'g'` $\to \text{"--."}$
      - `'i'` $\to \text{".."}$
      - `'n'` $\to \text{"-."}$
    - Concatenate:
      $$
      T(\text{"gin"}) = \text{"--."} + \text{".."} + \text{"-."} = \mathbf{\text{"--...-."}}
      $$
    - Insert into set:
      $$
      S \leftarrow \{ \text{"--...-."} \} \quad (|S| = 1)
      $$
  - **Word 2: `"zen"`:**
    - Letters: `'z'`, `'e'`, `'n'`.
      - `'z'` $\to \text{"--.."}$
      - `'e'` $\to \text{"."}$
      - `'n'` $\to \text{"-."}$
    - Concatenate:
      $$
      T(\text{"zen"}) = \text{"--.."} + \text{"."} + \text{"-."} = \mathbf{\text{"--...-."}}
      $$
    - Set already contains $\text{"--...-."} \implies \mathbf{Collision\ Detected!}$
    - Set remains unchanged:
      $$
      S = \{ \text{"--...-."} \} \quad (|S| = 1)
      $$
  - **Word 3: `"gig"`:**
    - Letters: `'g'`, `'i'`, `'g'`.
      - `'g'` $\to \text{"--."}$
      - `'i'` $\to \text{".."}$
      - `'g'` $\to \text{"--."}$
    - Concatenate:
      $$
      T(\text{"gig"}) = \text{"--."} + \text{".."} + \text{"--."} = \mathbf{\text{"--...--."}}
      $$
    - Insert new transformation into set:
      $$
      S \leftarrow \{ \text{"--...-."}, \; \mathbf{\text{"--...--."}} \} \quad (|S| = 2)
      $$
  - **Word 4: `"msg"`:**
    - Letters: `'m'`, `'s'`, `'g'`.
      - `'m'` $\to \text{"--"}$
      - `'s'` $\to \text{"..."}$
      - `'g'` $\to \text{"--."}$
    - Concatenate:
      $$
      T(\text{"msg"}) = \text{"--"} + \text{"..."} + \text{"--."} = \mathbf{\text{"--...--."}}
      $$
    - Set already contains $\text{"--...--."} \implies \mathbf{Collision\ Detected!}$
    - Set remains unchanged:
      $$
      S = \{ \text{"--...-."}, \; \text{"--...--."} \} \quad (|S| = 2)
      $$
  - **Output Result:**
    - Final set size:
      $$
      ans = |S| = \mathbf{2}
      $$
- **Letter Boundary Ambiguity Trace ($words = [\text{"a"}, \text{"et"}]$):**
  - `"a"`: $\text{morse}(\text{'a'}) = \text{".-"}$.
  - `"et"`: $\text{morse}(\text{'e'}) + \text{morse}(\text{'t'}) = \text{"."} + \text{"-"} = \text{".-"}$.
  - A 1-letter word and a 2-letter word produce the exact same Morse code!
  - Set size: **1**.
- **Single Word Array ($words = [\text{"code"}]$):**
  - Only 1 word $\implies$ set size is always **1**.

This instance demonstrates free monoid non-injective homomorphisms and prefix code ambiguity, mathematically proves why omitting synchronization symbols creates non-trivial kernel congruence classes, and derives $O(\sum |w_i|)$ execution time and $O(\sum |w_i|)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a list of words:
Convert each word to Morse code (without spaces) and count the **number of unique transformations**.

```text
words = [ "gin", "zen", "gig", "msg" ]

Transformations:
  "gin" -> "--." + ".." + "-."   = "--...-."
  "zen" -> "--.." + "." + "-."   = "--...-."  (Collides with "gin"!)
  "gig" -> "--." + ".." + "--."  = "--...--."
  "msg" -> "--" + "..." + "--."  = "--...--." (Collides with "gig"!)

Unique Morse strings:
  1. "--...-."
  2. "--...--."

Result: 2
```

### The Invariant of the Non-Injective Code
- Without spaces between letters, Morse code is ambiguous: multiple words map to the exact same dot-dash string.
- Using a hash set to collect $T(w)$ automatically filters duplicate representations in linear time.

---

## 2. Conceptual Foundation & Invariants

### 1. Homomorphic String Encoding:
$$
T(w) = \prod_{c \in w} \text{Morse}[c]
$$

### 2. Set Deduplication Metric:
$$
ans = |\{ T(w) \mid w \in words \}|
$$

> **Monoid Quotient Invariant.** The Morse substitution induces an equivalence relation $u \sim v \iff h(u) = h(v)$ on $\Sigma^*$. The quotient set $(words / \sim)$ is measured by inserting evaluated words into a hash table.

---

## 3. Step-by-Step Worked Execution

We trace $words = [\text{"gin"}, \text{"zen"}, \text{"gig"}, \text{"msg"}]$:

---

### Step 1: `"gin"`
- `"--...-."` $\implies$ added to set. Size = 1.

---

### Step 2: `"zen"`
- `"--...-."` $\implies$ already in set (collision). Size = 1.

---

### Step 3: `"gig"`
- `"--...--."` $\implies$ added to set. Size = 2.

---

### Step 4: `"msg"`
- `"--...--."` $\implies$ already in set (collision). Size = 2.

---

### Step 5: Output
$$
\mathbf{2}
$$

---

## 4. Complete Execution Trace

| Word $w$ | Letters Processed | Morse Concatenation $T(w)$ | Already in Set? | Set Size $\lvert S \rvert$ |
|:---:|:---:|:---:|:---:|:---:|
| `"gin"` | `'g'`, `'i'`, `'n'` | `"--...-."` | No (New) | $1$ |
| `"zen"` | `'z'`, `'e'`, `'n'` | `"--...-."` | Yes (Collision) | $1$ |
| `"gig"` | `'g'`, `'i'`, `'g'` | `"--...--."` | No (New) | $2$ |
| **`"msg"`** | **`'m'`, `'s'`, `'g'`** | **`"--...--."`** | **Yes (Collision)** | **`2`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Word ($[\text{"a"}]$):** 1 unique code $\implies 1$.
- **All Distinct Words:** No collisions $\implies ans = |words|$.
- **All Identical Words ($[\text{"a"}, \text{"a"}, \text{"a"}]$):** Set deduplicates to 1.
- **Varying Length Collisions ($"a"$ vs $"et"$):** Non-prefix nature causes collisions across words of different lengths $\implies 1$.

---

## 6. Traps & Common Anti-Patterns

- **Searching in a List Instead of a Hash Set ($O(W^2 \cdot L)$):** Checking `if morse in list` takes linear time per word, causing quadratic performance. A hash set checks membership in $O(L)$ average time.
- **Hardcoding Letter Indexing Incorrectly:** Offset `'a'` using `ord(c) - ord('a')` ensures safe 0-to-25 array indexing.
- **Allocating Intermediate Substrings Repeatedly:** Use list comprehension `"".join(codes[ord(c) - 97] for c in w)` for optimal allocation.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N$ be the number of words, and $L$ the maximum word length.
  - Converting each word takes $\mathcal{O}(L)$ operations.
  - Hashing and set insertion takes $\mathcal{O}(L)$.
  - Total Time: strictly linear in total input characters $\mathcal{O}(\sum |w_i|)$ where $\sum |w_i| \le 1200$. Completes in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(\sum |w_i|)$ memory to store unique Morse strings in the hash set.
