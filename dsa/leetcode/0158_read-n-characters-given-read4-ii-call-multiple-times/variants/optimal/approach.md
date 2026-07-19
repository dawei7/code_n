## General
**Primitive-buffer state belongs to the reader object, not one call**

Persist a four-character array, `cache_size`, and `cache_index` on the reader instance. The unread cached range is `[cache_index, cache_size)`. Local output count resets for each `read`, but these fields must survive so a later call resumes after exactly the character previously returned.

**Refill only when no unread fetched character remains**

For each request, if `cache_index < cache_size`, copy from the cache first. Only when the indices are equal may `read4` overwrite the cache with a new chunk; then reset `cache_index = 0` and set `cache_size` to the returned count.

Copy one or several cached characters until the request is full or the cache empties. A zero-sized refill proves EOF and ends the call.

**Stopping mid-cache preserves exact stream position**

If a refill supplies more characters than the current call needs, stop with `cache_index < cache_size`. The file primitive has already advanced past the whole chunk, but the logical reader position sits at that saved cache index. The next call must consume this suffix before fetching again.

A short read indicates the primitive reached EOF, yet its returned cached characters must still be delivered across current or future requests before all later calls return empty.

**Logical unread stream is cached suffix plus unfetched file suffix**

At every point, the unread file stream is exactly the unread suffix of the cache followed by the portion not yet fetched through `read4`. Output across all calls is therefore a contiguous prefix of the original file with no omissions or repetitions.

**Trace one overread across three calls**

For content `abcdef` and requests `[1,3,2]`, the first `read4` caches `abcd` and returns only `a`, leaving index one. The second call consumes `bcd` without a refill. The third refills `ef`, returns both, and records that EOF has no remaining cached data.

**The persistent cache preserves stream position across calls**

At the start of every public `read` call, the unconsumed cache suffix is exactly the next part of the file that has been fetched but not returned. Characters leave that suffix in order and each cache position is consumed once. A new `read4` call occurs only after the suffix is empty, so refills continue from the correct underlying file position.

The method stops after satisfying the current request or after both EOF and an empty cache. Thus each call returns the next available stream segment, while any surplus characters remain intact for the following call.

## Complexity detail
Across calls, each returned or cached character is copied a constant number of times, giving $O(n)$ time for `n` total consumed characters. The persistent cache holds at most four characters, so auxiliary space is $O(1)$ beyond output buffers.

## Alternatives and edge cases
- **Use the single-call algorithm independently:** loses over-read characters between calls.
- **Read one character at a time from fresh `read4` calls:** still loses the other three characters and makes correct stream position impossible.
- **Cache the whole remaining file:** is correct but violates constant auxiliary space.
- A zero-length request must not consume cached or file characters. Requests may end within any cached chunk.
- Once EOF is reached and cached characters are exhausted, every later call returns zero characters without changing logical position.
