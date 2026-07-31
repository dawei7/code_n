## General

**Expand one substring boundary at a time**

Fix a left endpoint and move the right endpoint across the string. A
ten-element frequency array can be updated in constant time when the new digit
enters the substring. Track both the number of digits with positive frequency
and the largest current frequency.

**Recognize equal frequencies without rescanning ten counters**

Suppose the current substring has length $L$, contains $d$ distinct digits,
and its largest frequency is $f$. Every positive frequency is at most $f$, so
their sum is at most $df$. The substring is balanced exactly when

$$
L=df.
$$

Equality forces all $d$ positive frequencies to equal $f$; conversely, equal
frequencies plainly satisfy the equation. This makes each balance check
constant time after the incremental update.

**Deduplicate by substring value**

The same text may occur at several positions and must contribute once. While
extending a substring, update two independent base-$11$ polynomial hashes.
For each balanced substring, store its length and both residues. Including the
length distinguishes sequences that would otherwise differ only through
leading structure, while two large moduli make accidental identity collisions
negligible. The stored key depends only on the digit sequence, so repeated
occurrences share one entry.

Every nonempty substring is visited once by its pair of endpoints. The
frequency equation accepts exactly the balanced ones, and the hash set counts
each accepted value once. The final set size is therefore the requested
distinct count, subject to the standard expected-correctness assumption of
paired rolling hashes.

## Complexity detail

There are $O(n^2)$ endpoint pairs, and every expansion performs constant
expected-time counter, hash, and set operations. The expected running time is
$O(n^2)$. Up to $O(n^2)$ qualifying identities may be retained, so auxiliary
space is $O(n^2)$.

The bounds assume ordinary constant-time hashing and no collision between the
paired modular fingerprints. The benchmark defines `size` as the string length
$n$ and uses deterministic mixed digits at three scales. Rebuilding a
frequency table separately for every candidate substring takes $O(n^3)$ time
on the same inputs.

## Alternatives and edge cases

- **Store substring slices directly:** A set of the exact qualifying strings
  avoids rolling-hash collision risk, but materializing and hashing every slice
  can process $O(n^3)$ total characters.
- **Suffix trie:** Trie nodes identify substring values exactly in $O(n^2)$
  expected construction time, but a Python node per distinct substring has
  substantially greater memory overhead than compact fingerprints.
- A one-character substring always qualifies because it has one present digit
  with frequency one.
- When only one digit is present, every nonempty substring qualifies by
  frequency, but repeated text of the same length is counted once.
- Absent digits are ignored; they do not need frequency zero to equal the
  positive frequencies.
- Leading zeros are characters of the substring and remain part of its
  identity.
- Distinct positions spelling identical text must not create duplicate count
  entries.
