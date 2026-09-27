# Guided Example: Read N Characters Given read4 II - Call Multiple Times

We trace the step-by-step persistent internal buffer queueing and multi-call state preservation across successive read requests:

- **Input:** $\text{file} = \text{"abc"}$, successive calls $\text{read}(1), \, \text{read}(2), \, \text{read}(1)$
- **Required outputs:** $[1, 2, 0]$ (Emitting buffers `['a']`, `['b', 'c']`, `[]`)
- **Multi-Chunk Refill Instance:** $\text{file} = \text{"abcdefghijkl"}$, calls $\text{read}(5), \, \text{read}(5) \implies [5, 5]$

This instance demonstrates designing a persistent object-level circular/linear queue (`buf4`, `head`, `tail`) to prevent data loss when `read4` reads ahead past the caller's immediate request $n$, synchronizes multiple sequential consumer calls, and achieves $O(N)$ amortized time with $O(1)$ auxiliary storage.

---

## 1. Instance & Teaching Goal

Given a file with content `"abc"`, an external caller executes three sequential calls on the same reader instance:
1. `read(buf, 1)`: asks for 1 character.
2. `read(buf, 2)`: asks for 2 characters.
3. `read(buf, 1)`: asks for 1 character.

Because the underlying OS/file primitive only supports `read4`:
- Calling `read4` during call 1 reads all 3 available characters `['a', 'b', 'c']`.
- Call 1 only needs 1 character (`'a'`).
- If characters `'b'` and `'c'` are discarded, call 2 will call `read4` again and encounter EOF, permanently losing `'b'` and `'c'`!

To support multiple sequential invocations, the reader class must maintain persistent internal state:
- An internal 4-slot buffer `buf4`.
- A read pointer `head` and boundary pointer `tail`.
Unconsumed characters remain queued in `buf4[head : tail]` between method calls, ensuring zero character loss across independent `read` requests.

---

## 2. Conceptual Foundation & Invariants

### Persistent Buffer Queue Architecture
Define persistent instance variables in `__init__`:
- `self.buf4 = [''] * 4`: internal hardware staging array.
- `self.head = 0`: index of next unconsumed character in `self.buf4`.
- `self.tail = 0`: count of valid characters currently in `self.buf4`.

### The Multi-Call Read Protocol (`read(buf, n)`)
Initialize local consumer counter `copied = 0`.

While `copied < n`:
1. **Check Persistent Buffer Depletion:**
   If `self.head == self.tail`:
   - All previously fetched characters have been consumed.
   - Refill from stream:
     $$
     \text{self.tail} = \text{read4}(\text{self.buf4})
     $$
     $$
     \text{self.head} = 0
     $$
   - If `self.tail == 0`:
     End-Of-File reached. Break out of loop.
2. **Drain Persistent Buffer to Destination:**
   While `copied < n` and `self.head < self.tail`:
   $$
   \text{buf}[\text{copied}] = \text{self.buf4}[\text{self.head}]
   $$
   $$
   \text{copied} \leftarrow \text{copied} + 1
   $$
   $$
   \text{self.head} \leftarrow \text{self.head} + 1
   $$

Return `copied`.

> **Invariant.** Between successive calls to `read`, the interval $\text{buf4}[\text{head} : \text{tail}]$ contains all characters read from the file stream that have not yet been delivered to the caller, in exact stream order.

---

## 3. Step-by-Step Worked Execution

We trace three calls on $\text{file} = \text{"abc"}$:
Initial state: `head = 0, tail = 0`.

---

### Call 1: `read(buf, n = 1)`
- `copied = 0, n = 1`.
- `head == tail == 0` (internal buffer empty).
- **Refill:** Call `read4(self.buf4)`.
  - Reads `['a', 'b', 'c']`.
  - Updates: `self.tail = 3, self.head = 0`.
- **Drain 1 Character:**
  - `buf[0] = self.buf4[0] = 'a'`.
  - `copied = 1`.
  - `self.head = 1`.
- Loop condition: $\text{copied} == n == 1$.
- Call 1 terminates!
- **Persistent State Retained:**
  - `self.buf4 = ['a', 'b', 'c', '']`
  - `self.head = 1, self.tail = 3` (chars `'b'` and `'c'` preserved!)
- Return: $\mathbf{1}$ (with `buf = ['a']`).

---

### Call 2: `read(buf, n = 2)`
- `copied = 0, n = 2`.
- `head = 1 < tail = 3` (internal buffer has 2 pending characters!).
- **Drain Directly from Persistent Buffer (No `read4` call!):**
  - Iteration 1:
    - `buf[0] = self.buf4[1] = 'b'`.
    - `copied = 1, self.head = 2`.
  - Iteration 2:
    - `buf[1] = self.buf4[2] = 'c'`.
    - `copied = 2, self.head = 3`.
- Loop condition: $\text{copied} == n == 2$.
- Call 2 terminates!
- **Persistent State Retained:**
  - `self.head = 3, self.tail = 3` (buffer now empty).
- Return: $\mathbf{2}$ (with `buf = ['b', 'c']`).

---

### Call 3: `read(buf, n = 1)`
- `copied = 0, n = 1`.
- `head == tail == 3` (internal buffer empty).
- **Refill:** Call `read4(self.buf4)`.
  - Stream is at EOF.
  - Return: $\text{self.tail} = 0, \, \text{self.head} = 0$.
- Check: $\text{self.tail} == 0 \implies$ EOF!
- Loop breaks with $\text{copied} = 0$.
- Return: $\mathbf{0}$ (with `buf = []`).

---

## 4. Complete Execution Trace

```text
Stream Content: "abc"
Initial:        head=0, tail=0

Call 1: read(buf, 1)
  -> Refill: read4 -> tail=3, head=0 (['a', 'b', 'c'])
  -> Drain 1 char: buf[0]='a', head=1
  -> Return 1. Leftovers: head=1, tail=3 ('b', 'c')

Call 2: read(buf, 2)
  -> Drain 2 chars: buf[0]='b', buf[1]='c', head=3
  -> Return 2. Leftovers: head=3, tail=3 (empty)

Call 3: read(buf, 1)
  -> Refill: read4 -> tail=0 (EOF)
  -> Return 0
```

| Invoc. | Request $n$ | Initial Buffer State | Action Taken | Chars Transferred | New `(head, tail)` | Return Value |
|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| **Call 1** | 1 | `head=0, tail=0` | Refill via `read4` (`['a','b','c']`) | `buf[0] = 'a'` | `head=1, tail=3` | **1** |
| **Call 2** | 2 | `head=1, tail=3` | Drain existing buffer (no I/O) | `buf[0]='b', buf[1]='c'` | `head=3, tail=3` | **2** |
| **Call 3** | 1 | `head=3, tail=3` | Refill via `read4` (returns 0) | None (EOF) | `head=0, tail=0` | **0** |

### Queue carry-over on a Second Instance

The same protocol on $\text{file} = \text{"abcdefghij"}$ with requests $[2, 1, 4, 3]$ shows how the queue absorbs the mismatch between three primitive reads and four consumer calls:

| Invocation | Request $n$ | Delivered | Queued on entry | `read4` calls during the call | Queued on exit | Stream offset after the call |
|:---:|:---:|:---|:---|:---|:---|:---:|
| `read(buf, 2)` | 2 | `"ab"` | empty | 1, delivering `a b c d` | `buf4[2:4] = "cd"` | 4 |
| `read(buf, 1)` | 1 | `"c"` | `buf4[2:4] = "cd"` | 0, the queue is drained first | `buf4[3:4] = "d"` | 4 |
| `read(buf, 4)` | 4 | `"defg"` | `buf4[3:4] = "d"` | 1, delivering `e f g h` | `buf4[3:4] = "h"` | 8 |
| `read(buf, 3)` | 3 | `"hij"` | `buf4[3:4] = "h"` | 1, delivering `i j` | empty, `head == tail` | 10 |

Three primitive reads deliver all ten characters across four calls: the queue spends the surplus of a four-character block on the requests that follow, and no character is read twice or skipped.

### Boundary Shapes Covered by the Authored Instances

| Boundary shape | Authored instance | Returned values | Why no special case is needed |
|:---|:---|:---|:---|
| First request exceeds the file | `"abc"`, requests `[4, 1]` | $3$, then $0$ | the first call drains the three-character block and the next refill reports $0$, which breaks the loop; the second call finds an empty queue and refills to $0$ again |
| A later call reaches EOF and stays there | `"xy"`, requests $[1, 5, 1]$ | $1$, $1$, $0$ | the second call takes `'y'` from the queue and then pays one refill reporting $0$, so it returns $1$ although $n = 5$ |
| Requests that exactly partition the file | `"abcdef"`, requests $[1, 3, 2]$ | $1$, $3$, $2$ | each request consumes exactly its own count: the first leaves `'bcd'` queued, the second empties that surplus, the third leaves `head == tail` |
| A call ending exactly on a block boundary | `"abcde"`, requests $[4, 1]$ | $4$, $1$ | the first call drains the whole block and queues nothing, so the second call must refill and receives the single remaining character |
| Smallest instance | `"Z"`, requests $[1]$ | $1$ | one refill delivers one character, which is drained at once and leaves `head` and `tail` equal at $1$ |
| Maximum instance | 500-character file, requests $[1, 3, 4, 7, 8, 15, 31, 63, 128, 500]$ | $1, 3, 4, 7, 8, 15, 31, 63, 128, 240$ | the last request asks for $500$ but only $240$ characters remain, so it returns $240$; the ten calls cost $126$ refills, one more than the $125$ full blocks because the file ends exactly on a block boundary and only a refill returning $0$ proves exhaustion |

---

## 5. Algorithmic Correctness

**Soundness.** Characters are delivered to the destination buffer strictly in the order they were produced by `read4`. Because unused characters remain in `self.buf4` indexed by `self.head` between function calls, no data is dropped or duplicated.

**Completeness.** Every character in the underlying file is consumed exactly once. When `self.head == self.tail`, the buffer is replenished from the source stream until the stream reports `0` (EOF), ensuring all available characters are delivered.

---

## 6. Traps This Instance Exposes

- **Calling `read4` Before Draining:** If a new `read` call immediately calls `read4` without checking whether `self.head < self.tail`, unconsumed characters from the previous read are permanently overwritten and lost!
- **Persistent State Scope:** In LeetCode 157, `read` is called once, so local variables suffice. In LeetCode 158, buffer pointers must be stored as object attributes (`self.head`, `self.tail`) to survive between calls.
- **Multiple Refills in a Single Call:** If a caller asks for $n = 10$, a single call must be able to drain the remaining 2 characters, refill 4 characters, drain them, and refill again. The outer `while copied < n` handles multi-chunk requests naturally.

The alternative designs below all look reasonable in isolation; the sample instance separates them, which is why the queue check has to come before the refill:

| Candidate design | Mechanism | Consequence on `"abc"` with requests `[1, 2, 1]` | Verdict |
|:---|:---|:---|:---|
| Discard the unconsumed tail when the call returns | keep the staging array local to the call and forget `head`, `tail` between calls | returns $1$, then $0$, then $0$: `'b'` and `'c'` are unrecoverable | correct for a single invocation, wrong here — two characters are lost |
| Refill unconditionally at the start of every call | call `read4` before checking whether anything is still queued | the second call sets `tail` to $0$ and makes `'b'`, `'c'` unreachable | survives only when every request is a multiple of four |
| Hold pending characters in a growable queue | replace the fixed array and two indices with a dynamically sized container | returns the same $1$, $2$, $0$ | identical behaviour, but pending characters can never exceed three, so the growth is never used |
| Use modular indices in a circular buffer | wrap `head` arithmetically instead of resetting it to $0$ at each refill | returns the same $1$, $2$, $0$ | guards against a refill into a non-empty buffer, which this protocol never performs |
| Hand the surplus back to the caller | write every character the block delivered, ignoring $n$ | the first call writes `'a'`, `'b'`, `'c'` for $n = 1$ and reports $3$ | breaks the contract twice: the destination is written past the requested length and the return value no longer answers the request |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$ amortized time, where $N$ is the total number of characters read across all calls. Each character is fetched by `read4` once and copied into `buf` once ($O(1)$ operations per character).
- **Auxiliary Space Complexity:** $O(1)$ constant auxiliary memory, using a single 4-element array `buf4` and two pointer integers `head` and `tail`.
