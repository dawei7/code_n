## General

**Start with the total number of ones**

If three parts must contain the same number of ones, the total one-count must be divisible by three.

The source computes the total with `sum(c == '1' for c in s)`. Each Boolean contributes one for a one character and zero for a zero.

`divmod(total, 3)` returns quotient `cnt` and remainder `m`. Each part must contain exactly `cnt` ones.

If `m` is nonzero, equal division is impossible and the method returns zero immediately.

**Handle an all-zero string separately**

When `cnt == 0`, every character is zero. Any choice of two distinct cut gaps creates three nonempty substrings, and all three contain zero ones.

A length-`n` string has `n-1` internal gaps. Choosing two of them gives:

$$
\binom{n-1}{2}=\frac{(n-1)(n-2)}{2}.
$$

The source computes this expression and applies the required modulo.

The nonempty requirement is built into choosing two distinct internal gaps; neither cut can lie outside the string or coincide with the other.

**Locate boundaries between one-count groups**

For a positive `cnt`, the first part must end after its `cnt`-th one but before the next one.

Helper `find(x)` scans from the start, counts ones, and returns the first index where the cumulative count reaches `x`.

`i1 = find(cnt)` is the index of the last required one in part one.

`i2 = find(cnt + 1)` is the index of the first one that must belong to part two.

Any first cut after an index from `i1` through `i2-1` gives the first part exactly `cnt` ones. The number of choices is `i2 - i1`.

Zeros between those two ones create the extra choices.

**Locate the second cut independently**

After two parts, the cumulative number of ones must be `2*cnt`.

`j1 = find(cnt * 2)` locates the last required one in part two, and `j2 = find(cnt * 2 + 1)` locates the first one belonging to part three.

The second cut has `j2 - j1` valid positions.

Every first-cut choice lies before every second-cut choice because positive `cnt` separates the relevant one ranks. Therefore choices combine independently.

The total number is:

`(i2 - i1) * (j2 - j1)`

reduced modulo the constant.

**Tracing 10101**

There are three ones, so each part needs one.

The first one is at index zero and the second at index two. The first cut can follow index zero or one, giving two choices.

The second one is at index two and the third at index four. The second cut can follow index two or three, also giving two choices.

Their product is four, matching the listed splits.

**Why zeros before the first one and after the last do not matter**

The first substring must begin at index zero, so leading zeros cannot be assigned to an earlier part. They are always in part one.

Similarly, the third substring must end at the string's final index, so trailing zeros always belong to part three.

Only zeros between the boundary one-ranks can move across a cut, which is exactly what the index differences count.

**Why helper searches are valid**

When total ones is positive and divisible by three, it is at least three. The requested ranks `cnt`, `cnt+1`, `2cnt`, and `2cnt+1` all exist within the total.

Thus `find` always returns an index in this branch. No missing-result handling is needed.

The helper rescans `s` four times, but a constant number of linear scans remains linear overall.


If total ones is not divisible by three, no valid split exists. If it is zero, every pair of internal cuts is valid and the combination formula counts all pairs.

For positive equal share `cnt`, a valid first cut must lie precisely between the `cnt`-th and `cnt+1`-th ones. A valid second cut must lie precisely between the `2cnt`-th and `2cnt+1`-th ones.

The source counts every position in both independent ranges, so their product counts all and only valid nonempty three-part splits.

## Complexity detail

Let $N$ be string length. Counting total ones costs $O(N)$. In the positive branch, four `find` calls each scan at most $N$ characters, so total time is still $O(N)$.

The algorithm stores counters, indices, and the modulus only. Auxiliary space is $O(1)$, matching the manifest.

Arithmetic is reduced modulo $10^9+7$ for the returned count.

## Alternatives and edge cases

- **Single scan recording one positions:** Store all one indices, then compute the same gaps. It uses $O(N)$ extra space.
- **Single scan with four boundary variables:** Capture the required ranks without rescanning and keep $O(1)$ space.
- **Try every pair of cuts:** There are $O(N^2)$ possibilities.
- **Total ones not divisible by three:** Return zero immediately.
- **No ones:** Any two distinct internal gaps work.
- **Exactly three ones:** Each part receives one, and zeros between them determine multiplicity.
- **No zeros between boundary ones:** The corresponding cut has exactly one position.
- **Many boundary zeros:** Each creates another legal placement for that cut.
- **Leading zeros:** They are fixed in the first part and do not create a cut choice before its start.
- **Trailing zeros:** They are fixed in the third part.
- **Nonempty pieces:** Internal gap choices and positive boundary ranks enforce them.
- **Modulo:** It is applied after the product or all-zero combination count.
- **Boolean sum:** In Python, comparison results act as integers zero and one.
