## General

Each letter has a mapped integer from one through nine. A substring is divisible when its mapped-value sum is divisible by its length, equivalently when its average mapped value is an integer.

The exact source builds the mapping and enumerates every substring while maintaining its sum incrementally.

**Construct the phone-style mapping**

List

`["ab", "cde", "fgh", "ijk", "lmn", "opq", "rst", "uvw", "xyz"]`

groups letters assigned to digits $1$ through $9$. The nested initialization loop uses `enumerate(d, 1)`, so every character in the first group maps to one, every character in the second to two, and so forth.

Dictionary `mp` ends with one entry for each of the 26 lowercase letters.

**Fix a substring start**

For each left endpoint `i`, running mapped sum `s` starts at zero. The inner loop moves right endpoint `j` from `i` through the end:

1. Add `mp[word[j]]` to `s`.
2. Current length is `j - i + 1`.
3. Test `s % length == 0`.
4. Add the Boolean result to `ans`.

Because Python treats `True` as one and `False` as zero, the last statement increments the answer exactly for divisible substrings.

**Why the running sum stays correct**

At the first inner iteration, `s` equals the mapped value of `word[i]`. Each later iteration adds exactly the newly included rightmost character. By induction, after processing $j$,

$$
\texttt{s}
=
\sum_{p=i}^{j}\texttt{mp}[\texttt{word}[p]].
$$

The divisor `j - i + 1` is exactly the number of characters in the same interval, so the modulus test implements the definition directly.

**Why every substring is counted once**

A nonempty substring has one unique pair of endpoints $(i,j)$ with $i\le j$. The outer and inner loops visit every such pair once. The test accepts it if and only if its mapped sum is divisible by its length.

Therefore `ans` contains exactly the number of divisible substrings, with no duplication or omission.

**A useful interpretation**

The condition says the substring's average belongs to the integer set $\{1,\ldots,9\}$. A faster method can try each possible integer average $q$, transform character values to `value - q`, and count zero-sum substrings using equal prefix sums.

The Optimal manifest describes such a nine-average $O(n)$ method. The checked-in source does not implement it; it uses endpoint enumeration.

For any one-character substring, its sum equals its mapped integer and its length is one, so it always qualifies. This gives a baseline of at least `len(word)`, which the loops include at `j == i`.

## Complexity detail

The number of endpoint pairs is $n(n+1)/2$. Each extension does constant dictionary lookup and integer arithmetic, so actual time complexity is $O(n^2)$.

The mapping dictionary has exactly 26 entries and the group list has nine strings, both constant with respect to $n$. Apart from scalar counters, no growing structure is allocated, so auxiliary space is $O(1)$.

These bounds contradict the manifest's $O(n)$ time and $O(n)$ space summary. That summary belongs to the transformed-prefix approach, not this exact nested-loop source.

## Alternatives and edge cases

- **Nine transformed prefix scans:** For each possible average $q=1..9$, count equal prefix sums after subtracting $q$ from every mapped value. This achieves $O(9n)=O(n)$ time.
- **Prefix sums plus all endpoints:** Prefix sums make each range sum constant time but still leave $O(n^2)$ endpoint pairs; the source's running sum is simpler.
- **Recompute each substring sum:** Summing from scratch for every pair would take $O(n^3)$ time.
- **Single character:** Always divisible because any integer is divisible by length one.
- **All characters share a mapped value:** Every substring has that integer average and qualifies.
- **Average need not be a mapped character present:** Only integrality matters; the integer average may differ from each individual value.
- **Lowercase guarantee:** Every input character exists in `mp`, so dictionary lookup cannot fail.
- **Boolean arithmetic:** `ans += condition` relies on Python converting the comparison result to zero or one.
- **Input length 2000:** Quadratic work is about two million substrings, which explains why direct enumeration can still run for this contract.
- **Manifest mismatch:** The approach and complexity must be documented as $O(n^2)$/$O(1)$ for the checked-in implementation.
- **Mapping covers all letters once:** The nine group strings are disjoint and together contain `a` through `z`, so later assignments never overwrite a character with a different value.
- **Integer-average range:** Because mapped values lie from one to nine, any substring average also lies in that interval. This is why the faster alternative needs only nine transformations.
- **Running sum reset:** Each new left endpoint sets `s=0` so characters before `i` do not contaminate the new family of substrings.
- **Modulo divisor is never zero:** Every visited substring is nonempty, making `j-i+1 >= 1`.
- **Endpoint uniqueness:** Equal substring text occurring at two locations counts twice because the problem counts substrings by positions; the nested endpoint loops represent this correctly.
