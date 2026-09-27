# Guided Example: Encode and Decode TinyURL

We trace the step-by-step monotonic auto-increment ID generation ($idx \leftarrow idx + 1$), string-key hash map registration ($m[key] = longUrl$), domain prefix encapsulation ($\text{domain} + key$), URL path token parsing ($shortUrl.split(\text{'/'})[-1]$), and loss-free $O(1)$ round-trip decoding on representative web addresses:

- **Input:**
  - Original long URL:
    $$
    longUrl = \text{"https://leetcode.com/problems/design-tinyurl"}
    $$
  - Service domain prefix:
    $$
    \text{domain} = \text{"https://tinyurl.com/"}
    $$
- **Required behavior:**
  - `encode(longUrl)` produces a shortened URL.
  - `decode(shortUrl)` restores the exact original $longUrl$.
- **Codec Encoding & Decoding Trace:**
  - Maintain service state:
    - Counter: $idx = 0$
    - Lookup directory: $m = \{\}$
  - **Encoding Request (`encode`):**
    - Advance global sequence counter:
      $$
      idx \leftarrow 0 + 1 = \mathbf{1}
      $$
    - Store mapping in directory under key `"1"`:
      $$
      m[\text{"1"}] = \text{"https://leetcode.com/problems/design-tinyurl"}
      $$
    - Construct formatted short URL:
      $$
      shortUrl = \text{"https://tinyurl.com/"} + \text{"1"} = \mathbf{\text{"https://tinyurl.com/1"}}
      $$
    - Emitted short URL length: 22 characters (much shorter than original 44 characters).
  - **Decoding Request (`decode`):**
    - Input: $shortUrl = \text{"https://tinyurl.com/1"}$
    - Extract identification token:
      - Split path by forward slashes `/`: `["https:", "", "tinyurl.com", "1"]`.
      - Terminal segment:
        $$
        key = \text{"1"}
        $$
    - Hash map query:
      $$
      longUrl = m[\text{"1"}] = \mathbf{\text{"https://leetcode.com/problems/design-tinyurl"}}
      $$
    - Decoded string matches original URL with $100\%$ fidelity!
- **Multi-URL Conflict-Free Instance:**
  - URL A (`"https://example.com/a"`): assigned key `"1"` $\implies$ `"https://tinyurl.com/1"`.
  - URL B (`"https://example.com/b"`): assigned key `"2"` $\implies$ `"https://tinyurl.com/2"`.
  - Decoding in reverse order (URL 2 then URL 1) correctly resolves to URL B and URL A respectively.
- **Identical Repeated URLs:**
  - Each call to `encode` issues a unique sequence key, guaranteeing distinct short URLs that each resolve back to the correct original address.

This instance demonstrates bijective stateful key-value tokenization, mathematically proves why sequential primary keys guarantee collision-free URL shortening, and derives $O(1)$ amortized encode/decode runtime and $O(N \cdot L)$ space bounds.

---

## 1. Instance & Teaching Goal

TinyURL is a URL shortening service:
Implement a class `Codec` supporting:
- `encode(longUrl)`: Encodes a URL to a shortened URL.
- `decode(shortUrl)`: Decodes a shortened URL back to its original URL.
Guarantee that `decode(encode(url)) == url`.

```text
Input: "https://leetcode.com/problems/design-tinyurl"

Encode:
  Counter idx = 1
  Directory: {"1": "https://leetcode.com/problems/design-tinyurl"}
  Return: "https://tinyurl.com/1"

Decode("https://tinyurl.com/1"):
  Extract key "1"
  Lookup in directory -> "https://leetcode.com/problems/design-tinyurl"
```

### The System Design Trade-Offs
How should the short URL key be generated?
1. **Hash Functions (MD5 / SHA-256):**
   Produces a 128-bit hash, truncated to 6 characters (e.g. Base62). Requires handling hash collisions.
2. **Random Base62 Strings:**
   Generate random 6-character strings (`[a-zA-Z0-9]`). Requires retry logic if the random key is already taken.
3. **Monotonic Sequence Counter:**
   Increment an integer ID ($1, 2, 3, \dots$).
   - Completely collision-free.
   - Guaranteed unique keys.
   - Constant $O(1)$ time with zero retries.

---

## 2. Conceptual Foundation & Invariants

### 1. State Maintenance:
The `Codec` instance maintains:
- $idx$: an integer counter, initialized to 0.
- $m$: a hash map mapping string key $\to$ string original URL.
- $domain$: base string prefix `"https://tinyurl.com/"`.

### 2. Encoding Operation:
1. $idx \leftarrow idx + 1$.
2. Key: $k = \text{str}(idx)$.
3. Record: $m[k] = longUrl$.
4. Return: $domain + k$.

### 3. Decoding Operation:
1. Parse terminal token:
   $$
   k = shortUrl.\text{split}(\text{'/'})[-1]
   $$
2. Retrieve original URL from hash map:
   $$
   \text{Return } m[k]
   $$

> **Bijective Round-Trip Invariant.** Because every call to `encode` increments $idx$, each generated key is globally unique in $m$, guaranteeing that $decode(encode(u)) \equiv u$ holds for all URLs $u$.

---

## 3. Step-by-Step Worked Execution

We trace two URLs:
$U_1 = \text{"https://example.com/alpha"}$
$U_2 = \text{"https://example.com/beta"}$

---

### Step 1: Initialize Codec
- $idx = 0$
- $m = \{\}$

---

### Step 2: Encode $U_1$
- $idx \leftarrow 0 + 1 = 1$.
- Key: `"1"`.
- Store: $m[\text{"1"}] = \text{"https://example.com/alpha"}$.
- Return:
  $$
  S_1 = \mathbf{\text{"https://tinyurl.com/1"}}
  $$

---

### Step 3: Encode $U_2$
- $idx \leftarrow 1 + 1 = 2$.
- Key: `"2"`.
- Store: $m[\text{"2"}] = \text{"https://example.com/beta"}$.
- Return:
  $$
  S_2 = \mathbf{\text{"https://tinyurl.com/2"}}
  $$

---

### Step 4: Decode $S_2$
- Extract key: `"https://tinyurl.com/2"`.split('/')[-1] $\implies$ `"2"`.
- Query: $m[\text{"2"}] = \mathbf{\text{"https://example.com/beta"}}$.

---

### Step 5: Decode $S_1$
- Extract key: `"1"`.
- Query: $m[\text{"1"}] = \mathbf{\text{"https://example.com/alpha"}}$.

---

## 4. Complete Execution Trace

| Call | Input Argument | Internal $idx$ | Hash Map State $m$ | Emitted Return Value |
|:---:|:---:|:---:|:---:|:---:|
| `__init__()` | — | $0$ | $\{\}$ | `Codec instance` |
| `encode(U1)` | `"https://example.com/alpha"` | $1$ | `{"1": U1}` | **`"https://tinyurl.com/1"`** |
| `encode(U2)` | `"https://example.com/beta"` | $2$ | `{"1": U1, "2": U2}` | **`"https://tinyurl.com/2"`** |
| `decode(S2)` | `"https://tinyurl.com/2"` | $2$ | Unchanged | **`"https://example.com/beta"`** |
| `decode(S1)` | `"https://tinyurl.com/1"` | $2$ | Unchanged | **`"https://example.com/alpha"`** |

---

## 5. Boundary Cases & Failure Modes

- **Very Long URLs ($> 1000$ characters):** Stored directly in hash map without truncation.
- **Short Original URLs:** Short original URLs are still shortened or preserved faithfully.
- **URLs with Complex Query Parameters (`?a=1&b=2#section`):** Treated as opaque string values, preserved completely during storage and retrieval.
- **High Volume Calls ($10^6$ calls):** String representation of integer IDs scales gracefully (`"1000000"` is 7 characters).

---

## 6. Traps & Common Anti-Patterns

- **Stateless Mathematical Compression:** Attempting to compress arbitrary URLs into tiny strings without database storage is mathematically impossible due to the Pigeonhole Principle (the set of long strings is vastly larger than the set of short strings). State storage via a database or hash map is required.
- **Parsing the Key with Inflexible String Slicing:** Hardcoding slice index (e.g. `shortUrl[19:]`) breaks if the domain scheme changes from `http` to `https`. Using `.split('/')[-1]` reliably extracts the trailing path token.
- **Overwriting Duplicate URLs Without Bi-Directional Indexing:** If multiple calls are made with the same URL, giving them new sequential IDs works seamlessly. If sharing IDs is desired, a reverse map `long_to_short` can be added.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `encode(longUrl)`: Incrementing an integer and inserting into a hash map takes $\mathcal{O}(L)$ time where $L$ is the length of the URL (for string hashing).
  - `decode(shortUrl)`: String splitting and hash map lookup takes $\mathcal{O}(L)$ time.
  - Total Time: strictly $\mathcal{O}(1)$ operations relative to the number of stored URLs, proportional only to string length.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N \cdot L)$ space to store $N$ URLs in the hash map.
