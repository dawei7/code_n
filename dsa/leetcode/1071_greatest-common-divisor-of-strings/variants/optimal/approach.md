## General
**Determine the only possible greatest length:** If a string of length $L$ divides both inputs, then $L$ divides both $N$ and $M$. Therefore the greatest possible common-divisor length is $G=\gcd(N,M)$. Take the first $G$ characters of `str1` as the candidate.

**Verify periodic construction:** Scan each input. At index `i`, its character must equal `candidate[i % G]`. If either scan finds a mismatch, the candidate does not generate both strings and no shorter common divisor can rescue incompatible primitive patterns, so return `""`.

**Return the greatest candidate:** If both strings are repetitions of the length-$G$ prefix, that prefix divides them. No longer common divisor is possible because its length would have to divide both input lengths and exceed their numeric gcd.

For the failure case, suppose some common string did exist. Both inputs would then be repetitions of the same primitive pattern, and the length-$G$ prefix would also consist of a whole number of copies of that primitive pattern. It would pass the periodic check, contradicting the observed mismatch.

## Complexity detail
Euclid's numeric gcd calculation is dominated by the string scans. Every character in both inputs is checked once, giving $O(N+M)$ time. Apart from the returned prefix and a few indices, the algorithm uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Concatenation identity:** Check whether `str1 + str2 == str2 + str1`, then return the gcd-length prefix. It is concise and linear but allocates temporary strings of total length $O(N+M)$.
- **Repeated string subtraction:** Remove the shorter matching prefix from the longer string until they agree. It is correct, but repeated slicing can take quadratic time.
- **Try every prefix:** Testing candidates from longest to shortest repeats the same comparisons and can also become quadratic.
- **Equal strings:** The entire string is their greatest common divisor.
- **Coprime lengths:** Only a one-character divisor is possible, and it succeeds only when both strings repeat that character.
- **Same letters but one mismatch:** A single incompatible position means no common divisor string exists.
- **One string divides the other:** The shorter string is returned when it is itself periodic-compatible with the longer one.
