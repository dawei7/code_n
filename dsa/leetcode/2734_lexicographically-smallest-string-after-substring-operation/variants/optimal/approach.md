## General

**Lexicographic order is decided at the first changed position**

One nonempty substring must be transformed. Every selected non-`'a'` letter decreases by one, which makes the string smaller at that position. A selected `'a'` wraps to `'z'`, which makes the string larger at that position.

When comparing candidate results, the earliest position where they differ from the original dominates every later change. This observation determines both where the chosen substring should begin and where it should end.

**Never begin inside the leading block of a characters**

Suppose `s` begins with one or more `'a'` characters and later contains a non-`'a'`. Selecting any leading `'a'` changes it to `'z'`. At the first selected leading position, the candidate becomes larger than the original and larger than a candidate that leaves the prefix unchanged and decreases the later non-`'a'`.

Therefore the code advances `i` while `s[i] == "a"`. The optimal operation must skip this entire leading block when a reducible character exists later.

**Start at the first non-a character**

At the first non-`'a'` index `i`, decrementing the letter makes it strictly smaller. Starting after `i` would leave this position unchanged, so a substring starting at `i` wins lexicographically at the earliest differing position.

Starting before `i` would include a leading `'a'` and change that earlier character to `'z'`, which is worse. Thus `i` is the uniquely optimal start position whenever the string is not all `'a'`.

**Continue through the maximal non-a block**

The code advances `j` while characters remain different from `'a'`. It decrements every character in `s[i:j]`.

Why not stop earlier within that block? All candidates starting at `i` make identical changes through any shared prefix. At the first non-`'a'` that a shorter candidate leaves unchanged but a longer candidate decrements, the longer candidate has the smaller character. Therefore extending across another non-`'a'` always improves the result.

**Stop before the next a**

Including the next `'a'` would turn it into `'z'`. Compare the candidate that stops before this `'a'` with one that includes it. They are identical at every earlier position. At this position, the stopping candidate keeps `'a'` while the extending candidate has `'z'`, so stopping is lexicographically smaller regardless of any later decrements.

Hence the first `'a'` after the chosen block is the exact optimal endpoint boundary.

**Construct the transformed string**

The return expression concatenates three pieces:

- `s[:i]`, the unchanged leading prefix;
- a joined generator that maps each character in `s[i:j]` to `chr(ord(c) - 1)`;
- `s[j:]`, the unchanged suffix.

Every character in the middle is known not to be `'a'`, so subtracting one code point produces its preceding lowercase letter without needing wraparound logic.

For `"cbabc"`, `i=0` and `j=2` because the first `'a'` occurs at index two. Decrementing `"cb"` gives `"ba"`, and appending `"abc"` produces `"baabc"`.

For `"acbbc"`, the leading `'a'` is skipped, then the entire `"cbbc"` block is decremented to `"baab"`. The result is `"abaab"`.

**The all-a case is fundamentally different**

If `i == n`, every character is `'a'`. The operation is mandatory, so some selected `'a'` must become `'z'`; no candidate can be smaller than the original.

To make the forced worsening as late as possible, change only the last character. Candidates that change an earlier position become larger at that earlier first difference. Changing multiple trailing characters is also worse than changing only the last because the first changed position moves left or additional later `'z'` values provide no compensation.

The code returns `s[:-1] + "z"`. For `"aa"`, this produces `"az"`.

**Why exactly one contiguous block is respected**

The selected middle `s[i:j]` is nonempty in the normal case because `i` points to a non-`'a'` and `j>i`. In the all-a case, the last one-character substring is nonempty. Both branches perform exactly one legal substring operation.


If a non-`'a'` exists, any operation touching an earlier leading `'a'` is worse, while any operation starting after the first non-`'a'` misses the earliest possible decrease. So the start is `i`. From that start, extending over each non-`'a'` makes the first newly affected position smaller, while extending onto an `'a'` makes it larger; hence the endpoint is just before the next `'a'`. If all characters are `'a'`, every operation worsens the string, and changing only the last position delays the first difference maximally. The constructed result is therefore lexicographically smallest in all cases.

## Complexity detail

Let $n$ be the string length. The scan for `i` and the scan for `j` together visit at most $n$ characters. Building the decremented middle and concatenating the returned string also process $O(n)$ characters. Total time is $O(n)$.

Python strings are immutable, so slicing, joining, and concatenation allocate a new result and intermediate string pieces totaling $O(n)$ space. This matches the manifest's $O(n)$ auxiliary/output-space summary.

The scans use $O(1)$ scalar state; string construction is the dominant storage.

## Alternatives and edge cases

- **Try every substring:** There are $O(n^2)$ choices and comparing or constructing each result is far slower than the greedy boundary proof.
- **Decrement the whole string:** Incorrect when an `'a'` appears after a useful block because wrapping it to `'z'` worsens the first such position.
- **Skip only one leading a:** Incorrect when the leading run contains several `'a'` characters; all must remain unchanged if a later non-`'a'` exists.
- **All a characters:** Change only the last one to `'z'` because an operation is mandatory.
- **No leading a:** Start at index zero for the earliest possible improvement.
- **No later a:** Decrement from the first non-`'a'` through the end.
- **Single non-a character:** It is decremented and forms a legal one-character substring.
- **Single-character `"a"`:** The all-a branch returns `"z"`.
- **Single-character non-a:** It is replaced by its predecessor.
- **Contiguity:** Stopping at the first interior `'a'` is required; the operation cannot skip it and resume later.
