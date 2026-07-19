## General
**`read4` exposes the file only in bounded sequential chunks**

Allocate one fixed four-character temporary buffer. While the caller still needs characters, invoke `read4(temp)`. It writes the next zero through four file characters in order and returns that count; no random access or rewind is available.

**A primitive chunk may be larger than the caller's remaining capacity**

Copy exactly `min(read_count, n - copied)` temporary characters into the caller buffer, starting at its current written count. This prevents writing beyond `n` when the final primitive call overreads the request.

Because this version invokes `read` only once, unused characters from that final chunk never need to serve a later request and may be discarded. That assumption is the decisive difference from problem 158.

**A short primitive read proves EOF after its returned characters**

A zero count means EOF was already reached. A positive count smaller than four means those are the final available characters; copy the permitted portion and stop rather than issuing a redundant primitive call. A full count of four may or may not be the final chunk, so continue only if the request remains unfilled.

**Copied output is always the exact file prefix required so far**

Before each primitive call, the output contains exactly the first `copied` file characters, where `copied <= n`. Each iteration extends that prefix without exceeding the request.

**Every copied chunk extends the same file prefix**

`read4` exposes consecutive file characters in their original order. Before each primitive call, the output already contains exactly the first `copied` characters. Copying at most `n - copied` characters from the next chunk extends that prefix without skipping, reordering, or exceeding the request.

The loop ends only when $n$ characters have been copied or `read4` reports the end of the file. The output is therefore exactly the first `min(n, file_length)` characters.

## Complexity detail
At most $\left\lceil n / 4 \right\rceil$ useful primitive calls and `n` character copies occur, giving $O(n)$ time. The native algorithm uses a fixed four-character temporary buffer, or $O(1)$ auxiliary space beyond the caller's output.

## Alternatives and edge cases
- **Call `read4` once:** fails whenever $n > 4$.
- **Copy every returned character:** can write beyond the requested `n`.
- **Persist surplus characters:** is unnecessary for this single-call version but becomes essential in Problem 158.
- The file may be empty, `n` may be zero, and the final primitive read may return one to three characters.
- A request smaller than four uses at most one primitive call and copies only its requested prefix.
