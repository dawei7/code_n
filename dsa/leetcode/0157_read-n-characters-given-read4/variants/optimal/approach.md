## General

**Bridge a four-character API to an arbitrary request**

The solution cannot inspect the file directly. Its only way to advance the
file pointer is `read4(buf4)`, which writes up to four consecutive characters
into a supplied temporary buffer and returns how many positions it filled.

The requested method has a different interface: place at most `n` characters
in `buf` and report how many were actually copied. The file may end before
`n`, and `n` may not be divisible by four. Therefore the method needs two
counts:

- `v`, the number returned by the most recent `read4`;
- `i`, the number of characters already copied into the destination.

The selected source allocates `buf4 = [0] * 4`. Its initial numeric values are
only placeholders; every position below the count returned by `read4` is
replaced with a real character before being read.

**Use a short block as the end-of-file signal**

The loop continues while `v >= 4`. Before the first call, `v` is set to five
only to enter the loop. It is not a claim that five characters were read.

After calling `read4(buf4)`, there are three possible results:

- four means a complete block was available, so the file may still contain
  more characters;
- one, two, or three means those characters are the final partial block;
- zero means the file pointer was already at end of file.

The contract of `read4` makes a return smaller than four an end-of-file signal.
After copying that partial result, the next loop check fails, so another API
call is unnecessary.

The loop does not use `i < n` as its outer condition. Instead, the inner copy
returns immediately when `i` reaches `n`. Either organization can work; here
the early return is the protection against placing too many characters in the
destination.

**Copy only the positions reported as valid**

For each API result `v`, the source iterates `j` from zero through `v - 1`.
Only those positions in `buf4` were written by the current call. Reading all
four positions after a short call would copy stale data left from an earlier
block, so the returned count must control the copy loop.

Each valid temporary character is assigned to `buf[i]`, then `i` is
incremented. If `i >= n`, the method returns `n` immediately. Since `i`
increases by exactly one after each successful assignment and begins at zero,
the first such event is exactly `i == n`; no destination position at index
`n` is written.

If the loop ends because `read4` returned fewer than four, then every remaining
file character has been copied unless the early limit return occurred. The
method returns `i`, the actual number copied.

**Why limited over-reading is acceptable here**

Suppose the file is `"abcde"` and `n = 3`. The first `read4` consumes `"abcd"`
from the underlying file. The method copies only `"abc"` and immediately
returns three; the fourth fetched character is discarded.

This would be a serious issue if the same solution object had to support a
second `read` call, because that later call would expect to receive `"d"`.
The local Reference explicitly guarantees that `read` is called only once per
test case. Consequently, unread temporary leftovers never need to be
preserved, and discarding up to three fetched characters after reaching `n` is
valid for this problem.

**Trace both stopping conditions**

For file `"abc"` and `n = 4`, the first API call returns three. The loop copies
`a`, `b`, and `c`; `i` becomes three. Because `v` is below four, the loop ends
and returns three. No uninitialized fourth buffer slot is copied.

For file `"abcde"` and `n = 5`, the first call returns four and fills the first
four destination positions. Since `v` is four, another iteration reads one
character, copies `e`, and then the short-block condition ends the loop. The
result is five.

For file `"abcdABCD1234"` and `n = 12`, three full blocks are read. The twelfth
copy makes `i` equal to `n`, so the method returns twelve from inside the third
copy loop.

If `n` is larger than the file length, the algorithm stops at the first short
read and returns the file length. If the file length is a multiple of four and
smaller than `n`, one additional `read4` call returns zero; it copies nothing,
then terminates. This extra constant-cost call is necessary because a full
block alone does not prove that it was the final block.

**Why the returned count matches the destination**

The invariant before every copy is that `buf[0:i]` contains exactly the first
`i` characters obtained from the file, in order, and $i \le n$. A `read4`
call produces the next consecutive characters because it owns the advancing
file pointer. The inner loop appends those characters to consecutive
destination positions, preserving order.

Reaching `n` proves exactly `n` characters were written. Reaching a short read
proves the file is exhausted after every reported character is copied.
Therefore the returned value is precisely the smaller of the requested count
and the available file length.

## Complexity detail

Let $k$ be the number of characters actually copied, where
$k \le n$. Every copied character is assigned once, and each `read4` call
accounts for at most four characters. The number of calls is at most
$\lceil k/4\rceil+1$, so time is $O(k)$ and therefore $O(n)$.

The temporary buffer always has four entries, and the counters occupy constant
storage. Excluding the required destination buffer, auxiliary space is $O(1)$.
These bounds match the manifest.

## Alternatives and edge cases

- **Direct block writes in pointer-based languages:** Full groups of four can be written directly into the correct destination offset, avoiding a second character-by-character copy; Python's given API still expects a separate list buffer.
- **Preserve leftover characters:** Required by the follow-up where `read` may be called repeatedly, but unnecessary under the single-call guarantee.
- **Read one character at a time conceptually:** Impossible because the only permitted file interface advances in blocks of up to four.
- **File shorter than `n`:** A short return is copied completely, then its size stops the loop.
- **File length divisible by four:** If more characters are requested, a final zero-length API call is needed to discover EOF.
- **`n` smaller than four:** One block may be fetched, but the early return prevents more than `n` destination writes.
- **Stale temporary positions:** Only indices below `v` are valid after a call; the loop correctly ignores all others.
- **Destination capacity:** The contract guarantees room for `n`, and the source never writes beyond index `n - 1`.
- **Single-call dependency:** Fetched but uncopied characters are discarded; this solution must not be reused unchanged for multiple `read` calls.
- **Platform API:** `read4` and its file pointer are harness-provided; the solution should not attempt to manipulate the file directly.
