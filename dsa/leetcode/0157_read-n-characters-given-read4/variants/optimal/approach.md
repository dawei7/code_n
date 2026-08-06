## General

**Consume the file through one fixed four-character buffer**

The candidate allocates a temporary buffer of length four and repeatedly calls `read4`. Each call exposes the next
zero to four file characters and advances the source position. `copied` records how many characters already occupy
the caller's destination.

After a call returns `available`, copy only `min(available, n - copied)` characters into the destination. This cap
matters when the final primitive call reads beyond the remaining request. The candidate uses the conventional loop
variable `i` for these positions and advances `copied` by the number actually written.

A zero return means the file was already exhausted. A positive return below four includes the final file
characters, so the method stops after copying them. A full chunk may be followed by more input, and the loop
continues only while fewer than `n` characters have been written.

Before every primitive call, the destination contains exactly the first `copied` file characters in order. Copying
a prefix of the next sequential chunk preserves that property and never exceeds the request. The loop therefore
returns exactly the first `min(n, file_length)` characters. Because `read` is called only once, any surplus consumed
by the final `read4` call never needs to be retained for a future request.

The app-local adapter installs an equivalent advancing `read4`, invokes the same `Solution.read` method, and returns
the populated destination prefix as a string.

## Complexity detail

Let $m = \min(n, \text{file length})$. The method copies $m$ characters and makes at most
$\lceil m / 4 \rceil + 1$ primitive calls, where the possible extra call detects end of file. Its time is $O(n)$
under the required upper bound. The native method uses one four-character temporary buffer, so auxiliary space is
$O(1)$ beyond the caller-owned output; the app adapter's returned buffer is output storage.

## Alternatives and edge cases

- **Call `read4` once:** fails whenever the requested prefix extends beyond the first four file characters.
- **Copy every returned character:** can write past the requested count when fewer than four positions remain.
- **Persist surplus characters:** is unnecessary for this single-call contract but becomes required in problem 158.
- When `n` exceeds the file length, a short chunk or a subsequent zero return terminates the read at EOF.
- A request smaller than four may consume one full primitive chunk but copies only the requested prefix.
- A file length divisible by four can require one final zero-length primitive call when `n` is larger than the file.
