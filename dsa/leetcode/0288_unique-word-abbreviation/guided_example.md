# Guided Example: Unique Word Abbreviation

We trace the step-by-step word abbreviation generation ($s[0] + \text{str}(\text{len}(s) - 2) + s[-1]$), dictionary hash map grouping into unique word sets, and dual-clause uniqueness verification on representative dictionary queries:

- **Input:** $\text{dictionary} = [\text{"deer"}, \text{"door"}, \text{"cake"}, \text{"card"}]$; queries: `["dear", "cart", "cane", "make", "cake"]`
- **Required output:** `[false, true, false, true, true]`
  - `isUnique("dear")` $\implies$ `false` (Abbreviation `"d2r"` matches dictionary words `"deer"` and `"door"`)
  - `isUnique("cart")` $\implies$ `true` (Abbreviation `"c2t"` does not exist anywhere in dictionary)
  - `isUnique("cane")` $\implies$ `false` (Abbreviation `"c2e"` matches dictionary word `"cake"`)
  - `isUnique("make")` $\implies$ `true` (Abbreviation `"m2e"` does not exist in dictionary)
  - `isUnique("cake")` $\implies$ `true` (Abbreviation `"c2e"` matches only `"cake"` itself in dictionary)
- **Duplicate Dictionary Entries:** $\text{dictionary} = [\text{"a", "a"}]$; query `"a"` $\implies$ `true` (Deduplicated inside set)
- **Short Words Base Case:** Length $< 3$ words like `"it"` or `"a"` abbreviate directly to themselves without numeric interior formatting

This instance demonstrates hash table grouping with set deduplication, formalizes the two distinct criteria under which an abbreviation is deemed unique, handles edge cases with repeated dictionary entries, and achieves $O(L)$ query time with $O(C)$ total dictionary preprocessing storage.

---

## 1. Instance & Teaching Goal

Given a dictionary of words:
$$
\text{dictionary} = [\text{"deer"}, \text{"door"}, \text{"cake"}, \text{"card"}]
$$
An **abbreviation** of a word $s$ is formed as:
- If $\text{len}(s) < 3$: abbreviation is $s$ itself.
- If $\text{len}(s) \ge 3$: $s[0] + \text{str}(\text{len}(s) - 2) + s[-1]$.

A word's abbreviation is defined as **unique** relative to the dictionary if and only if **either**:
1. **Condition 1:** No word in `dictionary` shares this abbreviation.
2. **Condition 2:** Every word in `dictionary` sharing this abbreviation is **identical to `word` itself**.

```text
Dictionary Abbreviations:
"deer" -> "d2r"
"door" -> "d2r"
"cake" -> "c2e"
"card" -> "c2d"

Map d[abbr]:
"d2r" -> {"deer", "door"}
"c2e" -> {"cake"}
"c2d" -> {"card"}
```

---

## 2. Conceptual Foundation & Invariants

### Hash Table Architecture
To answer each `isUnique(word)` query in $O(\text{len}(word))$ time without scanning all dictionary words:
1. Maintain a hash map `d` mapping each abbreviation string to a **set of distinct dictionary words**:
   $$
   d[\text{abbr}] = \{w_1, w_2, \dots\}
   $$
2. **Set Deduplication Invariant:**
   Using a set rather than a list or integer count ensures that duplicate occurrences of the same word (e.g. `["cake", "cake"]`) do not cause false collisions. If `"cake"` appears multiple times, $d[\text{"c2e"}]$ is still the singleton set `{"cake"}`.

### Query Evaluation Protocol
For a queried string `word`, compute its abbreviation $a = \text{abbr}(word)$:
- **Step 1:** Check if $a \notin d$.
  If the abbreviation has never been seen in the dictionary, no conflicts can exist.
  $$
  \text{return True} \quad (\text{Satisfies Condition 1})
  $$
- **Step 2:** If $a \in d$, verify that all words in $d[a]$ equal `word`:
  $$
  \text{return } \forall t \in d[a], \; (t == word)
  $$
  If $d[a] == \{word\}$, the only word in the dictionary with this abbreviation is `word` itself.
  $$
  \text{return True} \quad (\text{Satisfies Condition 2})
  $$
  If $d[a]$ contains any word distinct from `word`, return `False`.

> **Invariant.** An abbreviation is unique if and only if no dictionary word *different from `word`* maps to the same abbreviation string.

---

## 3. Step-by-Step Worked Execution

We trace the dictionary $\text{dictionary} = [\text{"deer"}, \text{"door"}, \text{"cake"}, \text{"card"}]$ across multiple representative queries:

### Constructor Preprocessing
1. `"deer"`: length 4 $\implies \text{abbr} = \text{"d"} + 2 + \text{"r"} = \text{"d2r"}$. Add to $d[\text{"d2r"}]$.
2. `"door"`: length 4 $\implies \text{abbr} = \text{"d"} + 2 + \text{"r"} = \text{"d2r"}$. Add to $d[\text{"d2r"}]$.
   Set: $d[\text{"d2r"}] = \{\text{"deer"}, \text{"door"}\}$.
3. `"cake"`: length 4 $\implies \text{abbr} = \text{"c"} + 2 + \text{"e"} = \text{"c2e"}$.
   Set: $d[\text{"c2e"}] = \{\text{"cake"}\}$.
4. `"card"`: length 4 $\implies \text{abbr} = \text{"c"} + 2 + \text{"d"} = \text{"c2d"}$.
   Set: $d[\text{"c2d"}] = \{\text{"card"}\}$.

---

### Query 1: `isUnique("dear")`
- Compute abbreviation: $\text{abbr}(\text{"dear"}) = \text{"d2r"}$.
- Check map: $\text{"d2r"} \in d$.
- Dictionary set: $d[\text{"d2r"}] = \{\text{"deer"}, \text{"door"}\}$.
- Test condition: Is every element in $d[\text{"d2r"}]$ equal to `"dear"`?
  - `"deer" == "dear"` $\implies$ **False**.
- **Return `false`**.

---

### Query 2: `isUnique("cart")`
- Compute abbreviation: $\text{abbr}(\text{"cart"}) = \text{"c2t"}$.
- Check map: $\text{"c2t"} \notin d$.
- Condition 1 holds: No dictionary word has abbreviation `"c2t"`.
- **Return `true`**.

---

### Query 3: `isUnique("cane")`
- Compute abbreviation: $\text{abbr}(\text{"cane"}) = \text{"c2e"}$.
- Check map: $\text{"c2e"} \in d$.
- Dictionary set: $d[\text{"c2e"}] = \{\text{"cake"}\}$.
- Test condition: Is every element in $d[\text{"c2e"}]$ equal to `"cane"`?
  - `"cake" == "cane"` $\implies$ **False**.
- **Return `false`**.

---

### Query 4: `isUnique("make")`
- Compute abbreviation: $\text{abbr}(\text{"make"}) = \text{"m2e"}$.
- Check map: $\text{"m2e"} \notin d$.
- Condition 1 holds: Abbreviation does not exist in dictionary.
- **Return `true`**.

---

### Query 5: `isUnique("cake")`
- Compute abbreviation: $\text{abbr}(\text{"cake"}) = \text{"c2e"}$.
- Check map: $\text{"c2e"} \in d$.
- Dictionary set: $d[\text{"c2e"}] = \{\text{"cake"}\}$.
- Test condition: Is every element in $d[\text{"c2e"}]$ equal to `"cake"`?
  - Set contains only `{"cake"}`. `"cake" == "cake"` $\implies$ **True**.
- Condition 2 holds: The query word is the sole owner of this abbreviation in the dictionary.
- **Return `true`**.

---

## 4. Complete Execution Trace

```text
Dictionary: ["deer", "door", "cake", "card"]
Groups:
  "d2r" -> {"deer", "door"}
  "c2e" -> {"cake"}
  "c2d" -> {"card"}

Query "dear": abbr="d2r" -> in d, set has {"deer", "door"} != "dear" -> false
Query "cart": abbr="c2t" -> not in d                                 -> true
Query "cane": abbr="c2e" -> in d, set has {"cake"} != "cane"         -> false
Query "make": abbr="m2e" -> not in d                                 -> true
Query "cake": abbr="c2e" -> in d, set has {"cake"} == "cake"         -> true

Results: [false, true, false, true, true]
```

| Query `word` | Computed Abbreviation | In Map $d$? | Stored Set $d[\text{abbr}]$ | All Elements $== \text{word}$? | Final Decision |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `"dear"` | `"d2r"` | Yes | `{"deer", "door"}` | No (`"deer" != "dear"`) | **`false`** |
| `"cart"` | `"c2t"` | **No** | $\emptyset$ | Vacuously True | **`true`** |
| `"cane"` | `"c2e"` | Yes | `{"cake"}` | No (`"cake" != "cane"`) | **`false`** |
| `"make"` | `"m2e"` | **No** | $\emptyset$ | Vacuously True | **`true`** |
| **`"cake"`** | **`"c2e"`** | **Yes** | **`{"cake"}`** | **Yes (`"cake" == "cake"`)** | **`true`** |

---

## 5. Algorithmic Correctness

**Soundness.** If an abbreviation is absent from the dictionary, no existing word can conflict with it (Condition 1). If an abbreviation is present, checking that all elements of $d[\text{abbr}]$ equal `word` ensures that no other word in the dictionary shares that abbreviation (Condition 2).

**Completeness.** By mapping every word in the dictionary to its unique canonical abbreviation during construction, all potential collisions are grouped into their respective buckets. Testing set containment and equality accounts for all valid and invalid configurations.

---

## 6. Traps This Instance Exposes

- **Duplicate Words in Dictionary:** If the dictionary contains `["cake", "cake"]`, using a frequency count would report count $= 2$, erroneously concluding that `"cake"` is not unique! Storing words in a `set` collapses duplicates to `{"cake"}`, correctly reporting uniqueness.
- **Short Words ($\text{len} < 3$):** Words like `"it"` or `"a"` have fewer than 3 characters. Attempting to format as `s[0] + str(len - 2) + s[-1]` would produce `"i0t"` or cause negative indexing errors. The guard `s if len(s) < 3 else ...` handles short strings properly.
- **Query Word Not in Dictionary vs Unique:** A word does NOT need to be in the dictionary to be unique. If `word`'s abbreviation does not exist in the dictionary (e.g. `"cart"`), it is unique.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - **Constructor:** $O(C)$, where $C = \sum \text{len}(w)$ is the total number of characters across all words in `dictionary`. Each word is abbreviated and inserted into the hash map in linear time relative to its length.
  - **`isUnique(word)` Query:** $O(L)$, where $L = \text{len}(word)$. Computing the abbreviation takes $O(L)$ time, hash table lookup takes $O(L)$ time, and iterating over the small word set takes $O(L)$ time.
- **Auxiliary Space Complexity:** $O(C)$ to store all dictionary words and their abbreviations in the hash map.
