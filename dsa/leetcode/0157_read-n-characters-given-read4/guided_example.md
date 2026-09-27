# Guided Example: Read N Characters Given Read4

We trace the step-by-step 4-byte chunked file reading, temporary buffer transfer, and EOF boundary detection on representative file stream instances:

- **Input:** $\text{file} = \text{"leetcode"}$, $n = 5$
- **Required output:** $5$ (Buffer populated with `['l', 'e', 'e', 't', 'c']`)
- **EOF Before Limit Instance:** $\text{file} = \text{"abc"}$, $n = 4 \implies 3$ (Buffer populated with `['a', 'b', 'c']`)

This instance demonstrates bridging a fixed 4-character chunking API (`read4`) to an arbitrary length destination buffer, managing buffer capacity bounds ($\min(\text{count}, n - \text{copied})$), detecting End-Of-File when `count < 4`, and executing in $O(N)$ time with $O(1)$ auxiliary storage.

---

## 1. Instance & Teaching Goal

You are given a file and can only read it through the API `read4(buf4)`:
- `read4` reads up to 4 consecutive characters from the underlying file stream into temporary buffer `buf4` and returns the actual number of characters read ($0 \dots 4$).
Implement `read(buf, n)` to read $n$ characters into destination buffer `buf` and return the total number of characters copied.

On $\text{file} = \text{"leetcode"}$ with $n = 5$:
1. Call 1 to `read4`: reads $4$ characters `['l', 'e', 'e', 't']`.
   All $4$ characters are needed. Copy into `buf[0...3]`. Total copied $= 4$.
2. Call 2 to `read4`: reads $4$ characters `['c', 'o', 'd', 'e']`.
   Only $5 - 4 = 1$ character is needed. Copy `buf4[0]` (`'c'`) into `buf[4]`. Total copied $= 5 == n$.
Halt reading and return $5$.

Directly reading $n$ characters is disallowed because file access must obey the 4-byte hardware block abstraction.
The buffer transfer invariant: at each chunk iteration, copy exactly $\min(\text{count}, n - \text{copied})$ characters from `buf4` to `buf`. If `count < 4` or `copied == n`, the read terminates cleanly.

---

## 2. Conceptual Foundation & Invariants

### Block Transfer Protocol
Maintain:
- `buf4 = [''] * 4`: reusable 4-character chunk buffer.
- `copied = 0`: count of valid characters transferred to destination `buf`.
- `eof = False`: flag indicating file stream exhaustion.

While `copied < n` and `not eof`:
1. **Fetch Next Chunk:**
   $$
   \text{count} = \text{read4}(\text{buf4})
   $$
2. **Detect End-Of-File:**
   If $\text{count} < 4$:
   $$
   \text{eof} = \text{True}
   $$
3. **Determine Transfer Quantity:**
   Calculate how many characters to copy from `buf4`:
   $$
   \text{to\_copy} = \min(\text{count}, \, n - \text{copied})
   $$
4. **Transfer Bytes:**
   For $j$ from $0$ to $\text{to\_copy} - 1$:
   $$
   \text{buf}[\text{copied}] = \text{buf4}[j]
   $$
   $$
   \text{copied} \leftarrow \text{copied} + 1
   $$

Return `copied`.

> **Invariant.** After processing each chunk, `copied` represents the exact number of consecutive file stream characters written to `buf`, and `buf` is never written past index $n - 1$.

---

## 3. Step-by-Step Worked Execution

We trace the algorithm on $\text{file} = \text{"leetcode"}$ with $n = 5$:

### Initial State
- `buf4 = ['', '', '', '']`
- `copied = 0`, $n = 5$.

---

### Chunk 1: Fetch First 4 Bytes
- Call API: $\text{count} = \text{read4}(\text{buf4})$.
- Stream reads: `['l', 'e', 'e', 't']`. Return $\text{count} = 4$.
- EOF check: $4 \ge 4 \implies$ not EOF.
- Transfer bound:
  $$
  \text{to\_copy} = \min(4, \, 5 - 0) = \min(4, 5) = 4
  $$
- Copy $4$ characters into `buf`:
  - `buf[0] = 'l'`
  - `buf[1] = 'e'`
  - `buf[2] = 'e'`
  - `buf[3] = 't'`
  - `copied = 4`.
- Condition: $\text{copied} = 4 < 5$. Continue loop.

---

### Chunk 2: Fetch Second 4 Bytes
- Call API: $\text{count} = \text{read4}(\text{buf4})$.
- Stream reads: `['c', 'o', 'd', 'e']`. Return $\text{count} = 4$.
- EOF check: $4 \ge 4 \implies$ not EOF.
- Transfer bound:
  $$
  \text{to\_copy} = \min(4, \, 5 - 4) = \min(4, 1) = \mathbf{1}
  $$
- Copy $1$ character into `buf`:
  - `buf[4] = buf4[0] = 'c'`
  - `copied = 4 + 1 = \mathbf{5}`.
- Condition check: $\text{copied} == n == 5$.

Loop terminates immediately!
Characters `'o', 'd', 'e'` remain in `buf4` uncopied.
Return `copied = 5`.

---

## 4. Complete Execution Trace

```text
File Stream:   [ l   e   e   t ] [ c   o   d   e ]
Chunk 1:       read4 -> 4 chars. Copied 4. (copied = 4 / 5)
Chunk 2:       read4 -> 4 chars. Copied 1. (copied = 5 / 5) -> LIMIT REACHED!
Result:        buf = ['l', 'e', 'e', 't', 'c'], return 5
```

| Chunk Call | Stream Offset | `read4` Result | Chars in `buf4` | `to_copy` ($\min(\text{count}, n - \text{copied})$) | Chars Written to `buf` | Updated `copied` | Loop Status |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 0 | 4 | `['l', 'e', 'e', 't']` | $\min(4, 5) = 4$ | `buf[0..3] = ['l','e','e','t']` | 4 | Continue ($4 < 5$) |
| **2** | **4** | **4** | **`['c', 'o', 'd', 'e']`** | **$\min(4, 1) = 1$** | **`buf[4] = 'c'`** | **5** | **Halt ($5 == n$)** |
| End | - | - | - | - | - | **5** | **Return 5** |

### Contrast: File Shorter than $n$ ($\text{file} = \text{"abc"}, n = 4$)
- Chunk 1: $\text{count} = \text{read4}(\text{buf4})$ returns $3$.
- $\text{count} < 4 \implies$ EOF encountered!
- $\text{to\_copy} = \min(3, 4 - 0) = 3$. Writes `['a', 'b', 'c']`.
- `copied = 3`. EOF terminates loop.
- Return $3$.

---

## 5. Algorithmic Correctness

**Soundness.** `buf` receives only characters directly written by `read4`. Because $\text{to\_copy} = \min(\text{count}, n - \text{copied})$, `buf` is never overwritten beyond the requested length $n$, and stale leftover positions in `buf4` beyond index $\text{count} - 1$ are never read.

**Completeness.** If the file contains fewer than $n$ characters, `read4` returns $< 4$, triggering `eof = True` and halting with the exact number of characters available. If the file contains at least $n$ characters, the transfer condition terminates when `copied == n`.

---

## 6. Traps This Instance Exposes

- **Overwriting Destination Capacity:** Blindly copying all $\text{count}$ characters into `buf` when $\text{copied} + \text{count} > n$ causes buffer overflow in memory-constrained environments or writes past requested boundary $n$.
- **Ignoring Stale Buffer Characters:** If `read4` returns 2 characters on a partial block, indices 2 and 3 in `buf4` contain leftover characters from previous reads. Copying all 4 positions corrupts the destination with stale data.
- **Multiple Call Reusability (Distinction from LeetCode 158):** In LeetCode 157, `read` is called only **once**. Any uncopied characters left in `buf4` (like `'o', 'd', 'e'`) are discarded. In LeetCode 158, `read` is called repeatedly, requiring an internal persistent queue to preserve leftovers.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$ time. At most $\lceil n / 4 \rceil$ API calls are made to `read4`, each copying up to 4 characters into `buf`.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, requiring only the fixed 4-character array `buf4`.
