## General

The task accepts any valid pair, so the exact Optimal solution enumerates the first number `a` in increasing order and derives the only possible companion:

`b = n - a`.

There is no need to enumerate both independently because the sum equation fixes `b` once `a` is chosen.

**Generating candidates**

`count(1)` yields $1,2,3,\ldots$ without a built-in stopping point. For each positive `a`, the code computes `b`.

The problem guarantees at least one valid answer. A valid pair has both numbers positive, so it must be found for some `a` from one through `n - 1`. Under that guarantee, the infinite iterator always returns before reaching candidates with nonpositive `b`.

Without the guarantee, using `count` would be unsafe. Once `a > n`, `b` becomes negative, and a negative decimal string without zero could accidentally pass even though positivity is required. A defensive implementation would use `range(1, n)` and handle failure after the loop.

**Checking both decimal representations at once**

`f"{a}{b}"` converts both integers to decimal text and concatenates them. The condition

`"0" not in f"{a}{b}"`

is true exactly when neither representation contains a zero. If either number has a zero digit, that character appears somewhere in the combined string.

No separator is needed. The property being tested is simply whether zero occurs anywhere; joining the texts cannot remove or create a zero digit.

This equivalence can be stated in both directions. If `a` contains a zero, its characters appear unchanged at the beginning of the formatted result, so the combined membership test fails. If `b` contains a zero, its characters appear unchanged at the end and the same test fails. Conversely, if the combined text contains zero, that character must have come from one of the two decimal representations because formatting inserts no other characters between positive integers. Therefore, passing the one combined test proves that both numbers are No-Zero integers; it is not a shortcut that weakens either individual requirement.

For `n = 11`:

- `a = 1` gives `b = 10`, and `"110"` contains zero, so it is rejected;
- `a = 2` gives `b = 9`, and `"29"` contains no zero, so `[2, 9]` is returned.

The first valid pair is returned immediately. It does not need to minimize either number because any valid answer is accepted.

Increasing enumeration also makes termination easy to reason about under the promise. A valid pair `[a, b]` has some positive first component. The counter visits every positive integer in order without skipping that component. Earlier rejected candidates do not affect later ones because each `b` is recomputed directly from `n - a`. As soon as the promised component is reached, the exact sum relation and zero test both hold, so control leaves the otherwise unbounded iterator.

**Why the returned pair is valid**

`a` begins at one, and the solution guarantee ensures return before `a` reaches `n`, so both `a` and `b = n - a` are positive. Their sum is algebraically

$$
a+(n-a)=n.
$$

The string condition verifies that neither decimal representation includes digit zero. Therefore, every returned list satisfies all three requirements.

Conversely, because enumeration tries every positive `a < n` in order and derives its matching `b`, it eventually reaches the first component of at least one guaranteed valid pair. That iteration passes the digit test and terminates.

**Why conversion is a reasonable choice**

Decimal-string conversion directly matches the definition, which is about decimal digits rather than arithmetic factors. An arithmetic loop using remainder ten would also work, but the string test is concise and clear for the small constraint `n <= 10000`.

The function has no explicit return after the loop because the contract promises success. In normal execution, Python leaves only through the return inside the condition.

## Complexity detail

In the worst case, the method tests $O(n)$ candidate values before finding a pair. Each candidate has $O(\log n)$ decimal digits across `a` and `b`. Formatting, concatenating, and scanning the combined string therefore take $O(\log n)$ time.

Total worst-case time is $O(n\log n)$, matching the manifest.

The temporary formatted string has $O(\log n)$ characters, so the exact implementation uses $O(\log n)$ transient auxiliary space. The returned two-element list is constant-sized. Some analyses call digit conversion space constant under fixed integer bounds, but the manifest's $O(\log n)$ accurately reflects generalized representation length.

The iterator itself stores constant state.

## Alternatives and edge cases

- **Bounded enumeration:** `for a in range(1, n)` enforces positivity of `b` even without the solution guarantee and is safer than an infinite counter.
- **Arithmetic digit test:** Repeatedly inspect `x % 10` and divide by ten. It avoids string allocation but still takes $O(\log n)$ time per candidate.
- **Construct digits without zero:** A direct carry-aware construction can avoid testing many candidates, but it is more complex than needed for `n <= 10000`.
- **`n = 2`:** The first candidate gives `[1,1]`, which is valid.
- **A candidate containing zero:** It is rejected even if only one of the two numbers has zero.
- **Concatenation boundary:** No separator is needed because the test asks only whether any zero exists.
- **Multiple answers:** Increasing enumeration returns the one with the smallest `a`; this is incidental, not a requirement.
- **Guaranteed existence:** The lack of loop bounds and fallback return relies on it. Removing that promise requires a bounded loop.
- **Negative string outside intended range:** A minus sign is not zero, so unbounded enumeration could accept a negative `b` if no valid positive pair existed.
- **Leading zeros:** Ordinary integer formatting never creates leading zeroes, so only actual digits of the number are examined.
