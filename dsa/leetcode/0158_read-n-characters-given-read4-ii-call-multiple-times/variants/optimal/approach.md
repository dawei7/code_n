## General

**Keep unread primitive output on the reader instance**

The same `Solution` object serves every request, so its four-character `temporary` buffer, `available` count, and
`position` must persist between calls. The unread cached interval is `temporary[position:available]`; `copied` is
local to one public `read` call.

Consume cached characters before requesting more input. Only when `position == available` may `read4` overwrite the
temporary buffer. A refill stores its returned count in `available`, resets `position` to zero, and stops the current
call if no characters remain at EOF.

The inner loop copies cached characters in order until either the current destination reaches `n` characters or the
cache is exhausted. If the request ends first, the saved `position` leaves the unused suffix intact for the next
call. Although `read4` has already advanced past its entire chunk, that cached suffix therefore remains the next
logical part of the stream.

At every point, the unread logical stream is exactly the cached suffix followed by the portion not yet fetched by
`read4`. Copying advances only through the first component, and refilling occurs only when it is empty, so no
character is skipped or duplicated across calls. Each request returns the next available prefix up to its requested
length.

The app-local adapter installs an advancing `read4`, creates one persistent `Solution`, and invokes it for every
request in the batch, matching the lifetime of the native reader state.

## Complexity detail

Across any request sequence, each fetched character enters the fixed buffer once and is copied to an output once.
For $n$ total returned characters, the total time is $O(n)$, plus one constant-time EOF check per request after the
file is exhausted. Each individual call takes $O(k)$ for the $k$ characters it returns. The four-character cache and
three counters use $O(1)$ auxiliary space beyond output buffers.

## Alternatives and edge cases

- **Reuse the single-call solution independently:** discards characters fetched beyond one request and loses the
  logical stream position.
- **Call `read4` for every requested character:** consumes and loses the other characters in each primitive chunk.
- **Cache the entire unread file:** is correct but uses $O(n)$ auxiliary storage instead of a fixed four-character
  buffer.
- A request may stop at any position inside a cached chunk, including immediately after its first character.
- A short final primitive read can leave characters for a later request before EOF is observed again.
- After EOF and cache exhaustion, later calls return an empty result; the implementation may make another harmless
  zero-length `read4` call to confirm EOF.
