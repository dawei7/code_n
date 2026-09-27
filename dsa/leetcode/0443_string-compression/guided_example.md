# Guided Example: String Compression

We trace the step-by-step consecutive run-length encoding (RLE), two-pointer in-place write cursor advance ($k \le i$), multi-digit integer string serialization, and array prefix modification on representative character arrays:

- **Input:** $chars = [\text{'a'}, \text{'a'}, \text{'b'}, \text{'b'}, \text{'c'}, \text{'c'}, \text{'c'}]$
- **Required output:** Length `6`, with modified prefix:
  $$
  [\text{'a'}, \text{'2'}, \text{'b'}, \text{'2'}, \text{'c'}, \text{'3'}]
  $$
- **Two-pointer execution trace:**
  - Read pointer: $i = 0$, Write pointer: $k = 0$, Total length: $n = 7$
  - **Run 1 (Character `'a'`):**
    - Consecutive occurrences: $i = 0$ to $j = 2$ (`chars[0] == chars[1] == 'a'`)
    - Run length: $j - i = 2 - 0 = 2$
    - Write character: $chars[k] \leftarrow \text{'a'}, \; k \leftarrow 1$
    - Because run length $> 1$: write digit `'2'`: $chars[k] \leftarrow \text{'2'}, \; k \leftarrow 2$
    - Advance read pointer: $i \leftarrow j = 2$
  - **Run 2 (Character `'b'`):**
    - Consecutive occurrences: $i = 2$ to $j = 4$ (`chars[2] == chars[3] == 'b'`)
    - Run length: $4 - 2 = 2$
    - Write character: $chars[k] \leftarrow \text{'b'}, \; k \leftarrow 3$
    - Write digit `'2'`: $chars[k] \leftarrow \text{'2'}, \; k \leftarrow 4$
    - Advance read pointer: $i \leftarrow j = 4$
  - **Run 3 (Character `'c'`):**
    - Consecutive occurrences: $i = 4$ to $j = 7$ (`chars[4] == chars[5] == chars[6] == 'c'`)
    - Run length: $7 - 4 = 3$
    - Write character: $chars[k] \leftarrow \text{'c'}, \; k \leftarrow 5$
    - Write digit `'3'`: $chars[k] \leftarrow \text{'3'}, \; k \leftarrow 6$
    - Advance read pointer: $i \leftarrow j = 7$
  - All elements processed. Return new length: $k = \mathbf{6}$.
- **Multi-Digit Run Instance:** $chars = [\text{'a'}] + [\text{'b'}] \times 12 \implies \text{'a'}$ (length 1), then $\text{'b'}$ with count 12 written as `'1'` and `'2'` $\implies [\text{'a'}, \text{'b'}, \text{'1'}, \text{'2'}]$, length $\mathbf{4}$
- **Single Character Instance:** $chars = [\text{'a'}] \implies [\text{'a'}]$, length $\mathbf{1}$ (count 1 is omitted per specification)

This instance demonstrates in-place two-pointer array compression, mathematically proves why the write pointer never overtakes the read pointer ($k \le i$), and achieves $O(N)$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an array of characters $chars = [\text{'a'}, \text{'a'}, \text{'b'}, \text{'b'}, \text{'c'}, \text{'c'}, \text{'c'}]$:
Compress the array in-place using the following rules:
- For each group of consecutive repeating characters:
  - If the group's length is 1, append the character itself.
  - If the group's length is $> 1$, append the character followed by the group's length (split into individual digit characters if length $\ge 10$).
- Modify the input array in-place and return the new length of the compressed prefix.

```text
Original Array:
  [ 'a', 'a', 'b', 'b', 'c', 'c', 'c' ]
    \_____/   \_____/   \_________/
     run: 2    run: 2     run: 3

In-Place Compressed Result:
  [ 'a', '2', 'b', '2', 'c', '3' ]
  <----------------------------->
         New Length: 6
```

### The In-Place Non-Overwriting Invariant
Why is it safe to write back into the same array without extra memory?
- For a group of length 1: we write 1 character (`'x'`) and consume 1 character $\implies \Delta = 0$.
- For a group of length $L \ge 2$: we write 1 character plus $d = \lfloor \log_{10} L \rfloor + 1$ digits.
- Since $1 + d \le L$ for all integers $L \ge 2$ (e.g. for $L=2$, $1+1=2 \le 2$; for $L=10$, $1+2=3 \le 10$):
The number of written characters is **always less than or equal to** the number of scanned characters!
Therefore, the write pointer $k$ is guaranteed to satisfy:
$$
k \le i \quad \text{at all times}
$$
The write cursor never overwrites unprocessed future characters.

---

## 2. Conceptual Foundation & Invariants

### 1. Two-Pointer Mechanics:
- Read Pointer $i$: Points to the start of the current consecutive run.
- Runner Pointer $j$: Scans ahead until $chars[j] \ne chars[i]$ to determine run length $L = j - i$.
- Write Pointer $k$: Marks the insertion point for the compressed output.

### 2. Compression Encoding Steps:
1. Write the run character: $chars[k] \leftarrow chars[i], \; k \leftarrow k + 1$.
2. If $L > 1$:
   - Convert $L$ to its decimal string representation (e.g. $12 \to \text{"12"}$).
   - For each character digit $c$ in the decimal representation:
     $$
     chars[k] \leftarrow c, \quad k \leftarrow k + 1
     $$
3. Advance the read pointer: $i \leftarrow j$.

> **Write Invariant.** The compressed prefix occupies $chars[0 \dots k-1]$. The remaining suffix $chars[i \dots n-1]$ is completely unread and uncorrupted, with $k \le i$.

---

## 3. Step-by-Step Worked Execution

We trace $chars = [\text{'a'}, \text{'a'}, \text{'b'}, \text{'b'}, \text{'c'}, \text{'c'}, \text{'c'}]$ ($n = 7$):
Initialize $i = 0, k = 0$.

---

### Step 1: Process Run 1 (`'a'`)
- Start index: $i = 0$, character $chars[0] = \text{'a'}$.
- Advance runner $j$:
  - $j = 1: chars[1] == \text{'a'}$
  - $j = 2: chars[2] == \text{'b'} \ne \text{'a'}$. Stop.
- Run length: $L = j - i = 2 - 0 = 2$.
- Write character:
  $$
  chars[k] = \text{'a'} \implies chars[0] = \text{'a'}, \quad k \leftarrow 1
  $$
- Length $L = 2 > 1$. Write count `'2'`:
  $$
  chars[k] = \text{'2'} \implies chars[1] = \text{'2'}, \quad k \leftarrow 2
  $$
- Advance read pointer: $i \leftarrow 2$.
- Array state: `['a', '2', 'b', 'b', 'c', 'c', 'c']`.

---

### Step 2: Process Run 2 (`'b'`)
- Start index: $i = 2$, character $chars[2] = \text{'b'}$.
- Advance runner $j$:
  - $j = 3: chars[3] == \text{'b'}$
  - $j = 4: chars[4] == \text{'c'} \ne \text{'b'}$. Stop.
- Run length: $L = 4 - 2 = 2$.
- Write character:
  $$
  chars[k] = \text{'b'} \implies chars[2] = \text{'b'}, \quad k \leftarrow 3
  $$
- Length $L = 2 > 1$. Write count `'2'`:
  $$
  chars[k] = \text{'2'} \implies chars[3] = \text{'2'}, \quad k \leftarrow 4
  $$
- Advance read pointer: $i \leftarrow 4$.
- Array state: `['a', '2', 'b', '2', 'c', 'c', 'c']`.

---

### Step 3: Process Run 3 (`'c'`)
- Start index: $i = 4$, character $chars[4] = \text{'c'}$.
- Advance runner $j$:
  - $j = 5: chars[5] == \text{'c'}$
  - $j = 6: chars[6] == \text{'c'}$
  - $j = 7 == n$. Stop.
- Run length: $L = 7 - 4 = 3$.
- Write character:
  $$
  chars[k] = \text{'c'} \implies chars[4] = \text{'c'}, \quad k \leftarrow 5
  $$
- Length $L = 3 > 1$. Write count `'3'`:
  $$
  chars[k] = \text{'3'} \implies chars[5] = \text{'3'}, \quad k \leftarrow 6
  $$
- Advance read pointer: $i \leftarrow 7$.
- Array state: `['a', '2', 'b', '2', 'c', '3', 'c']`.

---

### Termination:
Read pointer $i = 7 == n$. Loop terminates.
Return final write length: $k = \mathbf{6}$.
Prefix of length 6: `['a', '2', 'b', '2', 'c', '3']`.

---

## 4. Complete Execution Trace

| Group # | Read Span $[i, j-1]$ | Char | Run Length $L$ | Chars Written | Write Indices Populated | Written Substring | Write Head $k$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1** | $[0, 1]$ | `'a'` | $2$ | `'a'`, `'2'` | $0, 1$ | `"a2"` | $2$ |
| **2** | $[2, 3]$ | `'b'` | $2$ | `'b'`, `'2'` | $2, 3$ | `"b2"` | $4$ |
| **3** | $[4, 6]$ | `'c'` | $3$ | `'c'`, `'3'` | $4, 5$ | `"c3"` | **$6$** |
| **Done**| All scanned | — | — | — | — | — | **Result: $6$** |

---

## 5. Boundary Cases & Failure Modes

- **Single Character ($chars = [\text{'a'}]$):** $L = 1$. Writes `'a'`, count is omitted per specification $\implies k = 1$.
- **All Unique Characters ($[\text{'a'}, \text{'b'}, \text{'c'}]$):** Each run has length 1. Output is `['a', 'b', 'c']`, length 3.
- **Large Run ($\ge 10$ characters):** If a run has length $12$, writes the character followed by `'1'` and `'2'`. Consumes 12 positions, writes 3 positions ($k \ll i$).
- **Maximum Length Array ($N = 2000$ identical chars):** $L = 2000$. Writes `'x'`, then `'2'`, `'0'`, `'0'`, `'0'`. Final length is 5.

---

## 6. Traps & Common Anti-Patterns

- **Writing Count When $L = 1$:** Appending `'1'` for singleton characters violates the format rules (`"a"` must not be compressed to `"a1"`). Counts must strictly be emitted only when $L > 1$.
- **Allocating Intermediate String Buffers:** Creating a new string or dynamic list and copying back to $chars$ wastes $O(N)$ extra memory. In-place pointer assignment runs in strictly $O(1)$ extra space.
- **Multi-Digit Number Formatting:** Writing the integer directly (e.g. setting $chars[k] = 12$) crashes or truncates because array cells store single characters. Iterating through the digits of `str(count)` writes each decimal place correctly.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The read runner $j$ advances from $0$ to $N$ across all groups without backtracking.
  - The write pointer $k$ advances at most $N$ times.
  - Converting run counts to digits takes $O(\log_{10} L) \le 4$ operations per run.
  - Total Time: $\mathcal{O}(N)$. For $N = 2000$, execution finishes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$. All transformations are performed directly within the input array with scalar index variables.
