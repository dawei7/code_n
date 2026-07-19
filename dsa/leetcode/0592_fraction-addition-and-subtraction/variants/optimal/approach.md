## General
**Parse one signed fraction at a time**

Advance an index through the expression. Read an optional leading sign, then collect numerator digits up to `/` and denominator digits up to the next sign or end of input. Applying the sign to the numerator keeps every denominator positive.

**Maintain one exact running fraction**

If the running value is $a / b$ and the next term is $c / d$, replace it with $(a d + c b) / (b d)$. This uses integer arithmetic throughout, so no precision is lost.

**Reduce after every addition**

Compute `gcd(abs(numerator), denominator)` and divide both parts by it after each term. Incremental reduction keeps intermediate integers smaller and automatically turns any zero result into $0 / 1$.

**Why the final fraction is canonical**

The update is the standard common-denominator identity, so induction over terms shows the running fraction equals the parsed prefix exactly. Dividing numerator and denominator by their greatest common divisor preserves that value and leaves them coprime. Since every parsed denominator is positive, the final denominator stays positive, giving the unique requested representation.

## Complexity detail
The parser advances monotonically across `n` characters. Each term performs a greatest-common-divisor calculation taking $O(\log V)$ arithmetic steps for the current integer magnitude `V`, so total time is $O(n \log V)$. Only indices and the running numerator and denominator are stored, giving $O(1)$ auxiliary space apart from integer representation.

## Alternatives and edge cases
- **Regular-expression tokenization:** cleanly extracts signed fractions, but stores all tokens and uses $O(n)$ additional space.
- **Language rational-number type:** can simplify arithmetic when available, though the parsing and output contract still need care.
- **Repeated suffix rebuilding:** is correct but can repeatedly copy the unparsed expression and take $O(n^2)$ time.
- **Zero result:** must be normalized to $0/1$.
- **Negative first term:** its leading minus belongs to the numerator.
- **Positive first term:** may omit a leading plus.
- **Integer result:** still returns an explicit denominator of one.
- **Several denominators:** use exact cross multiplication, never floating-point conversion.
- **Large intermediate products:** reduce after each term to control growth.
