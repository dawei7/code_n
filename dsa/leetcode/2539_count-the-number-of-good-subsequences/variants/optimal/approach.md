## General

**Group good subsequences by their common frequency**

In a good non-empty subsequence, choose some non-empty set of distinct character values. Every chosen character must appear the same positive number `i` of times.

The common frequency `i` is unique for that subsequence. The method iterates `i` from one through the maximum frequency present in `s` and counts all good subsequences having exactly that common frequency.

**Choose occurrences by index**

Suppose character `c` occurs `v` times in the original string. To include `c` with frequency `i`, choose any `i` of those `v` occurrence indices:

$$
\binom vi
$$

choices.

Once indices are chosen, their order in the subsequence is forced by their original string positions. There is no additional permutation factor.

If `v<i`, that character cannot participate at this common frequency.

**Include or exclude each character independently**

For a character with `v>=i`:

- exclude it: one choice;
- include it by choosing `i` occurrences: $\binom vi$ choices.

That gives $\binom vi+1$ choices.

Choices for different character values are independent, so multiplying these quantities counts every selection of characters and occurrence indices.

Characters with `v<i` contribute only the forced exclude choice one, so the source simply skips them.

**Remove the empty character selection**

The product includes the option that every eligible character is excluded. That produces the empty subsequence, which is not good.

Subtracting one from `x` removes exactly this single case:

`ans=(ans+x-1)%MOD`.

Every remaining selection uses at least one character, and all included characters occur exactly `i` times, so it is good.

**Why summing over `i` does not double-count**

A non-empty good subsequence has one actual frequency shared by all its distinct characters. It appears only in the iteration for that `i`.

For another frequency, the selected occurrence counts differ, so it cannot represent the same subsequence. The frequency classes are disjoint and can be added.

**Precompute factorials and modular inverses**

Global array `f` stores factorials modulo `MOD`:

`f[i]=i! mod MOD`.

`g[i]` stores the modular inverse of `f[i]`, computed using Fermat's theorem:

`pow(f[i],MOD-2,MOD)`.

Because `MOD` is prime and all factorial indices are below it, these inverses exist.

Combination helper returns

$$
\binom nk
\equiv
n!\,(k!)^{-1}\,((n-k)!)^{-1}
\pmod{\texttt{MOD}}.
$$

The fixed table size 10,001 covers the maximum string length $10^4$.

**Trace `"aabb"`**

Frequencies are two for `a` and two for `b`.

For common frequency one:

$$
(\binom21+1)^2-1
=(2+1)^2-1
=8.
$$

These include subsequences using only `a`, only `b`, or one of each.

For common frequency two:

$$
(\binom22+1)^2-1
=(1+1)^2-1
=3.
$$

These are `"aa"`, `"bb"`, and `"aabb"` by chosen indices. Total is 11.

**Why character order needs no special work**

A subsequence preserves original order automatically after its set of occurrence indices is selected. Different index subsets produce distinct subsequences under the counting convention, even if their resulting character text is equal.

The binomial factors count those indexed choices exactly.

This is why the method counts choices of occurrences rather than distinct resulting text strings.


For each common frequency `i`, the product independently chooses either zero or exactly `i` occurrences for every character capable of participating. Removing the all-zero choice leaves exactly all non-empty good subsequences of that frequency.

Unique common frequencies make the iterations disjoint. Summing them produces every good subsequence exactly once.

**Global preprocessing cost**

The manifest reports per-solution $O(n)$ behavior after factorial tables exist. The module-level source computes every inverse factorial with a separate modular exponentiation, rather than deriving them with one backward recurrence.

This one-time initialization is fixed at 10,001 entries but is materially more work than the method body.

## Complexity detail

Let $n=\lvert s\rvert$, $F$ be the maximum character frequency, and $A\le26$ the number of distinct lowercase characters. The method loops through $F$ frequencies and at most $A$ counts, taking $O(AF)=O(n)$ time.

The counter uses $O(A)=O(1)$ space relative to input. Global factorial and inverse arrays use $O(N)$ fixed table space with `N=10001`.

Module initialization performs $N$ factorial multiplications and $N$ modular exponentiations, costing $O(N\log MOD)$ with the exact construction. Once initialized, each combination lookup is $O(1)$.

## Alternatives and edge cases

- **Backward inverse-factorial fill:** Compute one inverse at `N-1` and derive the rest in $O(N)$ preprocessing.
- **All characters distinct:** Only common frequency one contributes, producing $2^n-1$ non-empty subsequences.
- **One repeated character:** Every non-empty choice of its occurrences is good.
- **Character frequency below `i`:** It must be excluded for that iteration.
- **Empty selection:** Subtract exactly one from each frequency product.
- **Indexed occurrences:** Binomial coefficients count different position choices.
- **Unique common frequency:** It prevents cross-iteration double counting.
- **Modulo inverse:** It is valid because factorial factors are below the prime modulus.
- **Maximum table index:** 10,000 fits inside arrays of length 10,001.
- **Global cost:** Exact preprocessing uses repeated `pow` calls.
