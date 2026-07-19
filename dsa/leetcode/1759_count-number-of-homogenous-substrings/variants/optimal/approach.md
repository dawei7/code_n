## General
**Count substrings by their ending position**

When a character extends a current run to length $r$, exactly $r$ homogenous substrings end at that position: the suffixes of the run having lengths $1$ through $r$. Every homogenous substring has one unique ending position, so adding these contributions counts every valid occurrence exactly once.

**Maintain the current equal-character run**

Scan from left to right. If the current character equals the preceding run's character, increment the run length. Otherwise begin a new run of length one. No earlier character outside the current run can participate in a homogenous substring ending at this position.

**Accumulate with the modulus**

Add the current run length to the total at every position and reduce modulo $M$. For a maximal run of length $L$, the accumulated contributions are $1+2+\cdots+L=L(L+1)/2$, matching the number of ways to choose a nonempty interval inside that run.

The maximal equal-character runs partition `s`, and a homogenous substring cannot cross a boundary between distinct characters. Summing the exact ending-position contributions within every run therefore gives the complete answer.

## Complexity detail
The algorithm performs one constant-time update for each of the $n$ characters, taking $O(n)$ time. It stores only the previous character, current run length, total, and modulus, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Sum completed runs:** Detect each maximal run and add $L(L+1)/2$ when it ends. This is also linear but requires explicitly flushing the final run.
- **Enumerate all substrings:** Extending from every starting position and stopping at the first different character is correct, but takes $O(n^2)$ time for a uniform string.
- **Single character:** The only substring is homogenous, so the answer is one.
- **All characters distinct:** Every run has length one, and the answer is $n$.
- **All characters equal:** The answer before reduction is $n(n+1)/2$.
- **Repeated text at different positions:** Equal substring values still count separately because their intervals are different.
- **Run boundaries:** A substring containing both sides of a character change is never homogenous.
- **Large count:** Apply the modulus during accumulation so implementations with fixed-width integers do not overflow.
