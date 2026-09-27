# Guided Example: Unique Substrings With Equal Digit Frequency

We analyze and execute the rolling-hash equal-frequency substring enumeration algorithm on a representative digit string instance, demonstrating how the product identity $\text{length} = \text{max\_freq} \times \text{distinct\_digits}$ certifies uniform frequency in $O(1)$ time.

- **Input:** `s = "1212"`
- **Output:** `5`

This instance illustrates incremental character expansion, constant-time uniform frequency testing, polynomial rolling hash deduplication, and set collection.

---

## 1. Problem Overview & Representative Instance

Given a string `s` consisting only of decimal digits (`'0'` through `'9'`), a non-empty contiguous substring qualifies if every distinct digit present in it occurs with the **exact same frequency**. Absent digits do not participate in the frequency comparison.

We must count the total number of **distinct** substring strings that qualify. Identical text appearing at multiple distinct start/end positions contributes to the total count only once.

In our representative instance:
- `s = "1212"` of length $n = 4$.
- Substrings of length 1: `"1"`, `"2"`.
- Substrings of length 2: `"12"`, `"21"`.
- Substrings of length 3: `"121"`, `"212"`.
- Substrings of length 4: `"1212"`.

Notice that `"12"` appears at both indices $s[0 \dots 1]$ and $s[2 \dots 3]$, but must be counted only once.

---

## 2. Mathematical & Algorithmic Principles

### The Uniform Frequency Product Criterion

Let a substring of length $L = j - i + 1$ have:
- $D$: The number of distinct digits present in the substring with non-zero frequency.
- $F_{\max} = \max_{d} \text{freq}[d]$: The maximum frequency of any digit in the substring.

Because every present digit has frequency at most $F_{\max}$, the total length is bounded by:
$$L = \sum_{d \text{ present}} \text{freq}[d] \le \sum_{d \text{ present}} F_{\max} = D \times F_{\max}$$

The inequality becomes an equality if and only if **every** present digit has $\text{freq}[d] = F_{\max}$:
$$\text{All present digits have equal frequency} \iff L = D \times F_{\max}$$

This single integer multiplication provides a strictly sound $O(1)$ test per substring expansion, avoiding any 10-iteration loop over digit buckets.

### Substring Deduplication via Rolling Hash

To count distinct substrings across all $O(n^2)$ pairs $(i, j)$:
- For a fixed starting index $i$, as $j$ advances from $i$ to $n - 1$:
  - Maintain a polynomial rolling hash:
    $$H \leftarrow (H \cdot B + \operatorname{val}(s[j])) \bmod M$$
    using a large prime modulus $M$ (or 64-bit integer overflow) and base $B = 31$ or $37$.
  - Maintain the digit frequency table $\text{freq}[0 \dots 9]$.
  - Update distinct digit counter $D$ and maximum frequency $F_{\max}$.
  - If $L == D \times F_{\max}$, insert $H$ (or the substring slice) into a hash set $\mathcal{U}$.
- The final answer is the cardinality $|\mathcal{U}|$.

| Metric / Variable | Mathematical Meaning | Role in $O(1)$ Verification |
|---|---|---|
| Substring Length $L$ | $j - i + 1$ | Total character count in active window |
| Distinct Digits $D$ | $\sum \mathbf{1}_{\{\text{freq}[d] > 0\}}$ | Number of non-zero digit classes |
| Peak Frequency $F_{\max}$ | $\max_{d} \text{freq}[d]$ | Maximum occurrence count among present digits |
| Uniformity Condition | $L == D \times F_{\max}$ | Constant-time certificate of equal digit frequency |
| Substring Hash $H$ | Polynomial hash of $s[i \dots j]$ | Deduplicates identical substrings at different positions |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace `s = "1212"` of length $n = 4$.
All $\binom{4+1}{2} = 10$ candidate substrings are evaluated.

```
String: "1212"
Indices: 0   1   2   3
Chars:   1   2   1   2
```

### Step 1: Start Index $i = 0$
Initialize $\text{freq} = [0 \dots 0], D = 0, F_{\max} = 0, H = 0$.
- **$j = 0$ (Character `'1'`, Substring `"1"`):**
  - Length $L = 1$.
  - Update: $\text{freq}[1] = 1 \implies D = 1, F_{\max} = 1$.
  - Test: $L == D \times F_{\max} \implies 1 == 1 \times 1$ (True).
  - Add `"1"` to set $\mathcal{U} = \{\text{"1"}\}$.
- **$j = 1$ (Character `'2'`, Substring `"12"`):**
  - Length $L = 2$.
  - Update: $\text{freq}[2] = 1 \implies D = 2, F_{\max} = 1$.
  - Test: $L == D \times F_{\max} \implies 2 == 2 \times 1$ (True).
  - Add `"12"` to set $\mathcal{U} = \{\text{"1"}, \text{"12"}\}$.
- **$j = 2$ (Character `'1'`, Substring `"121"`):**
  - Length $L = 3$.
  - Update: $\text{freq}[1] = 2 \implies D = 2, F_{\max} = 2$.
  - Test: $L == D \times F_{\max} \implies 3 == 2 \times 2 = 4$ (False).
  - Not uniform (`'1'` occurs twice, `'2'` occurs once). Discard.
- **$j = 3$ (Character `'2'`, Substring `"1212"`):**
  - Length $L = 4$.
  - Update: $\text{freq}[2] = 2 \implies D = 2, F_{\max} = 2$.
  - Test: $L == D \times F_{\max} \implies 4 == 2 \times 2 = 4$ (True).
  - Add `"1212"` to set $\mathcal{U} = \{\text{"1"}, \text{"12"}, \text{"1212"}\}$.

### Step 2: Start Index $i = 1$
Initialize $\text{freq} = [0 \dots 0], D = 0, F_{\max} = 0, H = 0$.
- **$j = 1$ (Character `'2'`, Substring `"2"`):**
  - $L = 1, D = 1, F_{\max} = 1 \implies 1 == 1$.
  - Add `"2"` to set $\mathcal{U} = \{\text{"1"}, \text{"12"}, \text{"1212"}, \text{"2"}\}$.
- **$j = 2$ (Character `'1'`, Substring `"21"`):**
  - $L = 2, D = 2, F_{\max} = 1 \implies 2 == 2 \times 1$.
  - Add `"21"` to set $\mathcal{U} = \{\text{"1"}, \text{"12"}, \text{"1212"}, \text{"2"}, \text{"21"}\}$.
- **$j = 3$ (Character `'2'`, Substring `"212"`):**
  - $L = 3, D = 2, F_{\max} = 2 \implies 3 == 4$ (False). Discard.

### Step 3: Start Index $i = 2$
Initialize $\text{freq} = [0 \dots 0], D = 0, F_{\max} = 0, H = 0$.
- **$j = 2$ (Character `'1'`, Substring `"1"`):**
  - $L = 1 \implies$ Valid. Already present in $\mathcal{U}$ (Duplicate skipped).
- **$j = 3$ (Character `'2'`, Substring `"12"`):**
  - $L = 2 \implies$ Valid. Already present in $\mathcal{U}$ (Duplicate skipped).

### Step 4: Start Index $i = 3$
Initialize $\text{freq} = [0 \dots 0], D = 0, F_{\max} = 0, H = 0$.
- **$j = 3$ (Character `'2'`, Substring `"2"`):**
  - $L = 1 \implies$ Valid. Already present in $\mathcal{U}$ (Duplicate skipped).

### Step 5: Finalization
- Total unique qualifying substrings in $\mathcal{U}$:
  $$\mathcal{U} = \{\text{"1"}, \text{"2"}, \text{"12"}, \text{"21"}, \text{"1212"}\}$$
- Distinct count: $5$.

---

## 4. Comprehensive State Trace

The table below catalogs every contiguous substring of `s = "1212"`:

| Window $[i \dots j]$ | Substring | Length $L$ | Frequencies Active | Distinct $D$ | $F_{\max}$ | $D \times F_{\max}$ | Qualifies ($L == D \cdot F_{\max}$)? | Added to Unique Set? |
|---|---|---|---|---|---|---|---|---|
| $[0 \dots 0]$ | `"1"` | $1$ | `{'1': 1}` | $1$ | $1$ | $1$ | **Yes** | **Yes** (New: `"1"`) |
| $[0 \dots 1]$ | `"12"` | $2$ | `{'1': 1, '2': 1}` | $2$ | $1$ | $2$ | **Yes** | **Yes** (New: `"12"`) |
| $[0 \dots 2]$ | `"121"` | $3$ | `{'1': 2, '2': 1}` | $2$ | $2$ | $4$ | No ($3 \ne 4$) | No |
| $[0 \dots 3]$ | `"1212"` | $4$ | `{'1': 2, '2': 2}` | $2$ | $2$ | $4$ | **Yes** | **Yes** (New: `"1212"`) |
| $[1 \dots 1]$ | `"2"` | $1$ | `{'2': 1}` | $1$ | $1$ | $1$ | **Yes** | **Yes** (New: `"2"`) |
| $[1 \dots 2]$ | `"21"` | $2$ | `{'2': 1, '1': 1}` | $2$ | $1$ | $2$ | **Yes** | **Yes** (New: `"21"`) |
| $[1 \dots 3]$ | `"212"` | $3$ | `{'2': 2, '1': 1}` | $2$ | $2$ | $4$ | No ($3 \ne 4$) | No |
| $[2 \dots 2]$ | `"1"` | $1$ | `{'1': 1}` | $1$ | $1$ | $1$ | **Yes** | No (Duplicate) |
| $[2 \dots 3]$ | `"12"` | $2$ | `{'1': 1, '2': 1}` | $2$ | $1$ | $2$ | **Yes** | No (Duplicate) |
| $[3 \dots 3]$ | `"2"` | $1$ | `{'2': 1}` | $1$ | $1$ | $1$ | **Yes** | No (Duplicate) |

Unique set size: $5$.

---

## 5. Algorithmic Correctness & Soundness

### Exact Arithmetic Characterization
Let the present distinct digits in a substring be $d_1, d_2, \dots, d_D$.
The total length is $L = \sum_{k=1}^D \text{freq}[d_k]$.
Since $\text{freq}[d_k] \le F_{\max}$ for all $k$:
$$L = \sum_{k=1}^D \text{freq}[d_k] \le \sum_{k=1}^D F_{\max} = D \cdot F_{\max}$$
Equality holds if and only if $\text{freq}[d_k] = F_{\max}$ for every $k \in \{1, \dots, D\}$.
Thus, testing $L == D \times F_{\max}$ is mathematically equivalent to verifying that all present digits share the exact same frequency $F_{\max}$.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Single Digit Repeated (`s = "000"`):**
   - Distinct values: `"0"`, `"00"`, `"000"`.
   - Each has $D = 1$. For `"000"`, $L = 3, F_{\max} = 3 \implies 3 == 1 \times 3$. All qualify; returns $3$.
2. **All Digits Distinct (`s = "123"`):**
   - Every contiguous substring has all frequencies equal to $1$ ($F_{\max} = 1$). Every distinct substring qualifies.
3. **Strings with Zeros:** Character `'0'` has numeric index $0$; handled seamlessly by 10-bucket counting array.

### Common Anti-Patterns
- **Iterating Through All 10 Digits to Check Equality:** Checking if all non-zero entries in `freq` are equal takes up to $10$ loop steps per substring. The product check $L == D \times F_{\max}$ accomplishes this in a single $O(1)$ arithmetic operation.
- **Substring String Slicing in Python (`s[i:j+1]`):** Slicing strings of length up to $1000$ costs $O(L)$ memory and time per substring, leading to an $O(n^3)$ algorithm. A rolling hash (or Trie insertion) keeps each extension at $O(1)$ time.
- **Overlooking Multi-Occurrence Deduplication:** Substrings must be deduplicated by string value, not by interval indices. Using a `Set` of hashes guarantees distinct content counting.

---

## 7. Complexity Analysis

### Time Complexity
- There are $n$ outer iterations for starting position $i$.
- For each $i$, the inner loop advances $j$ from $i$ to $n - 1$ ($n$ inner steps).
- Inside the inner loop:
  - Frequency update: $O(1)$.
  - Rolling hash update: $O(1)$.
  - Uniformity check ($L == D \times F_{\max}$): $O(1)$.
  - Set insertion of 64-bit integer hash: $O(1)$ expected time.
- Total time complexity is strictly $O(n^2)$.
- For $n = 1000$, $n^2 / 2 = 5 \times 10^5$ iterations, running in under $60$ milliseconds.

### Auxiliary Space Complexity
- A fixed 10-element frequency array.
- A hash set storing at most $O(n^2) \le 5 \cdot 10^5$ 64-bit integers.
- Total auxiliary space complexity is $O(n^2)$ memory for the hash set (or $O(n^2)$ Trie nodes).
