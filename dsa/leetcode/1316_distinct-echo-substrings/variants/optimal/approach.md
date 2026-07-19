## General
**Enumerate a start and a half-length**

Every echo substring is determined by a starting index `start` and a positive half-length `length`, with `start + 2 * length <= n`. There are $O(n^2)$ such candidates. The candidate qualifies exactly when `text[start:start + length]` equals `text[start + length:start + 2 * length]`.

Comparing those halves character by character would add another factor of $n$. Precompute polynomial prefix hashes and powers so the hash of any half-open range can be normalized and obtained in constant time. Use two different prime moduli; both half hashes must match before a candidate is accepted.

**Deduplicate the substring value, not its location**

For a qualifying candidate, its full value is determined by its half. Store a key containing the half-length and both normalized half hashes. The same echo value at another location produces the same key, while a different length or content produces a different key under the dual-hash representation. The number of stored keys is the answer.

The implementation maps letters to positive integers and uses the same base for both moduli. Dual modular hashes make accidental equality between different strings negligibly unlikely and avoid copying every candidate substring; this is the standard rolling-hash model for this constraint.

## Complexity detail
Prefix hashes and powers take $O(n)$ time and space. The nested half-length and start loops examine $O(n^2)$ candidates, each with constant-time hash extraction and set work, for $O(n^2)$ expected time. At most $O(n^2)$ distinct echo keys can be stored, so space is $O(n^2)$ in the worst case.

## Alternatives and edge cases
- **Direct half comparison:** Testing characters for every candidate is exact but can take $O(n^3)$ time on highly repetitive text.
- **Store substring slices:** A set of actual echo strings avoids hash collisions, but materializing many long slices can copy cubic total characters in the worst case.
- **Trie-based starts:** Tries can share repeated prefixes and support deterministic comparison, but the implementation and memory accounting are more involved.
- **Odd lengths:** They cannot split into two equal-length nonempty halves and are never candidates.
- **Repeated occurrences:** A value is counted once even if it appears at many starts.
- **One-character input:** No nonempty echo substring can fit, so the answer is 0.
- **Overlapping occurrences:** Overlap is allowed; only substring boundaries and equal halves matter.
