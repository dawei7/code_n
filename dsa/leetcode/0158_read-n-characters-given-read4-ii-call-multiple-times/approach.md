## General

**Preserve characters fetched for a later call**

`read4` may advance the file pointer by more characters than the current
`read` call requests. If the file begins `"abcd"` and the caller asks for one
character, `read4` still fetches four. Returning `"a"` while discarding
`"bcd"` would make the next call start at the wrong logical position.

The solution therefore keeps a four-slot staging buffer as object state:

- `self.buf4` stores the most recently fetched block;
- `self.size` is the number of valid characters in that block;
- `self.i` is the index of the next valid character that has not yet been
  returned to a caller.

The unread portion is `self.buf4[self.i:self.size]`. These fields are created
in `__init__`, so they survive between calls to `read` on the same solution
object. At construction both counts are zero, meaning no buffered character is
available.

**Consume buffered data before touching the file**

Each `read(buf, n)` uses a local counter `j`, the number of characters written
for this particular call. The outer loop continues while `j < n`.

At its start, the method checks `self.i == self.size`. Equality means every
valid character from the previous block has been consumed. Only then does it
call `read4(self.buf4)`, save the returned count in `self.size`, and reset
`self.i` to zero.

This order is essential. Calling `read4` while `self.i < self.size` would
overwrite unread characters in the staging buffer. Since the file pointer has
already moved past them, those characters could never be recovered.

If a refill returns zero, the file is exhausted. The method breaks and returns
however many characters it supplied during this call. A return of one through
four creates a new valid interval `[0, self.size)`.

**Copy until either side reaches its limit**

The inner loop has two conditions: `j < n` and `self.i < self.size`.
For each iteration, it copies the next staged character into `buf[j]`, then
increments both indices.

The loop can stop for two distinct reasons:

- `j == n`: the caller has received its requested number. Any staged
  characters from `self.i` through `self.size - 1` remain untouched for the
  next call.
- `self.i == self.size`: the current staging block is exhausted. If the caller
  still needs more, control returns to the outer loop, which refills it.

Separating the requested count from the staging-buffer count prevents mixing
positions from different coordinate systems. `j` always starts at zero for a
new destination request, whereas `self.i` deliberately retains its old value
across requests.

**Trace multiple calls on one file**

Let the file be `"abc"` and the queries be `[1,2,1]`.

The first call starts with an empty staging buffer. `read4` fetches all three
characters, so `self.size = 3` and `self.i = 0`. The method copies `"a"`,
making `j = 1` and `self.i = 1`. The request is complete and returns one.
Crucially, `"bc"` remains in positions one and two.

The second call resets only local `j` to zero. Since
`self.i = 1 < self.size = 3`, it does not call `read4`; it copies `"b"` and
`"c"` from the preserved staging buffer. Both counters reach their respective
limits, and the method returns two.

The third call finds `self.i == self.size`, so it asks the file API for another
block. The file pointer is at EOF, `read4` returns zero, and the method returns
zero without writing the destination.

For queries `[4,1]` on the same file, the first call copies the three-character
short block and then performs a refill that returns zero before it can reach
four. It returns three. The second call may query EOF again and returns zero;
the results remain correct.

**State the cross-call invariant**

Before and after every `read` call:

- $0 \le \texttt{self.i} \le \texttt{self.size} \le 4$;
- positions from `self.i` up to, but excluding, `self.size` contain exactly the
  file characters already fetched but not yet returned;
- all file characters before that unread region have already been returned in
  order;
- the platform file pointer begins immediately after the valid staged block.

A refill is performed only when the unread region is empty, so overwriting the
buffer loses nothing. A copy removes exactly its first unread character and
delivers it next, preserving order. These operations maintain the invariant
for arbitrarily many valid calls.

When a call stops at `j == n`, it has written exactly `n` requested characters.
When it stops after a zero refill, every file character has already been
returned. Thus `j` is exactly the number the current call should report.

**Reset state per test case**

The Reference warns that class-level or static data can persist unexpectedly.
This source uses instance attributes initialized by `__init__`, so a fresh
`Solution` object resets the staging buffer and both counts. Reusing one object
within a test case preserves leftovers as required; creating a new object for a
new file prevents old leftovers from leaking into it.

## Complexity detail

For one call requesting `n` characters, let $k \le n$ be the number returned.
Each returned character is copied once. There is at most one constant-size
refill per four consumed characters plus a possible EOF check, so the call
takes $O(k+1)$ time, conventionally reported as $O(n)$.

Across many calls, each file character is still staged once and copied once.
No repeated scanning occurs.

The persistent buffer has exactly four positions and the method stores a fixed
number of counters. Auxiliary space is $O(1)$ regardless of the file length,
call count, or requested sizes. The caller-owned destination is excluded.
These bounds match the manifest.

## Alternatives and edge cases

- **Queue of leftovers:** A deque can express pending characters naturally, but its size never exceeds three here, so an indexed four-slot array is simpler and has the same $O(1)$ bound.
- **Single-call strategy:** Discarding the unused part of a fetched block works for ID 157 but is incorrect when this method may be called again.
- **Read one character per loop:** The competitive variant does this with the same persistent state; chunking through an inner loop reduces repeated branch checks.
- **Request smaller than remaining buffer:** No API call occurs, and the unused suffix remains for the next request.
- **Request spans several blocks:** The inner loop exhausts a block, and the outer loop refills until the request or file ends.
- **Short final block:** Its valid count prevents stale positions from being copied; leftovers can still survive to the next call.
- **Repeated calls after EOF:** They return zero; an optional persistent EOF flag could avoid repeated zero-result API calls.
- **Same destination object:** Each call writes from `buf[0]` as specified; persistent reader state is independent of the destination's earlier contents.
- **New test case:** Construct a new solution instance so old buffer indices do not persist across files.
- **Platform contract:** `read4` owns the file pointer and is supplied by the harness; only its returned prefix is valid.
