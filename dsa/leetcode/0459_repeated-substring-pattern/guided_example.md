# Guided Example: Repeated Substring Pattern

We trace the step-by-step string period duplication theorem ($s \in (s + s)[1:-1]$), string doubling circular shift analysis, KMP failure function border periodicity ($n \pmod{n - \pi[n-1]} == 0$), and sub-block tiling verification on representative string instances:

- **Input:** $s = \text{"abab"}$
- **Required output:** `true`
  - Total length: $n = 4$
  - String concatenation doubling:
    $$
    s + s = \text{"abab"} + \text{"abab"} = \text{"abababab"}
    $$
  - Boundary character trimming (remove index $0$ and index $2n - 1$):
    $$
    T' = (s + s)[1 : 7] = \text{"bababa"}
    $$
  - Substring search for target $s = \text{"abab"}$ within $T'$:
    - Index 0 in $T'$: `"baba"` $\ne$ `"abab"`
    - Index 1 in $T'$: `"abab"` $==$ `"abab"` (**Match Found!**)
  - Because $s$ occurs at an internal shift (index $1$ in $T'$, corresponding to shift $L = 2$ in $s + s$), $s$ is composed of repeating sub-blocks of length $2$ (`"ab"` repeated twice).
  - Return **`true`**.
- **Non-Periodic Instance:** $s = \text{"aba"}$ ($n = 3$)
  - Doubled: $s + s = \text{"abaaba"}$
  - Trimmed: $T' = \text{"baab"}$
  - Search `"aba"` in `"baab"`: not found $\implies \mathbf{false}$
- **Multiple Copies Instance:** $s = \text{"abcabcabcabc"}$ ($n = 12$)
  - Block length $3$ (`"abc"` repeated 4 times) $\implies$ First match at shift $3 < 12 \implies \mathbf{true}$

This instance demonstrates string periodicity theorems, mathematically proves why doubled string containment $(s + s)[1:-1]$ is equivalent to existence of a non-trivial period, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s = \text{"abab"}$:
Check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

```text
Original String s: "abab"
Candidate Sub-block: "ab" (repeated 2 times)

Doubled String Concatenation:
  s + s:   [ a  b  a  b ] [ a  b  a  b ]
  Indices:   0  1  2  3     4  5  6  7

Trim Outermost Characters:
  (s + s)[1:-1]:    b [ a  b  a  b ] a
                      ^-----------^
                      Target 'abab' found at internal shift index 2!

Result: true (Period L = 2 exists)
```

### The String Doubling Theorem
Let $s$ have length $n$.
- If $s$ is formed by repeating a block $P$ of length $L$ ($k \ge 2$ times), then $s = P^k$.
- Consider the doubled string:
  $$
  s + s = P^{2k}
  $$
- Copies of $s$ occur inside $s + s$ starting at every multiple of $L$:
  $$
  \text{Occurrences of } s \text{ in } s + s \text{ start at indices: } 0, \; L, \; 2L, \; \dots, \; (2k - k)L = n
  $$
- Since $k \ge 2$, the first internal period occurs at index $L \le \frac{n}{2} < n$.
- If we remove the first character (index 0) and the last character (index $2n - 1$) to form $T' = (s + s)[1 : 2n - 1]$:
  - The trivial match at index 0 is destroyed.
  - The trivial match at index $n$ is destroyed.
  - Therefore, $s$ is found inside $T'$ **if and only if** there exists an internal period $L \in [1, n - 1]$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Doubling Invariant:
$$
s \text{ is periodic} \iff s \in (s + s)[1 : -1]
$$
- If $s$ is periodic with period $L$, a full copy of $s$ begins at shift index $L$ in $s + s$. Since $1 \le L \le n - 1$, this copy is entirely contained within the interior of $(s + s)$ excluding the first and last characters.
- If $s$ is not periodic, the only occurrences of $s$ in $s + s$ are at index $0$ and index $n$. Trimming the first and last characters excludes both trivial matches, so the search returns $-1$.

### 2. The Equivalent KMP Failure Function Invariant:
Let $\pi$ be the prefix function (failure table) of $s$:
- $\pi[n - 1]$ is the length of the longest proper prefix of $s$ that is also a suffix of $s$.
- If $s$ is periodic:
  - The length of the minimal repeating unit is $L = n - \pi[n - 1]$.
  - The string is periodic if and only if $\pi[n - 1] > 0$ and $n \pmod L == 0$.

> **Periodicity Theorem.** A string of length $n$ is a repetition of a shorter substring if and only if its shortest non-zero shift in the circular string space equals the length of that repeating substring.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"abab"}$ ($n = 4$):

---

### Step 1: Form Concatenated Doubled String
Concatenate $s$ with itself:
$$
s + s = \text{"abab"} + \text{"abab"} = \text{"abababab"} \quad (|s+s| = 8)
$$

---

### Step 2: Trim Extremities
Drop the first character at index $0$ (`'a'`) and the last character at index $7$ (`'b'`):
$$
T' = (s + s)[1 : 7] = \text{"bababa"} \quad (|T'| = 6)
$$

---

### Step 3: Search for $s = \text{"abab"}$ in $T'$
Scan $T'$ for target pattern `"abab"` of length 4:
- Offset 0: $T'[0:4] = \text{"baba"} \ne \text{"abab"}$
- Offset 1: $T'[1:5] = \text{"abab"} == \text{"abab"}$ (**Exact Match!**)
Match starts at offset 1 in $T'$, which corresponds to shift $1 + 1 = 2$ in $s + s$.
Since $2 < 4$, a non-trivial repetition period exists ($L = 2$).
Return **`true`**.

---

### Counter-Example Walk: $s = \text{"aba"}$ ($n = 3$)
- $s + s = \text{"abaaba"}$
- Trimmed $T' = \text{"baab"}$
- Check offsets for target `"aba"`:
  - Offset 0: $T'[0:3] = \text{"baa"} \ne \text{"aba"}$
  - Offset 1: $T'[1:4] = \text{"aab"} \ne \text{"aba"}$
- Target `"aba"` not found in $T'$.
- Return **`false`**.

---

## 4. Complete Execution Trace

| Candidate String $s$ | Length $n$ | Doubled $s + s$ | Trimmed Interior $(s+s)[1:-1]$ | Match Location in Interior | Found? | Result |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `"abab"` | $4$ | `"abababab"` | `"bababa"` | Index 1 (Shift 2) | **Yes** | **`true`** |
| `"aba"` | $3$ | `"abaaba"` | `"baab"` | None | No | **`false`** |
| `"abcabcabcabc"` | $12$ | `"abc...abc"` | `"bc...ab"` | Index 2 (Shift 3) | **Yes** | **`true`** |
| `"a"` | $1$ | `"aa"` | `""` | None | No | **`false`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Character ($s = \text{"a"}):$** A repeated substring requires at least 2 copies of a non-empty substring ($k \ge 2$), so $|s|$ must be $\ge 2$. $s + s = \text{"aa"}$, trimming leaves `""`, search fails $\implies \mathbf{false}$.
- **All Identical Characters ($s = \text{"aaaa"}):$** $L = 1$. Interior search finds match at shift $1 \implies \mathbf{true}$.
- **Prime Length String with Alternating Substrings ($s = \text{"ababa"}):$** Ends and starts with `"aba"`, but cannot tile the full string without overlap $\implies \mathbf{false}$.

---

## 6. Traps & Common Anti-Patterns

- **Searching in $s + s$ Without Trimming:** Searching $s$ in $s + s$ directly always matches at index $0$ (the first copy itself), falsely concluding that every string is periodic. Trimming the boundary characters is mandatory to eliminate trivial matches.
- **Trial-and-Error Divisor Loop ($O(N \sqrt{N})$):** Testing every divisor of $n$ and repeatedly checking `s[:d] * (n // d) == s` works, but is slower than the elegant $O(N)$ string doubling or KMP check.
- **Off-by-One in Trim Slicing:** In 0-indexed slicing, taking `(s + s)[1:-1]` removes exactly the first and last characters. Removing more characters can destroy valid period matches.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - String concatenation $s + s$ takes $O(N)$ time.
  - Slicing and substring search using Knuth-Morris-Pratt (or Python's optimized Boyer-Moore-Horspool search) takes $O(N)$ time.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^4$, completes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ auxiliary space to allocate the doubled string.
