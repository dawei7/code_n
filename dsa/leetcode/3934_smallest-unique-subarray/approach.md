## General

For a fixed length $L$, consider every contiguous window of exactly $L$ elements. The decision question is:

> Does at least one exact sequence occur at only one starting position?

If this question could be answered exactly in linear time, binary search could find the smallest successful length because uniqueness is monotone with respect to extension. Unfortunately, the checked source replaces exact sequences with a single rolling hash, and that replacement introduces a real correctness defect.

**Why the exact-sequence predicate is monotone**

Suppose a sequence of length $L<n$ occurs exactly once. Its occurrence cannot touch both ends of the array unless $L=n$, so it can be extended by one adjacent element on at least one side. If that longer sequence occurred somewhere else, the contained length-$L$ sequence would also occur somewhere else, contradicting uniqueness.

Therefore, if an exact unique subarray exists at length $L$, some exact unique subarray exists at length $L+1$. Repeating this argument shows that the true decision predicate has the form

`false, false, ..., true, true, ...`.

The complete array of length $n$ always occurs at its only possible start, so a successful length always exists. This justifies initializing the result to $n$ and binary-searching lengths from one through $n$—but only if `_check_uniqueness` answers the predicate exactly.

**The polynomial hash used by the source**

The source sets base $B=19$ and modulus $M=10^9+7$. For a window

$$
a_0,a_1,\ldots,a_{L-1},
$$

its intended hash is

$$
a_0B^{L-1}+a_1B^{L-2}+\cdots+a_{L-2}B+a_{L-1}
\pmod M.
$$

The first window is built from left to right by multiplying the current hash by 19, adding the next value, and reducing modulo $M$.

To move the window one position right, the old leftmost value's contribution is removed:

`current_hash -= powers[L - 1] * old_value`.

The remaining polynomial is multiplied by the base, the new rightmost value is added, and the result is reduced modulo $M$. Python's modulo operation normalizes a negative intermediate result, so not reducing immediately after subtraction does not by itself break the recurrence.

The dictionary `hash_values` counts how many windows produce each hash. The method returns true if any hash count equals one.

**How the outer binary search uses that check**

The midpoint length is tested. A true result records it as the best known length and searches smaller lengths. A false result searches larger lengths. Each decision scan clears the hash dictionary, recomputes powers, hashes all windows, and then checks whether a count of one exists.

If equal hashes implied equal sequences, this would correctly locate the first unique length.

**Concrete correctness defect: hashes are not sequences**

Different subarrays can have the same polynomial hash. This is not only a remote modulo collision. Because input values may be much larger than the base, collisions occur even before taking the modulus.

For base 19:

$$
\operatorname{hash}([2,1])=2\cdot19+1=39,
$$

while

$$
\operatorname{hash}([1,20])=1\cdot19+20=39.
$$

Use the valid input

`nums = [2, 1, 20]`.

Every length-one subarray is unique, so the correct answer is `1`. The two length-two subarrays `[2, 1]` and `[1, 20]` are also different and each occurs once. However, the source merges them under hash 39, records a count of two, and concludes that length two has no unique window.

The initial binary-search midpoint for $n=3$ is length two. After this false negative, the search discards all shorter lengths—including the correct answer length one—and eventually returns `3`. Direct execution confirms that the exact source returns 3 for `[2, 1, 20]`.

Thus the present Optimal implementation is not correct for the stated constraints. The manifest's claim that the source builds a suffix automaton is also inaccurate; no suffix automaton appears in `solution.py`.

**Why a single hash count cannot be repaired by explanation**

Hash equality is only evidence that sequences might be equal. To make the decision exact, colliding windows would need an independent equality check or a collision-free suffix structure. Merely choosing a larger modulus, a randomized base, or two hashes reduces collision probability but does not turn hashes into a mathematical proof of equality.

The source also assumes that its hash-based predicate remains monotone. Hash collisions create false negatives, and those false negatives need not be monotone across lengths. The counterexample has a true exact predicate at lengths one and two, but the hashed check reports false at length two. Binary search then magnifies a local collision into the wrong minimum.

**What remains valid in the intended reasoning**

Ignoring collisions, rolling the polynomial window is algebraically correct, the dictionary counts hash occurrences, and binary search follows the monotonicity of actual unique sequences. The full-length window has one hash entry and count one, so the method terminates with some answer. The defect lies specifically in treating one modular hash as an exact identity.

This distinction matters: randomized testing over a small alphabet may pass many cases, yet the fixed base makes adversarial collisions easy to construct within the allowed value range.

## Complexity detail

Let $n$ be the array length. One call to `_check_uniqueness(L)` recomputes all $n+1$ powers even though only powers through $L-1$ are needed. It then scans $n-L+1$ windows and performs expected constant-time dictionary operations. One check therefore takes $O(n)$ expected time.

Binary search performs $O(\log n)$ checks, giving $O(n\log n)$ expected time. This contradicts the manifest's $O(n)$ suffix-automaton claim.

The `powers` array holds $n+1$ integers. At a tested length, the dictionary may contain $O(n)$ distinct hash keys. Additional space is $O(n)$.

These complexity bounds describe execution, not correctness. The method can finish within them and still return the wrong result because of a collision.

## Alternatives and edge cases

- **Suffix automaton or another exact suffix structure:** This is the direction claimed by the manifest. An exact structure can derive substring occurrence counts without equating unrelated sequences by one hash, but it is not present in the source.
- **Suffix array plus longest-common-prefix information:** For each suffix, the shortest prefix not shared with either neighboring suffix determines a unique subarray candidate. This can provide an exact near-linear or $O(n\log n)$ solution after coordinate handling.
- **Double or randomized rolling hashes:** These make accidental collisions far less likely but remain probabilistic unless matching windows are verified element by element.
- **Compare colliding windows exactly:** Hashes can serve as buckets, but exact comparison inside a bucket is required for guaranteed correctness and can affect worst-case time.
- **Brute-force tuple counting by length:** This is exact and useful as a small-input oracle, but copying and counting all windows across lengths can be quadratic or worse.
- **Concrete failing input:** For `[2, 1, 20]`, the correct answer is 1 and the source returns 3 because `[2, 1]` and `[1, 20]` both hash to 39.
- **All elements equal:** The shortest unique sequence is the full array. Every shorter all-equal window repeats, and the source happens to handle this case.
- **A singleton value occurs once:** The answer is 1. A collision at a longer midpoint can nevertheless prevent this implementation from ever testing length one.
- **Overlapping equal occurrences:** They count separately. Any exact method must count start positions, not only disjoint copies.
- **Whole array:** Length $n$ has exactly one window, guaranteeing existence of an answer.
- **Values larger than the base:** They are legal and make simple non-modular polynomial collisions such as the demonstrated one possible.
- **Dictionary membership syntax:** `current_hash not in self.hash_values.keys()` is functionally equivalent to testing the dictionary directly, though the latter is clearer.
- **Input remains unchanged:** The source stores a reference in `self.nums` but only reads its elements while hashing.
