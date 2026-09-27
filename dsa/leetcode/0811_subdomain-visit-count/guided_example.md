# Guided Example: Subdomain Visit Count

We trace the step-by-step count-paired domain parsing ($s \to (count, domain)$), dot-delimited hierarchical suffix extraction ($d_1.d_2.d_3 \to \{d_1.d_2.d_3, d_2.d_3, d_3\}$), hash table frequency aggregation ($cnt[subdomain] \mathrel{+}= count$), and formatted count-paired string generation on representative web domain logs:

- **Input:**
  $$
  cpdomains = [\text{"9001 discuss.leetcode.com"}]
  $$
- **Required output:**
  $$
  [\text{"9001 discuss.leetcode.com"}, \; \text{"9001 leetcode.com"}, \; \text{"9001 com"}]
  $$
  *(Order of domains in output list is arbitrary)*
  - Domain hierarchy & visit count rules:
    - A count-paired domain string consists of an integer count $v$, a space, and a domain name (e.g. `"9001 discuss.leetcode.com"`).
    - When a domain $d_1.d_2.d_3$ is visited $v$ times, every parent subdomain in its hierarchy is also visited $v$ times:
      1. The full domain: $d_1.d_2.d_3$
      2. The second-level domain: $d_2.d_3$
      3. The top-level domain: $d_3$
    - Objective: Aggregate visit counts across all subdomains and return them formatted as `"count domain"`.
    - For `"9001 discuss.leetcode.com"`:
      - Count $v = 9001$.
      - Subdomain 1: `"discuss.leetcode.com"` receives $9001$ visits.
      - Subdomain 2: `"leetcode.com"` receives $9001$ visits.
      - Subdomain 3: `"com"` receives $9001$ visits.
      - Output: `["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"]`.
- **Suffix Hierarchy & Hash Table Accumulation Invariant:**
  - **The Domain Suffix Decomposition:**
    - Any domain with $k$ dot-separated labels $d_1.d_2 \dots d_k$ generates exactly $k$ valid subdomains:
      $$
      \text{subdomains}(d_1.d_2 \dots d_k) = \{ d_i.d_{i+1} \dots d_k \mid 1 \le i \le k \}
      $$
    - In string representation, a new subdomain begins immediately after:
      1. The initial space `' '` separating the visit count from the domain.
      2. Every subsequent period `'.'` inside the domain string.
  - **Frequency Accumulation ($cnt$):**
    - Maintain a hash map $cnt$ mapping subdomain string $\to$ integer count.
    - For each input string $s$:
      - Parse integer count: $v = \text{int}(s[0 \dots \text{space} - 1])$.
      - For every index $i$ where character $s[i]$ is a space `' '` or dot `'.'`:
        - The suffix $s[i + 1 \dots]$ is a valid subdomain!
        - Accumulate:
          $$
          cnt[s[i + 1 \dots]] \leftarrow cnt[s[i + 1 \dots]] + v
          $$
    - Format entries as strings `"{count} {subdomain}"`.
- **Step-by-Step Worked Execution Trace on Sample 1:**
  - Input log: $s = \text{"9001 discuss.leetcode.com"}$.
  - Initialize hash map: $cnt = \{\}$.
  - **Step 1: Extract Visit Count:**
    - First space located at index 4: $s[4] = \text{' '}$.
    - Parse integer prefix:
      $$
      v = \text{int}(s[:4]) = \mathbf{9001}
      $$
  - **Step 2: Stream Characters and Detect Suffix Boundaries:**
    - Boundary 1 at index 4 ($s[4] = \text{' '}$):
      - Suffix from index 5: $s[5:] = \mathbf{\text{"discuss.leetcode.com"}}$.
      - Accumulate:
        $$
        cnt[\text{"discuss.leetcode.com"}] \leftarrow 0 + 9001 = \mathbf{9001}
        $$
    - Boundary 2 at index 12 ($s[12] = \text{'.'}$, between `"discuss"` and `"leetcode"`):
      - Suffix from index 13: $s[13:] = \mathbf{\text{"leetcode.com"}}$.
      - Accumulate:
        $$
        cnt[\text{"leetcode.com"}] \leftarrow 0 + 9001 = \mathbf{9001}
        $$
    - Boundary 3 at index 21 ($s[21] = \text{'.'}$, between `"leetcode"` and `"com"`):
      - Suffix from index 22: $s[22:] = \mathbf{\text{"com"}}$.
      - Accumulate:
        $$
        cnt[\text{"com"}] \leftarrow 0 + 9001 = \mathbf{9001}
        $$
  - **Step 3: Format Output Strings:**
    - Key `"discuss.leetcode.com"` $\to \mathbf{\text{"9001 discuss.leetcode.com"}}$
    - Key `"leetcode.com"` $\to \mathbf{\text{"9001 leetcode.com"}}$
    - Key `"com"` $\to \mathbf{\text{"9001 com"}}$
    - Result:
      $$
      ans = [\text{"9001 discuss.leetcode.com"}, \; \text{"9001 leetcode.com"}, \; \text{"9001 com"}]
      $$
- **Step-by-Step Worked Execution Trace on Overlapping Domains (Sample 2):**
  - Input: `["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]`
  - Processing `"900 google.mail.com"`:
    - `"google.mail.com"`: 900
    - `"mail.com"`: 900
    - `"com"`: 900
  - Processing `"50 yahoo.com"`:
    - `"yahoo.com"`: 50
    - `"com"`: $900 + 50 = \mathbf{950}$
  - Processing `"1 intel.mail.com"`:
    - `"intel.mail.com"`: 1
    - `"mail.com"`: $900 + 1 = \mathbf{901}$
    - `"com"`: $950 + 1 = \mathbf{951}$
  - Processing `"5 wiki.org"`:
    - `"wiki.org"`: 5
    - `"org"`: 5
  - Aggregated outputs:
    - `"951 com"`, `"900 google.mail.com"`, `"1 intel.mail.com"`, `"50 yahoo.com"`, `"901 mail.com"`, `"5 wiki.org"`, `"5 org"`.

This instance demonstrates tree-structured hierarchical path aggregation and suffix monoid counting via hash multiset accumulation, mathematically proves why suffix factoring linearizes prefix-tree volume measures, and derives $O(\sum |s_i|)$ execution time and $O(\sum |s_i|)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given domain visit counts like `"9001 discuss.leetcode.com"`:
A visit to `a.b.c` also counts as a visit to `b.c` and `c`.
Aggregate total visits for every subdomain.

```text
Input: "9001 discuss.leetcode.com"

Subdomains generated:
  1. "discuss.leetcode.com" -> 9001
  2. "leetcode.com"         -> 9001
  3. "com"                  -> 9001

Result: [ "9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com" ]
```

### The Invariant of Suffix Hierarchy Aggregation
- Every subdomain is a suffix of the full domain name starting after a space or a dot.
- By streaming characters and slicing whenever a delimiter `c in ' .'` appears, all subdomains are discovered in a single pass.
- Accumulate counts in a hash map and format the keys.

---

## 2. Conceptual Foundation & Invariants

### 1. Suffix Partition Function:
$$
\text{Subdomains}(domain) = \{ domain[i:] \mid i = 0 \lor domain[i - 1] = \text{'.'} \}
$$

### 2. Multi-Log Aggregation:
$$
cnt[sub] = \sum_{(v, d) \in logs, \; sub \in \text{Subdomains}(d)} v
$$

> **Poset Upper Set Invariant.** The domain name hierarchy is a forest of rooted trees ordered by reverse suffix inclusion (e.g. $com \prec leetcode.com \prec discuss.leetcode.com$). Visits push measure uniformly to all ancestors in the principal filter $\uparrow(d)$.

---

## 3. Step-by-Step Worked Execution

We trace `"9001 discuss.leetcode.com"`:

---

### Step 1: Parse Number
- $v = 9001$.

---

### Step 2: Delimiter 1 (Space)
- Suffix: `"discuss.leetcode.com"` $\implies cnt += 9001$.

---

### Step 3: Delimiter 2 (First Dot)
- Suffix: `"leetcode.com"` $\implies cnt += 9001$.

---

### Step 4: Delimiter 3 (Second Dot)
- Suffix: `"com"` $\implies cnt += 9001$.

---

### Step 5: Output
$$
[\text{"9001 discuss.leetcode.com"}, \; \text{"9001 leetcode.com"}, \; \text{"9001 com"}]
$$

---

## 4. Complete Execution Trace

| Processed Domain Entry | Suffix Subdomain | Current Accumulated Count | Final Formatted String |
|:---:|:---:|:---:|:---:|
| `"9001 discuss.leetcode.com"` | `"discuss.leetcode.com"` | $9001$ | `"9001 discuss.leetcode.com"` |
| `"9001 discuss.leetcode.com"` | `"leetcode.com"` | $9001$ | `"9001 leetcode.com"` |
| **`"9001 discuss.leetcode.com"`** | **`"com"`** | **$9001$** | **`"9001 com"`** |

---

## 5. Boundary Cases & Failure Modes

- **Two-Label Domain (`"50 yahoo.com"`):** Generates only 2 subdomains: `"yahoo.com"` and `"com"`.
- **Multiple Logs with Overlapping Domains:** Subdomain counts sum up across different lines (e.g. `"com"` receives visits from Google, Yahoo, Intel).
- **Single Log Line:** Evaluates 2 or 3 subdomains directly.
- **Large Counts ($10^4$):** Handled safely by integer addition.

---

## 6. Traps & Common Anti-Patterns

- **Splitting on Dots Forward Instead of Suffixes:** Slicing from the front produces prefixes (`"discuss"`, `"discuss.leetcode"`), which are NOT valid subdomains. Subdomains are always suffixes (`"com"`, `"leetcode.com"`).
- **Manual String Splitting with Multiple Copies:** Finding indices of `' '` and `'.'` allows slicing suffixes directly in a single pass without generating intermediate string arrays.
- **Forgetting Space Separator in Output:** Output strings must strictly follow the format `"{count} {subdomain}"`.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Let $N$ be the number of domain logs, and $L$ the max length of a domain string ($L \le 100$).
  - Each domain has at most 3 labels, so each string generates at most 3 suffixes.
  - Suffix hashing and hash map addition: $\mathcal{O}(L)$.
  - Total Time: strictly linear in total characters $\mathcal{O}(\sum |s_i|)$ where $\sum |s_i| \le 10^4$. Completes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(\sum |s_i|)$ memory to store unique subdomains in the hash map.
