## General

**Search candidates in increasing numerical order**

The source begins `count(n + 1)`, an unbounded iterator producing `n+1, n+2, n+3, ...`. Starting at `n+1` enforces the word “strictly”: even if `n` itself is numerically balanced, it cannot be returned.

Each candidate is tested independently. The first candidate passing the balance condition is immediately returned.

Because candidates are examined in increasing order with no gaps, no smaller valid number greater than `n` can have been skipped. This ordering provides the minimality proof directly.

**Count decimal digits without converting to a string**

For candidate `x`, the source copies it into `y` and creates ten zero counts, one for each digit from zero through nine.

The loop

`y, v = divmod(y, 10)`

simultaneously obtains the remaining higher digits in `y` and the final decimal digit in `v`. It increments `cnt[v]` and repeats until no digits remain.

For example, processing 1333 extracts digits three, three, three, and one. The resulting counts have `cnt[1]=1` and `cnt[3]=3`.

**Translate the balance definition into one condition per digit**

The final predicate is

`all(v == 0 or i == v for i, v in enumerate(cnt))`.

Here `i` is the digit and `v` is its occurrence count. A digit satisfies the condition in either of two cases:

- it is absent, so `v == 0`;
- it is present exactly `i` times, so `i == v`.

The `all` requires this for every digit class. This matches the definition exactly: only digits that occur impose their occurrence-number requirement.

**Why digit zero can never appear**

For digit index zero, a positive count cannot satisfy `i == v` because zero cannot equal a positive occurrence count. It also cannot satisfy `v == 0`. Therefore any candidate containing digit zero is rejected.

This explains why a number such as 1022 is not balanced even though the two digit occurrences are correct. The single zero violates the rule for digit zero.

**Trace a balanced candidate**

For 1333, digit one occurs once, digit three occurs three times, and every other digit is absent. The condition succeeds for index one through equality, for index three through equality, and for all other indices through zero count.

For 3133, the positions differ but the frequency vector is the same, so it is also balanced. Numerical balance depends on counts, not digit order.

**Trace a rejection**

For 122, the counts are one copy of digit one and two copies of digit two, so it is balanced.

For 123, digit one is correct, but digit two appears only once instead of twice and digit three appears only once instead of three times. The `all` generator fails as soon as it reaches an invalid class.

**Why the returned number exists for the input bound**

The local constraints stop at one million, while larger balanced numbers exist above that limit. The enumeration will therefore reach a valid candidate and return.

The source does not encode an explicit upper bound or fallback return. It relies on the mathematical existence guaranteed by the constrained problem domain. `itertools.count` itself would otherwise continue indefinitely.

**Why the algorithm is correct**

For any candidate accepted by the predicate, every absent digit has count zero and every present digit `d` has count exactly `d`. It is numerically balanced.

Conversely, any numerically balanced candidate has exactly that frequency property, so every clause in `all` succeeds.

The predicate is therefore necessary and sufficient. Since enumeration begins at the first allowed integer and proceeds upward, the first accepted candidate is exactly the smallest balanced integer strictly greater than `n`.

**The actual method differs from lookup-table optimization**

A precomputed sorted list of all relevant balanced numbers could answer with a binary search. The protected source does not use such a table; it performs digit counting for every integer in the gap.

Its benefit is conceptual simplicity and constant extra storage. Its cost depends on how far the next answer lies from `n`.

## Complexity detail

Let $G$ be the gap between `n` and the returned answer, and let $D$ be the maximum number of decimal digits among tested candidates. Each test extracts $O(D)$ digits and scans the fixed ten-entry count array, so time is $O(G(D+10))$, usually written $O(GD)$ or, with the constrained digit count treated as constant, $O(G)$.

The manifest's $O(1)$ time can only be interpreted under the fully fixed input ceiling, where both the largest search gap and digit count have absolute constants. It does not describe how the exact enumeration scales as the answer gap changes.

The ten-entry count list and scalar variables use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Precomputed balanced-number table:** Store all relevant values and use `bisect_right` for logarithmic lookup in the table size.
- **Generate digit multisets and permutations:** Construct only balanced numbers, sort them, and select the next one.
- **String-based counting:** `Counter(str(x))` is concise but allocates a string and mapping per candidate.
- **`n` already balanced:** Enumeration starts at `n+1`, so it still returns a strictly greater value.
- **`n=0`:** Candidate one is balanced and is returned.
- **Digit zero:** Any occurrence makes a candidate invalid.
- **Repeated balanced layouts:** Numbers such as 1333 and 3133 share counts but are distinct candidates ordered numerically.
- **Absent digit:** It imposes no requirement beyond a zero count.
- **Digit nine:** If present, it would need nine occurrences.
- **First valid candidate:** Immediate return is safe because the search order is increasing.
- **No explicit loop bound:** Correctness relies on existence within the problem's bounded domain.
- **Manifest mismatch:** Exact work is sequential in the answer gap, not a literal constant number of operations.
