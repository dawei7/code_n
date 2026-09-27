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

The authored instances cover six distinct boundary shapes, and each one halts the loop for a different reason:

| Boundary shape | Instance | `read4` results | Return | Why the loop stops there |
|:---|:---|:---|:---|:---|
| File shorter than the request | `"abc"`, $n = 4$ | one call returning $3$ | $3$ | a partial block sets `eof`, and $\min(3, 4 - 0) = 3$ transfers every character that exists |
| Request shorter than the first block | `"abcd"`, $n = 2$ | one call returning $4$ | $2$ | $\min(4, 2) = 2$ copies `'a'` and `'b'`; `'c'` and `'d'` were read off the stream but are never delivered |
| Request ending exactly on a block boundary | `"abcde"`, $n = 4$ | one call returning $4$ | $4$ | `copied` reaches $n$ with the block fully transferred, so no second call is made and the stream stays positioned at `'e'` |
| Smallest possible request | `"Z"`, $n = 1$ | one call returning $1$ | $1$ | the single character satisfies $n$ and reports `eof` at the same time, so both stopping conditions agree |
| Request crossing blocks, partial final block | `"abcdefghijk"`, $n = 9$ | calls returning $4$, $4$, $3$ | $9$ | the third call delivers $3$ characters, `eof` is set, and $\min(3, 9 - 8) = 1$ stops at the ninth character while `'j'` and `'k'` are discarded |
| File length a multiple of $4$, still shorter than $n$ | 500-character file, $n = 1000$ | 125 calls returning $4$, then one call returning $0$ | $500$ | no call reports fewer than $4$ characters until the pointer reaches the end, so detecting that end costs one extra call delivering nothing |

---

## 5. Algorithmic Correctness

**Soundness.** `buf` receives only characters directly written by `read4`. Because $\text{to\_copy} = \min(\text{count}, n - \text{copied})$, `buf` is never overwritten beyond the requested length $n$, and stale leftover positions in `buf4` beyond index $\text{count} - 1$ are never read.

**Completeness.** If the file contains fewer than $n$ characters, `read4` returns $< 4$, triggering `eof = True` and halting with the exact number of characters available. If the file contains at least $n$ characters, the transfer condition terminates when `copied == n`.

---

## 6. Traps This Instance Exposes

- **Overwriting Destination Capacity:** Blindly copying all $\text{count}$ characters into `buf` when $\text{copied} + \text{count} > n$ causes buffer overflow in memory-constrained environments or writes past requested boundary $n$.
- **Ignoring Stale Buffer Characters:** If `read4` returns 2 characters on a partial block, indices 2 and 3 in `buf4` contain leftover characters from previous reads. Copying all 4 positions corrupts the destination with stale data.
- **Multiple Call Reusability (Distinction from LeetCode 158):** In LeetCode 157, `read` is called only **once**. Any uncopied characters left in `buf4` (like `'o', 'd', 'e'`) are discarded. In LeetCode 158, `read` is called repeatedly, requiring an internal persistent queue to preserve leftovers.

Each of the following plausible variations of the protocol breaks on one of the instances above; naming the failure makes the two stopping conditions and the transfer bound look necessary rather than arbitrary:

| Candidate rule | What it changes | Observable failure | Instance that exposes it |
|:---|:---|:---|:---|
| Transfer every delivered character | drops the $\min(\text{count}, n - \text{copied})$ bound | `buf` is written past the requested length whenever $n$ is not a multiple of $4$ | `"abcd"`, $n = 2$ writes four positions instead of two |
| Stop only when `count < 4` | drops the `copied == n` test | the loop keeps calling `read4` after the request is satisfied, consuming the next block for nothing; the count stays $4$ only because the transfer bound evaluates to $0$ | `"abcde"`, $n = 4$ spends a second call on `'e'` |
| Stop only when `copied == n` | drops the `count < 4` test | a file shorter than $n$ never terminates the loop, because every later call returns $0$ and adds nothing | `"abc"`, $n = 4$ spins on empty blocks |
| Ask for one character at a time | call the API once per requested character | each call still consumes up to $4$ stream characters, so three of every four are lost | `"abcdefghijk"`, $n = 9$ yields `'a'`, `'e'`, `'i'` — three characters instead of nine |
| Keep a leftover queue across calls | persists the unconsumed tail of `buf4`, as LeetCode 158 requires | correct here but dead state: `read` runs once, so nothing ever consults the queue | `"abcd"`, $n = 2$ queues `'c'` and `'d'` that no later call reads |

---

## 7. Complexity Derivation

The cost of a fixed $4$-character block API is best seen by counting, for every authored instance, how much the API delivered, how much the destination received, and how much was read off the stream and thrown away:

| Instance | $n$ | `read4` calls | Characters delivered | Characters copied into `buf` | Read but never delivered | Returned |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| `"Z"` | 1 | 1 | 1 | 1 | 0 | 1 |
| `"abcd"` | 2 | 1 | 4 | 2 | 2 | 2 |
| `"abc"` | 4 | 1 | 3 | 3 | 0 | 3 |
| `"abcde"` | 4 | 1 | 4 | 4 | 0 | 4 |
| `"abcde"` | 5 | 2 | 5 | 5 | 0 | 5 |
| `"abcdefghijk"` | 9 | 3 | 11 | 9 | 2 | 9 |
| `"abcdABCD1234"` | 12 | 3 | 12 | 12 | 0 | 12 |
| 500-character file | 1000 | 126 | 500 | 500 | 0 | 500 |

The discarded column is the price of a block granularity: a call cannot be undone, so any character of the final block beyond the requested length is lost to this invocation, and to the caller as well because `read` is not called again.

- **Time Complexity:** $O(n)$ time. At most $\lceil n / 4 \rceil$ API calls are made to `read4`, each copying up to 4 characters into `buf`.
- **Auxiliary Space Complexity:** $O(1)$ constant memory, requiring only the fixed 4-character array `buf4`.
