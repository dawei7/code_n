# Guided Example: Group Anagrams

We trace the step-by-step hash-based anagram bucket categorization on a representative word list instance:

- **Input:** $\text{strs} = [\text{"eat"}, \text{"tea"}, \text{"tan"}, \text{"ate"}, \text{"nat"}, \text{"bat"}]$
- **Required output:** $[[\text{"eat"}, \text{"tea"}, \text{"ate"}], \, [\text{"tan"}, \text{"nat"}], \, [\text{"bat"}]]$

This instance demonstrates defining a canonical hashable signature for multiset letter equality (sorted string or 26-element character count tuple), streaming dictionary bucket accumulation, and emitting equivalence classes in $O(N \cdot K)$ time.

---

## 1. Instance & Teaching Goal

Given an array of $N = 6$ strings:
$$
[\text{"eat"}, \text{"tea"}, \text{"tan"}, \text{"ate"}, \text{"nat"}, \text{"bat"}]
$$
where the maximum string length is $K = 3$, group all anagrams together. Two strings are anagrams if and only if they contain the exact same characters with identical frequencies.

A naive pair-wise comparison compares every string against every other string in $O(N^2 \cdot K)$ time. By transforming each string into a canonical signature that is invariant under character permutation, we map anagrams to the same hash table bucket in a single pass.

---

## 2. Conceptual Foundation & Invariants

### Signature Formulations
Two primary methods exist to generate an anagram signature:

1. **Sorted Character String ($O(K \log K)$ per word):**
   Sort the characters of word $s$ alphabetically:
   $$
   \text{key} = \text{sort}(s)
   $$
   - $\text{"eat"}, \text{"tea"}, \text{"ate"} \longmapsto \text{"aet"}$
   - $\text{"tan"}, \text{"nat"} \longmapsto \text{"ant"}$
   - $\text{"bat"} \longmapsto \text{"abt"}$

2. **Character Frequency Vector ($O(K)$ per word):**
   Count the frequency of each lowercase English letter in a 26-tuple:
   $$
   \text{count} = [c_a, c_b, \dots, c_z]
   $$
   - For $\text{"eat"}$: $(a:1, e:1, t:1, \text{others}:0)$.
   Since tuples are immutable and hashable in Python, `tuple(count)` serves as an exact $O(K)$ hash key.

### Grouping Mechanism
We maintain a hash map $M: \text{Key} \to \text{List[String]}$:
- For each word $s \in \text{strs}$:
  - Compute signature $k$.
  - Append original word $s$ to bucket $M[k]$.
- Return the collection of all bucket lists: $\text{list}(M.\text{values}())$.

> **Invariant.** After processing string $s$, all words residing in bucket $M[k]$ are mutual anagrams of each other, and no anagram of $s$ can reside in any other bucket.

---

## 3. Step-by-Step Worked Execution

We trace the hash map state as each string in $[\text{"eat"}, \text{"tea"}, \text{"tan"}, \text{"ate"}, \text{"nat"}, \text{"bat"}]$ is ingested:

- **Word 1: $\text{"eat"}$**
  - Character decomposition: $\{a: 1, e: 1, t: 1\}$.
  - Sorted key: $\text{"aet"}$.
  - Lookup $\text{"aet"}$ in map: New key! Initialize bucket.
  - Bucket state:
    $$
    \text{"aet"} \longrightarrow [\text{"eat"}]
    $$

- **Word 2: $\text{"tea"}$**
  - Character decomposition: $\{a: 1, e: 1, t: 1\}$.
  - Sorted key: $\text{"aet"}$.
  - Lookup $\text{"aet"}$: Key exists! Append $\text{"tea"}$.
  - Bucket state:
    $$
    \text{"aet"} \longrightarrow [\text{"eat"}, \text{"tea"}]
    $$

- **Word 3: $\text{"tan"}$**
  - Character decomposition: $\{a: 1, n: 1, t: 1\}$.
  - Sorted key: $\text{"ant"}$.
  - Lookup $\text{"ant"}$: New key! Initialize bucket.
  - Bucket state:
    $$
    \text{"ant"} \longrightarrow [\text{"tan"}]
    $$

- **Word 4: $\text{"ate"}$**
  - Sorted key: $\text{"aet"}$.
  - Lookup $\text{"aet"}$: Key exists! Append $\text{"ate"}$.
  - Bucket state:
    $$
    \text{"aet"} \longrightarrow [\text{"eat"}, \text{"tea"}, \text{"ate"}]
    $$

- **Word 5: $\text{"nat"}$**
  - Sorted key: $\text{"ant"}$.
  - Lookup $\text{"ant"}$: Key exists! Append $\text{"nat"}$.
  - Bucket state:
    $$
    \text{"ant"} \longrightarrow [\text{"tan"}, \text{"nat"}]
    $$

- **Word 6: $\text{"bat"}$**
  - Sorted key: $\text{"abt"}$.
  - Lookup $\text{"abt"}$: New key! Initialize bucket.
  - Bucket state:
    $$
    \text{"abt"} \longrightarrow [\text{"bat"}]
    $$

All strings processed. Extracting values yields 3 groups:
$$
[[\text{"eat"}, \text{"tea"}, \text{"ate"}], \, [\text{"tan"}, \text{"nat"}], \, [\text{"bat"}]]
$$

---

## 4. Complete Execution Trace

| Step | Current Word $s$ | Computed Canonical Key | Key Exists in Map? | Target Bucket State After Insertion |
|:---:|:---:|:---:|:---:|:---|
| 1 | `"eat"` | `"aet"` | No (New) | `{"aet": ["eat"]}` |
| 2 | `"tea"` | `"aet"` | Yes | `{"aet": ["eat", "tea"]}` |
| 3 | `"tan"` | `"ant"` | No (New) | `{"aet": [...], "ant": ["tan"]}` |
| 4 | `"ate"` | `"aet"` | Yes | `{"aet": ["eat", "tea", "ate"], "ant": ["tan"]}` |
| 5 | `"nat"` | `"ant"` | Yes | `{"aet": [...], "ant": ["tan", "nat"]}` |
| 6 | `"bat"` | `"abt"` | No (New) | `{"aet": [...], "ant": [...], "abt": ["bat"]}` |

---

## 5. Algorithmic Correctness

**Soundness.** A bucket key uniquely identifies the multiset of characters in a string. Two strings produce the exact same key if and only if they are permutations of one another. Hence, every group emitted by the hash map consists strictly of mutual anagrams.

**Completeness.** Every string in $\text{strs}$ is mapped to its unique canonical key and appended to the corresponding bucket. Since the hash map preserves all original words, no input string is lost or misclassified.

---

## 6. Traps This Instance Exposes

- **Mutating the Input Word:** Storing the sorted string in the result instead of the original string violates the contract. The key is used only for hash map indexing; the original un-sorted word must be appended to the bucket.
- **Mutable Keys in Hash Maps:** Using a list `[0]*26` directly as a dictionary key causes a runtime `TypeError: unhashable type: 'list'`. Converting the count to an immutable tuple `tuple(count)` makes it hashable.
- **Empty Strings and Single Letters:** An empty string `""` has canonical key `""`. Single letters `"a"` have key `"a"`. Both are handled uniformly by sorting or count tuples without special casing.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - With Sorting: $O(N \cdot K \log K)$, where $N$ is the number of strings and $K$ is the maximum string length.
  - With 26-tuple Frequency Counting: $O(N \cdot K)$. Counting frequencies takes $O(K)$ time per word, and hashing a 26-element tuple takes $O(26) = O(1)$ time.
- **Auxiliary Space Complexity:** $O(N \cdot K)$ to store the hash map containing all words and signatures.
