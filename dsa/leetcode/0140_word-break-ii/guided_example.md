# Guided Example: Word Break II

We trace the step-by-step memoized depth-first suffix decomposition and sentence assembly on representative dictionary segmentation instances:

- **Input:** $s = \text{"catsanddog"}$, $\text{wordDict} = [\text{"cat"}, \text{"cats"}, \text{"and"}, \text{"sand"}, \text{"dog"}]$
- **Required output:** `["cats and dog", "cat sand dog"]`
- **Dead-End Suffix Instance:** $s = \text{"catsandog"}$, $\text{wordDict} = [\text{"cats"}, \text{"dog"}, \text{"sand"}, \text{"and"}, \text{"cat"}] \implies []$

This instance demonstrates top-down recursive suffix partitioning ($\text{dfs}(\text{start})$), memoizing intermediate sentence lists to prevent exponential recalculation of overlapping suffixes, composing sub-sentences via `word + " " + sub_sentence`, and pruning unreachable suffix branches in $O(N \cdot 2^N)$ worst-case output time.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"catsanddog"}$ of length $N = 10$ and a dictionary of words $\text{wordDict} = [\text{"cat"}, \text{"cats"}, \text{"and"}, \text{"sand"}, \text{"dog"}]$:
Construct all possible valid sentences formed by inserting spaces between dictionary words.
Words may be reused arbitrarily.

In this instance, two distinct sentence structures decompose $s$:
1. $\text{"cat"} + \text{" "} + \text{"sand"} + \text{" "} + \text{"dog"}$
2. $\text{"cats"} + \text{" "} + \text{"and"} + \text{" "} + \text{"dog"}$
Both paths share the identical terminal suffix $\text{"dog"}$ at index $7$.

A naive recursive search without memoization re-evaluates identical suffixes multiple times, leading to Time Limit Exceeded (TLE) on overlapping dictionaries (e.g. `s = "aaaaaaa"`, `words = ["a", "aa", "aaa"]`).
Memoized DFS decomposes the problem into independent suffix queries: function $\text{dfs}(\text{start})$ computes and caches all valid sentences that can be formed from suffix $s[\text{start}:]$. When multiple prefixes converge onto the same suffix, the results are retrieved from cache in $O(1)$ time.

---

## 2. Conceptual Foundation & Invariants

### Memoized Suffix DFS Protocol
Let `word_set = set(wordDict)`.
Maintain a memoization table `memo: Dict[int, List[str]]`.
Define recursive function $\text{dfs}(\text{start})$:

1. **Terminal Success Base Case:**
   If $\text{start} == |s|$:
   Return a list containing a single empty string anchor:
   $$
   \text{return } [\text{""}]
   $$
2. **Memoization Cache Lookup:**
   If $\text{start} \in \text{memo}$:
   Return cached sentence list:
   $$
   \text{return } \text{memo}[\text{start}]
   $$
3. **Prefix Matching and Suffix Recursion:**
   Initialize `sentences = []`.
   For $\text{end}$ from $\text{start} + 1$ to $|s|$:
   - Extract candidate word $\text{word} = s[\text{start} : \text{end}]$.
   - If $\text{word} \in \text{word\_set}$:
     - Recursively solve the remaining suffix: $\text{sub\_sentences} = \text{dfs}(\text{end})$.
     - For each $\text{sub} \in \text{sub\_sentences}$:
       - If $\text{sub} == \text{""}$: append $\text{word}$.
       - Else: append $\text{word} + \text{" "} + \text{sub}$.
4. **Commit to Cache:**
   $$
   \text{memo}[\text{start}] \leftarrow \text{sentences}
   $$
   $$
   \text{return } \text{sentences}
   $$

> **Invariant.** For any index $\text{start}$, $\text{memo}[\text{start}]$ stores the complete, exhaustive list of all valid space-delimited sentences that form the suffix $s[\text{start}:]$.

---

## 3. Step-by-Step Worked Execution

We trace $\text{dfs}(\text{start} = 0)$ on $s = \text{"catsanddog"}$:

### Level 1: Root Call $\text{dfs}(0)$
- Explore prefix cuts from index 0:
  - $\text{end} = 3$: $s[0:3] = \text{"cat"} \in \text{word\_set} \implies$ recurse $\text{dfs}(3)$.
  - $\text{end} = 4$: $s[0:4] = \text{"cats"} \in \text{word\_set} \implies$ recurse $\text{dfs}(4)$.

---

### Level 2: Sub-Problem $\text{dfs}(3)$ on Suffix `"sanddog"`
- Explore cuts from index 3:
  - $\text{end} = 7$: $s[3:7] = \text{"sand"} \in \text{word\_set} \implies$ recurse $\text{dfs}(7)$.

---

### Level 3: Sub-Problem $\text{dfs}(7)$ on Suffix `"dog"`
- Explore cuts from index 7:
  - $\text{end} = 10$: $s[7:10] = \text{"dog"} \in \text{word\_set} \implies$ recurse $\text{dfs}(10)$.
  - $\text{dfs}(10)$ hits base case ($\text{start} == 10$), returning `[""]`.
  - Assemble: $\text{"dog"} + \text{""} \implies \text{["dog"]}$.
- Commit to cache:
  $$
  \text{memo}[7] \leftarrow [\text{"dog"}]
  $$
- $\text{dfs}(7)$ returns `["dog"]`.

---

### Level 2 (Unwinding): Complete $\text{dfs}(3)$
- Combine $\text{"sand"}$ with results from $\text{dfs}(7)$:
  $$
  \text{"sand"} + \text{" "} + \text{"dog"} = \text{"sand dog"}
  $$
- Commit to cache:
  $$
  \text{memo}[3] \leftarrow [\text{"sand dog"}]
  $$
- $\text{dfs}(3)$ returns `["sand dog"]`.

---

### Level 1 (First Branch Assembled):
- Prefix $\text{"cat"}$ receives `["sand dog"]`:
  $$
  \text{"cat"} + \text{" "} + \text{"sand dog"} = \mathbf{\text{"cat sand dog"}}
  $$

---

### Level 2: Sub-Problem $\text{dfs}(4)$ on Suffix `"anddog"`
- Explore cuts from index 4:
  - $\text{end} = 7$: $s[4:7] = \text{"and"} \in \text{word\_set} \implies$ recurse $\text{dfs}(7)$.
  - **Memoization Hit!**
    $\text{start} = 7$ is already cached in `memo[7]` as `["dog"]`.
    Returns `["dog"]` immediately in $O(1)$ without recursion!
- Combine $\text{"and"}$ with `["dog"]`:
  $$
  \text{"and"} + \text{" "} + \text{"dog"} = \text{"and dog"}
  $$
- Commit to cache:
  $$
  \text{memo}[4] \leftarrow [\text{"and dog"}]
  $$
- $\text{dfs}(4)$ returns `["and dog"]`.

---

### Level 1 (Second Branch Assembled):
- Prefix $\text{"cats"}$ receives `["and dog"]`:
  $$
  \text{"cats"} + \text{" "} + \text{"and dog"} = \mathbf{\text{"cats and dog"}}
  $$

Total sentences assembled at root $\text{dfs}(0)$:
`["cat sand dog", "cats and dog"]`.

---

## 4. Complete Execution Trace

### Suffix DAG and Sentence Synthesis

```text
dfs(0)
  |-- "cat"  -> dfs(3) -> "sand" -> dfs(7) -> "dog" -> dfs(10) [""]
  |                                   |                 ^
  |                                   |              Base Case
  |                                memo[7] = ["dog"]
  |-- "cats" -> dfs(4) -> "and"  ----/ (Cache Hit!)
```

| Call State | Suffix Inspected | Matched Word $s[\text{start}:\text{end}]$ | Next Call | Suffix Result Returned | Assembled Sentence Committed |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $\text{dfs}(10)$ | $\emptyset$ | Base case | - | - | `[""]` |
| $\text{dfs}(7)$ | `"dog"` | `"dog"` | $\text{dfs}(10)$ | `[""]` | `["dog"]` |
| $\text{dfs}(3)$ | `"sanddog"` | `"sand"` | $\text{dfs}(7)$ | `["dog"]` | `["sand dog"]` |
| $\text{dfs}(4)$ | `"anddog"` | `"and"` | $\text{dfs}(7)$ | **`["dog"]` (Cache Hit)** | `["and dog"]` |
| **$\text{dfs}(0)$** | **`"catsanddog"`** | **`"cat"`** | $\text{dfs}(3)$ | `["sand dog"]` | **`"cat sand dog"`** |
| **$\text{dfs}(0)$** | **`"catsanddog"`** | **`"cats"`** | $\text{dfs}(4)$ | `["and dog"]` | **`"cats and dog"`** |

### Memoization Cache State After the Trace

The table below records what each index ultimately stores, which dictionary
prefixes were the only survivors of the cut scan, and which later calls were
answered from the cache instead of recursing again.

| `start` | Suffix $s[\text{start}:]$ | Dictionary prefixes that matched (`end` reached) | Value committed to `memo[start]` | Sentences stored | Later callers served from this cache entry |
|:---:|:---|:---|:---|:---:|:---|
| 10 | `""` (empty suffix) | none needed — this is the terminal base case | `[""]` | 1 | $\text{dfs}(7)$ |
| 7 | `"dog"` | `"dog"` ($\text{end} = 10$) | `["dog"]` | 1 | $\text{dfs}(3)$ and $\text{dfs}(4)$ both consume it, so `"dog"` is expanded once |
| 3 | `"sanddog"` | `"sand"` ($\text{end} = 7$) | `["sand dog"]` | 1 | $\text{dfs}(0)$, via the prefix `"cat"` |
| 4 | `"anddog"` | `"and"` ($\text{end} = 7$) | `["and dog"]` | 1 | $\text{dfs}(0)$, via the prefix `"cats"` |
| 0 | `"catsanddog"` | `"cat"` ($\text{end} = 3$) and `"cats"` ($\text{end} = 4$) | `["cat sand dog", "cats and dog"]` | 2 | the root call itself; the returned list is the answer |

Every cut that is *not* listed fails the dictionary test and therefore creates
no recursive call: from index 0 the rejected cuts are `"c"`, `"ca"`, `"catsa"`,
`"catsan"`, `"catsand"`, `"catsandd"`, `"catsando"`, `"catsanddog"`; from index
3 they are `"s"`, `"sa"`, `"san"`, `"sande"`, `"sandd"`, `"sanddog"`; from index
4 they are `"a"`, `"an"`, `"andd"`, `"anddo"`, `"anddog"`; and from index 7 they
are `"d"` and `"do"`. The five indices above are the complete set of cache
entries this instance ever writes, and index 7 is the only one written by one
call and read by two.

---

## 5. Algorithmic Correctness

**Soundness.** A sentence is constructed only by concatenating valid dictionary words separated by single spaces. The recursion strictly terminates at the end of the string ($|s|$), ensuring the concatenation of words in every returned sentence equals $s$.

**Completeness.** At each step, all prefix slices $s[\text{start}:\text{end}]$ are tested against `word_set`. All possible branch points are evaluated, ensuring that every valid combination of dictionary words that reconstructs $s$ is captured.

---

## 6. Traps This Instance Exposes

- **Exponential Re-evaluation Without Memoization:** If multiple paths converge on the same suffix (as $\text{dfs}(3)$ and $\text{dfs}(4)$ both reach index 7), recomputing suffixes causes an exponential $O(2^N)$ explosion. Memoizing by integer index `start` ensures each suffix is solved once.
- **Unmatchable Dead Ends:** On inputs like `s = "catsandog"`, the suffix `"og"` has no dictionary match. The recursive call returns `[]`, which naturally propagates up the call stack and produces an empty list `[]` without throwing exceptions.
- **Trailing Spaces:** Appending `" "` naively after every word creates trailing whitespace on the last word. Checking `if sub == "": append(word)` prevents trailing spaces.

### Boundary Behaviour of the Same Method

| Boundary scenario | Input | Result | Why the suffix recursion yields exactly that result |
|:---|:---|:---|:---|
| The whole string is a single dictionary word | $s = \text{"a"}$, $\text{wordDict} = [\text{"a"}]$ | `["a"]`, so $1$ sentence | The only cut is $\text{end} = 1$, and $\text{dfs}(1)$ is the base case returning `[""]`. The empty anchor is appended as the bare word, so no separator and no trailing space is emitted. |
| An unsegmentable suffix empties every branch | $s = \text{"catsandog"}$, $\text{wordDict} = [\text{"cats"}, \text{"dog"}, \text{"sand"}, \text{"and"}, \text{"cat"}]$ | `[]`, so $0$ sentences | The suffix `"og"` at index 7 matches no dictionary word, so `memo[7]` stores `[]`. Iterating over zero sub-sentences appends nothing, and $\text{dfs}(3)$ through `"sand"` and $\text{dfs}(4)$ through `"and"` both inherit the empty list, which propagates to $\text{dfs}(0)$. |
| Maximum branching inside the shortest string | $s = \text{"aaaa"}$, $\text{wordDict} = [\text{"a"}, \text{"aa"}, \text{"aaa"}]$ | $7$ sentences | Each distinct ordered composition of $4$ into parts of size $1$, $2$, or $3$ is one distinct sentence. Of the $2^{4-1} = 8$ compositions of $4$, exactly one uses the part $4$, which is absent from the dictionary, leaving $8 - 1 = 7$. |
| The same suffix is reached through two different prefix cuts | $s = \text{"pineapplepenapple"}$, $\text{wordDict} = [\text{"apple"}, \text{"pen"}, \text{"applepen"}, \text{"pine"}, \text{"pineapple"}]$ | $3$ sentences | Index 0 admits both `"pine"` and `"pineapple"`, and index 4 admits both `"apple"` and `"applepen"`. The suffix at index 9 (`"penapple"`) is solved once into `["pen apple"]` and reused by the `"pine"` branch and the `"pineapple"` branch, while the index-12 suffix `"apple"` serves all three assembled sentences. |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N^2 + 2^N)$, where $N = |s|$. In the worst case (where every prefix and suffix is valid), there can be $O(2^{N-1})$ distinct sentences, each taking $O(N)$ time to construct. Memoization ensures that non-branching subproblems are solved in $O(N^2)$ time.
- **Auxiliary Space Complexity:** $O(N \cdot 2^N)$ to store all valid sentences in the memoization table, with $O(N)$ recursion call stack depth.
