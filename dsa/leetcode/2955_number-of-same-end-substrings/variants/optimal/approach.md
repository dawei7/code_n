## General

**Count endpoint choices by character.** Fix one query range and one letter
that occurs $f$ times inside it. Every one of those occurrences forms a
length-one same-end substring. Every unordered pair of distinct occurrences
selects the left and right endpoints of exactly one longer substring, whose
interior characters do not affect the definition. The letter therefore
contributes

$$
f+\binom f2=\frac{f(f+1)}2
$$

same-end substrings. Summing this expression over all 26 letters counts every
substring once according to its common endpoint character.

**Answer range frequencies with prefixes.** Build a prefix row for every
string boundary, where each row stores the cumulative counts of all lowercase
letters. For inclusive query `[left, right]`, subtract row `left` from row
`right + 1` to obtain every frequency inside exactly that range. Apply the
triangular-number formula to each difference and append the sum.

The prefix subtraction is exact for inclusive boundaries. Each same-end
substring has one endpoint character and one endpoint pair (or one singleton
position), so the per-letter sums neither omit nor duplicate any valid
substring.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$ and let $Q$ be the number of queries. Building
and querying 26 counters takes $O(26N+26Q)=O(N+Q)$ time because the alphabet is
fixed. The prefix table stores 26 counts at each boundary and uses $O(N)$
auxiliary space. The returned array uses $O(Q)$ output space.

## Alternatives and edge cases

- **Rescan every query range:** Counting its letters directly is correct but can take $O(NQ)$ time over many long queries.
- **Enumerate endpoint pairs:** Testing every substring inside each query takes quadratic time per range.
- **Single-character range:** Its sole substring is same-end and contributes one.
- **All characters distinct:** Only the single-character substrings qualify, so the answer equals the range length.
- **All characters equal:** Every nonempty substring qualifies, giving $L(L+1)/2$ for range length $L$.
- **Inclusive right endpoint:** Prefix row `right + 1`, not row `right`, must be used.
- **Repeated or overlapping queries:** Each query is answered independently even when it describes the same positions.
