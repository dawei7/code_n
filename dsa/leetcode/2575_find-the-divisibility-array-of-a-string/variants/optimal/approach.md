## General

**The full prefix integers are unnecessary**

A prefix of a $10^5$-digit string is far too large for ordinary fixed-width integer types. Even languages with arbitrary-size integers would make repeatedly constructing and dividing ever-growing values unnecessarily expensive.

Divisibility by $m$ depends only on the remainder modulo $m$. A number is divisible exactly when that remainder is zero. The solution therefore carries only the current prefix remainder `x`.

**Extend one decimal prefix**

Suppose the numeric value of the processed prefix is $P$, and the next digit has numeric value $d$. Appending that digit in base ten creates

$$
P'=10P+d.
$$

If `x = P % m`, modular arithmetic gives

$$
P'\bmod m
=
(10(P\bmod m)+d)\bmod m.
$$

So the new remainder can be computed as

`x = (x * 10 + int(c)) % m`.

The old full value $P$ is never needed. Two values with the same remainder behave identically after the same next digit is appended because their difference is a multiple of $m$, and multiplying that difference by ten keeps it a multiple of $m$.

**Produce one answer per character**

After updating `x` with the current character, it is the remainder of the prefix ending at that character. The solution appends one when `x == 0` and zero otherwise.

The update must occur before the append. At index $i$, the query concerns `word[0:i+1]`, including the current digit. Testing the old remainder would answer for the previous shorter prefix.

The answer list begins empty and receives exactly one entry for every character, so it automatically has length $n$ and preserves prefix order.

**A proof by induction**

Before processing any digit, the empty numeric prefix may be treated as zero, and `x=0` is its correct remainder.

Assume before a loop iteration that `x` equals the remainder of all previously processed digits. The recurrence above shows that replacing it with `(x*10+d)%m` yields exactly the remainder of the prefix after appending digit $d$. The emitted bit is therefore one exactly when that new prefix is divisible by $m$.

This proves the maintained remainder and every output position by induction over the string.

**Trace `word = "1010"` with `m = 10`**

- Start with remainder $0$. Appending $1$ gives $(0\cdot10+1)\bmod10=1$, so append zero.
- Appending $0$ gives $(1\cdot10+0)\bmod10=0$, so append one. Prefix $10$ is divisible.
- Appending $1$ gives remainder $1$, so append zero.
- Appending $0$ gives remainder $0$, so append one. Prefix $1010$ is divisible.

The result is `[0,1,0,1]`.

**Why reducing after every digit is safe**

Write the true prefix as $P=qm+x$, where $x$ is its stored remainder. After appending digit $d$,

$$
10P+d=10qm+10x+d.
$$

The term $10qm$ is divisible by $m$ and contributes nothing to the remainder. Only `10*x+d` matters. Reducing at every step discards only multiples of $m$, never information relevant to future divisibility.

It also keeps `x` between $0$ and $m-1$. Before applying the next modulo, `x*10+d` is less than $10m$, so intermediate values remain small even when the processed prefix has tens of thousands of digits.

**Leading zeros and zero prefixes**

The string may contain zero digits, including at its beginning. A prefix such as `"000"` has numeric value zero and is divisible by every positive $m$. The recurrence keeps `x=0` through each leading zero and correctly emits ones.

Leading zeros require no parsing special case because positional recurrence treats them as ordinary digits with $d=0$.

When $m=1$, every remainder modulo one is zero, so every output entry is one. The formula handles this automatically.

**Why character conversion is valid**

The constraints guarantee every character lies from `'0'` through `'9'`. Python's `int(c)` therefore produces exactly one digit value between zero and nine and cannot fail. No signs, separators, or other characters need handling.

## Complexity detail

Let $n$ be the length of `word`. The loop performs a constant amount of arithmetic and one append per character, so time is $O(n)$. The integer `x` remains bounded by $m-1$, independent of prefix length.

The required output list uses $O(n)$ space, matching the manifest. Excluding output, only `x` and the current character/digit use $O(1)$ auxiliary space. No large prefix integer or substring is created.

## Alternatives and edge cases

- **Parse every prefix:** Converting `word[:i+1]` for each index copies and parses growing strings, leading to quadratic character work and enormous integers.
- **Maintain the full integer once:** Arbitrary-precision growth still makes arithmetic increasingly expensive, while the remainder contains all necessary information.
- **Prefix remainder recurrence:** The implemented method is the standard streaming solution and works even if digits arrive one at a time.
- **Modulus one:** Every prefix is divisible, so the result contains only ones.
- **Leading zeros:** Remainder remains zero until a nonzero digit changes it, correctly marking zero-valued prefixes divisible.
- **Single digit:** One recurrence step directly decides the sole output entry.
- **Prefix becomes divisible repeatedly:** A zero remainder is not terminal; later digits may make it nonzero and later still return it to zero.
- **Very long word:** The stored state never grows with the numeric prefix, preventing overflow and expensive big-integer operations.
- **Positive modulus:** The constraint `m >= 1` guarantees modulo is defined and avoids division by zero.
- **Output timing:** Append only after incorporating the current digit so index $i$ describes the prefix through $i$.
