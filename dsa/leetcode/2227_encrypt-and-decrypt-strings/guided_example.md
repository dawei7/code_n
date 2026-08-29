# Guided Example: Encrypt and Decrypt Strings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"operations": ["Encrypter", "encrypt", "decrypt"], "arguments": [[["a", "b", "c", "d"], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]], ["abcd"], ["eizfeiam"]]}`
- **Required output:** `[null, "eizfeiam", 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a character array `keys` containing **unique** characters and a string array `values` containing strings of length 2. You are also given another string array `dictionary` that contains all permitted original strings after decryption. You should implement a data structure that can encrypt or decrypt a **0-indexed** string.

The objective is to compute `[null, "eizfeiam", 2]` from `{"operations": ["Encrypter", "encrypt", "decrypt"], "arguments": [[["a", "b", "c", "d"], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]], ["abcd"], ["eizfeiam"]]}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Encryption is a direct character map

The constructor receives parallel arrays `keys` and `values`. The statement `dict(zip(keys, values))` builds `mp` so each unique key character maps directly to its required two-character code.

The `encrypt` method scans `word1` from left to right. For every character `c`, it first checks membership in `mp`. If the character has no mapping, encryption is impossible and the method immediately returns the empty string. Otherwise, it appends `mp[c]` to a list. Joining once at the end produces the concatenated ciphertext efficiently.

Because each code has length two, a valid plaintext of length `t` produces ciphertext length `2t`. The order of codes matches the order of plaintext characters.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"operations": ["Encrypter", "encrypt", "decrypt"], "arguments": [[["a", "b", "c", "d"], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]], ["abcd"], ["eizfeiam"]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Avoid enumerating ambiguous decryptions

Several different keys may map to the same two-character value. Direct decryption could branch at every ciphertext pair. If many pairs are ambiguous, the number of possible plaintext strings grows exponentially.

The query does not ask to list every possible plaintext. It asks only how many possible plaintexts also occur in the fixed `dictionary`. That allows the work to be reversed: encrypt every dictionary word once during construction, then count equal ciphertexts.

The constructor executes

`cnt = Counter(encrypt(v) for v in dictionary)`.

For each permitted original word `v`, it calls the same exact encryption procedure used by public requests. `Counter` maps the resulting ciphertext to the number of dictionary words that produce it.

Different dictionary words may collide intentionally. In the example, both `"abcd"` and `"abad"` encrypt to `"eizfeiam"` because `a` and `c` share code `"ei"` in relevant positions. The counter stores frequency two for that ciphertext.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Decryption becomes one frequency lookup

The method `decrypt(word2)` returns `cnt[word2]`. If the ciphertext was produced by three dictionary words, the result is three. If no dictionary word produced it, `Counter` returns zero for the missing key.

This lookup answers exactly the required question without choosing a reverse mapping for each pair. A dictionary word is a valid decryption of `word2` precisely when encrypting that word produces `word2`:

- if the word decrypts from `word2`, each character's code matches the corresponding two-character block, so re-encryption recreates `word2`;
- if its encryption equals `word2`, each of its characters is one allowed reverse choice for the matching blocks, so it is a possible decryption.

Counting pre-encrypted dictionary words is therefore equivalent to enumerating all possible decryptions and filtering by dictionary membership, but avoids the exponential intermediate set.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[null, "eizfeiam", 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"operations": ["Encrypter", "encrypt", "decrypt"], "arguments": [[["a", "b", "c", "d"], ["ei", "zf", "ei", "am"], ["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"]], ["abcd"], ["eizfeiam"]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[null, "eizfeiam", 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Backtrack through reverse mappings:** Build code-to-possible-characters lists and enumerate all plaintext combinations for `word2`. This can grow exponentially with the number of ambiguous pairs and wastes work on strings absent from the dictionary.
- **Decrypt every dictionary word per query:** Encrypt each dictionary entry and compare it to `word2` on every call. It is correct but repeats fixed work; preprocessing makes subsequent queries a lookup.
- **Store encrypted dictionary strings in a set:** A set loses collision multiplicity and cannot report how many distinct dictionary words decrypt from one ciphertext.
- **Build one reverse character per code:** Choosing only one key for a repeated value misses other valid plaintexts. Pre-encryption naturally accounts for all dictionary words.
- **Repeated values:** Multiple keys may map to the same code, and their dictionary words correctly increase the same counter entry.
- **Unmapped plaintext character:** `encrypt` immediately returns the empty string rather than a partial ciphertext.
- **Ciphertext absent from preprocessing:** `Counter` returns zero without requiring an explicit membership branch.
- **Repeated decrypt calls:** They reuse the constructor's counter and do not rescan the dictionary.
- **Unique dictionary strings with equal encryption:** Each distinct original contributes one, so the frequency can exceed one.
- **Even ciphertext length:** The contract guarantees legal pair boundaries. Lookup does not need to validate or split the string.
- **Empty encryption key in the counter:** It can arise only from an invalid dictionary word; legal decrypt inputs have length at least two and cannot match it.
- **Input preservation:** The constructor builds new mapping and counter objects; the supplied arrays and dictionary strings are not modified.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(K + D)$. Let `K` be the number of key mappings, let `D` be the total number of characters across all dictionary words, and let `L` be the plaintext length supplied to one `encrypt` call. Building `mp` takes `O(K)` expected time. Encrypting the dictionary during construction processes `D` characters, so constructor time is `O(K + D)`.
- **Auxiliary Space Complexity:** $O(D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
