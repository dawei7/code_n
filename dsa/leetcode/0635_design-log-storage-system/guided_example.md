# Guided Example: Design Log Storage System

We trace the step-by-step fixed-format timestamp decomposition (`YYYY:MM:DD:HH:MM:SS`), lexicographical chronological equivalence, granularity prefix slicing (`Year` $\to 4$, `Month` $\to 7$, `Day` $\to 10$, `Hour` $\to 13$, `Minute` $\to 16$, `Second` $\to 19$), interval range containment ($start[:k] \le ts[:k] \le end[:k]$), and filtered identifier retrieval on representative operational log databases:

- **Input:**
  - Operations:
    ```text
    LogSystem log = new LogSystem();
    log.put(1, "2017:01:01:23:59:59");
    log.put(2, "2017:01:01:22:59:59");
    log.put(3, "2016:01:01:00:00:00");
    log.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"); // Returns [1, 2, 3]
    log.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"); // Returns [1, 2]
    ```
- **Required outputs:**
  - `[null, null, null, null, [1, 2, 3], [1, 2]]` (Order of IDs within arrays may vary)
  - Core problem invariants:
    1. Timestamps have a strictly standardized 19-character format: `YYYY:MM:DD:HH:MM:SS`.
    2. All fields are zero-padded positive integers (e.g. `01` for January, not `1`).
    3. Hierarchical significance: Years are most significant, followed by Month, Day, Hour, Minute, and Second.
    4. Query granularity determines which temporal suffix fields should be **masked / ignored**.
- **Lexicographical Isomorphism & Prefix Slicing Architecture:**
  - Because ISO-like date strings place the most significant time units first with uniform zero-padded field widths, **alphabetical string order is strictly isomorphic to chronological time order**:
    $$
    T_1 < T_2 \iff \text{lexicographically } str(T_1) < str(T_2)
    $$
  - **Granularity Prefix Length Mapping ($k$):**
    - `"Year"`: characters $0 \dots 3$ $\implies k = \mathbf{4}$ (`YYYY`)
    - `"Month"`: characters $0 \dots 6$ $\implies k = \mathbf{7}$ (`YYYY:MM`)
    - `"Day"`: characters $0 \dots 9$ $\implies k = \mathbf{10}$ (`YYYY:MM:DD`)
    - `"Hour"`: characters $0 \dots 12$ $\implies k = \mathbf{13}$ (`YYYY:MM:DD:HH`)
    - `"Minute"`: characters $0 \dots 15$ $\implies k = \mathbf{16}$ (`YYYY:MM:DD:HH:MM`)
    - `"Second"`: characters $0 \dots 18$ $\implies k = \mathbf{19}$ (`YYYY:MM:DD:HH:MM:SS`)
  - **Granularity Filter Predicate:**
    - To test whether a log timestamp $ts$ falls between $start$ and $end$ at granularity $G$:
      $$
      start[0 \dots k-1] \le ts[0 \dots k-1] \le end[0 \dots k-1]
      $$
    - Any differences in characters beyond index $k - 1$ (e.g. minutes or seconds when checking `"Hour"`) are completely truncated and discarded!
- **Step-by-Step Worked Operation Trace:**
  - **Initial State:**
    - Stored log list:
      - Log 1: $(1, \; \text{"2017:01:01:23:59:59"})$
      - Log 2: $(2, \; \text{"2017:01:01:22:59:59"})$
      - Log 3: $(3, \; \text{"2016:01:01:00:00:00"})$
  - **Query 1: `retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year")`:**
    - Granularity is `"Year"` $\implies k = 4$.
    - Truncate query boundaries to first 4 characters:
      $$
      start_{prefix} = \text{"2016"}
      $$
      $$
      end_{prefix} = \text{"2017"}
      $$
    - Valid condition: $\text{"2016"} \le ts[:4] \le \text{"2017"}$.
    - Evaluate Log 1: $ts[:4] = \text{"2017"} \in [\text{"2016"}, \text{"2017"}] \implies \mathbf{Retain}$ (ID 1).
    - Evaluate Log 2: $ts[:4] = \text{"2017"} \in [\text{"2016"}, \text{"2017"}] \implies \mathbf{Retain}$ (ID 2).
    - Evaluate Log 3: $ts[:4] = \text{"2016"} \in [\text{"2016"}, \text{"2017"}] \implies \mathbf{Retain}$ (ID 3).
    - Returns: **`[1, 2, 3]`**.
  - **Query 2: `retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour")`:**
    - Granularity is `"Hour"` $\implies k = 13$.
    - Truncate query boundaries to first 13 characters:
      $$
      start_{prefix} = \text{"2016:01:01:01"}
      $$
      $$
      end_{prefix} = \text{"2017:01:01:23"}
      $$
    - Valid condition: $\text{"2016:01:01:01"} \le ts[:13] \le \text{"2017:01:01:23"}$.
    - **Evaluate Log 1:**
      - $ts[:13] = \text{"2017:01:01:23"}$.
      - Compare: $\text{"2016:01:01:01"} \le \text{"2017:01:01:23"} \le \text{"2017:01:01:23"} \implies \mathbf{True!}$
      - Retain ID 1.
    - **Evaluate Log 2:**
      - $ts[:13] = \text{"2017:01:01:22"}$.
      - Compare: $\text{"2016:01:01:01"} \le \text{"2017:01:01:22"} \le \text{"2017:01:01:23"} \implies \mathbf{True!}$
      - Retain ID 2.
    - **Evaluate Log 3:**
      - $ts[:13] = \text{"2016:01:01:00"}$.
      - Notice the hour field: $00 < 01$.
      - Compare: $\text{"2016:01:01:00"} < \text{"2016:01:01:01"}$ (Precedes start window!).
      - $\mathbf{False!} \implies$ Log 3 is excluded.
    - Returns: **`[1, 2]`**.
- **Day-Level Query Example:**
  - If granularity is `"Day"` ($k = 10$), `start = "2017:01:01:00:00:00"` and `end = "2017:01:01:23:59:59"`:
  - Both slice to `"2017:01:01"`.
  - Any log on January 1, 2017 matches, regardless of its time of day.

This instance demonstrates radix time representation and lexicographical prefix range evaluation, mathematically proves why fixed-width big-endian temporal formats preserve total ordering under substring projection, and derives $O(1)$ write time and $O(N)$ query time bounds.

---

## 1. Instance & Teaching Goal

Implement a log storage system supporting:
- `put(id, timestamp)`: Stores a log entry.
- `retrieve(start, end, granularity)`: Returns IDs of all logs in $[start, end]$ inclusive at the given granularity (`Year`, `Month`, `Day`, `Hour`, `Minute`, `Second`).

```text
Logs:
  1: 2017:01:01:23:59:59
  2: 2017:01:01:22:59:59
  3: 2016:01:01:00:00:00

retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"):
  Slice to 13 chars (YYYY:MM:DD:HH):
    start = "2016:01:01:01"
    end   = "2017:01:01:23"

  Log 1: "2017:01:01:23" in range -> KEEP
  Log 2: "2017:01:01:22" in range -> KEEP
  Log 3: "2016:01:01:00" < start  -> DROP

Result: [1, 2]
```

### The Invariant of Lexicographical Isomorphism
- When numbers are zero-padded to uniform widths and organized from most to least significant units, string comparison `S1 <= S2` exactly reflects chronological order.
- Slicing to the length corresponding to a granularity automatically ignores all lower-level fields without parsing dates.

---

## 2. Conceptual Foundation & Invariants

### 1. Granularity Cutoff Index:
| Granularity | Cutoff Index $k$ | Sample Prefix |
|:---:|:---:|:---:|
| `Year` | $4$ | `2017` |
| `Month` | $7$ | `2017:01` |
| `Day` | $10$ | `2017:01:01` |
| `Hour` | $13$ | `2017:01:01:23` |
| `Minute` | $16$ | `2017:01:01:23:59` |
| `Second` | $19$ | `2017:01:01:23:59:59` |

### 2. Slicing Invariant:
$$
\text{Matches}(ts) \iff start[:k] \le ts[:k] \le end[:k]
$$

> **Big-Endian Lexicographical Invariant.** The hierarchical big-endian encoding $\prod \text{field}_i$ establishes an order-preserving embedding $\phi: \mathcal{T} \to \Sigma^*$, such that prefix truncation induces the canonical quotient topology of the specified granularity.

---

## 3. Step-by-Step Worked Execution

We trace the query for `"Hour"`:

---

### Step 1: Lookup Cutoff
- Granularity is `"Hour"` $\implies k = 13$.

---

### Step 2: Slice Range
- $start[:13] = \text{"2016:01:01:01"}$.
- $end[:13] = \text{"2017:01:01:23"}$.

---

### Step 3: Test Each Stored Log
- Log 1: $ts[:13] = \text{"2017:01:01:23"}$. Inside $[\text{start}, \text{end}]$ $\implies$ Select.
- Log 2: $ts[:13] = \text{"2017:01:01:22"}$. Inside $[\text{start}, \text{end}]$ $\implies$ Select.
- Log 3: $ts[:13] = \text{"2016:01:01:00"}$. Slices to 00 hours, strictly before 01 hours $\implies$ Exclude.

---

### Step 4: Output
$$
\mathbf{[1, 2]}
$$

---

## 4. Complete Execution Trace

| Log ID | Full Timestamp | Prefix at $k = 13$ | $\ge \text{"2016:01:01:01"}$? | $\le \text{"2017:01:01:23"}$? | Included? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | `2017:01:01:23:59:59` | `2017:01:01:23` | **Yes** | **Yes** | **Yes** |
| $2$ | `2017:01:01:22:59:59` | `2017:01:01:22` | **Yes** | **Yes** | **Yes** |
| $3$ | `2016:01:01:00:00:00` | `2016:01:01:00` | No ($00 < 01$) | Yes | No |
| **Result** | — | — | — | — | **`[1, 2]`** |

---

## 5. Boundary Cases & Failure Modes

- **Granularity is `Second`:** Checks the entire string ($k = 19$).
- **Granularity is `Year`:** Checks only the year ($k = 4$).
- **Single Log Stored:** Handled smoothly.
- **Identical Start and End (`start == end`):** Matches all logs whose prefix equals $start[:k]$.

---

## 6. Traps & Common Anti-Patterns

- **Parsing Strings into Datetime Objects:** Converting strings to calendar dates via library functions is slow and unnecessary. String comparison is mathematically identical and orders of magnitude faster.
- **Off-by-One Slicing Index:** The separator colons `:` occur at indices 4, 7, 10, 13, 16. The correct cutoff includes the desired field, e.g. Year ends at 4 (`YYYY`), Month at 7 (`YYYY:MM`).
- **Assuming Ordered Output:** The problem allows IDs to be returned in any order; wrapping in a sort is unnecessary unless required by testing validators.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - `put`: $\mathcal{O}(1)$ to append the tuple to an array.
  - `retrieve`: $\mathcal{O}(N)$ where $N$ is total logs, performing a fixed 19-character string prefix comparison per log.
  - For $N = 300$ queries, completes in $< 2$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store the $N$ log entries.
