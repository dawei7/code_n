## General

**The factorial sum is permutation-invariant**

Rearranging digits changes their positions but not their values or multiplicities. Consequently, every permutation $x$ of `n` has the same digit-factorial sum:

$$
F(x)=F(\texttt{n}).
$$

Call this fixed sum $S$. If a qualifying permutation exists, it must satisfy $x=F(x)=S$. There is therefore only one numeric candidate to check: $S$ itself. A valid permutation exists exactly when the decimal digits of $S$ have the same multiplicities as the digits of `n`.

**Compare fixed-size digit counts**

Store the factorials from $0!$ through $9!$. While extracting the digits of `n`, accumulate $S$ and count how often each digit occurs. Then extract and count the digits of $S$. Return whether the two ten-entry count arrays are equal.

If the counts are equal, the ordinary decimal representation of $S$ uses exactly the input digits. That representation cannot start with zero, so it is a valid permutation, and its factorial sum is $F(S)=F(\texttt{n})=S$; hence it is digitorial. Conversely, if a valid digitorial permutation $x$ exists, permutation invariance gives $x=F(x)=F(\texttt{n})=S$. Thus $S$ and `n` must have identical digit counts. The comparison is both necessary and sufficient.

## Complexity detail

Let $D$ be the number of decimal digits in `n`. Extracting the digits of `n` and of $S$ takes $O(D)$ time: under the source bound, $S\le 10\cdot9!$, so its digit count is also bounded by a constant multiple of $D$. The two count arrays always contain ten entries, giving $O(1)$ auxiliary space.

The benchmark defines size as $D$ and uses inputs with distinct digits. The count method remains linear in the digit count, while a correct literal permutation search explores up to $D!$ arrangements before concluding that none equals the invariant factorial sum.

## Alternatives and edge cases

- **Enumerate every permutation:** Generate all digit arrangements, reject leading zeros, and test each number. This follows the definition directly but can require $O(D!\cdot D)$ time.
- **Sort digit strings:** Compare `sorted(str(n))` with `sorted(str(S))`. This is concise and correct in $O(D\log D)$ time, but fixed digit counts achieve linear time.
- **Precomputed digitorials:** The small decimal domain permits a lookup-oriented solution, but deriving and maintaining a special list obscures the permutation invariant and general reasoning.
- **Zero digit:** Include $0!=1$ in the sum and count every zero; zeros are ordinary digits even though they cannot lead a valid arrangement.
- **Leading zeros:** Equality of digit counts with the standard decimal representation of $S$ automatically supplies a nonzero leading digit. No separate permutation construction is needed.
- **Single digit:** Both `1` and `2` are digitorial because $1!=1$ and $2!=2$; other single-digit positive inputs are not.
- **Different digit lengths:** Count arrays cannot match when $S$ has fewer or more digits than `n`, so the method rejects immediately after counting.
