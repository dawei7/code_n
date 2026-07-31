## General

Process the prefixes in increasing length. A set records every character encountered so far, so after reading `s[k - 1]` its size is exactly the number of distinct characters in the prefix `s[0:k]`.

For each $k$ from $1$ through the string length, insert the newly included character and compare the set size with $k \bmod 3$. Increment the answer whenever they are equal. Every nonempty prefix appears once in this scan, and its set contains precisely its characters, so the test counts exactly the residue prefixes.

Because a nonempty prefix has at least one distinct character while $k \bmod 3$ is only $0$, $1$, or $2$, no prefix can qualify after a third distinct character has appeared. The direct scan remains simple and already meets the linear bound.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$. The scan performs one expected constant-time set insertion and one comparison per character, giving $O(N)$ time. The set contains at most the 26 lowercase English letters, so its auxiliary space is $O(1)$ under the fixed alphabet.

## Alternatives and edge cases

- **Rebuild a set for every prefix:** Computing `set(s[:k])` independently is correct but repeats earlier work and takes $O(N^2)$ total time.
- **Count character frequencies:** A 26-entry frequency array also supports a linear scan, but a set expresses the required distinct count directly.
- **Lengths divisible by three:** Their remainder is zero, which cannot equal the positive number of distinct characters in a nonempty prefix.
- **Repeated characters:** Inserting a letter already in the set leaves the distinct count unchanged while the prefix length and its remainder continue to change.
- **Single-character string:** Its only prefix has one distinct character and remainder one, so the result is always `1`.
