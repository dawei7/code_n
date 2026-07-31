## General

**Keep the prefix small by retaining only its remainder**

Suppose a processed prefix has numeric value $P$ and remainder $r = P \bmod m$. Appending a decimal digit $d$ creates $10P + d$. Modular arithmetic gives

$$
(10P + d) \bmod m = (10r + d) \bmod m.
$$

Therefore the complete prefix value is unnecessary. Start with remainder zero, process the digits from left to right, and replace the remainder with `(remainder * 10 + digit) % m` at each position. Append one exactly when the updated remainder is zero.

After processing index $i$, the stored value is the remainder of the numeric prefix `word[0:i + 1]`. This holds initially for the empty prefix and is preserved by the decimal-extension identity above. A prefix is divisible by `m` exactly when its remainder is zero, so every emitted bit is correct. Reducing after every digit also prevents the exponentially growing prefix from overflowing a fixed-width integer.

## Complexity detail

Each of the $n$ digits is processed once with constant arithmetic, giving $O(n)$ time. The returned divisibility array requires $O(n)$ space; excluding that required output, the running remainder uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Convert every prefix to an integer:** Repeatedly parse `word[0:i + 1]`. Prefixes can exceed fixed-width types, and reparsing all prefixes takes quadratic total work.
- **Recompute each remainder from the beginning:** Applying modular arithmetic separately to every prefix avoids overflow but revisits earlier digits and takes $O(n^2)$ time.
- **Arbitrary-precision accumulation:** Some languages can hold the growing integer, but its digit count increases with the input and makes arithmetic needlessly expensive compared with one bounded remainder.
- **Divisor one:** Every integer, including zero, is divisible by one, so the result contains only ones.
- **Leading zeroes:** A zero-valued prefix has remainder zero and must be marked divisible; leading zeroes do not change the positional recurrence.
- **Large divisor:** Since the stored remainder is always smaller than `m`, a 64-bit temporary safely holds `remainder * 10 + digit` for the stated bound.
