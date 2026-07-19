## General
**Let one pointer read and one pointer own the compacted prefix**

The first value is always unique, so set `write = 1`. Scan subsequent values with a read pointer. Whenever the current value differs from `nums[write - 1]`, copy it to `nums[write]` and advance `write`. Equal values are skipped.

The app returns `nums[:write]` for observable testing. LeetCode's platform method performs the same writes and returns `write` because its judge inspects that prefix in place.

**Sorted adjacency makes the last written value sufficient**

Before each read position, `nums[:write]` contains exactly the distinct values from the processed input prefix, in their original sorted order, and `nums[write - 1]` is the most recent distinct value. Because all equal values are contiguous in a sorted array, comparing only with that last written value detects precisely whether the new value extends the prefix.

Writing never destroys unread information: `write` cannot pass the read position, because it advances only for accepted values. Positions after the returned prefix are deliberately unspecified by the platform contract.

**Trace the write boundary**

For `[0, 0, 1, 1, 2]`, begin with prefix `[0]`. Skip the second zero, write 1 at index 1, skip its duplicate, and write 2 at index 2. The unique prefix is `[0, 1, 2]` and its official length is 3.

**The write boundary advances once per distinct run**

Sorted order makes every equal value one contiguous run. The first value of a new run differs from the last written value and is copied at the write boundary; every later value in that run compares equal and is skipped.

Consequently the written prefix contains one representative of every completed run in original sorted order. After the final read, all runs have been processed, so the prefix is complete, unique, and exactly the required length.

## Complexity detail
The read pointer visits each of the `n` elements once, and each accepted distinct value causes one constant-time write, so time is $O(n)$. The compaction uses only read and write indices, giving $O(1)$ auxiliary space. The app's returned slice is the observable result representation rather than workspace used by the core algorithm.

## Alternatives and edge cases
- **Set conversion:** removes duplicates but uses $O(n)$ storage and does not naturally preserve the required in-place prefix contract.
- **Delete duplicates while scanning:** repeated array shifts can require $O(n^2)$ time.
- **Build a new list with membership searches:** is easy to express but can be quadratic and uses extra storage.
- A one-element input already has a unique prefix of length one. The stated official constraint makes the input nonempty; variants allowing empty input should return count zero.
- Comparing against the immediately previous input element also works for sorted data, but comparing against the last written element states the compacted-prefix invariant directly.
