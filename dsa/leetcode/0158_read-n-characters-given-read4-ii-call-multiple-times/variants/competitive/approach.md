## General

**Turn `read4` into a persistent four-character stream**

The competitive solution maintains three private instance fields:
`__buf4`, `__i4`, and `__n4`. Their double-underscore names are Python name
mangling, which discourages accidental access from outside the class; it does
not change the algorithm.

`__n4` says how many entries of `__buf4` were filled by the most recent
`read4`. `__i4` identifies the next one not yet delivered. Thus a buffered
character exists exactly when `__i4 < __n4`.

These fields persist across calls. That persistence is the essential change
from the single-call version: if an API call fetches four characters but the
current request uses only one, the other three must be returned by later
requests before the file API is called again.

**Choose one of two actions per output character**

The local variable `i` counts how many characters have been written during the
current `read`. While `i < n`, the code first asks whether a staged character
is available.

If `__i4 < __n4`, it copies `__buf4[__i4]` to `buf[i]`, then increments both
indices. This consumes exactly one buffered character and places it in the next
requested destination position.

Otherwise, the previous staged block is empty or fully consumed. The code
calls `read4(__buf4)` and stores the result in `__n4`. A positive result resets
`__i4` to zero so the next loop iteration can consume the newly filled prefix.
A zero result means EOF, so the method breaks and returns the current `i`.

The refill branch does not copy immediately. It returns to the top of the loop,
where the normal available-character branch handles the first new character.
This keeps all copy logic in one place and makes the state transition explicit.

**Why resetting the read index is conditional**

When a refill succeeds, `__i4` must become zero because the valid region now
starts at the beginning of the overwritten array.

When it returns zero, the method breaks immediately, so the old value of
`__i4` is irrelevant for this call. On a later call, the test
`__i4 < __n4` is false because `__n4` is zero and `__i4` is nonnegative; the
method asks `read4` again and returns zero again. Resetting it on EOF would also
work, but is not required for correctness.

**Follow the `[1,2,1]` query sequence**

For file `"abc"`, construction begins with an empty valid region:
`__i4 = __n4 = 0`.

The first request for one character refills. The API returns three, so
`__n4 = 3` and `__i4 = 0`. On the next loop pass it copies `"a"` and advances
`__i4` to one. Local `i` reaches one, and the method returns.

The second request sets only local `i` back to zero. The private indices still
describe `"bc"` as unread. Two loop iterations copy them without advancing the
file pointer. The method returns two with `__i4 = __n4 = 3`.

The third request sees no staged character and refills. The API returns zero,
so it breaks and returns zero. No character has been lost or repeated.

**Maintain the stream invariant**

At the start of each loop:

- `buf[0:i]` contains the first `i` characters assigned to this call;
- `__buf4[__i4:__n4]` contains, in order, every fetched character not yet
  assigned to any call;
- the file pointer is immediately after the most recently fetched valid block.

Consuming a character advances both the destination progress and the unread
buffer boundary by one. Refilling is allowed only when the unread slice is
empty, so it cannot overwrite pending data. A zero refill proves there is no
next stream character.

Therefore the method returns exactly `n` if that many stream characters remain,
or the smaller number available before EOF. Since object fields survive, the
same reasoning continues seamlessly at the next call.

**Examine the file's custom API scaffold**

Like the competitive source for ID 157, this file includes a top-level
`read4` simulation based on global `file_content`. It copies at most four
characters and removes them from that global string.

That helper requires `file_content` to be initialized externally; otherwise it
raises `NameError`. On the native platform, `read4` is already provided, so a
submission should use the harness API rather than replace it. The persistent
buffering algorithm in `Solution` is valid with any conforming provider, while
the top-level helper is environment-specific scaffolding.

**Keep test cases isolated**

All reader state is initialized in `__init__`, not at class scope. A single
instance must be reused for all queries against one file so it can preserve
leftovers. A fresh instance should be constructed for a different test case,
resetting `__buf4`, `__i4`, and `__n4`.

## Complexity detail

For a call that returns $k \le n$ characters, each character goes through one
constant-time loop iteration. Every successful refill supplies up to four
future iterations, and there can be one final unsuccessful refill. The time is
$O(k+1)$ and is reported as $O(n)$ for the requested limit.

Across a sequence of calls, buffering does not duplicate work: each file
character is fetched once and copied once.

The private array always has four entries, and all indices are scalar.
Auxiliary space is $O(1)$. Unused capacity in the required destination buffer
does not count against the solution. These bounds match the manifest.

## Alternatives and edge cases

- **Chunk-copy inner loop:** Copy all possible staged characters in one nested loop, as the optimal variant does. It has the same asymptotic behavior and may execute fewer branch checks.
- **Deque for pending characters:** Correct and expressive, but the pending amount is bounded by three, so it offers no asymptotic benefit.
- **Discard the unused suffix:** Incorrect here because a later `read` call must receive it.
- **Small request:** It may leave most of a four-character block pending; the private indices preserve that suffix.
- **Large request:** The loop alternates between consuming blocks and refilling until `n` or EOF.
- **Short final block:** Only indices below `__n4` are considered valid.
- **Calls after EOF:** They can invoke `read4` again and return zero; an EOF flag could avoid that harmless repeated call.
- **Same `buf` across calls:** The method begins writing at index zero on each call, while its file-stream position remains in object state.
- **Different test cases:** Reusing static state would be wrong; the constructor correctly establishes fresh instance state.
- **Custom `read4` helper:** Its global dependency is not self-contained and should be regarded as local harness code.
