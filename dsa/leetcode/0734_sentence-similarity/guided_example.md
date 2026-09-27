# Guided Example: Sentence Similarity

We trace the step-by-step sentence length equality validation ($|sentence_1| == |sentence_2|$), symmetric similarity relation encoding in a hash set ($s = \{(x, y)\}$), position-by-position pairwise word comparison ($zip(sentence_1, sentence_2)$), reflexive self-similarity ($x == y$), symmetric pair membership testing ($(x, y) \in s \lor (y, x) \in s$), and non-transitive similarity verification on representative sentence pairs:

- **Input:**
  $$
  sentence_1 = [\text{"great"}, \; \text{"acting"}, \; \text{"skills"}]
  $$
  $$
  sentence_2 = [\text{"fine"}, \; \text{"drama"}, \; \text{"talent"}]
  $$
  $$
  similarPairs = [[\text{"great"}, \text{"fine"}], \; [\text{"drama"}, \text{"acting"}], \; [\text{"skills"}, \text{"talent"}]]
  $$
- **Required output:** `true`
  - Similarity specifications:
    - Two sentences are similar if and only if:
      1. They have the **exact same number of words** ($|sentence_1| == |sentence_2|$).
      2. For every position $i$, the word $sentence_1[i]$ is similar to $sentence_2[i]$.
    - Similarity relation properties:
      - **Reflexive:** Every word is automatically similar to itself ($w \sim w$).
      - **Symmetric:** If $x \sim y$, then $y \sim x$ (order in $similarPairs$ does not matter).
      - **Non-Transitive:** In Sentence Similarity I, similarity is strictly direct; $a \sim b$ and $b \sim c$ does **not** imply $a \sim c$.
    - For the input:
      - Position 0: `"great"` and `"fine"` form a declared pair $\implies$ valid.
      - Position 1: `"acting"` and `"drama"` form a declared pair (listed as `["drama", "acting"]`, symmetric) $\implies$ valid.
      - Position 2: `"skills"` and `"talent"` form a declared pair $\implies$ valid.
      - All 3 positions valid $\implies$ output is **`true`**.
- **Pairwise Symmetry & Set Lookup Invariant:**
  - **Sentence Length Gate:**
    - If $|sentence_1| \ne |sentence_2|$, the sentences have differing word counts and can never be similar $\implies$ return `false` immediately.
  - **Symmetric Hash Set ($s$):**
    - Store all given pairs in a hash set:
      $$
      s = \{ (x, y) \mid [x, y] \in similarPairs \}
      $$
  - **Positional Similarity Predicate:**
    - For each aligned pair $(x, y) = (sentence_1[i], sentence_2[i])$:
      - Criterion 1 (Reflexivity): $x == y$ (same word).
      - Criterion 2 (Direct Pair): $(x, y) \in s$.
      - Criterion 3 (Symmetric Pair): $(y, x) \in s$.
    - If a pair satisfies none of these three conditions:
      $$
      x \ne y \ \land \ (x, y) \notin s \ \land \ (y, x) \notin s \implies \mathbf{Return\ False!}
      $$
    - If all pairs satisfy the predicate, return `true`.
- **Step-by-Step Worked Execution Trace on the Sample Sentences:**
  - **Phase 0: Length Verification:**
    $$
    |sentence_1| = 3, \quad |sentence_2| = 3 \quad \mathbf{(Lengths\ Match)}
    $$
  - **Phase 1: Build Similarity Set:**
    - Given pairs:
      $$
      s = \{ (\text{"great"}, \text{"fine"}), \; (\text{"drama"}, \text{"acting"}), \; (\text{"skills"}, \text{"talent"}) \}
      $$
  - **Phase 2: Aligned Word-by-Word Inspection:**
    - **Position $i = 0$ ($x = \text{"great"}, y = \text{"fine"}$):**
      - Check identity: $\text{"great"} \ne \text{"fine"}$.
      - Check set membership:
        $$
        (\text{"great"}, \text{"fine"}) \in s \quad \mathbf{(Direct\ Match!)}
        $$
      - Valid.
    - **Position $i = 1$ ($x = \text{"acting"}, y = \text{"drama"}$):**
      - Check identity: $\text{"acting"} \ne \text{"drama"}$.
      - Check forward: $(\text{"acting"}, \text{"drama"}) \notin s$.
      - Check reverse (symmetry):
        $$
        (\text{"drama"}, \text{"acting"}) \in s \quad \mathbf{(Symmetric\ Match!)}
        $$
      - Valid.
    - **Position $i = 2$ ($x = \text{"skills"}, y = \text{"talent"}$):**
      - Check identity: $\text{"skills"} \ne \text{"talent"}$.
      - Check set membership:
        $$
        (\text{"skills"}, \text{"talent"}) \in s \quad \mathbf{(Direct\ Match!)}
        $$
      - Valid.
  - **Phase 3: Final Decision:**
    - Every position satisfies the similarity predicate.
    - Output:
      $$
      ans = \mathbf{true}
      $$
- **Different Length Sentences ($sentence_1 = [\text{"a"}], sentence_2 = [\text{"a"}, \text{"b"}]$):**
  - $|sentence_1| = 1 \ne |sentence_2| = 2$.
  - Fails length check immediately $\implies$ returns **`false`**.
- **Non-Transitive Counter-Example Trace:**
  - $similarPairs = [[\text{"great"}, \text{"fine"}], [\text{"fine"}, \text{"good"}]]$
  - Words compared: $x = \text{"great"}, y = \text{"good"}$.
  - Pair $(\text{"great"}, \text{"good"})$ is neither identical nor directly present in $s$.
  - In Sentence Similarity I, returns **`false`** (Transitivity is not recognized!).

This instance demonstrates symmetric binary relation verification and Cartesian product hash set lookups, mathematically proves why reflexivity and symmetry without transitive closure characterize direct matching, and derives $O(N + P)$ execution time and $O(P)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given two sentences and a list of word pairs:
Determine if the sentences are **similar**.
Sentences are similar if they have the same length and words at each index are:
1. Identical ($x == y$), OR
2. Form a pair in $similarPairs$ in either order.
**Note:** Similarity is NOT transitive here!

```text
sentence1 = [ "great", "acting", "skills" ]
sentence2 = [ "fine",  "drama",  "talent" ]
pairs = [ ["great", "fine"], ["drama", "acting"], ["skills", "talent"] ]

i = 0: ("great", "fine")   in pairs -> YES
i = 1: ("acting", "drama") reversed in pairs ("drama", "acting") -> YES
i = 2: ("skills", "talent") in pairs -> YES

All positions valid!
Result: true
```

### The Invariant of Symmetric Direct Lookup
- Two words are similar if $x == y$ or $(x, y) \in s$ or $(y, x) \in s$.
- Pre-populating a hash set with all given pairs allows $O(1)$ verification for each word position.

---

## 2. Conceptual Foundation & Invariants

### 1. Hash Set of Relations:
$$
s = \{ (x, y) \mid [x, y] \in similarPairs \}
$$

### 2. Positional Predicate:
$$
\text{similar}(x, y) \iff (x == y) \ \lor \ ((x, y) \in s) \ \lor \ ((y, x) \in s)
$$
$$
ans = (|sentence_1| == |sentence_2|) \ \land \ \bigwedge_{i=0}^{n-1} \text{similar}(sentence_1[i], sentence_2[i])
$$

> **Symmetric Binary Relation Invariant.** The similarity predicate $\sim$ is the reflexive symmetric closure of the given edge set $E \subset V \times V$, defined by $x \sim y \iff x = y \lor (x, y) \in E \lor (y, x) \in E$, resolvable in constant time per query via hash set membership.

---

## 3. Step-by-Step Worked Execution

We trace the sample data:

---

### Step 1: Length
- Both sentences have length 3.

---

### Step 2: Index-by-Index Inspection
- $i = 0$: `("great", "fine")` $\in s \implies$ Valid.
- $i = 1$: `("drama", "acting")` $\in s \implies$ Valid.
- $i = 2$: `("skills", "talent")` $\in s \implies$ Valid.

---

### Step 3: Output
$$
\mathbf{true}
$$

---

## 4. Complete Execution Trace

| Position $i$ | $sentence_1[i]$ | $sentence_2[i]$ | Identical? | Forward Pair in $s$? | Reverse Pair in $s$? | Position Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | `"great"` | `"fine"` | No | **Yes** | — | Valid |
| $1$ | `"acting"` | `"drama"` | No | No | **Yes** | Valid |
| **$2$** | **`"skills"`** | **`"talent"`** | **No** | **Yes** | **—** | **Valid** |
| **Final** | — | — | — | — | — | **Result: `true`** |

---

## 5. Boundary Cases & Failure Modes

- **Different Lengths:** Fails immediately $\implies$ returns `false`.
- **Identical Sentences with Empty Pairs:** $x == y$ at every index $\implies$ returns `true`.
- **Unmatched Words:** Any index failing all 3 checks $\implies$ returns `false`.
- **Transitive Chains ($a \sim b, b \sim c$ without direct $a \sim c$):** Returns `false`.

---

## 6. Traps & Common Anti-Patterns

- **Assuming Transitivity:** Assuming that if $A \sim B$ and $B \sim C$ then $A \sim C$ is incorrect for Sentence Similarity I. Only direct pairs (and their symmetric inverses) are valid. Transitivity belongs to Sentence Similarity II.
- **Checking Only Forward Pairs ($(x, y)$):** The problem states that if $x$ is similar to $y$, then $y$ is similar to $x$. Must check both `(x, y) in s` and `(y, x) in s`.
- **Forgetting Identity Check ($x == y$):** Words that are identical (e.g. `"the"` and `"the"`) might not be explicitly listed in $similarPairs$, but are always similar. Check `if x == y:` first.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Inserting $P$ pairs into hash set: $\mathcal{O}(P)$.
  - Comparing $N$ word positions: $N \times \mathcal{O}(1) = \mathcal{O}(N)$.
  - Total Time: strictly linear $\mathcal{O}(N + P)$. Completes in $< 1$ ms for $N, P \le 1000$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(P)$ space to store the pair tuples in the hash set.
