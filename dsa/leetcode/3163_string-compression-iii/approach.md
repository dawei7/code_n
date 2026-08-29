## General

**First identify maximal equal-character runs**

The compression operation repeatedly removes the longest prefix consisting of one repeated character, but no chunk may be longer than 9.

`groupby(word)` partitions the string into maximal consecutive runs of the same character. For example,

`"aaabbcccc"`

becomes runs `("a",3)`, `("b",2)`, and `("c",4)`.

Run boundaries are forced: a chunk can never contain two different characters. Therefore, each maximal run can be compressed independently.

**Split a long run into maximum legal chunks**

For one group, `c` is its character and iterator `v` yields the repeated occurrences. The code computes run length with

`k = len(list(v))`.

While characters remain, it chooses

`x = min(9, k)`.

This is the longest prefix allowed by the rule. It appends decimal count followed by the character, `str(x) + c`, then removes that many conceptually by `k -= x`.

For a run of length 14, chunks are 9 and 5, producing `"9a5a"`. For a run length at most 9, one iteration encodes the whole run.

Because $x$ is between 1 and 9, the count is always one digit and decoding boundaries remain clear: count, then character, repeatedly.

**Why group-first processing matches prefix removal**

At any point in the original algorithm, the remaining word begins inside one maximal run. The maximum single-character prefix has length equal to the remaining portion of that run, capped at 9. Choosing `min(9,k)` makes exactly that operation.

After consuming a chunk shorter than the whole run only because of the cap, the next prefix has the same character and is processed again. Once the run is exhausted, the next `groupby` group is exactly the next prefix character.

Thus the grouped implementation produces the identical chunk sequence as literal repeated slicing from the front, without modifying the string.


Consider a maximal run of character $c$ and length $r$. The loop emits chunks whose sizes are 9 until the remaining length is at most 9, then emits that remainder. Every size is legal, their sum is $r$, and each is the largest legal prefix at its step.

Runs cover every input position exactly once and do not overlap. Concatenating their encodings therefore accounts for every character in order and applies the specified operation at every step. `"".join(ans)` returns exactly `comp`.

**Examples**

For `"abcde"`, each run has length one. The emitted pieces are `"1a"`, `"1b"`, `"1c"`, `"1d"`, and `"1e"`.

For `"aaaaaaaaaaaaaabb"`, the 14-character `a` run becomes 9 and 5, while the two-character `b` run becomes 2. The result is `"9a5a2b"`.

Adjacent output chunks may name the same character when one input run exceeds 9. They must not be merged into a count such as 14 because the format caps every count at 9.

**Exact iterator behavior**

`groupby` group iterators share the underlying input iterator and normally must be consumed before advancing. Converting `v` to a list consumes the complete current group, so advancing the outer loop is safe.

That conversion temporarily stores every character in the run. Counting with `sum(1 for _ in v)` would avoid the list, but the exact source uses it.

## Complexity detail

Let $n$ be the word length.

`groupby` and all `list(v)` conversions collectively consume exactly $n$ characters. The chunk loops emit at most $\lceil n/9\rceil$ pieces plus run effects, still $O(n)$. Joining output whose length is $O(n)$ also takes $O(n)$. Total time is $O(n)$.

The output parts list and final compressed string use $O(n)$ space. Excluding required output, `list(v)` can hold the longest run, which is $O(n)$ in the worst case. Thus the exact auxiliary-space bound is $O(n)$, matching the manifest.

A streaming run counter could reduce working space apart from output to $O(1)$.

The input string is immutable and unchanged.

## Alternatives and edge cases

- **Two-pointer scan:** Measure each run with indices and emit chunks as its length is known. It avoids materializing group characters and can use $O(1)$ working space excluding output.
- **Streaming counter:** Track current character and count, flushing a chunk whenever count reaches 9 or the character changes.
- **Repeated front slicing:** It mirrors the statement but can copy string suffixes repeatedly and approach quadratic time.
- **Run length exactly nine:** It emits one `9c` chunk.
- **Run length ten:** It must emit `9c1c`, not a two-digit count.
- **Single character:** It becomes count 1 followed by that character.
- **Alternating characters:** Every run length is one, so compressed output is twice the input length.
- **Very long run:** The while loop emits as many 9-sized chunks as needed and one optional remainder.
- **Same character in separated runs:** Other characters between them prevent merging; `groupby` keeps them distinct.
- **Lowercase alphabet:** Counts and characters are unambiguous because each count is one digit and each symbol one character.
- **Group iterator consumption:** `list(v)` fully consumes each shared iterator before the outer `groupby` advances.
- **Output construction:** Accumulating parts and joining avoids repeated immutable-string concatenation costs.
