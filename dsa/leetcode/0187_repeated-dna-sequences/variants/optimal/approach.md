## General

**Enumerate every possible length-10 window**

A substring must be contiguous, so every candidate is determined by its start
index. For a string of length $n$, a 10-character window can start at indices
0 through $n - 10$, inclusive. That gives $n - 10 + 1$ candidates when
$n \ge 10$.

The loop uses `range(len(s) - 10 + 1)`, and each iteration slices
`s[i : i + 10]`. Python's slice has a half-open endpoint, so this expression
contains exactly indices `i` through `i + 9`: ten characters, neither nine nor
eleven.

When the input is shorter than ten characters, the range endpoint is zero or
negative and the loop naturally runs zero times. No length-10 substring exists,
so returning the initially empty answer is correct without a separate guard.

**Count windows by their actual text**

`cnt` is a `Counter` whose keys are length-10 strings. After extracting window
`t`, the query increments `cnt[t]`. Two windows with the same ten nucleotides
produce the same key even when they begin at different indices.

This is exactly the required equivalence relation. The task asks whether a DNA
sequence occurs more than once; its positions do not have to be disjoint.
Overlapping windows count as separate occurrences. In `AAAAAAAAAAA`, for
example, the length-10 string `AAAAAAAAAA` occurs at starts 0 and 1, so it is a
valid repeated sequence.

**Append only on the second occurrence**

After incrementing the count, the solution appends `t` only if `cnt[t] == 2`.
The first occurrence changes the count from zero to one and is merely recorded.
The second changes it from one to two and proves that the sequence occurs more
than once, so the sequence enters the answer.

The equality check, rather than `>= 2`, prevents duplicate output. A third,
fourth, or hundredth occurrence keeps increasing the count but never satisfies
`== 2` again. Thus every repeated sequence is returned exactly once even though
all of its occurrences are still scanned.

**Trace the all-`A` example**

For `AAAAAAAAAAAAA`, starts 0, 1, 2, and 3 all produce `AAAAAAAAAA`. At start
0 its count becomes one and nothing is appended. At start 1 it becomes two and
the sequence is appended. At starts 2 and 3 the counts become three and four,
so the answer remains a one-element list.

This demonstrates both overlap handling and output deduplication. No special
case for repeated identical characters is needed.

**Trace two different repeated windows**

In `AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT`, the scan first records each window.
When `AAAAACCCCC` is encountered again, its count reaches two and it is
appended. The same later happens to `CCCCCAAAAA`. Windows that appear once
remain only in the counter and never enter the result.

The answer follows the order in which sequences reach their second occurrence,
but the Reference accepts any order, so no sorting is required.

**Why the method returns exactly the desired set**

Every appended string has just reached count two. Therefore the scan has found
two distinct start positions producing that exact length-10 substring, so every
returned value truly occurs more than once.

Conversely, take any length-10 substring that occurs at least twice. The loop
visits every legal start index, including its first two occurrence positions.
At the second one, its counter value becomes exactly two and the solution
appends it. Later occurrences cannot remove it. Therefore no repeated sequence
is missed.

**Why a sliding-window hash map is enough**

There are only four possible characters, but the implementation does not need
to encode them numerically. Python strings already support equality and hashing,
and the window length is the fixed constant ten. Storing the substring itself
makes collisions harmless because dictionary equality confirms the complete
text after hashing.

For a generalized problem where window length $L$ could grow with input size,
creating every slice would cost $O(L)$ per start and store $O(L)$ characters
per distinct key. The local editorial discusses rolling hashes and bitmasks for
that setting. Here $L = 10$ is fixed by the contract, so those factors are
constants and the direct version remains linear and especially readable.

**Exact source integration detail**

The exact file refers to `Counter` and the return annotation `List[str]` without
showing imports for either name. A platform harness may provide them, but a
standalone Python module normally needs `from collections import Counter` and
`from typing import List` (or `list[str]` on modern Python). Without supplied
names, the file can fail before or during the call even though the algorithm is
correct. This is a source packaging issue, not a flaw in the counting logic.

## Complexity detail

Let $n$ be the DNA string length and let the window length be the fixed value
$L = 10$. There are at most $n - L + 1$ windows. Slicing, hashing, and comparing
one fixed-size window take $O(L) = O(1)$ time, so total time is $O(n)$ under
expected hash-table behavior.

At most $n - L + 1$ distinct window strings are stored, and the answer can also
contain linearly many values. Since every key has constant length ten,
auxiliary space is $O(n)$. If $L$ were variable, the more explicit bounds would
be $O((n-L+1)L)$ time and potentially the same character storage.

## Alternatives and edge cases

- **Two sets:** Keep `seen` windows and `repeated` windows; adding repeats to a set also guarantees one output copy.
- **Rolling base-4 hash:** Encode nucleotides as digits and update a window value in constant time; useful for variable $L$, but collision handling matters unless the encoding is exact.
- **Twenty-bit encoding:** Four nucleotides need two bits each, so a length-10 sequence fits exactly in 20 bits with no collisions.
- **Competitive three-bit encoding:** Also exact for these four characters, though it uses 30 bits instead of 20.
- **Input shorter than ten:** No loop iterations and an empty answer.
- **Input length exactly ten:** The sole window occurs once, so the answer is empty.
- **Overlapping repeats:** They count as distinct occurrences and are handled naturally.
- **More than two occurrences:** Append only when the count first reaches two.
- **Any order:** The scan's discovery order is acceptable; sorting is unnecessary.
- **Missing imports:** Supply `Counter` and `List` when the execution harness does not.
