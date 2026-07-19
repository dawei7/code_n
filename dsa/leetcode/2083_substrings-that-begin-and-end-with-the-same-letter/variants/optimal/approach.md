## General
**Count choices for each right endpoint**

Process the string from left to right. When the current character becomes a substring's right endpoint, its valid left endpoint may be the current position itself or any earlier position holding the same character. If that character has appeared $p$ times earlier, exactly $p+1$ new qualifying substrings end here.

**Maintain the required prefix frequency**

Store one counter for each of the 26 lowercase letters. Increment the current character's counter first, then add its new frequency to the answer. At that moment the frequency equals the number of valid left endpoints through the current position, so every qualifying substring is counted once at its unique right endpoint and no invalid endpoint pair is included.

**Connect the scan to the closed form**

If a letter occurs $f$ times in the whole string, it contributes $f$ single-character substrings plus one substring for each pair of distinct occurrences:

$$
f+\binom{f}{2}=\frac{f(f+1)}{2}.
$$

The streaming additions $1+2+\cdots+f$ produce exactly the same value while avoiding a separate final pass.

## Complexity detail
The scan performs constant work for each of the $n$ characters, giving $O(n)$ time. The frequency array always contains exactly 26 counters because the lowercase English alphabet is fixed, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Enumerate endpoint pairs:** Checking every $(i,j)$ is direct but takes $O(n^2)$ time.
- **Count all frequencies first:** Summing $f(f+1)/2$ over the 26 final counts is equally linear and constant-space, but the streaming invariant exposes why each substring is counted once.
- **All characters distinct:** Only the $n$ one-character substrings qualify.
- **All characters equal:** Every one of the $n(n+1)/2$ nonempty substrings qualifies.
- **Repeated substring text:** Different endpoint pairs remain distinct substrings even when their contents are equal.
- **One-character input:** Its frequency becomes one and contributes exactly one.
